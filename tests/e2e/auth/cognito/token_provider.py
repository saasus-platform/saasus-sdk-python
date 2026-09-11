"""
Cognito token provider with caching

boto3を使用してCognitoからトークンを取得し、30分間キャッシュします。
AdminInitiateAuthを使用してサーバーサイド認証を行います。
"""

import os
import time
from typing import Any, Dict, Optional
import boto3
from botocore.exceptions import ClientError


# トークンキャッシュ（メモリ内）
_token_cache: Dict[str, Dict[str, Any]] = {}
CACHE_DURATION = 30 * 60  # 30分


def get_cognito_tokens(
    user_pool_id: Optional[str] = None,
    client_id: Optional[str] = None,
    username: Optional[str] = None,
    password: Optional[str] = None,
    region: Optional[str] = None
) -> Dict[str, str]:
    """Cognitoからトークンを取得（キャッシュ付き）
    
    AdminInitiateAuthを使用してサーバーサイド認証を行います。
    AWS認証情報（AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY）が必要です。
    
    Returns:
        トークン辞書 {"access_token": "...", "id_token": "...", "refresh_token": "..."}
    """
    user_pool_id = user_pool_id or os.getenv("E2E_COGNITO_USER_POOL_ID")
    client_id = client_id or os.getenv("E2E_COGNITO_CLIENT_ID")
    username = username or os.getenv("E2E_COGNITO_USERNAME")
    password = password or os.getenv("E2E_COGNITO_PASSWORD")
    region = region or os.getenv("E2E_COGNITO_REGION", "ap-northeast-1")
    
    if not all([user_pool_id, client_id, username, password]):
        raise ValueError(
            "Cognito configuration is incomplete. "
            "Set E2E_COGNITO_USER_POOL_ID, E2E_COGNITO_CLIENT_ID, "
            "E2E_COGNITO_USERNAME, E2E_COGNITO_PASSWORD"
        )
    
    cache_key = f"{user_pool_id}:{client_id}:{username}"
    
    if cache_key in _token_cache:
        cached = _token_cache[cache_key]
        if time.time() - cached["timestamp"] < CACHE_DURATION:
            return cached["tokens"]
    
    cognito_client = boto3.client("cognito-idp", region_name=region)
    
    try:
        # AdminInitiateAuthを使用（AWS認証情報が必要）
        response = cognito_client.admin_initiate_auth(
            UserPoolId=user_pool_id,
            ClientId=client_id,
            AuthFlow="ADMIN_USER_PASSWORD_AUTH",
            AuthParameters={
                "USERNAME": username,
                "PASSWORD": password
            }
        )
        
        auth_result = response.get("AuthenticationResult", {})
        tokens = {
            "access_token": auth_result.get("AccessToken", ""),
            "id_token": auth_result.get("IdToken", ""),
            "refresh_token": auth_result.get("RefreshToken", "")
        }
        
        _token_cache[cache_key] = {
            "tokens": tokens,
            "timestamp": time.time()
        }
        
        return tokens
        
    except ClientError as e:
        error_code = e.response.get("Error", {}).get("Code", "Unknown")
        if error_code == "UserNotFoundException":
            # ユーザーが存在しない場合は作成を試行
            create_cognito_user(username, password, user_pool_id, client_id, region)
            return get_cognito_tokens(user_pool_id, client_id, username, password, region)
        raise


def create_cognito_user(
    username: str,
    password: str,
    user_pool_id: Optional[str] = None,
    client_id: Optional[str] = None,
    region: Optional[str] = None
) -> None:
    """Cognitoユーザーを作成"""
    user_pool_id = user_pool_id or os.getenv("E2E_COGNITO_USER_POOL_ID")
    region = region or os.getenv("E2E_COGNITO_REGION", "ap-northeast-1")
    
    cognito_client = boto3.client("cognito-idp", region_name=region)
    
    try:
        # ユーザー作成
        cognito_client.admin_create_user(
            UserPoolId=user_pool_id,
            Username=username,
            UserAttributes=[
                {"Name": "email", "Value": username},
                {"Name": "email_verified", "Value": "true"}
            ],
            MessageAction="SUPPRESS"
        )
        
        # パスワードを永続的に設定
        cognito_client.admin_set_user_password(
            UserPoolId=user_pool_id,
            Username=username,
            Password=password,
            Permanent=True
        )
    except ClientError as e:
        if e.response.get("Error", {}).get("Code") != "UsernameExistsException":
            raise


def clear_token_cache() -> None:
    """トークンキャッシュをクリア"""
    global _token_cache
    _token_cache = {}


def is_cognito_configured() -> bool:
    """Cognito環境変数が設定されているかチェック"""
    required_vars = [
        "E2E_COGNITO_USER_POOL_ID",
        "E2E_COGNITO_CLIENT_ID",
        "E2E_COGNITO_USERNAME",
        "E2E_COGNITO_PASSWORD"
    ]
    return all(os.getenv(v) for v in required_vars)


def get_cognito_tokens_safe() -> Optional[Dict[str, str]]:
    """Cognitoトークンを安全に取得（設定されていない場合はNone）"""
    if not is_cognito_configured():
        return None
    try:
        return get_cognito_tokens()
    except Exception:
        return None

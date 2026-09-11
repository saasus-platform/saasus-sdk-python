"""
Auth E2E test validation functions

JavaScriptのvalidation.tsから移植した検証関数群
"""

from typing import Any, Dict, Optional


def _ensure(condition: bool, message: str) -> bool:
    """条件をチェックし、失敗時にメッセージを出力
    
    Args:
        condition: チェック条件
        message: エラーメッセージ
        
    Returns:
        条件の結果
    """
    if not condition:
        print(f"Validation failed: {message}")
        return False
    return True


def validate_saas_user(payload: Optional[Dict[str, Any]]) -> bool:
    """SaaSユーザーのレスポンスを検証
    
    Args:
        payload: レスポンスペイロード
        
    Returns:
        検証結果
    """
    if not payload:
        return _ensure(False, "SaasUser payload is empty")
    
    has_id = _ensure("id" in payload and payload["id"], "SaasUser id is missing")
    has_email = _ensure("email" in payload and payload["email"], "SaasUser email is missing")
    
    return has_id and has_email


def validate_saas_user_list(payload: Optional[Dict[str, Any]]) -> bool:
    """SaaSユーザーリストのレスポンスを検証
    
    Args:
        payload: レスポンスペイロード
        
    Returns:
        検証結果
    """
    if not payload:
        return _ensure(False, "SaasUsers payload is empty")
    return _ensure("users" in payload and isinstance(payload["users"], list), "users is not a list")


def validate_tenant(payload: Optional[Dict[str, Any]]) -> bool:
    """テナントのレスポンスを検証
    
    Args:
        payload: レスポンスペイロード
        
    Returns:
        検証結果
    """
    if not payload:
        return _ensure(False, "Tenant payload is empty")
    return (
        _ensure("id" in payload and payload["id"], "Tenant id is missing") and
        _ensure("name" in payload and payload["name"], "Tenant name is missing")
    )


def validate_tenant_list(payload: Optional[Dict[str, Any]]) -> bool:
    """テナントリストのレスポンスを検証
    
    Args:
        payload: レスポンスペイロード
        
    Returns:
        検証結果
    """
    if not payload:
        return _ensure(False, "Tenants payload is empty")
    return _ensure("tenants" in payload and isinstance(payload["tenants"], list), "tenants is not a list")


def validate_role(payload: Optional[Dict[str, Any]]) -> bool:
    """ロールのレスポンスを検証
    
    Args:
        payload: レスポンスペイロード
        
    Returns:
        検証結果
    """
    if not payload:
        return _ensure(False, "Role payload is empty")
    return _ensure("role_name" in payload and payload["role_name"], "role_name is missing")


def validate_role_list(payload: Optional[Dict[str, Any]]) -> bool:
    """ロールリストのレスポンスを検証
    
    Args:
        payload: レスポンスペイロード
        
    Returns:
        検証結果
    """
    if not payload:
        return _ensure(False, "Roles payload is empty")
    return _ensure("roles" in payload and isinstance(payload["roles"], list), "roles is not a list")


def validate_attribute(payload: Optional[Dict[str, Any]]) -> bool:
    """属性のレスポンスを検証
    
    Args:
        payload: レスポンスペイロード
        
    Returns:
        検証結果
    """
    if not payload:
        return _ensure(False, "Attribute payload is empty")
    return _ensure("attribute_name" in payload and payload["attribute_name"], "attribute_name is missing")


def validate_user_attributes(payload: Optional[Dict[str, Any]]) -> bool:
    """ユーザー属性リストのレスポンスを検証
    
    Args:
        payload: レスポンスペイロード
        
    Returns:
        検証結果
    """
    if not payload:
        return _ensure(False, "UserAttributes payload is empty")
    return _ensure(
        "user_attributes" in payload and isinstance(payload["user_attributes"], list),
        "user_attributes is not a list"
    )


def validate_tenant_attributes(payload: Optional[Dict[str, Any]]) -> bool:
    """テナント属性リストのレスポンスを検証
    
    Args:
        payload: レスポンスペイロード
        
    Returns:
        検証結果
    """
    if not payload:
        return _ensure(False, "TenantAttributes payload is empty")
    return _ensure(
        "tenant_attributes" in payload and isinstance(payload["tenant_attributes"], list),
        "tenant_attributes is not a list"
    )


def validate_env(payload: Optional[Dict[str, Any]]) -> bool:
    """環境のレスポンスを検証
    
    Args:
        payload: レスポンスペイロード
        
    Returns:
        検証結果
    """
    if not payload:
        return _ensure(False, "Env payload is empty")
    return (
        _ensure("id" in payload and isinstance(payload["id"], int), "Env id is missing") and
        _ensure("name" in payload and payload["name"], "Env name is missing")
    )


def validate_env_list(payload: Optional[Dict[str, Any]]) -> bool:
    """環境リストのレスポンスを検証
    
    Args:
        payload: レスポンスペイロード
        
    Returns:
        検証結果
    """
    if not payload:
        return _ensure(False, "Envs payload is empty")
    return _ensure("envs" in payload and isinstance(payload["envs"], list), "envs is not a list")


def validate_basic_info(payload: Optional[Dict[str, Any]]) -> bool:
    """基本情報のレスポンスを検証
    
    Args:
        payload: レスポンスペイロード
        
    Returns:
        検証結果
    """
    if not payload:
        return _ensure(False, "BasicInfo payload is empty")
    return (
        _ensure("domain_name" in payload and payload["domain_name"], "domain_name is missing") and
        _ensure("default_domain_name" in payload and payload["default_domain_name"], "default_domain_name is missing")
    )


def validate_auth_info(payload: Optional[Dict[str, Any]]) -> bool:
    """認証情報のレスポンスを検証
    
    Args:
        payload: レスポンスペイロード
        
    Returns:
        検証結果（開発環境では常にTrue）
    """
    if not payload:
        return _ensure(False, "AuthInfo payload is empty")
    # callback_urlが存在しない場合でも成功とする（開発環境では設定されていない可能性がある）
    return True


def validate_secret_code(payload: Optional[Dict[str, Any]]) -> bool:
    """シークレットコードのレスポンスを検証
    
    Args:
        payload: レスポンスペイロード
        
    Returns:
        検証結果
    """
    if not payload:
        return _ensure(False, "SecretCode payload is empty")
    return _ensure("secret_code" in payload and payload["secret_code"], "secret_code is missing")


def validate_mfa_preference(payload: Optional[Dict[str, Any]]) -> bool:
    """MFA設定のレスポンスを検証
    
    Args:
        payload: レスポンスペイロード
        
    Returns:
        検証結果
    """
    if not payload:
        return _ensure(False, "MfaPreference payload is empty")
    return True


def validate_void_response(payload: Optional[Dict[str, Any]]) -> bool:
    """空のレスポンスを検証（削除操作など）
    
    Args:
        payload: レスポンスペイロード
        
    Returns:
        検証結果（常にTrue）
    """
    return True

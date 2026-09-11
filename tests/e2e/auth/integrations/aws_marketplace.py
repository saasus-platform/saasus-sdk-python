"""
AWS Marketplace integration setup

AWS Marketplace統合のセットアップとチェック機能を提供します。
"""

import os
import pytest


def is_aws_marketplace_enabled() -> bool:
    """AWS Marketplace統合が有効かチェック
    
    Returns:
        AWS_MARKETPLACE_REGISTRATION_TOKENが設定されている場合True
    """
    return bool(os.getenv("AWS_MARKETPLACE_REGISTRATION_TOKEN"))


def setup_aws_marketplace() -> None:
    """AWS Marketplace統合をセットアップ
    
    AWS_MARKETPLACE_REGISTRATION_TOKENが設定されていない場合はテストをスキップします。
    
    Raises:
        pytest.skip: AWS_MARKETPLACE_REGISTRATION_TOKENが未設定の場合
    """
    if not is_aws_marketplace_enabled():
        pytest.skip("AWS Marketplace integration skipped: AWS_MARKETPLACE_REGISTRATION_TOKEN not set")
    
    print("✅ AWS Marketplace integration enabled")


def get_aws_marketplace_token() -> str:
    """AWS Marketplace登録トークンを取得
    
    Returns:
        AWS Marketplace登録トークン
        
    Raises:
        ValueError: AWS_MARKETPLACE_REGISTRATION_TOKENが未設定の場合
    """
    token = os.getenv("AWS_MARKETPLACE_REGISTRATION_TOKEN")
    if not token:
        raise ValueError("AWS_MARKETPLACE_REGISTRATION_TOKEN environment variable is not set")
    return token

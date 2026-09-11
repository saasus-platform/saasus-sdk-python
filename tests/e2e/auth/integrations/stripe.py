"""
Stripe integration setup

Stripe統合のセットアップとチェック機能を提供します。
"""

import os
import pytest


def is_stripe_enabled() -> bool:
    """Stripe統合が有効かチェック
    
    Returns:
        STRIPE_SECRET_KEYが設定されている場合True
    """
    return bool(os.getenv("STRIPE_SECRET_KEY"))


def setup_stripe() -> None:
    """Stripe統合をセットアップ
    
    STRIPE_SECRET_KEYが設定されていない場合はテストをスキップします。
    
    Raises:
        pytest.skip: STRIPE_SECRET_KEYが未設定の場合
    """
    if not is_stripe_enabled():
        pytest.skip("Stripe integration skipped: STRIPE_SECRET_KEY not set")
    
    print("✅ Stripe integration enabled")


def get_stripe_secret_key() -> str:
    """Stripeシークレットキーを取得
    
    Returns:
        Stripeシークレットキー
        
    Raises:
        ValueError: STRIPE_SECRET_KEYが未設定の場合
    """
    secret_key = os.getenv("STRIPE_SECRET_KEY")
    if not secret_key:
        raise ValueError("STRIPE_SECRET_KEY environment variable is not set")
    return secret_key

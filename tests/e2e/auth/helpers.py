"""
Auth E2E test helper functions

JavaScriptのhelpers.tsから移植したヘルパー関数群
"""

import os
import time
from typing import Any, Dict, Optional

AUTH_E2E_PREFIX = "py-sdk-auth-e2e"


def get_cognito_tokens_safe() -> Optional[Dict[str, str]]:
    """Cognitoトークンを安全に取得（設定されていない場合はNone）"""
    from tests.e2e.auth.cognito import get_cognito_tokens_safe as _get_tokens
    return _get_tokens()


def is_cognito_configured() -> bool:
    """Cognito環境変数が設定されているかチェック"""
    from tests.e2e.auth.cognito import is_cognito_configured as _is_configured
    return _is_configured()


def unique_email(label: str) -> str:
    """ユニークなメールアドレスを生成
    
    Args:
        label: メールアドレスのラベル
        
    Returns:
        ユニークなメールアドレス
        
    Example:
        >>> email = unique_email("test")
        >>> assert "@example.com" in email
        >>> assert "py-sdk-auth-e2e-test-" in email
    """
    timestamp = int(time.time() * 1000)
    return f"{AUTH_E2E_PREFIX}-{label}-{timestamp}@example.com"


def unique_string(prefix: str) -> str:
    """ユニークな文字列を生成
    
    Args:
        prefix: プレフィックス
        
    Returns:
        ユニークな文字列
        
    Example:
        >>> s = unique_string("role")
        >>> assert "py-sdk-auth-e2e-role-" in s
    """
    timestamp = int(time.time() * 1000)
    return f"{AUTH_E2E_PREFIX}-{prefix}-{timestamp}"


def unique_env_id() -> int:
    """ユニークな環境IDを生成
    
    Returns:
        ユニークな環境ID（6桁）
        
    Example:
        >>> env_id = unique_env_id()
        >>> assert 100000 <= env_id <= 999999
    """
    timestamp = int(time.time() * 1000)
    return int(str(timestamp)[-6:])


def get_default_password() -> str:
    """デフォルトパスワードを取得
    
    Returns:
        デフォルトパスワード
    """
    return os.getenv("AUTH_E2E_DEFAULT_PASSWORD", "Passw0rd!")


def build_create_saas_user_params(email: str, password: Optional[str] = None) -> Any:
    """CreateSaasUserのパラメータを生成
    
    Args:
        email: メールアドレス
        password: パスワード（省略時はデフォルト）
        
    Returns:
        CreateSaasUserParamオブジェクト
    """
    from saasus_sdk_python.src.auth.models.create_saas_user_param import CreateSaasUserParam
    
    return CreateSaasUserParam(
        email=email,
        password=password or get_default_password()
    )


def build_create_tenant_params(name: str) -> Dict[str, Any]:
    """CreateTenantのパラメータを生成
    
    Args:
        name: テナント名
        
    Returns:
        パラメータ辞書
    """
    return {
        "name": name
    }


def build_create_role_params(role_name: str, display_name: str) -> Dict[str, Any]:
    """CreateRoleのパラメータを生成
    
    Args:
        role_name: ロール名
        display_name: 表示名
        
    Returns:
        パラメータ辞書
    """
    return {
        "role_name": role_name,
        "display_name": display_name
    }


def build_create_user_attribute_params(attribute_name: str, display_name: str) -> Any:
    """CreateUserAttributeのパラメータを生成
    
    Args:
        attribute_name: 属性名
        display_name: 表示名
        
    Returns:
        Attributeオブジェクト
    """
    from saasus_sdk_python.src.auth.models.attribute import Attribute
    
    return Attribute(
        attribute_name=attribute_name,
        display_name=display_name,
        attribute_type="string"
    )


def build_create_tenant_attribute_params(attribute_name: str) -> Dict[str, Any]:
    """CreateTenantAttributeのパラメータを生成
    
    Args:
        attribute_name: 属性名
        
    Returns:
        パラメータ辞書
    """
    return {
        "attribute_name": attribute_name,
        "attribute_type": "string"
    }


def build_create_env_params(env_id: int, name: str, display_name: str) -> Dict[str, Any]:
    """CreateEnvのパラメータを生成
    
    Args:
        env_id: 環境ID
        name: 環境名
        display_name: 表示名
        
    Returns:
        パラメータ辞書
    """
    return {
        "id": env_id,
        "name": name,
        "display_name": display_name
    }


def build_update_saas_user_password_params(user_id: str, password: str) -> Dict[str, Any]:
    """UpdateSaasUserPasswordのパラメータを生成
    
    Args:
        user_id: ユーザーID
        password: 新しいパスワード
        
    Returns:
        パラメータ辞書
    """
    return {
        "user_id": user_id,
        "password": password
    }


def build_create_secret_code_params(user_id: str) -> Dict[str, Any]:
    """CreateSecretCodeのパラメータを生成
    
    Args:
        user_id: ユーザーID
        
    Returns:
        パラメータ辞書
    """
    return {
        "user_id": user_id
    }


def build_update_software_token_params(user_id: str, code: str) -> Dict[str, Any]:
    """UpdateSoftwareTokenのパラメータを生成
    
    Args:
        user_id: ユーザーID
        code: TOTPコード
        
    Returns:
        パラメータ辞書
    """
    return {
        "user_id": user_id,
        "code": code
    }


def build_update_user_mfa_preference_params(
    user_id: str,
    software_token_enabled: bool = True,
    software_token_preferred: bool = True
) -> Dict[str, Any]:
    """UpdateUserMfaPreferenceのパラメータを生成
    
    Args:
        user_id: ユーザーID
        software_token_enabled: ソフトウェアトークンを有効化
        software_token_preferred: ソフトウェアトークンを優先
        
    Returns:
        パラメータ辞書
    """
    return {
        "user_id": user_id,
        "software_token_mfa_settings": {
            "enabled": software_token_enabled,
            "preferred_mfa": software_token_preferred
        }
    }


# Pricing API helpers

def create_pricing_plan_for_test() -> str:
    """テスト用のプランを作成し、plan_idを返す
    
    既存のプランがあればそれを使用し、なければ新規作成する。
    
    Returns:
        plan_id: プランID
    """
    from saasus_sdk_python.src.pricing.api.pricing_units_api import PricingUnitsApi
    from saasus_sdk_python.src.pricing.api.pricing_menus_api import PricingMenusApi
    from saasus_sdk_python.src.pricing.api.pricing_plans_api import PricingPlansApi
    from saasus_sdk_python.client.pricing_client import SignedPricingApiClient
    from saasus_sdk_python.src.pricing.models.pricing_fixed_unit_for_save import PricingFixedUnitForSave
    from saasus_sdk_python.src.pricing.models.pricing_unit_for_save import PricingUnitForSave
    from saasus_sdk_python.src.pricing.models.save_pricing_menu_param import SavePricingMenuParam
    from saasus_sdk_python.src.pricing.models.save_pricing_plan_param import SavePricingPlanParam
    from saasus_sdk_python.src.pricing.models.unit_type import UnitType
    from saasus_sdk_python.src.pricing.models.currency import Currency
    from saasus_sdk_python.src.pricing.models.recurring_interval import RecurringInterval
    
    client = SignedPricingApiClient()
    units_api = PricingUnitsApi(client)
    menus_api = PricingMenusApi(client)
    plans_api = PricingPlansApi(client)
    
    # Check for existing plan
    plans = plans_api.get_pricing_plans()
    for p in plans.pricing_plans:
        if p.name == "e2e-basic-plan":
            return p.id
    
    # Get or create unit
    units = units_api.get_pricing_units()
    unit_id = None
    for u in units.units:
        if u.actual_instance.name == "e2e-basic-unit":
            unit_id = u.actual_instance.id
            break
    
    if not unit_id:
        fixed_unit = PricingFixedUnitForSave(
            name="e2e-basic-unit",
            display_name="E2E Basic Unit",
            description="Basic unit for E2E testing",
            type=UnitType.FIXED,
            currency=Currency.JPY,
            unit_amount=1000,
            recurring_interval=RecurringInterval.MONTH
        )
        unit = units_api.create_pricing_unit(body=PricingUnitForSave(actual_instance=fixed_unit))
        unit_id = unit.actual_instance.id
    
    # Get or create menu
    menus = menus_api.get_pricing_menus()
    menu_id = None
    for m in menus.pricing_menus:
        if m.name == "e2e-basic-menu":
            menu_id = m.id
            break
    
    if not menu_id:
        menu = menus_api.create_pricing_menu(
            body=SavePricingMenuParam(
                name="e2e-basic-menu",
                display_name="E2E Basic Menu",
                description="Basic menu for E2E testing",
                unit_ids=[unit_id]
            )
        )
        menu_id = menu.id
    
    # Create plan
    plan = plans_api.create_pricing_plan(
        body=SavePricingPlanParam(
            name="e2e-basic-plan",
            display_name="E2E Basic Plan",
            description="Basic plan for E2E testing",
            menu_ids=[menu_id]
        )
    )
    return plan.id


def get_or_create_test_plan_id() -> str:
    """テスト用プランIDを取得（存在しなければ作成）"""
    from saasus_sdk_python.src.pricing.api.pricing_plans_api import PricingPlansApi
    from saasus_sdk_python.client.pricing_client import SignedPricingApiClient
    
    client = SignedPricingApiClient()
    plans_api = PricingPlansApi(client)
    
    plans = plans_api.get_pricing_plans()
    for p in plans.pricing_plans:
        if p.name == "e2e-basic-plan":
            return p.id
    
    return create_pricing_plan_for_test()


# Stripe helpers

def get_stripe_secret_key() -> Optional[str]:
    """Stripeシークレットキーを取得"""
    return os.getenv("STRIPE_SECRET_KEY")


def is_stripe_configured() -> bool:
    """Stripe環境変数が設定されているかチェック"""
    return get_stripe_secret_key() is not None


def setup_stripe_integration() -> bool:
    """Stripe連携を設定
    
    Returns:
        成功した場合True
    """
    secret_key = get_stripe_secret_key()
    if not secret_key:
        return False
    
    from saasus_sdk_python.src.billing.api.stripe_api import StripeApi
    from saasus_sdk_python.client.billing_client import SignedBillingApiClient
    from saasus_sdk_python.src.billing.models.update_stripe_info_param import UpdateStripeInfoParam
    
    client = SignedBillingApiClient()
    stripe_api = StripeApi(client)
    stripe_api.update_stripe_info(
        update_stripe_info_param=UpdateStripeInfoParam(secret_key=secret_key)
    )
    return True


def cleanup_stripe_state() -> None:
    """Stripeの状態をクリーンアップ（エラーは無視）"""
    if not is_stripe_configured():
        return
    
    from saasus_sdk_python.src.billing.api.stripe_api import StripeApi
    from saasus_sdk_python.client.billing_client import SignedBillingApiClient
    
    try:
        client = SignedBillingApiClient()
        stripe_api = StripeApi(client)
        stripe_api.delete_stripe_tenant_and_pricing()
    except Exception:
        pass  # 既にクリーンな状態の場合はエラーを無視

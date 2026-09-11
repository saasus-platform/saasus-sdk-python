"""
Auth E2E test state management

JavaScriptのstate.tsから移植したState管理機能
"""

from typing import Any, Dict, Optional
from dataclasses import dataclass, field

from tests.e2e.auth.helpers import (
    unique_email,
    unique_string,
    unique_env_id,
    get_default_password
)


@dataclass
class AuthStoryState:
    """Auth E2Eテストのステート管理
    
    Attributes:
        initialized: 初期化済みフラグ
        saas_user_id: SaaSユーザーID
        saas_user_email: SaaSユーザーメールアドレス
        saas_user_password: SaaSユーザーパスワード
        role_name: ロール名
        role_display_name: ロール表示名
        user_attribute_name: ユーザー属性名
        tenant_attribute_name: テナント属性名
        env_id: 環境ID
        env_name: 環境名
        env_display_name: 環境表示名
        tenant_id: テナントID
        tenant_name: テナント名
        tenant_staff_email: テナントスタッフメールアドレス
        tenant_user_id: テナントユーザーID
        tenant_user_email: テナントユーザーメールアドレス
        tenant_attributes: テナント属性
        tenant_user_attributes: テナントユーザー属性
    """
    initialized: bool = False
    saas_user_id: Optional[str] = None
    saas_user_email: Optional[str] = None
    saas_user_password: Optional[str] = None
    role_name: Optional[str] = None
    role_display_name: Optional[str] = None
    user_attribute_name: Optional[str] = None
    tenant_attribute_name: Optional[str] = None
    env_id: Optional[int] = None
    env_name: Optional[str] = None
    env_display_name: Optional[str] = None
    tenant_id: Optional[str] = None
    tenant_name: Optional[str] = None
    tenant_staff_email: Optional[str] = None
    tenant_user_id: Optional[str] = None
    tenant_user_email: Optional[str] = None
    tenant_attributes: Dict[str, Any] = field(default_factory=dict)
    tenant_user_attributes: Dict[str, Any] = field(default_factory=dict)


def ensure_auth_state(vars: Dict[str, Any]) -> AuthStoryState:
    """Auth Stateを初期化または取得
    
    Args:
        vars: ストーリー変数辞書
        
    Returns:
        初期化されたAuthStoryState
    """
    state_key = "auth_story_state"
    
    if state_key not in vars:
        vars[state_key] = AuthStoryState()
    
    state = vars[state_key]
    
    if not state.initialized:
        _initialize_state(state)
    
    return state


def _initialize_state(state: AuthStoryState) -> None:
    """Stateを初期化
    
    Args:
        state: AuthStoryState
    """
    state.saas_user_email = unique_email("saas-user")
    state.saas_user_password = get_default_password()
    state.role_name = unique_string("role")
    state.role_display_name = f"Auth E2E Role {state.role_name}"
    state.user_attribute_name = unique_string("user-attr")
    state.tenant_attribute_name = unique_string("tenant-attr")
    state.env_id = unique_env_id()
    state.env_name = unique_string("env")
    state.env_display_name = f"Auth E2E Env {state.env_name}"
    state.tenant_name = unique_string("tenant")
    state.tenant_staff_email = unique_email("tenant-staff")
    state.tenant_user_email = state.saas_user_email
    state.initialized = True


class StateManager:
    """State管理とクリーンアップを提供するマネージャー
    
    JavaScriptのStateManagerから移植
    """
    
    @staticmethod
    def cleanup_all_resources() -> None:
        """全リソースをクリーンアップ
        
        Note:
            実際のクリーンアップロジックは後で実装
        """
        print("🧹 Cleaning up all resources...")
    
    @staticmethod
    def handle_story_failure(error: Exception) -> None:
        """ストーリー失敗時のクリーンアップ
        
        Args:
            error: 発生したエラー
        """
        print(f"❌ Story failed: {error}")
        StateManager.cleanup_all_resources()

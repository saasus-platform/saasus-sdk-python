"""Integration (EventBridge) E2E test state management.

テスト前後でEventBridge設定を削除してクリーンな状態を保ちます。
404（未設定）は無視します。
"""

from typing import Any, Optional

LOG_PREFIX = "[Integration E2E]"


def _get_status(error: Exception) -> Optional[int]:
    return getattr(error, "status", None)


def _is_ignorable_delete_error(error: Exception) -> bool:
    return _get_status(error) == 404


def delete_settings_quietly(client: Any) -> None:
    """EventBridge設定を削除。未設定(404)は無視する。

    無視可能(404)以外の削除失敗は再送出し、クリーンアップ漏れをCIで可視化する。
    """
    try:
        client.delete_event_bridge_settings()
        print(f"{LOG_PREFIX} Deleted existing EventBridge settings.")
    except Exception as error:  # noqa: BLE001
        if _is_ignorable_delete_error(error):
            print(f"{LOG_PREFIX} No EventBridge settings to delete.")
            return
        print(f"{LOG_PREFIX} Failed to clean up EventBridge settings: {error}")
        raise


def ensure_integration_test_preconditions(client: Any) -> None:
    """テスト開始前に既存のEventBridge設定を削除する。"""
    delete_settings_quietly(client)


class StateManager:
    """State管理とクリーンアップを提供するマネージャー"""

    @staticmethod
    def cleanup_all_resources() -> None:
        print("\n🧹 Cleaning up integration resources...")

    @staticmethod
    def handle_story_failure(error: Exception) -> None:
        print(f"❌ Story failed: {error}")
        StateManager.cleanup_all_resources()

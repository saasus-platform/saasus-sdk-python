"""Communication (Feedback) E2E test state management.

テストで作成したフィードバック(タイトルのプレフィックスで判定)を
テスト前後で削除してクリーンな状態を保ちます。
"""

from typing import Any, Optional

from tests.e2e.communication.helpers import COMMUNICATION_TITLE_PREFIX

LOG_PREFIX = "[Communication E2E]"


def _get_status(error: Exception) -> Optional[int]:
    return getattr(error, "status", None)


def _is_ignorable_delete_error(error: Exception) -> bool:
    return _get_status(error) == 404


def _get_field(obj: Any, field: str) -> Any:
    if obj is None:
        return None
    if isinstance(obj, dict):
        return obj.get(field)
    if hasattr(obj, field):
        return getattr(obj, field)
    if hasattr(obj, "get"):
        try:
            return obj.get(field)
        except Exception:
            return None
    return None


def _is_test_feedback(feedback: Any) -> bool:
    title = _get_field(feedback, "feedback_title")
    return isinstance(title, str) and title.startswith(COMMUNICATION_TITLE_PREFIX)


def cleanup_communication_test_artifacts(client: Any) -> None:
    """テスト用プレフィックスのフィードバックを全削除する。

    無視可能(404)以外の削除失敗は、残りの削除を試みた上で再送出し、
    クリーンアップ漏れをCIで可視化する。
    """
    response = client.get_feedbacks()

    feedbacks = _get_field(response, "feedbacks") or []
    if not isinstance(feedbacks, list):
        return

    pending_error: Optional[Exception] = None
    for feedback in feedbacks:
        feedback_id = _get_field(feedback, "id")
        if not feedback_id or not _is_test_feedback(feedback):
            continue
        try:
            client.delete_feedback(feedback_id)
            print(f"{LOG_PREFIX} Deleted leftover test feedback {feedback_id}.")
        except Exception as error:  # noqa: BLE001
            if _is_ignorable_delete_error(error):
                print(f"{LOG_PREFIX} Feedback {feedback_id} already absent.")
                continue
            print(f"{LOG_PREFIX} Failed to delete feedback {feedback_id}: {error}")
            if pending_error is None:
                pending_error = error

    if pending_error is not None:
        raise pending_error


def ensure_communication_test_preconditions(client: Any) -> None:
    cleanup_communication_test_artifacts(client)


class StateManager:
    """State管理とクリーンアップを提供するマネージャー"""

    @staticmethod
    def cleanup_all_resources() -> None:
        print("\n🧹 Cleaning up communication resources...")

    @staticmethod
    def handle_story_failure(error: Exception) -> None:
        print(f"❌ Story failed: {error}")
        StateManager.cleanup_all_resources()

"""Communication (Feedback) E2E test validation functions.

JavaScriptのcommunication/validation.tsを参考にした検証関数群。
dict / モデルオブジェクトの両方のレスポンス形式に対応します。
"""

from typing import Any


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


def validate_feedback_list(response: Any) -> bool:
    if response is None:
        print("Feedbacks payload is empty")
        return False
    feedbacks = _get_field(response, "feedbacks")
    if not isinstance(feedbacks, list):
        print("Feedbacks payload does not include feedbacks array")
        return False
    return True


def validate_feedback(response: Any) -> bool:
    if response is None:
        print("Feedback payload is empty")
        return False
    if not _get_field(response, "id"):
        print("Feedback payload does not include id")
        return False
    if not _get_field(response, "feedback_title"):
        print("Feedback payload does not include feedback_title")
        return False
    if not _get_field(response, "feedback_description"):
        print("Feedback payload does not include feedback_description")
        return False
    if not _get_field(response, "user_id"):
        print("Feedback payload does not include user_id")
        return False
    return True


def validate_feedback_or_empty(response: Any) -> bool:
    if response is None:
        return True
    return validate_feedback(response)


def validate_comment(response: Any) -> bool:
    if response is None:
        print("Comment payload is empty")
        return False
    if not _get_field(response, "id"):
        print("Comment payload does not include id")
        return False
    if not _get_field(response, "body"):
        print("Comment payload does not include body")
        return False
    return True


def validate_comment_or_empty(response: Any) -> bool:
    if response is None:
        return True
    return validate_comment(response)


def validate_votes(response: Any) -> bool:
    if response is None:
        print("Votes payload is empty")
        return False
    users = _get_field(response, "users")
    if not isinstance(users, list):
        print("Votes payload does not include users array")
        return False
    count = _get_field(response, "count")
    if not isinstance(count, int):
        print("Votes payload does not include count")
        return False
    return True


def validate_votes_or_empty(response: Any) -> bool:
    if response is None:
        return True
    return validate_votes(response)


def validate_delete_response(_response: Any = None) -> bool:
    return True

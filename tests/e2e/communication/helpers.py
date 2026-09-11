"""Communication (Feedback) E2E test helper functions.

JavaScriptのcommunication/helpers.tsを参考にしたパラメータビルダー群。
create_feedback / create_feedback_comment のレスポンスをstore_asで保存し、
後続ステップでfeedback_id / comment_idを再利用します。
"""

import os
from datetime import datetime, timezone
from typing import Any, Dict

from saasus_sdk_python.src.communication.models.create_feedback_comment_param import (
    CreateFeedbackCommentParam,
)
from saasus_sdk_python.src.communication.models.create_feedback_param import CreateFeedbackParam
from saasus_sdk_python.src.communication.models.create_vote_user_param import CreateVoteUserParam
from saasus_sdk_python.src.communication.models.update_feedback_comment_param import (
    UpdateFeedbackCommentParam,
)
from saasus_sdk_python.src.communication.models.update_feedback_param import UpdateFeedbackParam
from saasus_sdk_python.src.communication.models.update_feedback_status_param import (
    UpdateFeedbackStatusParam,
)

COMMUNICATION_TITLE_PREFIX = "py-sdk-e2e-feedback"

# store_asで保存されるレスポンスの変数キー
FEEDBACK_STATE_KEY = "communication_feedback"
COMMENT_STATE_KEY = "communication_comment"

DEFAULT_TEST_USER_ID = "00000000-0000-0000-0000-000000000000"


def get_test_user_id() -> str:
    return os.getenv("TEST_USER_ID") or DEFAULT_TEST_USER_ID


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


def _require_feedback_id(vars: Dict[str, Any]) -> str:
    feedback = vars.get(FEEDBACK_STATE_KEY)
    feedback_id = _get_field(feedback, "id")
    if not feedback_id:
        raise ValueError("feedback_id is not available in shared state")
    return feedback_id


def _require_comment_id(vars: Dict[str, Any]) -> str:
    comment = vars.get(COMMENT_STATE_KEY)
    comment_id = _get_field(comment, "id")
    if not comment_id:
        raise ValueError("comment_id is not available in shared state")
    return comment_id


# ---- payload factories -------------------------------------------------

def _unique_title() -> str:
    stamp = datetime.now(tz=timezone.utc).isoformat()
    return f"{COMMUNICATION_TITLE_PREFIX}-{stamp}"


def create_feedback_payload() -> CreateFeedbackParam:
    return CreateFeedbackParam(
        user_id=get_test_user_id(),
        feedback_title=_unique_title(),
        feedback_description="Python SDK communication E2E feedback",
    )


def update_feedback_payload() -> UpdateFeedbackParam:
    # タイトル更新後もクリーンアップ(プレフィックス判定)で回収できるように
    # COMMUNICATION_TITLE_PREFIX を維持する。
    return UpdateFeedbackParam(
        feedback_title=f"{COMMUNICATION_TITLE_PREFIX}-updated",
        feedback_description="Updated feedback description from PY E2E",
    )


def update_feedback_status_payload() -> UpdateFeedbackStatusParam:
    return UpdateFeedbackStatusParam(status=1)


def create_feedback_comment_payload() -> CreateFeedbackCommentParam:
    return CreateFeedbackCommentParam(body="Python SDK communication E2E comment")


def update_feedback_comment_payload() -> UpdateFeedbackCommentParam:
    return UpdateFeedbackCommentParam(body="Updated Python SDK communication E2E comment")


def create_vote_payload() -> CreateVoteUserParam:
    return CreateVoteUserParam(user_id=get_test_user_id())


# ---- param builders (Step.params callables) ----------------------------

def build_get_feedbacks_params(_vars: Dict[str, Any]) -> Dict[str, Any]:
    return {}


def build_create_feedback_params(_vars: Dict[str, Any]) -> Dict[str, Any]:
    return {"create_feedback_param": create_feedback_payload()}


def build_get_feedback_params(vars: Dict[str, Any]) -> Dict[str, Any]:
    return {"feedback_id": _require_feedback_id(vars)}


def build_update_feedback_params(vars: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "feedback_id": _require_feedback_id(vars),
        "update_feedback_param": update_feedback_payload(),
    }


def build_update_feedback_status_params(vars: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "feedback_id": _require_feedback_id(vars),
        "update_feedback_status_param": update_feedback_status_payload(),
    }


def build_create_comment_params(vars: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "feedback_id": _require_feedback_id(vars),
        "create_feedback_comment_param": create_feedback_comment_payload(),
    }


def build_get_comment_params(vars: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "feedback_id": _require_feedback_id(vars),
        "comment_id": _require_comment_id(vars),
    }


def build_update_comment_params(vars: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "feedback_id": _require_feedback_id(vars),
        "comment_id": _require_comment_id(vars),
        "update_feedback_comment_param": update_feedback_comment_payload(),
    }


def build_create_vote_params(vars: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "feedback_id": _require_feedback_id(vars),
        "create_vote_user_param": create_vote_payload(),
    }


def build_delete_vote_params(vars: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "feedback_id": _require_feedback_id(vars),
        "user_id": get_test_user_id(),
    }


def build_delete_comment_params(vars: Dict[str, Any]) -> Dict[str, Any]:
    return build_get_comment_params(vars)


def build_delete_feedback_params(vars: Dict[str, Any]) -> Dict[str, Any]:
    return {"feedback_id": _require_feedback_id(vars)}

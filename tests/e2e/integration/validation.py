"""Integration (EventBridge) E2E test validation functions.

JavaScriptのintegration/validation.tsを参考にした検証関数群。
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


def _has_settings(response: Any) -> bool:
    if response is None:
        return False
    return bool(_get_field(response, "aws_account_id") and _get_field(response, "aws_region"))


def validate_event_bridge_settings_response(response: Any, expect_configured: bool) -> bool:
    """EventBridge設定レスポンスを検証。

    expect_configured=True の場合は aws_account_id / aws_region が存在することを要求。
    それ以外は未設定レスポンスでも許容する（ハードエラーが無ければOK）。
    """
    if expect_configured:
        if not _has_settings(response):
            print("EventBridgeSettings payload does not include aws_account_id/aws_region")
            return False
        return True
    return True

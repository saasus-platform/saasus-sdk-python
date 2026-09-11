"""ApiLog E2E test validation functions.

JavaScriptのapilogs/validation.tsを参考にした検証関数群。
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


def validate_api_logs_list(response: Any) -> bool:
    """ApiLogsレスポンスがapi_logs配列を持ち、少なくとも1件含むことを検証。"""
    if response is None:
        print("ApiLogs payload is empty")
        return False

    api_logs = _get_field(response, "api_logs")
    if not isinstance(api_logs, list):
        print("ApiLogs payload does not include api_logs array")
        return False
    if len(api_logs) == 0:
        print("ApiLogs payload does not contain any log entries")
        return False
    return True


def validate_api_log_entry(response: Any) -> bool:
    """ApiLogレスポンスがapi_log_idを持つことを検証。"""
    if response is None:
        print("ApiLog payload is empty")
        return False
    if not _get_field(response, "api_log_id"):
        print("ApiLog payload is missing api_log_id")
        return False
    return True

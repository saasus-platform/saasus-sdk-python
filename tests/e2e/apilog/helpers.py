"""ApiLog E2E test helper functions.

JavaScriptのapilogs/helpers.tsを参考にしたパラメータビルダー群。
get_logsで取得した最初のログ情報を後続ステップで再利用します。
"""

from datetime import date, datetime, timezone
from typing import Any, Dict

# store_asで保存されるApiLogsレスポンスの変数キー
APILOG_LIST_KEY = "apilog_list"


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


def _first_log(vars: Dict[str, Any]) -> Any:
    payload = vars.get(APILOG_LIST_KEY)
    if payload is None:
        raise ValueError("ApiLogs payload is not available in shared state")
    api_logs = _get_field(payload, "api_logs")
    if not isinstance(api_logs, list) or len(api_logs) == 0:
        raise ValueError("ApiLogs payload does not include any api_logs entries")
    return api_logs[0]


def create_empty_get_logs_params() -> Dict[str, Any]:
    """パラメータ無しのget_logs呼び出し。"""
    return {}


def create_get_logs_with_query_params(vars: Dict[str, Any]) -> Dict[str, Any]:
    """保存済みログのcreated_date/created_at/cursorを用いたget_logs呼び出し。

    パラメータは文字列で渡す（SDKの@validate_argumentsがdate/datetimeへ
    coerceする）。これによりスナップショットのJSONシリアライズも問題なく動作する。
    """
    first_log = _first_log(vars)

    created_date_raw = _get_field(first_log, "created_date")
    if not created_date_raw:
        raise ValueError("created_date is not populated on the stored api log")

    created_at_raw = _get_field(first_log, "created_at")
    if created_at_raw is None:
        raise ValueError("created_at is not populated on the stored api log")

    params: Dict[str, Any] = {
        "created_date": _to_date_str(created_date_raw),
        "created_at": _to_datetime_str(created_at_raw),
    }

    payload = vars.get(APILOG_LIST_KEY)
    cursor = _get_field(payload, "cursor")
    if cursor:
        params["cursor"] = cursor

    return params


def create_get_log_params(vars: Dict[str, Any]) -> Dict[str, Any]:
    """保存済みログのapi_log_idを用いたget_log呼び出し。"""
    first_log = _first_log(vars)
    api_log_id = _get_field(first_log, "api_log_id")
    if not api_log_id:
        raise ValueError("api_log_id is not available in shared state")
    return {"api_log_id": api_log_id}


def _to_date_str(value: Any) -> str:
    """created_dateを 'YYYY-MM-DD' 文字列に正規化する。"""
    if isinstance(value, (date, datetime)):
        return value.strftime("%Y-%m-%d")
    return str(value)


def _to_datetime_str(value: Any) -> str:
    """created_at(エポック秒 or datetime)をISO8601(UTC)文字列に正規化する。"""
    if isinstance(value, datetime):
        dt = value
    else:
        # created_atはエポック秒(int)を想定
        dt = datetime.fromtimestamp(int(value), tz=timezone.utc)
    return dt.isoformat()

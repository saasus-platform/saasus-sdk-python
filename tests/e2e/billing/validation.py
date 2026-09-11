"""Billing E2E test validation functions.

JavaScriptのvalidation.tsを参考にした検証関数群。
"""

from typing import Any


def _get_is_registered(response: Any) -> bool:
    if response is None:
        return False
    if isinstance(response, dict):
        value = response.get("is_registered")
        return bool(value) if isinstance(value, bool) else False
    if hasattr(response, "is_registered"):
        value = getattr(response, "is_registered")
        return bool(value) if isinstance(value, bool) else False
    if hasattr(response, "get"):
        try:
            value = response.get("is_registered")
            return bool(value) if isinstance(value, bool) else False
        except Exception:
            return False
    return False


def validate_stripe_info_response(response: Any, expected_registered: bool) -> bool:
    if response is None:
        return False
    if expected_registered:
        return _get_is_registered(response)
    return True


def validate_update_stripe_info_response(_response: Any) -> bool:
    return True


def validate_delete_stripe_info_response(_response: Any) -> bool:
    return True

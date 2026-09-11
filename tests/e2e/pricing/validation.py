"""Pricing E2E test validation functions.

JavaScriptのvalidation.tsを参考にした検証関数群。
"""

from typing import Any, List


def _unwrap(obj: Any) -> Any:
    if hasattr(obj, "actual_instance") and getattr(obj, "actual_instance") is not None:
        return getattr(obj, "actual_instance")
    return obj


def _get(obj: Any, key: str) -> Any:
    obj = _unwrap(obj)
    if obj is None:
        return None
    if isinstance(obj, dict):
        return obj.get(key)
    if hasattr(obj, key):
        return getattr(obj, key)
    if hasattr(obj, "get"):
        try:
            return obj.get(key)
        except Exception:
            return None
    return None


def _is_non_empty_string(value: Any) -> bool:
    if isinstance(value, str):
        return len(value.strip()) > 0
    if hasattr(value, "value") and isinstance(value.value, str):
        return len(value.value.strip()) > 0
    return False


def _is_number(value: Any) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def _is_bool(value: Any) -> bool:
    return isinstance(value, bool)


def _ensure_array_property(container: Any, keys: List[str], validator) -> bool:
    for key in keys:
        value = _get(container, key)
        if isinstance(value, list):
            return all(validator(item) for item in value)
    return False


def _ensure_optional_array(value: Any, validator) -> bool:
    if value is None:
        return True
    if isinstance(value, list):
        return all(validator(item) for item in value)
    return False


def _is_empty_response(response: Any) -> bool:
    if response is None:
        return True
    if isinstance(response, str):
        return response.strip() == ""
    if isinstance(response, dict):
        return len(response) == 0
    if isinstance(response, list):
        return len(response) == 0
    return False


def ensure_pricing_unit(unit: Any) -> bool:
    unit = _unwrap(unit)
    required_fields = [
        "id",
        "name",
        "display_name",
        "description",
        "currency",
        "type",
        "recurring_interval",
    ]
    for field in required_fields:
        if not _is_non_empty_string(_get(unit, field)):
            return False
    if not _is_number(_get(unit, "unit_amount")):
        return False
    used = _get(unit, "used")
    if used is not None and not _is_bool(used):
        return False
    return True


def ensure_pricing_menu(menu: Any) -> bool:
    menu = _unwrap(menu)
    for field in ["id", "name", "display_name", "description"]:
        if not _is_non_empty_string(_get(menu, field)):
            return False
    used = _get(menu, "used")
    if used is not None and not _is_bool(used):
        return False
    units = _get(menu, "units")
    if not _ensure_optional_array(units, ensure_pricing_unit):
        return False
    return True


def ensure_pricing_plan(plan: Any) -> bool:
    plan = _unwrap(plan)
    for field in ["id", "name", "display_name", "description"]:
        if not _is_non_empty_string(_get(plan, field)):
            return False
    menus = _get(plan, "pricing_menus")
    if not _ensure_optional_array(menus, ensure_pricing_menu):
        return False
    used = _get(plan, "used")
    if used is not None and not _is_bool(used):
        return False
    return True


def ensure_metering_unit(unit: Any) -> bool:
    unit = _unwrap(unit)
    for field in ["id", "unit_name", "display_name", "description"]:
        if not _is_non_empty_string(_get(unit, field)):
            return False
    aggregate_usage = _get(unit, "aggregate_usage")
    if aggregate_usage is not None and not _is_non_empty_string(aggregate_usage):
        return False
    used = _get(unit, "used")
    if used is not None and not _is_bool(used):
        return False
    return True


def ensure_tax_rate(tax: Any) -> bool:
    tax = _unwrap(tax)
    for field in ["id", "name", "display_name", "description", "country"]:
        if not _is_non_empty_string(_get(tax, field)):
            return False
    if not _is_number(_get(tax, "percentage")):
        return False
    inclusive = _get(tax, "inclusive")
    if inclusive is not None and not _is_bool(inclusive):
        return False
    return True


def validate_pricing_plans_response(response: Any) -> bool:
    return _ensure_array_property(response, ["pricing_plans"], ensure_pricing_plan)


def validate_pricing_plan_response(response: Any) -> bool:
    return ensure_pricing_plan(response)


def validate_create_pricing_plan_response(response: Any) -> bool:
    return validate_pricing_plan_response(response)


def validate_delete_response(response: Any) -> bool:
    return _is_empty_response(response)


def validate_pricing_menus_response(response: Any) -> bool:
    return _ensure_array_property(response, ["pricing_menus"], ensure_pricing_menu)


def validate_pricing_menu_response(response: Any) -> bool:
    return ensure_pricing_menu(response)


def validate_create_pricing_menu_response(response: Any) -> bool:
    return validate_pricing_menu_response(response)


def validate_pricing_units_response(response: Any) -> bool:
    return _ensure_array_property(response, ["units", "pricing_units"], ensure_pricing_unit)


def validate_pricing_unit_response(response: Any) -> bool:
    return ensure_pricing_unit(response)


def validate_create_pricing_unit_response(response: Any) -> bool:
    return ensure_pricing_unit(response)


def validate_metering_units_response(response: Any) -> bool:
    return _ensure_array_property(response, ["units", "metering_units"], ensure_metering_unit)


def validate_create_metering_unit_response(response: Any) -> bool:
    return ensure_metering_unit(response)


def validate_tax_rates_response(response: Any) -> bool:
    return _ensure_array_property(response, ["tax_rates"], ensure_tax_rate)


def validate_create_tax_rate_response(response: Any) -> bool:
    return ensure_tax_rate(response)


def validate_update_pricing_unit_response(response: Any) -> bool:
    return _is_empty_response(response)


def validate_update_pricing_menu_response(response: Any) -> bool:
    return _is_empty_response(response)


def validate_update_pricing_plan_response(response: Any) -> bool:
    return _is_empty_response(response)


def validate_update_pricing_plans_used_response(response: Any) -> bool:
    return _is_empty_response(response)


def validate_update_tax_rate_response(response: Any) -> bool:
    return _is_empty_response(response)

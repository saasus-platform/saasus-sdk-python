"""Pricing E2E test helper functions."""

from dataclasses import dataclass
import random
import time
from typing import Any, Dict, Optional

PRICING_E2E_PREFIX = "py-sdk-pricing-e2e"
STATE_KEY = "pricing_story_state"


@dataclass
class PricingStoryState:
    initialized: bool = False
    metering_unit_name: Optional[str] = None
    pricing_unit_name: Optional[str] = None
    menu_detach_pricing_unit_name: Optional[str] = None
    pricing_menu_name: Optional[str] = None
    pricing_plan_name: Optional[str] = None
    tax_rate_name: Optional[str] = None


def ensure_state(vars: Dict[str, Any]) -> PricingStoryState:
    if STATE_KEY not in vars:
        vars[STATE_KEY] = PricingStoryState()
    return vars[STATE_KEY]


def require_state_value(state: PricingStoryState, key: str, description: str) -> Any:
    value = getattr(state, key, None)
    if not value:
        raise ValueError(f"Missing {description} in story state")
    return value


def unique_name(base_name: str) -> str:
    timestamp = int(time.time() * 1000)
    random_suffix = random.randint(0, 9999)
    return f"{PRICING_E2E_PREFIX}-{base_name}-{timestamp}-{random_suffix}"


def _unwrap_actual_instance(obj: Any) -> Any:
    if hasattr(obj, "actual_instance") and getattr(obj, "actual_instance") is not None:
        return getattr(obj, "actual_instance")
    return obj


def get_field(obj: Any, field: str) -> Any:
    obj = _unwrap_actual_instance(obj)
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


test_data = {
    "metering_unit": {
        "unit_name": "user_counts",
        "display_name": "User Count",
        "description": "Metering unit for user count",
        "aggregate_usage": "max",
    },
    "pricing_unit": {
        "name": "fixed-unit",
        "display_name": "Fixed Unit",
        "description": "Fixed unit description",
        "type": "fixed",
        "currency": "JPY",
        "unit_amount": 300,
        "recurring_interval": "month",
    },
    "pricing_menu": {
        "name": "fixed-menu",
        "display_name": "Fixed Unit Menu",
        "description": "Menu description",
    },
    "pricing_plan": {
        "name": "plan-name",
        "display_name": "Sample Plan",
        "description": "Plan description",
    },
    "tax_rate": {
        "name": "tax-rate",
        "display_name": "Consumption Tax",
        "description": "Sample tax rate",
        "percentage": 10,
        "country": "JP",
        "inclusive": False,
    },
}

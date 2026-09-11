"""Pricing module story definitions."""

from typing import List, Optional
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from testlib.models import Story, Step
from tests.e2e.pricing.helpers import (
    ensure_state,
    require_state_value,
    unique_name,
    test_data,
    get_field,
)
from tests.e2e.pricing.validation import (
    validate_create_metering_unit_response,
    validate_create_pricing_menu_response,
    validate_create_pricing_plan_response,
    validate_create_pricing_unit_response,
    validate_create_tax_rate_response,
    validate_delete_response,
    validate_metering_units_response,
    validate_pricing_menu_response,
    validate_pricing_menus_response,
    validate_pricing_plan_response,
    validate_pricing_plans_response,
    validate_pricing_unit_response,
    validate_pricing_units_response,
    validate_tax_rates_response,
    validate_update_pricing_menu_response,
    validate_update_pricing_plan_response,
    validate_update_pricing_plans_used_response,
    validate_update_pricing_unit_response,
    validate_update_tax_rate_response,
)

from saasus_sdk_python.src.pricing.models.aggregate_usage import AggregateUsage
from saasus_sdk_python.src.pricing.models.currency import Currency
from saasus_sdk_python.src.pricing.models.metering_unit_props import MeteringUnitProps
from saasus_sdk_python.src.pricing.models.pricing_fixed_unit_for_save import PricingFixedUnitForSave
from saasus_sdk_python.src.pricing.models.pricing_unit_for_save import PricingUnitForSave
from saasus_sdk_python.src.pricing.models.recurring_interval import RecurringInterval
from saasus_sdk_python.src.pricing.models.save_pricing_menu_param import SavePricingMenuParam
from saasus_sdk_python.src.pricing.models.save_pricing_plan_param import SavePricingPlanParam
from saasus_sdk_python.src.pricing.models.tax_rate_props import TaxRateProps
from saasus_sdk_python.src.pricing.models.unit_type import UnitType
from saasus_sdk_python.src.pricing.models.update_pricing_plans_used_param import UpdatePricingPlansUsedParam
from saasus_sdk_python.src.pricing.models.update_tax_rate_param import UpdateTaxRateParam

MODULE = "pricing"


def _as_enum(enum_cls, value):
    if isinstance(value, enum_cls):
        return value
    return enum_cls(value)


def _get_required_id(vars_dict, key: str, description: str) -> str:
    obj = vars_dict.get(key)
    value = get_field(obj, "id")
    if not value:
        raise ValueError(f"Missing {description} in story state")
    return value


def _build_pricing_fixed_unit_for_save(name: str, display_name: str, description: str, unit_amount: int) -> PricingUnitForSave:
    fixed_unit = PricingFixedUnitForSave(
        name=name,
        display_name=display_name,
        description=description,
        type=_as_enum(UnitType, test_data["pricing_unit"]["type"]),
        currency=_as_enum(Currency, test_data["pricing_unit"]["currency"]),
        unit_amount=unit_amount,
        recurring_interval=_as_enum(RecurringInterval, test_data["pricing_unit"]["recurring_interval"]),
    )
    return PricingUnitForSave(actual_instance=fixed_unit)


def build_create_metering_unit_step() -> Step:
    def _params(vars_dict):
        state = ensure_state(vars_dict)
        unit_name = unique_name(test_data["metering_unit"]["unit_name"])
        state.metering_unit_name = unit_name
        return {
            "body": MeteringUnitProps(
                unit_name=unit_name,
                display_name=test_data["metering_unit"]["display_name"],
                description=test_data["metering_unit"]["description"],
                aggregate_usage=_as_enum(AggregateUsage, test_data["metering_unit"]["aggregate_usage"]),
            )
        }

    return Step(
        method_name="create_metering_unit",
        description="Create Metering Unit",
        params=_params,
        expected_status=201,
        validation_func=validate_create_metering_unit_response,
        store_as="metering_unit",
    )


def build_get_metering_units_step() -> Step:
    return Step(
        method_name="get_metering_units",
        description="Get Metering Units",
        params={},
        expected_status=200,
        validation_func=validate_metering_units_response,
    )


def build_create_pricing_unit_step(store_as_key: str, name_state_key: str, description_suffix: str = "") -> Step:
    def _params(vars_dict):
        state = ensure_state(vars_dict)
        name = unique_name(test_data["pricing_unit"]["name"])
        setattr(state, name_state_key, name)
        display_name = test_data["pricing_unit"]["display_name"]
        description = test_data["pricing_unit"]["description"]
        if description_suffix:
            display_name = f"{display_name} {description_suffix}".strip()
            description = f"{description} {description_suffix}".strip()
        return {
            "body": _build_pricing_fixed_unit_for_save(
                name=name,
                display_name=display_name,
                description=description,
                unit_amount=test_data["pricing_unit"]["unit_amount"],
            )
        }

    return Step(
        method_name="create_pricing_unit",
        description="Create Pricing Unit",
        params=_params,
        expected_status=201,
        validation_func=validate_create_pricing_unit_response,
        store_as=store_as_key,
    )


def build_update_pricing_unit_step() -> Step:
    def _params(vars_dict):
        state = ensure_state(vars_dict)
        pricing_unit_id = _get_required_id(vars_dict, "pricing_unit", "pricing unit id")
        name = require_state_value(state, "pricing_unit_name", "pricing unit name")
        return {
            "pricing_unit_id": pricing_unit_id,
            "body": _build_pricing_fixed_unit_for_save(
                name=name,
                display_name=f"{test_data['pricing_unit']['display_name']} (updated)",
                description=f"{test_data['pricing_unit']['description']} (updated)",
                unit_amount=test_data["pricing_unit"]["unit_amount"] + 100,
            ),
        }

    return Step(
        method_name="update_pricing_unit",
        description="Update Pricing Unit",
        params=_params,
        expected_status=200,
        validation_func=validate_update_pricing_unit_response,
    )


def build_get_pricing_units_step() -> Step:
    return Step(
        method_name="get_pricing_units",
        description="Get Pricing Units",
        params={},
        expected_status=200,
        validation_func=validate_pricing_units_response,
    )


def build_get_pricing_unit_step() -> Step:
    def _params(vars_dict):
        pricing_unit_id = _get_required_id(vars_dict, "pricing_unit", "pricing unit id")
        return {"pricing_unit_id": pricing_unit_id}

    return Step(
        method_name="get_pricing_unit",
        description="Get Pricing Unit",
        params=_params,
        expected_status=200,
        validation_func=validate_pricing_unit_response,
    )


def build_create_pricing_menu_step(unit_key: str, store_as_key: str, name_state_key: str) -> Step:
    def _params(vars_dict):
        state = ensure_state(vars_dict)
        unit_id = _get_required_id(vars_dict, unit_key, "pricing unit id")
        name = unique_name(test_data["pricing_menu"]["name"])
        setattr(state, name_state_key, name)
        return {
            "body": SavePricingMenuParam(
                name=name,
                display_name=test_data["pricing_menu"]["display_name"],
                description=test_data["pricing_menu"]["description"],
                unit_ids=[unit_id],
            )
        }

    return Step(
        method_name="create_pricing_menu",
        description="Create Pricing Menu",
        params=_params,
        expected_status=201,
        validation_func=validate_create_pricing_menu_response,
        store_as=store_as_key,
    )


def build_get_pricing_menus_step() -> Step:
    return Step(
        method_name="get_pricing_menus",
        description="Get Pricing Menus",
        params={},
        expected_status=200,
        validation_func=validate_pricing_menus_response,
    )


def build_get_pricing_menu_step() -> Step:
    def _params(vars_dict):
        menu_id = _get_required_id(vars_dict, "pricing_menu", "pricing menu id")
        return {"menu_id": menu_id}

    return Step(
        method_name="get_pricing_menu",
        description="Get Pricing Menu",
        params=_params,
        expected_status=200,
        validation_func=validate_pricing_menu_response,
    )


def build_update_pricing_menu_step(unit_key: str, name_state_key: str) -> Step:
    def _params(vars_dict):
        state = ensure_state(vars_dict)
        menu_id = _get_required_id(vars_dict, "pricing_menu", "pricing menu id")
        name = require_state_value(state, name_state_key, "pricing menu name")
        unit_id = _get_required_id(vars_dict, unit_key, "pricing unit id")
        return {
            "menu_id": menu_id,
            "body": SavePricingMenuParam(
                name=name,
                display_name=f"{test_data['pricing_menu']['display_name']} (updated)",
                description=f"{test_data['pricing_menu']['description']} (updated)",
                unit_ids=[unit_id],
            ),
        }

    return Step(
        method_name="update_pricing_menu",
        description="Update Pricing Menu",
        params=_params,
        expected_status=200,
        validation_func=validate_update_pricing_menu_response,
    )


def build_create_pricing_plan_step() -> Step:
    def _params(vars_dict):
        state = ensure_state(vars_dict)
        menu_id = _get_required_id(vars_dict, "pricing_menu", "pricing menu id")
        name = unique_name(test_data["pricing_plan"]["name"])
        state.pricing_plan_name = name
        return {
            "body": SavePricingPlanParam(
                name=name,
                display_name=test_data["pricing_plan"]["display_name"],
                description=test_data["pricing_plan"]["description"],
                menu_ids=[menu_id],
            )
        }

    return Step(
        method_name="create_pricing_plan",
        description="Create Pricing Plan",
        params=_params,
        expected_status=201,
        validation_func=validate_create_pricing_plan_response,
        store_as="pricing_plan",
    )


def build_get_pricing_plans_step() -> Step:
    return Step(
        method_name="get_pricing_plans",
        description="Get Pricing Plans",
        params={},
        expected_status=200,
        validation_func=validate_pricing_plans_response,
    )


def build_get_pricing_plan_step() -> Step:
    def _params(vars_dict):
        plan_id = _get_required_id(vars_dict, "pricing_plan", "pricing plan id")
        return {"plan_id": plan_id}

    return Step(
        method_name="get_pricing_plan",
        description="Get Pricing Plan",
        params=_params,
        expected_status=200,
        validation_func=validate_pricing_plan_response,
    )


def build_update_pricing_plan_step() -> Step:
    def _params(vars_dict):
        state = ensure_state(vars_dict)
        plan_id = _get_required_id(vars_dict, "pricing_plan", "pricing plan id")
        menu_id = _get_required_id(vars_dict, "pricing_menu", "pricing menu id")
        name = require_state_value(state, "pricing_plan_name", "pricing plan name")
        return {
            "plan_id": plan_id,
            "body": SavePricingPlanParam(
                name=name,
                display_name=f"{test_data['pricing_plan']['display_name']} (updated)",
                description=f"{test_data['pricing_plan']['description']} (updated)",
                menu_ids=[menu_id],
            ),
        }

    return Step(
        method_name="update_pricing_plan",
        description="Update Pricing Plan",
        params=_params,
        expected_status=200,
        validation_func=validate_update_pricing_plan_response,
    )


def build_update_pricing_plans_used_step() -> Step:
    def _params(vars_dict):
        plan_id = _get_required_id(vars_dict, "pricing_plan", "pricing plan id")
        return {
            "update_pricing_plans_used_param": UpdatePricingPlansUsedParam(plan_ids=[plan_id])
        }

    return Step(
        method_name="update_pricing_plans_used",
        description="Update Pricing Plans Used",
        params=_params,
        expected_status=200,
        validation_func=validate_update_pricing_plans_used_response,
        allow_failure=True,
    )


def build_create_tax_rate_step() -> Step:
    def _params(vars_dict):
        state = ensure_state(vars_dict)
        name = unique_name(test_data["tax_rate"]["name"])
        state.tax_rate_name = name
        return {
            "body": TaxRateProps(
                name=name,
                display_name=test_data["tax_rate"]["display_name"],
                description=test_data["tax_rate"]["description"],
                percentage=test_data["tax_rate"]["percentage"],
                country=test_data["tax_rate"]["country"],
                inclusive=test_data["tax_rate"]["inclusive"],
            )
        }

    return Step(
        method_name="create_tax_rate",
        description="Create Tax Rate",
        params=_params,
        expected_status=201,
        validation_func=validate_create_tax_rate_response,
        store_as="tax_rate",
    )


def build_get_tax_rates_step() -> Step:
    return Step(
        method_name="get_tax_rates",
        description="Get Tax Rates",
        params={},
        expected_status=200,
        validation_func=validate_tax_rates_response,
    )


def build_update_tax_rate_step() -> Step:
    def _params(vars_dict):
        tax_rate_id = _get_required_id(vars_dict, "tax_rate", "tax rate id")
        return {
            "tax_rate_id": tax_rate_id,
            "update_tax_rate_param": UpdateTaxRateParam(
                display_name=f"{test_data['tax_rate']['display_name']} (updated)",
                description=f"{test_data['tax_rate']['description']} (updated)",
            ),
        }

    return Step(
        method_name="update_tax_rate",
        description="Update Tax Rate",
        params=_params,
        expected_status=200,
        validation_func=validate_update_tax_rate_response,
    )


def build_delete_pricing_menu_step() -> Step:
    def _params(vars_dict):
        menu_id = _get_required_id(vars_dict, "pricing_menu", "pricing menu id")
        return {"menu_id": menu_id}

    return Step(
        method_name="delete_pricing_menu",
        description="Delete Pricing Menu",
        params=_params,
        expected_status=200,
        validation_func=validate_delete_response,
    )


def build_delete_pricing_unit_step() -> Step:
    def _params(vars_dict):
        pricing_unit_id = _get_required_id(vars_dict, "pricing_unit", "pricing unit id")
        return {"pricing_unit_id": pricing_unit_id}

    return Step(
        method_name="delete_pricing_unit",
        description="Delete Pricing Unit",
        params=_params,
        expected_status=200,
        validation_func=validate_delete_response,
    )


def build_delete_metering_unit_step() -> Step:
    def _params(vars_dict):
        metering_unit_id = _get_required_id(vars_dict, "metering_unit", "metering unit id")
        return {"metering_unit_id": metering_unit_id}

    return Step(
        method_name="delete_metering_unit_by_id",
        description="Delete Metering Unit",
        params=_params,
        expected_status=200,
        validation_func=validate_delete_response,
    )


def build_delete_pricing_plan_step() -> Step:
    def _params(vars_dict):
        plan_id = _get_required_id(vars_dict, "pricing_plan", "pricing plan id")
        return {"plan_id": plan_id}

    return Step(
        method_name="delete_pricing_plan",
        description="Delete Pricing Plan",
        params=_params,
        expected_status=200,
        validation_func=validate_delete_response,
    )


def build_delete_all_pricing_data_step() -> Step:
    return Step(
        method_name="delete_all_plans_and_menus_and_units_and_meters_and_tax_rates",
        description="Delete all pricing resources",
        params={},
        expected_status=200,
        validation_func=validate_delete_response,
    )


def build_standard_flow_steps() -> List[Step]:
    return [
        build_create_metering_unit_step(),
        build_get_metering_units_step(),
        build_create_pricing_unit_step("pricing_unit", "pricing_unit_name"),
        build_update_pricing_unit_step(),
        build_get_pricing_units_step(),
        build_get_pricing_unit_step(),
        build_create_pricing_unit_step("menu_detach_pricing_unit", "menu_detach_pricing_unit_name", "(detach)"),
        build_create_pricing_menu_step("menu_detach_pricing_unit", "pricing_menu", "pricing_menu_name"),
        build_get_pricing_menus_step(),
        build_get_pricing_menu_step(),
        build_create_tax_rate_step(),
        build_get_tax_rates_step(),
        build_update_pricing_menu_step("menu_detach_pricing_unit", "pricing_menu_name"),
        build_update_tax_rate_step(),
        build_delete_pricing_menu_step(),
        build_delete_pricing_unit_step(),
        build_delete_metering_unit_step(),
        build_delete_all_pricing_data_step(),
    ]


def build_additional_coverage_steps() -> List[Step]:
    return [
        build_create_metering_unit_step(),
        build_create_pricing_unit_step("pricing_unit", "pricing_unit_name"),
        build_create_pricing_menu_step("pricing_unit", "pricing_menu", "pricing_menu_name"),
        build_create_pricing_plan_step(),
        build_get_pricing_plans_step(),
        build_get_pricing_plan_step(),
        build_update_pricing_plan_step(),
        build_update_pricing_plans_used_step(),
        build_create_tax_rate_step(),
        build_update_tax_rate_step(),
        build_delete_pricing_plan_step(),
        build_delete_all_pricing_data_step(),
    ]


def get_pricing_stories(filters: Optional[List[str]] = None) -> List[Story]:
    stories = [
        Story(
            name="Postman Collection Story - Standard Methods",
            description="Pricing flow using standard client methods",
            module=MODULE,
            steps=build_standard_flow_steps(),
            tags=["standard"],
        ),
        Story(
            name="Additional Coverage Story - Standard Struct Methods",
            description="Exercises update endpoints using standard methods",
            module=MODULE,
            steps=build_additional_coverage_steps(),
            tags=["standard", "additional_coverage"],
        ),
    ]

    if not filters:
        return stories

    lower = [name.lower() for name in filters]
    return [story for story in stories if story.name.lower() in lower]


# pytest統合用のテスト関数
# conftest.pyのtest_storyと同じシグネチャ

def test_story(
    story: Story,
    module_name: str,
    story_runner,
    coverage_tracker,
    story_results,
    test_config,
    snapshot_engine,
    request,
):
    from tests.e2e.conftest import test_story as conftest_test_story

    conftest_test_story(
        story,
        module_name,
        story_runner,
        coverage_tracker,
        story_results,
        test_config,
        snapshot_engine,
        request,
    )

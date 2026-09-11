"""Billing module story definitions."""

from typing import List, Optional
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from testlib.models import Story, Step
from tests.e2e.billing.helpers import create_update_stripe_info_param
from tests.e2e.billing.validation import (
    validate_delete_stripe_info_response,
    validate_stripe_info_response,
    validate_update_stripe_info_response,
)

MODULE = "billing"


def build_get_stripe_step(description: str, expected_registered: bool) -> Step:
    return Step(
        method_name="get_stripe_info",
        description=description,
        params={},
        expected_status=200,
        validation_func=lambda response: validate_stripe_info_response(
            response, expected_registered
        ),
    )


def build_update_stripe_step(description: str) -> Step:
    return Step(
        method_name="update_stripe_info",
        description=description,
        params=lambda _vars: {
            "update_stripe_info_param": create_update_stripe_info_param()
        },
        expected_status=200,
        validation_func=validate_update_stripe_info_response,
    )


def build_delete_stripe_step(description: str) -> Step:
    return Step(
        method_name="delete_stripe_info",
        description=description,
        params={},
        expected_status=200,
        validation_func=validate_delete_stripe_info_response,
    )


def get_billing_stories(filters: Optional[List[str]] = None) -> List[Story]:
    stories = [
        Story(
            name="Postman Collection Story - Standard Methods",
            description="Reproduces the Postman collection flow using standard billing client methods",
            module=MODULE,
            steps=[
                build_get_stripe_step("Pre_GetStripeConnectionInformation", False),
                build_update_stripe_step("Update Stripe connection"),
                build_get_stripe_step("GetStripeConnectionInformation", True),
                build_delete_stripe_step("DeleteStripeConnection"),
                build_get_stripe_step("Final_GetStripeConnectionInformation", False),
            ],
            tags=["standard"],
        ),
        Story(
            name="Postman Collection Story - Standard Methods With Body",
            description="Standard methods that send request bodies",
            module=MODULE,
            steps=[
                build_get_stripe_step("Pre_GetStripeConnectionInformation", False),
                build_update_stripe_step("Update Stripe connection with body"),
                build_get_stripe_step("GetStripeConnectionInformation", True),
                build_delete_stripe_step("DeleteStripeConnection"),
                build_get_stripe_step("Final_GetStripeConnectionInformation", False),
            ],
            tags=["standard", "with-body"],
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

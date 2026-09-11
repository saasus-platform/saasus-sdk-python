"""Integration (EventBridge) module story definitions.

JavaScriptのintegration/stories.tsを参考にしたストーリー定義。
"""

from typing import List, Optional
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from testlib.models import Story, Step
from tests.e2e.integration.helpers import (
    create_event_bridge_event_param,
    create_event_bridge_settings_param,
)
from tests.e2e.integration.validation import validate_event_bridge_settings_response

MODULE = "integration"


def build_save_settings_step() -> Step:
    return Step(
        method_name="save_event_bridge_settings",
        description="SaveEventBridgeSettings",
        params=lambda _vars: {"body": create_event_bridge_settings_param()},
        expected_status=200,
        validation_func=lambda _response: True,
    )


def build_get_settings_step() -> Step:
    return Step(
        method_name="get_event_bridge_settings",
        description="GetEventBridgeSettings_AfterSave",
        params={},
        expected_status=200,
        validation_func=lambda response: validate_event_bridge_settings_response(response, True),
    )


def build_test_event_step() -> Step:
    return Step(
        method_name="create_event_bridge_test_event",
        description="CreateEventBridgeTestEvent",
        params={},
        expected_status=201,
        validation_func=lambda _response: True,
    )


def build_create_event_step() -> Step:
    # JS側のallowed_statuses[200,201,500,501]に相当。環境依存の失敗を許容する。
    return Step(
        method_name="create_event_bridge_event",
        description="CreateEventBridgeEvent",
        params=lambda _vars: {"create_event_bridge_event_param": create_event_bridge_event_param()},
        expected_status=200,
        validation_func=lambda _response: True,
        allow_failure=True,
    )


def build_delete_settings_step() -> Step:
    return Step(
        method_name="delete_event_bridge_settings",
        description="DeleteEventBridgeSettings",
        params={},
        expected_status=200,
        validation_func=lambda _response: True,
    )


def get_integration_stories(filters: Optional[List[str]] = None) -> List[Story]:
    stories = [
        Story(
            name="Postman Collection Story - Standard Methods",
            description="Reproduces the Postman collection flow using standard integration client methods",
            module=MODULE,
            steps=[
                build_save_settings_step(),
                build_get_settings_step(),
                build_test_event_step(),
                build_create_event_step(),
                build_delete_settings_step(),
            ],
            tags=["standard"],
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

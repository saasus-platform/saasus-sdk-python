"""ApiLog module story definitions.

JavaScriptのapilogs/stories.tsを参考にしたストーリー定義。
"""

from typing import List, Optional
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from testlib.models import Story, Step
from tests.e2e.apilog.helpers import (
    APILOG_LIST_KEY,
    create_empty_get_logs_params,
    create_get_log_params,
    create_get_logs_with_query_params,
)
from tests.e2e.apilog.validation import (
    validate_api_log_entry,
    validate_api_logs_list,
)

MODULE = "apilog"


def build_pre_get_logs_step() -> Step:
    return Step(
        method_name="get_logs",
        description="Pre_GetApiLogs",
        params=lambda _vars: create_empty_get_logs_params(),
        expected_status=200,
        validation_func=validate_api_logs_list,
        store_as=APILOG_LIST_KEY,
    )


def build_get_logs_step() -> Step:
    return Step(
        method_name="get_logs",
        description="GetApiLogs",
        params=lambda _vars: create_empty_get_logs_params(),
        expected_status=200,
        validation_func=validate_api_logs_list,
    )


def build_get_logs_with_query_step() -> Step:
    return Step(
        method_name="get_logs",
        description="GetApiLogs With QueryParameters",
        params=create_get_logs_with_query_params,
        expected_status=200,
        validation_func=validate_api_logs_list,
    )


def build_get_log_step() -> Step:
    return Step(
        method_name="get_log",
        description="GetApiLog",
        params=create_get_log_params,
        expected_status=200,
        validation_func=validate_api_log_entry,
    )


def get_apilog_stories(filters: Optional[List[str]] = None) -> List[Story]:
    stories = [
        Story(
            name="Postman Collection Story - Standard Methods",
            description="Reproduces the Postman collection flow using standard ApiLog client methods",
            module=MODULE,
            steps=[
                build_pre_get_logs_step(),
                build_get_logs_step(),
                build_get_logs_with_query_step(),
                build_get_log_step(),
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

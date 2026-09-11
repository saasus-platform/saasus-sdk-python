"""Communication (Feedback) module story definitions.

JavaScriptのcommunication/stories.tsを参考にしたストーリー定義。
create_feedback / create_feedback_comment のレスポンスをstore_asで保存し、
後続ステップでfeedback_id / comment_idを再利用します。
"""

from typing import List, Optional
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from testlib.models import Story, Step
from tests.e2e.communication.helpers import (
    COMMENT_STATE_KEY,
    FEEDBACK_STATE_KEY,
    build_create_comment_params,
    build_create_feedback_params,
    build_create_vote_params,
    build_delete_comment_params,
    build_delete_feedback_params,
    build_delete_vote_params,
    build_get_comment_params,
    build_get_feedback_params,
    build_get_feedbacks_params,
    build_update_comment_params,
    build_update_feedback_params,
    build_update_feedback_status_params,
)
from tests.e2e.communication.validation import (
    validate_comment,
    validate_comment_or_empty,
    validate_delete_response,
    validate_feedback,
    validate_feedback_list,
    validate_feedback_or_empty,
    validate_votes,
    validate_votes_or_empty,
)

MODULE = "communication"


def get_communication_stories(filters: Optional[List[str]] = None) -> List[Story]:
    steps = [
        Step(
            method_name="get_feedbacks",
            description="ListFeedbacks",
            params=build_get_feedbacks_params,
            expected_status=200,
            validation_func=validate_feedback_list,
        ),
        Step(
            method_name="create_feedback",
            description="CreateFeedback",
            params=build_create_feedback_params,
            expected_status=201,
            validation_func=validate_feedback,
            store_as=FEEDBACK_STATE_KEY,
        ),
        Step(
            method_name="get_feedback",
            description="GetFeedback",
            params=build_get_feedback_params,
            expected_status=200,
            validation_func=validate_feedback,
        ),
        Step(
            method_name="update_feedback",
            description="UpdateFeedback",
            params=build_update_feedback_params,
            expected_status=200,
            validation_func=validate_feedback_or_empty,
        ),
        Step(
            method_name="update_feedback_status",
            description="UpdateFeedbackStatus",
            params=build_update_feedback_status_params,
            expected_status=200,
            validation_func=validate_feedback_or_empty,
        ),
        Step(
            method_name="create_feedback_comment",
            description="CreateFeedbackComment",
            params=build_create_comment_params,
            expected_status=201,
            validation_func=validate_comment,
            store_as=COMMENT_STATE_KEY,
        ),
        Step(
            method_name="get_feedback_comment",
            description="GetFeedbackComment",
            params=build_get_comment_params,
            expected_status=200,
            validation_func=validate_comment,
        ),
        Step(
            method_name="update_feedback_comment",
            description="UpdateFeedbackComment",
            params=build_update_comment_params,
            expected_status=200,
            validation_func=validate_comment_or_empty,
        ),
        Step(
            method_name="create_vote_user",
            description="CreateVoteUser",
            params=build_create_vote_params,
            expected_status=201,
            validation_func=validate_votes,
        ),
        Step(
            method_name="delete_vote_for_feedback",
            description="DeleteVoteForFeedback",
            params=build_delete_vote_params,
            expected_status=200,
            validation_func=validate_votes_or_empty,
        ),
        Step(
            method_name="delete_feedback_comment",
            description="DeleteFeedbackComment",
            params=build_delete_comment_params,
            expected_status=200,
            validation_func=validate_delete_response,
        ),
        Step(
            method_name="delete_feedback",
            description="DeleteFeedback",
            params=build_delete_feedback_params,
            expected_status=200,
            validation_func=validate_delete_response,
        ),
    ]

    stories = [
        Story(
            name="Postman Collection Story - Standard Methods",
            description="Recreates the Postman story with standard Communication API methods",
            module=MODULE,
            steps=steps,
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

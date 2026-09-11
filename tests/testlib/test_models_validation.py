"""
データモデルのバリデーションテスト

models.pyのバリデーション機能が正しく動作することを確認します。
"""

import pytest
from tests.testlib.models import Story, Step, StepResult, StoryResult


def test_step_requires_method_name():
    """Stepのmethod_nameが必須であることを検証"""
    with pytest.raises(ValueError, match="method_nameは必須です"):
        Step(method_name="", params={})


def test_step_requires_params():
    """Stepのparamsが必須であることを検証"""
    with pytest.raises(ValueError, match="paramsは必須です"):
        Step(method_name="test_method", params=None)


def test_step_valid_creation():
    """有効なStepが作成できることを検証"""
    step = Step(
        method_name="test_method",
        params={"key": "value"},
        description="テストステップ"
    )
    assert step.method_name == "test_method"
    assert step.params == {"key": "value"}
    assert step.description == "テストステップ"


def test_step_with_callable_params():
    """callableなparamsを持つStepが作成できることを検証"""
    def param_func(vars):
        return {"dynamic": "value"}
    
    step = Step(
        method_name="test_method",
        params=param_func
    )
    assert callable(step.params)


def test_story_requires_name():
    """Storyのnameが必須であることを検証"""
    with pytest.raises(ValueError, match="nameは必須です"):
        Story(
            name="",
            description="テスト",
            module="auth",
            steps=[Step(method_name="test", params={})]
        )


def test_story_requires_module():
    """Storyのmoduleが必須であることを検証"""
    with pytest.raises(ValueError, match="moduleは必須です"):
        Story(
            name="test_story",
            description="テスト",
            module="",
            steps=[Step(method_name="test", params={})]
        )


def test_story_requires_steps():
    """Storyのstepsが必須であることを検証"""
    with pytest.raises(ValueError, match="stepsは必須です"):
        Story(
            name="test_story",
            description="テスト",
            module="auth",
            steps=[]
        )


def test_story_valid_creation():
    """有効なStoryが作成できることを検証"""
    step = Step(method_name="test_method", params={})
    story = Story(
        name="test_story",
        description="テストストーリー",
        module="auth",
        steps=[step],
        tags=["test", "auth"]
    )
    assert story.name == "test_story"
    assert story.module == "auth"
    assert len(story.steps) == 1
    assert story.tags == ["test", "auth"]


def test_story_with_setup_and_cleanup():
    """setup/cleanupを持つStoryが作成できることを検証"""
    setup_step = Step(method_name="setup", params={})
    main_step = Step(method_name="main", params={})
    cleanup_step = Step(method_name="cleanup", params={})
    
    story = Story(
        name="test_story",
        description="テスト",
        module="auth",
        setup=[setup_step],
        steps=[main_step],
        cleanup=[cleanup_step]
    )
    assert len(story.setup) == 1
    assert len(story.steps) == 1
    assert len(story.cleanup) == 1


def test_step_result_creation():
    """StepResultが正しく作成できることを検証"""
    step = Step(method_name="test", params={})
    result = StepResult(
        step=step,
        success=True,
        response={"data": "test"},
        status_code=200,
        execution_time=1.5
    )
    assert result.success is True
    assert result.response == {"data": "test"}
    assert result.status_code == 200
    assert result.execution_time == 1.5


def test_story_result_creation():
    """StoryResultが正しく作成できることを検証"""
    step = Step(method_name="test", params={})
    story = Story(
        name="test_story",
        description="テスト",
        module="auth",
        steps=[step]
    )
    step_result = StepResult(step=step, success=True)
    
    story_result = StoryResult(
        story=story,
        success=True,
        step_results=[step_result],
        execution_time=2.0
    )
    assert story_result.success is True
    assert len(story_result.step_results) == 1
    assert story_result.execution_time == 2.0

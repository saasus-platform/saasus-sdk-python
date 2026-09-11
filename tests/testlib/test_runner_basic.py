"""
StoryRunnerの基本的な動作確認テスト
"""

import pytest
from tests.testlib.runner import StoryRunner
from tests.testlib.config import Config
from tests.testlib.logger import TestLogger
from tests.testlib.models import Story, Step


class MockClient:
    """テスト用のモッククライアント"""
    
    def __init__(self):
        self.call_count = 0
    
    def test_method(self, param1=None):
        """テスト用メソッド"""
        self.call_count += 1
        return {"result": "success", "param1": param1, "call_count": self.call_count}
    
    def failing_method(self):
        """失敗するメソッド"""
        raise ValueError("This method always fails")


def test_story_runner_basic_execution():
    """基本的なストーリー実行のテスト"""
    # 設定を作成
    config = Config(
        base_url="http://test.example.com",
        api_key="test_key",
        secret_key="test_secret",
        saas_id="test_saas_id",
        log_level="ERROR"  # テスト中はエラーのみ出力
    )
    
    # ロガーを作成
    logger = TestLogger(config)
    
    # モッククライアントを作成
    client = MockClient()
    
    # ストーリーランナーを作成
    runner = StoryRunner(client, config, logger)
    
    # テストストーリーを作成
    story = Story(
        name="test_story",
        description="Test story for basic execution",
        module="test",
        steps=[
            Step(
                method_name="test_method",
                params={"param1": "value1"},
                description="First test step"
            ),
            Step(
                method_name="test_method",
                params={"param1": "value2"},
                description="Second test step"
            )
        ]
    )
    
    # ストーリーを実行
    result = runner.run_story(story)
    
    # 結果を検証
    assert result.success is True
    assert len(result.step_results) == 2
    assert all(sr.success for sr in result.step_results)
    assert client.call_count == 2


def test_story_runner_with_setup_and_cleanup():
    """setup/cleanupを含むストーリー実行のテスト"""
    config = Config(
        base_url="http://test.example.com",
        api_key="test_key",
        secret_key="test_secret",
        saas_id="test_saas_id",
        log_level="ERROR"
    )
    
    logger = TestLogger(config)
    client = MockClient()
    runner = StoryRunner(client, config, logger)
    
    story = Story(
        name="test_story_with_phases",
        description="Test story with setup and cleanup",
        module="test",
        setup=[
            Step(
                method_name="test_method",
                params={"param1": "setup"},
                description="Setup step"
            )
        ],
        steps=[
            Step(
                method_name="test_method",
                params={"param1": "main"},
                description="Main step"
            )
        ],
        cleanup=[
            Step(
                method_name="test_method",
                params={"param1": "cleanup"},
                description="Cleanup step"
            )
        ]
    )
    
    result = runner.run_story(story)
    
    assert result.success is True
    assert len(result.setup_results) == 1
    assert len(result.step_results) == 1
    assert len(result.cleanup_results) == 1
    assert client.call_count == 3


def test_story_runner_fail_fast_enabled():
    """Fail Fastモードのテスト"""
    config = Config(
        base_url="http://test.example.com",
        api_key="test_key",
        secret_key="test_secret",
        saas_id="test_saas_id",
        fail_fast=True,
        log_level="ERROR"
    )
    
    logger = TestLogger(config)
    client = MockClient()
    runner = StoryRunner(client, config, logger)
    
    story = Story(
        name="test_fail_fast",
        description="Test fail fast behavior",
        module="test",
        steps=[
            Step(
                method_name="test_method",
                params={"param1": "step1"},
                description="First step (should succeed)"
            ),
            Step(
                method_name="failing_method",
                params={},
                description="Second step (should fail)"
            ),
            Step(
                method_name="test_method",
                params={"param1": "step3"},
                description="Third step (should be skipped)"
            )
        ]
    )
    
    result = runner.run_story(story)
    
    assert result.success is False
    assert len(result.step_results) == 2  # 3番目のステップはスキップされる
    assert result.step_results[0].success is True
    assert result.step_results[1].success is False


def test_story_runner_fail_fast_disabled():
    """Fail Fast無効モードのテスト"""
    config = Config(
        base_url="http://test.example.com",
        api_key="test_key",
        secret_key="test_secret",
        saas_id="test_saas_id",
        fail_fast=False,
        log_level="ERROR"
    )
    
    logger = TestLogger(config)
    client = MockClient()
    runner = StoryRunner(client, config, logger)
    
    story = Story(
        name="test_continue_on_failure",
        description="Test continue on failure behavior",
        module="test",
        steps=[
            Step(
                method_name="test_method",
                params={"param1": "step1"},
                description="First step (should succeed)"
            ),
            Step(
                method_name="failing_method",
                params={},
                description="Second step (should fail)"
            ),
            Step(
                method_name="test_method",
                params={"param1": "step3"},
                description="Third step (should execute)"
            )
        ]
    )
    
    result = runner.run_story(story)
    
    assert result.success is False
    assert len(result.step_results) == 3  # すべてのステップが実行される
    assert result.step_results[0].success is True
    assert result.step_results[1].success is False
    assert result.step_results[2].success is True


def test_story_runner_dry_run_mode():
    """Dry Runモードのテスト"""
    config = Config(
        base_url="http://test.example.com",
        api_key="test_key",
        secret_key="test_secret",
        saas_id="test_saas_id",
        dry_run=True,
        log_level="ERROR"
    )
    
    logger = TestLogger(config)
    client = MockClient()
    runner = StoryRunner(client, config, logger)
    
    story = Story(
        name="test_dry_run",
        description="Test dry run mode",
        module="test",
        steps=[
            Step(
                method_name="test_method",
                params={"param1": "value1"},
                description="Step that should be skipped",
                skip_on_dry_run=True
            ),
            Step(
                method_name="test_method",
                params={"param1": "value2"},
                description="Step that should execute",
                skip_on_dry_run=False
            )
        ]
    )
    
    result = runner.run_story(story)
    
    assert result.success is True
    assert len(result.step_results) == 2
    
    # 最初のステップはdry runでスキップされる
    assert result.step_results[0].response["dry_run"] is True
    
    # 2番目のステップは実行される
    assert "dry_run" not in result.step_results[1].response
    assert client.call_count == 1  # 2番目のステップのみ実行


def test_story_runner_cleanup_always_runs():
    """Cleanupが常に実行されることを確認するテスト"""
    config = Config(
        base_url="http://test.example.com",
        api_key="test_key",
        secret_key="test_secret",
        saas_id="test_saas_id",
        fail_fast=True,
        log_level="ERROR"
    )
    
    logger = TestLogger(config)
    client = MockClient()
    runner = StoryRunner(client, config, logger)
    
    story = Story(
        name="test_cleanup_always_runs",
        description="Test that cleanup always runs",
        module="test",
        steps=[
            Step(
                method_name="failing_method",
                params={},
                description="Failing step"
            )
        ],
        cleanup=[
            Step(
                method_name="test_method",
                params={"param1": "cleanup"},
                description="Cleanup step"
            )
        ]
    )
    
    result = runner.run_story(story)
    
    assert result.success is False
    assert len(result.step_results) == 1
    assert result.step_results[0].success is False
    
    # Cleanupは実行される
    assert len(result.cleanup_results) == 1
    assert result.cleanup_results[0].success is True
    assert client.call_count == 1  # cleanupのtest_methodのみ実行


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

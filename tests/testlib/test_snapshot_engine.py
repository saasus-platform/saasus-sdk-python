"""スナップショットエンジンの基本テスト"""

import json
import tempfile
from pathlib import Path


from tests.testlib.models import Story, Step, StoryResult, StepResult
from tests.testlib.snapshot import SnapshotEngine, SnapshotConfig
from tests.testlib.logger import TestLogger
from tests.testlib.config import Config


def test_snapshot_engine_capture():
    """スナップショットのキャプチャ機能をテスト"""
    
    # 一時ディレクトリを使用
    with tempfile.TemporaryDirectory() as tmpdir:
        # 設定を作成
        config = Config(
            base_url="http://test.example.com",
            api_key="test_key",
            secret_key="test_secret",
            saas_id="test_saas"
        )
        
        snapshot_config = SnapshotConfig(
            snapshot_dir=tmpdir,
            capture_enabled=True,
            compare_enabled=False,
            report_enabled=False
        )
        
        logger = TestLogger(config)
        engine = SnapshotEngine(snapshot_config, logger)
        
        # テスト用のストーリー結果を作成
        story = Story(
            name="test_story",
            description="テストストーリー",
            module="test_module",
            steps=[
                Step(
                    method_name="test_method",
                    params={"param1": "value1"}
                )
            ]
        )
        
        step_result = StepResult(
            step=story.steps[0],
            success=True,
            response={"result": "success", "api_key": "secret123"},
            status_code=200,
            execution_time=0.5
        )
        
        story_result = StoryResult(
            story=story,
            success=True,
            step_results=[step_result],
            execution_time=1.0
        )
        
        # スナップショットをキャプチャ
        snapshot_path = engine.capture(story_result)
        
        # 検証
        assert snapshot_path is not None
        assert snapshot_path.exists()
        
        # スナップショットの内容を確認
        with open(snapshot_path, 'r', encoding='utf-8') as f:
            snapshot_data = json.load(f)
        
        assert snapshot_data["story"]["name"] == "test_story"
        assert snapshot_data["story"]["module"] == "test_module"
        assert snapshot_data["success"] is True
        assert len(snapshot_data["step_results"]) == 1
        
        # 機密情報がマスキングされていることを確認
        step_response = snapshot_data["step_results"][0]["response"]
        assert step_response["api_key"] == "***MASKED***"
        assert step_response["result"] == "success"
        
        # メタデータが含まれていることを確認
        assert "metadata" in snapshot_data
        assert snapshot_data["metadata"]["story_name"] == "test_story"
        assert snapshot_data["metadata"]["masked_count"] == 1
        
        print("✓ スナップショットキャプチャテスト成功")


def test_snapshot_engine_compare():
    """スナップショットの比較機能をテスト"""
    
    with tempfile.TemporaryDirectory() as tmpdir:
        # 設定を作成
        config = Config(
            base_url="http://test.example.com",
            api_key="test_key",
            secret_key="test_secret",
            saas_id="test_saas"
        )
        
        snapshot_config = SnapshotConfig(
            snapshot_dir=tmpdir,
            capture_enabled=True,
            compare_enabled=True,
            report_enabled=False,
            compatibility_check=False  # 互換性チェックは無効
        )
        
        logger = TestLogger(config)
        engine = SnapshotEngine(snapshot_config, logger)
        
        # 最初のストーリー結果を作成してキャプチャ
        story = Story(
            name="test_story",
            description="テストストーリー",
            module="test_module",
            steps=[
                Step(
                    method_name="test_method",
                    params={"param1": "value1"}
                )
            ]
        )
        
        step_result1 = StepResult(
            step=story.steps[0],
            success=True,
            response={"result": "success", "count": 10},
            status_code=200,
            execution_time=0.5
        )
        
        story_result1 = StoryResult(
            story=story,
            success=True,
            step_results=[step_result1],
            execution_time=1.0
        )
        
        engine.capture(story_result1)
        
        # 2回目の実行（レスポンスが異なる）
        step_result2 = StepResult(
            step=story.steps[0],
            success=True,
            response={"result": "success", "count": 20},  # countが変更
            status_code=200,
            execution_time=0.6
        )
        
        story_result2 = StoryResult(
            story=story,
            success=True,
            step_results=[step_result2],
            execution_time=1.1
        )
        
        # 比較を実行
        diff = engine.compare(story_result2)
        
        # 検証
        assert diff is not None
        assert diff["has_differences"] is True
        assert diff["summary"]["values_changed"] > 0
        
        # 差分ファイルが作成されていることを確認
        diff_path = Path(tmpdir) / "test_module" / "story_comparisons" / "test_story_diff.json"
        assert diff_path.exists()
        
        print("✓ スナップショット比較テスト成功")


def test_snapshot_engine_compatibility_check():
    """互換性チェック機能をテスト"""
    
    with tempfile.TemporaryDirectory() as tmpdir:
        # 設定を作成
        config = Config(
            base_url="http://test.example.com",
            api_key="test_key",
            secret_key="test_secret",
            saas_id="test_saas"
        )
        
        snapshot_config = SnapshotConfig(
            snapshot_dir=tmpdir,
            capture_enabled=True,
            compare_enabled=True,
            report_enabled=False,
            compatibility_check=True
        )
        
        logger = TestLogger(config)
        engine = SnapshotEngine(snapshot_config, logger)
        
        # 最初のストーリー結果を作成
        story1 = Story(
            name="test_story",
            description="テストストーリー",
            module="test_module",
            steps=[
                Step(
                    method_name="method_a",
                    params={}
                ),
                Step(
                    method_name="method_b",
                    params={}
                )
            ]
        )
        
        story_result1 = StoryResult(
            story=story1,
            success=True,
            step_results=[
                StepResult(step=story1.steps[0], success=True, response={}),
                StepResult(step=story1.steps[1], success=True, response={})
            ],
            execution_time=1.0
        )
        
        engine.capture(story_result1)
        
        # 2回目の実行（メソッドが変更）
        story2 = Story(
            name="test_story",
            description="テストストーリー",
            module="test_module",
            steps=[
                Step(
                    method_name="method_a",
                    params={}
                ),
                Step(
                    method_name="method_c",  # method_bがmethod_cに変更
                    params={}
                )
            ]
        )
        
        story_result2 = StoryResult(
            story=story2,
            success=True,
            step_results=[
                StepResult(step=story2.steps[0], success=True, response={}),
                StepResult(step=story2.steps[1], success=True, response={})
            ],
            execution_time=1.0
        )
        
        # 比較を実行
        diff = engine.compare(story_result2)
        
        # 検証
        assert diff is not None
        assert "compatibility_issues" in diff
        
        issues = diff["compatibility_issues"]
        assert len(issues) > 0
        
        # method_bが削除され、method_cが追加されたことを確認
        issue_types = [issue["type"] for issue in issues]
        assert "method_removed" in issue_types or "method_added" in issue_types
        
        print("✓ 互換性チェックテスト成功")


if __name__ == "__main__":
    test_snapshot_engine_capture()
    test_snapshot_engine_compare()
    test_snapshot_engine_compatibility_check()
    print("\n✓ すべてのテストが成功しました")

"""
SnapshotEngineとSnapshotReporterの統合テスト
"""

import json



from tests.testlib.snapshot.engine import SnapshotEngine
from tests.testlib.snapshot.config import SnapshotConfig
from tests.testlib.logger import TestLogger
from tests.testlib.config import Config



def test_snapshot_engine_generate_report(tmp_path):
    """SnapshotEngineのレポート生成機能のテスト"""
    # 設定を作成
    test_config = Config(
        base_url="http://test.example.com",
        api_key="test_key",
        secret_key="test_secret",
        saas_id="test_saas_id",
        log_level="INFO"
    )
    
    snapshot_config = SnapshotConfig(
        snapshot_dir=str(tmp_path),
        capture_enabled=True,
        compare_enabled=True,
        report_enabled=True
    )
    
    # ロガーとエンジンを作成
    logger = TestLogger(test_config)
    engine = SnapshotEngine(snapshot_config, logger)
    
    # テスト用の差分データ
    all_diffs = [
        {
            "story_name": "test_story_1",
            "module": "auth",
            "has_differences": True,
            "summary": {
                "values_changed": 1,
                "items_added": 0,
                "items_removed": 0,
                "type_changes": 0
            },
            "details": {
                "values_changed": [
                    {
                        "path": "root['user']['name']",
                        "old_value": "old_name",
                        "new_value": "new_name"
                    }
                ],
                "items_added": [],
                "items_removed": [],
                "type_changes": {}
            },
            "compatibility_issues": []
        }
    ]
    
    # レポートを生成
    report_paths = engine.generate_report(all_diffs, module="auth")
    
    # レポートが生成されたことを確認
    assert report_paths is not None
    assert "json" in report_paths
    assert "html" in report_paths
    assert report_paths["json"].exists()
    assert report_paths["html"].exists()
    
    # JSONレポートの内容を確認
    with open(report_paths["json"], 'r', encoding='utf-8') as f:
        report_data = json.load(f)
    
    assert report_data["summary"]["total_comparisons"] == 1
    assert report_data["summary"]["differences_found"] == 1


def test_snapshot_engine_report_disabled(tmp_path):
    """レポート生成が無効の場合のテスト"""
    # 設定を作成（レポート無効）
    test_config = Config(
        base_url="http://test.example.com",
        api_key="test_key",
        secret_key="test_secret",
        saas_id="test_saas_id",
        log_level="INFO"
    )
    
    snapshot_config = SnapshotConfig(
        snapshot_dir=str(tmp_path),
        report_enabled=False
    )
    
    # ロガーとエンジンを作成
    logger = TestLogger(test_config)
    engine = SnapshotEngine(snapshot_config, logger)
    
    # レポートを生成
    report_paths = engine.generate_report([])
    
    # Noneが返されることを確認
    assert report_paths is None

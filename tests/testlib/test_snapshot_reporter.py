"""
SnapshotReporterのテスト
"""

import json


from tests.testlib.snapshot.reporter import SnapshotReporter
from tests.testlib.snapshot.config import SnapshotConfig


def test_snapshot_reporter_json_generation(tmp_path):
    """JSONレポート生成のテスト"""
    # 設定を作成
    config = SnapshotConfig(
        snapshot_dir=str(tmp_path),
        report_enabled=True
    )
    
    # レポーターを作成
    reporter = SnapshotReporter(config)
    
    # テスト用の差分データ
    all_diffs = [
        {
            "story_name": "test_story_1",
            "module": "auth",
            "has_differences": True,
            "summary": {
                "values_changed": 2,
                "items_added": 1,
                "items_removed": 0,
                "type_changes": 0
            },
            "details": {
                "values_changed": [
                    {
                        "path": "root['user']['email']",
                        "old_value": "old@example.com",
                        "new_value": "new@example.com"
                    }
                ],
                "items_added": ["root['user']['phone']"],
                "items_removed": [],
                "type_changes": {}
            },
            "compatibility_issues": []
        },
        {
            "story_name": "test_story_2",
            "module": "auth",
            "has_differences": False,
            "summary": {
                "values_changed": 0,
                "items_added": 0,
                "items_removed": 0,
                "type_changes": 0
            },
            "details": {
                "values_changed": [],
                "items_added": [],
                "items_removed": [],
                "type_changes": {}
            },
            "compatibility_issues": []
        }
    ]
    
    # レポートを生成
    report_paths = reporter.generate(all_diffs, module="auth")
    
    # JSONレポートが生成されたことを確認
    assert "json" in report_paths
    assert report_paths["json"].exists()
    
    # JSONレポートの内容を確認
    with open(report_paths["json"], 'r', encoding='utf-8') as f:
        report_data = json.load(f)
    
    assert "generated_at" in report_data
    assert report_data["summary"]["total_comparisons"] == 2
    assert report_data["summary"]["differences_found"] == 1
    assert report_data["summary"]["compatibility_issues_found"] == 0
    assert len(report_data["comparisons"]) == 2
    assert len(report_data["comparisons_with_differences"]) == 1


def test_snapshot_reporter_html_generation(tmp_path):
    """HTMLレポート生成のテスト"""
    # 設定を作成
    config = SnapshotConfig(
        snapshot_dir=str(tmp_path),
        report_enabled=True
    )
    
    # レポーターを作成
    reporter = SnapshotReporter(config)
    
    # テスト用の差分データ
    all_diffs = [
        {
            "story_name": "test_story_with_compat_issue",
            "module": "auth",
            "has_differences": False,
            "summary": {
                "values_changed": 0,
                "items_added": 0,
                "items_removed": 0,
                "type_changes": 0
            },
            "details": {
                "values_changed": [],
                "items_added": [],
                "items_removed": [],
                "type_changes": {}
            },
            "compatibility_issues": [
                {
                    "type": "parameters_added",
                    "method_name": "create_user",
                    "parameters": ["new_param"],
                    "message": "Method 'create_user' has new parameters: new_param"
                }
            ]
        }
    ]
    
    # レポートを生成
    report_paths = reporter.generate(all_diffs, module="auth")
    
    # HTMLレポートが生成されたことを確認
    assert "html" in report_paths
    assert report_paths["html"].exists()
    
    # HTMLレポートの内容を確認
    with open(report_paths["html"], 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    assert "<!DOCTYPE html>" in html_content
    assert "スナップショット比較レポート" in html_content
    assert "test_story_with_compat_issue" in html_content
    assert "互換性問題" in html_content
    assert "parameters_added" in html_content


def test_snapshot_reporter_no_differences(tmp_path):
    """差分がない場合のレポート生成テスト"""
    # 設定を作成
    config = SnapshotConfig(
        snapshot_dir=str(tmp_path),
        report_enabled=True
    )
    
    # レポーターを作成
    reporter = SnapshotReporter(config)
    
    # 差分がないデータ
    all_diffs = [
        {
            "story_name": "test_story_1",
            "module": "auth",
            "has_differences": False,
            "summary": {
                "values_changed": 0,
                "items_added": 0,
                "items_removed": 0,
                "type_changes": 0
            },
            "details": {
                "values_changed": [],
                "items_added": [],
                "items_removed": [],
                "type_changes": {}
            },
            "compatibility_issues": []
        }
    ]
    
    # レポートを生成
    report_paths = reporter.generate(all_diffs, module="auth")
    
    # レポートが生成されたことを確認
    assert "json" in report_paths
    assert "html" in report_paths
    
    # HTMLに「すべて一致」メッセージが含まれることを確認
    with open(report_paths["html"], 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    assert "すべてのスナップショットが一致しています" in html_content


def test_snapshot_reporter_disabled(tmp_path):
    """レポート生成が無効の場合のテスト"""
    # 設定を作成（レポート無効）
    config = SnapshotConfig(
        snapshot_dir=str(tmp_path),
        report_enabled=False
    )
    
    # レポーターを作成
    reporter = SnapshotReporter(config)
    
    # レポートを生成
    report_paths = reporter.generate([], module="auth")
    
    # 空の辞書が返されることを確認
    assert report_paths == {}


def test_html_escape():
    """HTMLエスケープ処理のテスト"""
    config = SnapshotConfig(report_enabled=True)
    reporter = SnapshotReporter(config)
    
    # エスケープが必要な文字列
    text = '<script>alert("XSS")</script>'
    escaped = reporter._escape_html(text)
    
    assert "&lt;" in escaped
    assert "&gt;" in escaped
    assert "&quot;" in escaped
    assert "<script>" not in escaped


def test_format_value():
    """値の整形処理のテスト"""
    config = SnapshotConfig(report_enabled=True)
    reporter = SnapshotReporter(config)
    
    # None
    assert reporter._format_value(None) == "null"
    
    # 辞書
    result = reporter._format_value({"key": "value"})
    assert "key" in result
    assert "value" in result
    
    # リスト
    result = reporter._format_value([1, 2, 3])
    assert "1" in result
    
    # 文字列
    assert reporter._format_value("test") == "test"

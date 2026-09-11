"""
スナップショットレポート生成

スナップショットの差分情報からJSON形式とHTML形式のレポートを生成します。
"""

import json
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime

from tests.testlib.snapshot.config import SnapshotConfig


class SnapshotReporter:
    """スナップショットレポート生成クラス
    
    差分情報からJSON形式とHTML形式のレポートを生成します。
    
    Attributes:
        config: スナップショット設定
    """
    
    def __init__(self, config: SnapshotConfig):
        """SnapshotReporterを初期化
        
        Args:
            config: スナップショット設定
        """
        self.config = config
    
    def generate(self, all_diffs: List[Dict[str, Any]], module: Optional[str] = None) -> Dict[str, Path]:
        """差分レポートを生成
        
        Args:
            all_diffs: すべてのストーリーの差分情報のリスト
            module: モジュール名（指定された場合、モジュール別のレポートを生成）
            
        Returns:
            生成されたレポートファイルのパスを含む辞書（"json"と"html"キー）
        """
        if not self.config.report_enabled:
            return {}
        
        # レポートデータを作成
        report_data = self._create_report_data(all_diffs)
        
        # レポート保存先ディレクトリを決定
        if module:
            report_dir = self.config.get_reports_dir(module)
        else:
            report_dir = Path(self.config.snapshot_dir) / "reports"
        
        report_dir.mkdir(parents=True, exist_ok=True)
        
        # タイムスタンプ付きファイル名
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        
        # JSONレポートを生成
        json_path = report_dir / f"snapshot_report_{timestamp}.json"
        self._generate_json_report(report_data, json_path)
        
        # HTMLレポートを生成
        html_path = report_dir / f"snapshot_report_{timestamp}.html"
        self._generate_html_report(report_data, html_path)
        
        return {
            "json": json_path,
            "html": html_path
        }
    
    def _create_report_data(self, all_diffs: List[Dict[str, Any]]) -> Dict[str, Any]:
        """レポートデータを作成
        
        Args:
            all_diffs: すべてのストーリーの差分情報のリスト
            
        Returns:
            レポートデータを含む辞書
        """
        # 統計情報を計算
        total_comparisons = len(all_diffs)
        differences_found = sum(1 for diff in all_diffs if diff.get("has_differences", False))
        compatibility_issues_found = sum(
            1 for diff in all_diffs 
            if diff.get("compatibility_issues") and len(diff["compatibility_issues"]) > 0
        )
        
        # サマリを作成
        summary = {
            "total_comparisons": total_comparisons,
            "differences_found": differences_found,
            "compatibility_issues_found": compatibility_issues_found,
            "success_rate": ((total_comparisons - differences_found) / total_comparisons * 100) if total_comparisons > 0 else 100.0
        }
        
        # 差分の詳細を整理
        comparisons_with_diffs = [
            diff for diff in all_diffs 
            if diff.get("has_differences", False) or (diff.get("compatibility_issues") and len(diff["compatibility_issues"]) > 0)
        ]
        
        return {
            "generated_at": datetime.now().isoformat(),
            "summary": summary,
            "comparisons": all_diffs,
            "comparisons_with_differences": comparisons_with_diffs
        }
    
    def _generate_json_report(self, report_data: Dict[str, Any], output_path: Path) -> None:
        """JSON形式のレポートを生成
        
        Args:
            report_data: レポートデータ
            output_path: 出力ファイルパス
        """
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(report_data, f, indent=2, ensure_ascii=False)
    
    def _generate_html_report(self, report_data: Dict[str, Any], output_path: Path) -> None:
        """HTML形式のレポートを生成
        
        Args:
            report_data: レポートデータ
            output_path: 出力ファイルパス
        """
        html_content = self._create_html_content(report_data)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
    
    def _create_html_content(self, report_data: Dict[str, Any]) -> str:
        """HTMLコンテンツを生成
        
        Args:
            report_data: レポートデータ
            
        Returns:
            HTML文字列
        """
        summary = report_data["summary"]
        comparisons_with_diffs = report_data.get("comparisons_with_differences", [])
        
        # HTMLテンプレート
        html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>スナップショット比較レポート</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background-color: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        h1 {{
            color: #333;
            border-bottom: 3px solid #4CAF50;
            padding-bottom: 10px;
        }}
        h2 {{
            color: #555;
            margin-top: 30px;
            border-bottom: 2px solid #ddd;
            padding-bottom: 8px;
        }}
        h3 {{
            color: #666;
            margin-top: 20px;
        }}
        .summary {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin: 20px 0;
        }}
        .summary-card {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            border-radius: 8px;
            text-align: center;
        }}
        .summary-card.success {{
            background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%);
        }}
        .summary-card.warning {{
            background: linear-gradient(135deg, #ff9800 0%, #f57c00 100%);
        }}
        .summary-card.error {{
            background: linear-gradient(135deg, #f44336 0%, #d32f2f 100%);
        }}
        .summary-card h3 {{
            margin: 0 0 10px 0;
            font-size: 14px;
            opacity: 0.9;
            color: white;
            border: none;
        }}
        .summary-card .value {{
            font-size: 36px;
            font-weight: bold;
            margin: 0;
        }}
        .comparison {{
            background-color: #f9f9f9;
            border: 1px solid #ddd;
            border-radius: 6px;
            padding: 20px;
            margin: 15px 0;
        }}
        .comparison-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 15px;
        }}
        .comparison-title {{
            font-size: 18px;
            font-weight: bold;
            color: #333;
        }}
        .badge {{
            padding: 5px 12px;
            border-radius: 12px;
            font-size: 12px;
            font-weight: bold;
        }}
        .badge.differences {{
            background-color: #ff9800;
            color: white;
        }}
        .badge.compatibility {{
            background-color: #f44336;
            color: white;
        }}
        .diff-section {{
            margin: 15px 0;
        }}
        .diff-item {{
            background-color: white;
            border-left: 4px solid #2196F3;
            padding: 10px 15px;
            margin: 8px 0;
            border-radius: 4px;
        }}
        .diff-item.added {{
            border-left-color: #4CAF50;
            background-color: #e8f5e9;
        }}
        .diff-item.removed {{
            border-left-color: #f44336;
            background-color: #ffebee;
        }}
        .diff-item.changed {{
            border-left-color: #ff9800;
            background-color: #fff3e0;
        }}
        .diff-path {{
            font-family: 'Courier New', monospace;
            font-size: 13px;
            color: #666;
            margin-bottom: 5px;
        }}
        .diff-value {{
            font-family: 'Courier New', monospace;
            font-size: 12px;
            padding: 5px;
            background-color: rgba(0,0,0,0.05);
            border-radius: 3px;
            margin: 3px 0;
        }}
        .compatibility-issue {{
            background-color: #ffebee;
            border-left: 4px solid #f44336;
            padding: 12px 15px;
            margin: 8px 0;
            border-radius: 4px;
        }}
        .issue-type {{
            font-weight: bold;
            color: #d32f2f;
            margin-bottom: 5px;
        }}
        .issue-message {{
            color: #555;
            font-size: 14px;
        }}
        .timestamp {{
            color: #999;
            font-size: 12px;
            margin-top: 5px;
        }}
        .no-differences {{
            text-align: center;
            padding: 40px;
            color: #4CAF50;
            font-size: 18px;
        }}
        pre {{
            background-color: #f5f5f5;
            padding: 10px;
            border-radius: 4px;
            overflow-x: auto;
            font-size: 12px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>📊 スナップショット比較レポート</h1>
        <p class="timestamp">生成日時: {report_data['generated_at']}</p>
        
        <h2>サマリ</h2>
        <div class="summary">
            <div class="summary-card">
                <h3>総比較数</h3>
                <div class="value">{summary['total_comparisons']}</div>
            </div>
            <div class="summary-card {'warning' if summary['differences_found'] > 0 else 'success'}">
                <h3>差分検出</h3>
                <div class="value">{summary['differences_found']}</div>
            </div>
            <div class="summary-card {'error' if summary['compatibility_issues_found'] > 0 else 'success'}">
                <h3>互換性問題</h3>
                <div class="value">{summary['compatibility_issues_found']}</div>
            </div>
            <div class="summary-card {'success' if summary['success_rate'] == 100 else 'warning'}">
                <h3>一致率</h3>
                <div class="value">{summary['success_rate']:.1f}%</div>
            </div>
        </div>
"""
        
        # 差分がある場合のみ詳細を表示
        if comparisons_with_diffs:
            html += """
        <h2>差分の詳細</h2>
"""
            for comparison in comparisons_with_diffs:
                html += self._create_comparison_html(comparison)
        else:
            html += """
        <div class="no-differences">
            ✅ すべてのスナップショットが一致しています
        </div>
"""
        
        html += """
    </div>
</body>
</html>
"""
        return html
    
    def _create_comparison_html(self, comparison: Dict[str, Any]) -> str:
        """個別の比較結果のHTMLを生成
        
        Args:
            comparison: 比較結果データ
            
        Returns:
            HTML文字列
        """
        story_name = comparison.get("story_name", "Unknown")
        has_diffs = comparison.get("has_differences", False)
        compat_issues = comparison.get("compatibility_issues", [])
        
        html = f"""
        <div class="comparison">
            <div class="comparison-header">
                <div class="comparison-title">{story_name}</div>
                <div>
"""
        
        if has_diffs:
            html += """
                    <span class="badge differences">差分あり</span>
"""
        
        if compat_issues:
            html += """
                    <span class="badge compatibility">互換性問題</span>
"""
        
        html += """
                </div>
            </div>
"""
        
        # 互換性の問題を表示
        if compat_issues:
            html += """
            <div class="diff-section">
                <h3>互換性の問題</h3>
"""
            for issue in compat_issues:
                issue_type = issue.get("type", "unknown")
                message = issue.get("message", "")
                html += f"""
                <div class="compatibility-issue">
                    <div class="issue-type">{issue_type}</div>
                    <div class="issue-message">{self._escape_html(message)}</div>
                </div>
"""
            html += """
            </div>
"""
        
        # 差分の詳細を表示
        if has_diffs:
            details = comparison.get("details", {})
            
            # 変更された値
            values_changed = details.get("values_changed", [])
            if values_changed:
                html += """
            <div class="diff-section">
                <h3>変更された値</h3>
"""
                for change in values_changed:
                    path = change.get("path", "")
                    old_value = self._format_value(change.get("old_value"))
                    new_value = self._format_value(change.get("new_value"))
                    html += f"""
                <div class="diff-item changed">
                    <div class="diff-path">{self._escape_html(path)}</div>
                    <div class="diff-value">旧: {self._escape_html(old_value)}</div>
                    <div class="diff-value">新: {self._escape_html(new_value)}</div>
                </div>
"""
                html += """
            </div>
"""
            
            # 追加された項目
            items_added = details.get("items_added", [])
            if items_added:
                html += """
            <div class="diff-section">
                <h3>追加された項目</h3>
"""
                for item in items_added:
                    html += f"""
                <div class="diff-item added">
                    <div class="diff-path">{self._escape_html(str(item))}</div>
                </div>
"""
                html += """
            </div>
"""
            
            # 削除された項目
            items_removed = details.get("items_removed", [])
            if items_removed:
                html += """
            <div class="diff-section">
                <h3>削除された項目</h3>
"""
                for item in items_removed:
                    html += f"""
                <div class="diff-item removed">
                    <div class="diff-path">{self._escape_html(str(item))}</div>
                </div>
"""
                html += """
            </div>
"""
        
        html += """
        </div>
"""
        return html
    
    def _format_value(self, value: Any) -> str:
        """値を文字列形式に整形
        
        Args:
            value: 整形する値
            
        Returns:
            整形された文字列
        """
        if value is None:
            return "null"
        
        if isinstance(value, (dict, list)):
            return json.dumps(value, ensure_ascii=False, indent=2)
        
        return str(value)
    
    def _escape_html(self, text: str) -> str:
        """HTMLエスケープ処理
        
        Args:
            text: エスケープするテキスト
            
        Returns:
            エスケープされたテキスト
        """
        if not isinstance(text, str):
            text = str(text)
        
        return (text
                .replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;")
                .replace('"', "&quot;")
                .replace("'", "&#x27;"))

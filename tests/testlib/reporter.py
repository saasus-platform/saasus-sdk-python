"""
レポート生成モジュール

E2Eテスト結果のレポートを生成します。
JSON形式とテキスト形式の両方をサポートします。
"""

import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional

from tests.testlib.models import StoryResult, StepResult
from tests.testlib.config import Config


class Reporter:
    """テスト結果のレポートを生成
    
    テスト実行結果を集計し、JSON形式とテキスト形式のレポートを生成します。
    また、コンソールにサマリを出力します。
    
    Attributes:
        config: テスト設定
    """
    
    def __init__(self, config: Config):
        """Reporterを初期化
        
        Args:
            config: テスト設定
        """
        self.config = config
    
    def generate(
        self,
        story_results: List[StoryResult],
        coverage_report: Dict[str, Any],
        snapshot_diffs: Optional[List[Dict]] = None
    ) -> Dict[str, Path]:
        """レポートを生成（JSON + テキスト）
        
        テスト結果を集計し、JSON形式とテキスト形式のレポートを生成します。
        また、コンソールにサマリを出力します。
        
        Args:
            story_results: ストーリー実行結果のリスト
            coverage_report: カバレッジレポート
            snapshot_diffs: スナップショット差分のリスト（オプション）
        
        Returns:
            生成されたレポートファイルのパス辞書
            - "json": JSONレポートのパス
            - "text": テキストレポートのパス
        
        Examples:
            >>> reporter = Reporter(config)
            >>> paths = reporter.generate(story_results, coverage_report)
            >>> print(f"JSONレポート: {paths['json']}")
            >>> print(f"テキストレポート: {paths['text']}")
        """
        # サマリを作成
        summary = self._create_summary(story_results, coverage_report)
        
        # 詳細レポート
        detailed_report = {
            "summary": summary,
            "story_results": [
                self._serialize_story_result(sr) for sr in story_results
            ],
            "coverage": coverage_report,
            "snapshot_diffs": snapshot_diffs or [],
            "timestamp": datetime.now().isoformat()
        }
        
        # JSONレポート
        json_path = Path("reports/e2e_report.json")
        json_path.parent.mkdir(parents=True, exist_ok=True)
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(detailed_report, f, indent=2, ensure_ascii=False)
        
        # テキストレポート
        text_path = Path("reports/e2e_report.txt")
        with open(text_path, 'w', encoding='utf-8') as f:
            f.write(self._format_text_report(detailed_report))
        
        # コンソール出力
        self._print_summary(summary)
        
        return {
            "json": json_path,
            "text": text_path
        }

    def _create_summary(
        self,
        story_results: List[StoryResult],
        coverage_report: Dict[str, Any]
    ) -> Dict[str, Any]:
        """サマリを作成
        
        テスト結果を集計し、統計情報を計算します。
        
        Args:
            story_results: ストーリー実行結果のリスト
            coverage_report: カバレッジレポート
        
        Returns:
            サマリ情報の辞書
            - total_stories: 総ストーリー数
            - successful_stories: 成功したストーリー数
            - failed_stories: 失敗したストーリー数
            - success_rate: 成功率（%）
            - total_execution_time: 総実行時間（秒）
            - coverage_percentage: カバレッジ率（%）
        """
        total_stories = len(story_results)
        successful_stories = sum(1 for sr in story_results if sr.success)
        failed_stories = total_stories - successful_stories
        
        total_time = sum(sr.execution_time for sr in story_results)
        
        return {
            "total_stories": total_stories,
            "successful_stories": successful_stories,
            "failed_stories": failed_stories,
            "success_rate": successful_stories / total_stories * 100 if total_stories > 0 else 0,
            "total_execution_time": total_time,
            "coverage_percentage": coverage_report.get("coverage_percentage", 0)
        }

    def _serialize_story_result(self, story_result: StoryResult) -> Dict[str, Any]:
        """StoryResultをシリアライズ可能な辞書に変換
        
        StoryResultオブジェクトをJSON形式で保存できる辞書に変換します。
        
        Args:
            story_result: ストーリー実行結果
        
        Returns:
            シリアライズ可能な辞書
        """
        return {
            "story": {
                "name": story_result.story.name,
                "description": story_result.story.description,
                "module": story_result.story.module,
                "tags": story_result.story.tags,
                "timeout": story_result.story.timeout
            },
            "success": story_result.success,
            "execution_time": story_result.execution_time,
            "timestamp": story_result.timestamp.isoformat(),
            "setup_results": [
                self._serialize_step_result(sr) for sr in story_result.setup_results
            ],
            "step_results": [
                self._serialize_step_result(sr) for sr in story_result.step_results
            ],
            "cleanup_results": [
                self._serialize_step_result(sr) for sr in story_result.cleanup_results
            ]
        }
    
    def _serialize_step_result(self, step_result: StepResult) -> Dict[str, Any]:
        """StepResultをシリアライズ可能な辞書に変換
        
        StepResultオブジェクトをJSON形式で保存できる辞書に変換します。
        
        Args:
            step_result: ステップ実行結果
        
        Returns:
            シリアライズ可能な辞書
        """
        result = {
            "step": {
                "method_name": step_result.step.method_name,
                "description": step_result.step.description,
                "expected_status": step_result.step.expected_status,
                "store_as": step_result.step.store_as,
                "skip_on_dry_run": step_result.step.skip_on_dry_run
            },
            "success": step_result.success,
            "status_code": step_result.status_code,
            "execution_time": step_result.execution_time,
            "timestamp": step_result.timestamp.isoformat()
        }
        
        # エラー情報を追加
        if step_result.error:
            result["error"] = {
                "type": type(step_result.error).__name__,
                "message": str(step_result.error)
            }
        
        # レスポンスのサマリを追加（機密情報を含まないように）
        if step_result.response is not None:
            result["response_summary"] = self._create_response_summary(step_result.response)
        
        return result
    
    def _create_response_summary(self, response: Any) -> Dict[str, Any]:
        """レスポンスのサマリを作成
        
        レスポンスオブジェクトから機密情報を含まないサマリを作成します。
        
        Args:
            response: レスポンスオブジェクト
        
        Returns:
            レスポンスサマリの辞書
        """
        summary = {
            "type": type(response).__name__
        }
        
        # 辞書型の場合、キーのリストを含める
        if isinstance(response, dict):
            summary["keys"] = list(response.keys())
            summary["size"] = len(response)
        # リスト型の場合、要素数を含める
        elif isinstance(response, list):
            summary["length"] = len(response)
        # 文字列型の場合、長さを含める
        elif isinstance(response, str):
            summary["length"] = len(response)
        
        return summary

    def _format_text_report(self, report: Dict[str, Any]) -> str:
        """テキスト形式のレポートを生成
        
        人間が読みやすいテキスト形式のレポートを生成します。
        失敗したストーリーの詳細を含めます。
        
        Args:
            report: 詳細レポートの辞書
        
        Returns:
            テキスト形式のレポート文字列
        """
        lines = [
            "=" * 80,
            "E2E Test Report",
            "=" * 80,
            "",
            "Summary:",
            f"  Total Stories: {report['summary']['total_stories']}",
            f"  Successful: {report['summary']['successful_stories']}",
            f"  Failed: {report['summary']['failed_stories']}",
            f"  Success Rate: {report['summary']['success_rate']:.2f}%",
            f"  Total Time: {report['summary']['total_execution_time']:.2f}s",
            f"  Coverage: {report['summary']['coverage_percentage']:.2f}%",
            "",
            "=" * 80
        ]
        
        # 失敗したストーリーの詳細
        if report['summary']['failed_stories'] > 0:
            lines.append("")
            lines.append("Failed Stories:")
            lines.append("-" * 80)
            
            for story_result in report['story_results']:
                if not story_result['success']:
                    lines.append(f"\n  Story: {story_result['story']['name']}")
                    lines.append(f"  Description: {story_result['story']['description']}")
                    lines.append(f"  Module: {story_result['story']['module']}")
                    lines.append(f"  Execution Time: {story_result['execution_time']:.2f}s")
                    lines.append("")
                    
                    # Setup の失敗
                    failed_setup = [sr for sr in story_result['setup_results'] if not sr['success']]
                    if failed_setup:
                        lines.append("    Setup Failures:")
                        for step_result in failed_setup:
                            lines.append(f"      ✗ {step_result['step']['method_name']}")
                            if step_result.get('error'):
                                lines.append(f"        Error: {step_result['error']['type']}: {step_result['error']['message']}")
                        lines.append("")
                    
                    # Steps の失敗
                    failed_steps = [sr for sr in story_result['step_results'] if not sr['success']]
                    if failed_steps:
                        lines.append("    Step Failures:")
                        for step_result in failed_steps:
                            lines.append(f"      ✗ {step_result['step']['method_name']}")
                            if step_result['step']['description']:
                                lines.append(f"        Description: {step_result['step']['description']}")
                            if step_result.get('error'):
                                lines.append(f"        Error: {step_result['error']['type']}: {step_result['error']['message']}")
                            if step_result.get('status_code'):
                                lines.append(f"        Status Code: {step_result['status_code']}")
                        lines.append("")
                    
                    # Cleanup の失敗
                    failed_cleanup = [sr for sr in story_result['cleanup_results'] if not sr['success']]
                    if failed_cleanup:
                        lines.append("    Cleanup Failures:")
                        for step_result in failed_cleanup:
                            lines.append(f"      ✗ {step_result['step']['method_name']}")
                            if step_result.get('error'):
                                lines.append(f"        Error: {step_result['error']['type']}: {step_result['error']['message']}")
                        lines.append("")
        
        # 成功したストーリーのサマリ
        if report['summary']['successful_stories'] > 0:
            lines.append("")
            lines.append("Successful Stories:")
            lines.append("-" * 80)
            
            for story_result in report['story_results']:
                if story_result['success']:
                    lines.append(
                        f"  ✓ {story_result['story']['name']} "
                        f"({story_result['execution_time']:.2f}s)"
                    )
        
        # カバレッジ情報
        if report.get('coverage'):
            lines.append("")
            lines.append("Coverage:")
            lines.append("-" * 80)
            coverage = report['coverage']
            lines.append(f"  Total Methods: {coverage.get('total_methods', 0)}")
            lines.append(f"  Executed Methods: {coverage.get('executed_methods', 0)}")
            lines.append(f"  Not Executed Methods: {coverage.get('not_executed_methods', 0)}")
            lines.append(f"  Coverage: {coverage.get('coverage_percentage', 0):.2f}%")
            
            # 未実行メソッドのリスト（最初の10個のみ）
            not_executed = coverage.get('not_executed_list', [])
            if not_executed:
                lines.append("")
                lines.append("  Not Executed Methods (first 10):")
                for method in not_executed[:10]:
                    lines.append(f"    - {method}")
                if len(not_executed) > 10:
                    lines.append(f"    ... and {len(not_executed) - 10} more")
        
        # スナップショット差分情報
        if report.get('snapshot_diffs'):
            lines.append("")
            lines.append("Snapshot Differences:")
            lines.append("-" * 80)
            diffs_with_changes = [d for d in report['snapshot_diffs'] if d.get('has_differences')]
            if diffs_with_changes:
                lines.append(f"  Stories with differences: {len(diffs_with_changes)}")
                for diff in diffs_with_changes:
                    lines.append(f"    - {diff.get('story_name', 'Unknown')}")
            else:
                lines.append("  No differences detected")
        
        # タイムスタンプ
        lines.append("")
        lines.append("=" * 80)
        lines.append(f"Report generated at: {report['timestamp']}")
        lines.append("=" * 80)
        
        return "\n".join(lines)

    def _print_summary(self, summary: Dict[str, Any]) -> None:
        """サマリをコンソールに出力
        
        テスト結果のサマリを見やすい形式でコンソールに出力します。
        
        Args:
            summary: サマリ情報の辞書
        """
        print("\n" + "=" * 80)
        print("E2E Test Summary")
        print("=" * 80)
        print(f"Stories: {summary['successful_stories']}/{summary['total_stories']} passed")
        print(f"Success Rate: {summary['success_rate']:.2f}%")
        print(f"Coverage: {summary['coverage_percentage']:.2f}%")
        print(f"Total Time: {summary['total_execution_time']:.2f}s")
        print("=" * 80 + "\n")

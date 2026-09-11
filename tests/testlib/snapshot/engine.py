"""スナップショットエンジン

このモジュールは、スナップショットのキャプチャ、比較、レポート生成を管理します。
"""

import json
from pathlib import Path
from typing import Any, Dict, List, Optional
from datetime import datetime, timezone

from tests.testlib.models import StoryResult, StepResult
from tests.testlib.snapshot.config import SnapshotConfig
from tests.testlib.snapshot.masker import Masker
from tests.testlib.snapshot.comparator import Comparator
from tests.testlib.snapshot.reporter import SnapshotReporter
from tests.testlib.logger import TestLogger


class SnapshotEngine:
    """スナップショットのキャプチャ、比較、レポート生成を管理
    
    Attributes:
        config: スナップショット設定
        logger: ロガーインスタンス
        masker: 機密情報マスキング用インスタンス
        comparator: 差分比較用インスタンス
    """
    
    def __init__(self, config: SnapshotConfig, logger: TestLogger):
        """SnapshotEngineを初期化
        
        Args:
            config: スナップショット設定
            logger: ロガーインスタンス
        """
        self.config = config
        self.logger = logger
        self.masker = Masker(config.mask_patterns)
        self.comparator = Comparator()
        self.reporter = SnapshotReporter(config)
    
    def capture(self, story_result: StoryResult, client: Optional[Any] = None) -> Optional[Path]:
        """ストーリー結果をスナップショットとして保存
        
        Args:
            story_result: ストーリー実行結果
            client: SDKクライアントオブジェクト（オプション、シグネチャ記録に使用）
            
        Returns:
            保存されたスナップショットファイルのパス、キャプチャが無効の場合はNone
        """
        if not self.config.capture_enabled:
            return None
        
        # レスポンスをシリアライズ
        snapshot_data = self._serialize_story_result(story_result)
        
        # マスキング前にPydanticモデル等を完全に辞書へ変換する。
        # マスカーはキー名ベースで動作するため、モデルのまま渡すと
        # ネストされたapi_key/saas_id等の機密フィールドがマスクされずに
        # 残ってしまう（_serialize_responseはdictの値を再帰変換しないため）。
        snapshot_data = self._deep_serialize(snapshot_data)
        
        # 機密情報をマスク
        masked_data = self.masker.mask(snapshot_data)
        
        # メタデータを追加
        masked_data["summary"] = {
            "total_steps": len(story_result.step_results),
            "successful_steps": sum(1 for sr in story_result.step_results if sr.success),
            "failed_steps": sum(1 for sr in story_result.step_results if not sr.success),
            "total_duration": int(story_result.execution_time * 1_000_000_000),
            "average_step_duration": int(story_result.execution_time * 1_000_000_000 / len(story_result.step_results)) if story_result.step_results else 0
        }
        
        masked_data["metadata"] = {
            "sdk_version": "1.0.0",
            "test_environment": "dev",
            "capture_level": "FULL",
            "git_tag": self.config.get_snapshot_tag(),
            "module": story_result.story.module,
            "tags": story_result.story.tags,
            "captured_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
            "masked_count": self.masker.get_masked_count()
        }
        
        # ファイルに保存
        snapshot_path = self._get_snapshot_path(story_result.story.module, story_result.story.name)
        snapshot_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Pydanticモデルを辞書に変換
        masked_data = self._deep_serialize(masked_data)
        
        with open(snapshot_path, 'w', encoding='utf-8') as f:
            json.dump(masked_data, f, indent=2, ensure_ascii=False)
        
        # タグ付きスナップショットを保存
        tagged_path = self.config.get_tagged_snapshot_path(story_result.story.module, story_result.story.name)
        tagged_path.parent.mkdir(parents=True, exist_ok=True)
        with open(tagged_path, 'w', encoding='utf-8') as f:
            json.dump(masked_data, f, indent=2, ensure_ascii=False)
        
        # バリデーション結果を保存
        self._save_validation_result(story_result)
        
        self.logger.logger.debug(f"Snapshot captured: {snapshot_path}")
        self.logger.logger.debug(f"Tagged snapshot: {tagged_path}")
        return snapshot_path
    
    def _save_validation_result(self, story_result: StoryResult) -> None:
        """バリデーション結果を保存
        
        Args:
            story_result: ストーリー実行結果
        """
        validation_dir = self.config.get_story_validations_dir(story_result.story.module)
        validation_dir.mkdir(parents=True, exist_ok=True)
        validation_path = validation_dir / f"{story_result.story.name}.json"
        
        total_errors = sum(1 for sr in story_result.step_results if not sr.success)
        
        validation_data = {
            "story_name": story_result.story.name,
            "validation_time": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
            "is_valid": story_result.success,
            "completion_status": "complete" if story_result.success else "failed",
            "sequence_errors": None,
            "state_transition_errors": None,
            "comparison_differences": None,
            "timing_errors": None,
            "summary": {
                "total_errors": total_errors,
                "total_warnings": 0,
                "total_info": 0,
                "is_valid": story_result.success
            }
        }
        
        with open(validation_path, 'w', encoding='utf-8') as f:
            json.dump(validation_data, f, indent=2, ensure_ascii=False)
    
    def _deep_serialize(self, obj: Any) -> Any:
        """オブジェクトを再帰的にシリアライズ可能な形式に変換
        
        Args:
            obj: シリアライズするオブジェクト
            
        Returns:
            シリアライズ可能なオブジェクト
        """
        if obj is None:
            return None
        
        # Pydanticモデルの場合
        if hasattr(obj, 'model_dump'):
            return self._deep_serialize(obj.model_dump())
        elif hasattr(obj, 'dict'):
            return self._deep_serialize(obj.dict())
        
        # 辞書の場合
        if isinstance(obj, dict):
            return {key: self._deep_serialize(value) for key, value in obj.items()}
        
        # リストの場合
        if isinstance(obj, (list, tuple)):
            return [self._deep_serialize(item) for item in obj]
        
        # その他のプリミティブ型
        return obj

    def compare(self, story_result: StoryResult, client: Optional[Any] = None) -> Optional[Dict]:
        """現在の結果と前回のスナップショットを比較
        
        Args:
            story_result: ストーリー実行結果
            client: SDKクライアントオブジェクト（オプション、互換性チェックに使用）
            
        Returns:
            差分情報を含む辞書、比較が無効または前回のスナップショットがない場合はNone
        """
        if not self.config.compare_enabled:
            return None
        
        snapshot_path = self._get_snapshot_path(story_result.story.module, story_result.story.name)
        
        if not snapshot_path.exists():
            self.logger.logger.warning(
                f"No previous snapshot found for {story_result.story.name}"
            )
            return None
        
        # 前回のスナップショットを読み込み
        with open(snapshot_path, 'r', encoding='utf-8') as f:
            previous_snapshot = json.load(f)
        
        # 現在の結果をシリアライズ
        current_snapshot = self._serialize_story_result(story_result)
        # マスキング前にPydanticモデル等を完全に辞書へ変換する（captureと整合）
        current_snapshot = self._deep_serialize(current_snapshot)
        current_snapshot = self.masker.mask(current_snapshot)
        
        # 差分を計算
        diff = self.comparator.compare(previous_snapshot, current_snapshot)
        
        # ストーリー名を追加（レポート生成で使用）
        diff["story_name"] = story_result.story.name
        diff["module"] = story_result.story.module
        
        # 差分を保存
        if diff["has_differences"]:
            diff_path = self._get_comparison_path(story_result.story.module, story_result.story.name)
            diff_path.parent.mkdir(parents=True, exist_ok=True)
            
            with open(diff_path, 'w', encoding='utf-8') as f:
                json.dump(diff, f, indent=2, ensure_ascii=False)
            
            self.logger.logger.info(f"Differences detected and saved to: {diff_path}")
        
        return diff
    
    def _serialize_story_result(self, story_result: StoryResult) -> Dict[str, Any]:
        """StoryResultをシリアライズ可能な辞書に変換
        
        Args:
            story_result: ストーリー実行結果
            
        Returns:
            シリアライズ可能な辞書
        """
        steps = [self._serialize_step_result(sr) for sr in story_result.step_results]
        
        # サマリー統計を計算
        total_steps = len(steps)
        successful_steps = sum(1 for s in steps if s["success"])
        failed_steps = total_steps - successful_steps
        total_duration = sum(s["duration"] for s in steps)
        average_step_duration = total_duration // total_steps if total_steps > 0 else 0
        
        return {
            "story_name": story_result.story.name,
            "description": story_result.story.description,
            "timestamp": story_result.timestamp.isoformat() + "Z",
            "duration": int(story_result.execution_time * 1_000_000_000),  # ナノ秒
            "status": "passed" if story_result.success else "failed",
            "variables": {
                "story_name": story_result.story.name
            },
            "steps": steps,
            "summary": {
                "total_steps": total_steps,
                "successful_steps": successful_steps,
                "failed_steps": failed_steps,
                "total_duration": total_duration,
                "average_step_duration": average_step_duration
            },
            "metadata": {
                "sdk_version": "1.0.0",
                "test_environment": "dev",
                "capture_level": "FULL",
                "git_tag": self.config.get_snapshot_tag(),
                "module": story_result.story.module,
                "tags": story_result.story.tags
            }
        }
    
    def _serialize_step_result(self, step_result: StepResult) -> Dict[str, Any]:
        """StepResultをシリアライズ可能な辞書に変換
        
        Args:
            step_result: ステップ実行結果
            
        Returns:
            シリアライズ可能な辞書
        """
        # 解決されたパラメータを使用（なければ元のparamsを試す）
        params = step_result.resolved_params
        if params is None:
            params = step_result.step.params
            if callable(params):
                params = {}  # 関数の場合は空の辞書
        
        # Pydanticモデルを辞書に変換
        params = self._serialize_params(params)
        
        executed_method = step_result.executed_method_name or step_result.step.method_name
        method_original = step_result.step.method_name

        # スキップされたステップの処理
        if step_result.step.skip:
            return {
                "step_name": step_result.step.description or step_result.step.method_name,
                "method": executed_method,
                "method_original": method_original,
                "parameters": params,
                "return_value": {
                    "type": "*http.Response",
                    "status_code": None,
                    "status": "SKIPPED",
                    "http_response": {
                        "status_code": None,
                        "status": "SKIPPED",
                        "headers": {},
                        "content_length": 0,
                        "trace_id": ""
                    },
                    "json_data": None,
                    "json_schema": {"type": "unknown"},
                    "body": "",
                    "headers": {}
                },
                "duration": 0,
                "status_code": None,
                "success": True,
                "timestamp": step_result.timestamp.isoformat() + "Z"
            }
        
        # レスポンスデータを取得
        json_data = self._serialize_response(step_result.response)
        
        original_status_code = step_result.status_code
        effective_status_code = original_status_code
        if effective_status_code is None:
            effective_status_code = 200

        # HTTPレスポンス情報を構築
        http_response = {
            "status_code": effective_status_code,
            "status": self._get_status_text(effective_status_code),
            "headers": {},
            "content_length": 0,
            "trace_id": ""
        }
        
        serialized = {
            "step_name": step_result.step.description or step_result.step.method_name,
            "method": executed_method,
            "method_original": method_original,
            "parameters": params,
            "return_value": {
                "type": "*http.Response" if original_status_code is not None else "dict",
                "status_code": effective_status_code,
                "status": self._get_status_text(effective_status_code),
                "http_response": http_response,
                "json_data": json_data,
                "json_schema": self._generate_json_schema(json_data),
                "body": "",
                "headers": {}
            },
            "duration": int(step_result.execution_time * 1_000_000_000),  # ナノ秒
            "status_code": effective_status_code,
            "success": step_result.success,
            "timestamp": step_result.timestamp.isoformat() + "Z"
        }
        
        return serialized
    
    def _serialize_params(self, params: Any) -> Dict[str, Any]:
        """パラメータをシリアライズ可能な辞書に変換
        
        Args:
            params: パラメータ（辞書、Pydanticモデル、その他）
            
        Returns:
            シリアライズ可能な辞書
        """
        if params is None:
            return {}
        
        if isinstance(params, dict):
            result = {}
            for key, value in params.items():
                # Pydanticモデルを辞書に変換
                if hasattr(value, 'model_dump'):
                    result[key] = value.model_dump()
                elif hasattr(value, 'dict'):
                    result[key] = value.dict()
                elif isinstance(value, dict):
                    result[key] = self._serialize_params(value)
                else:
                    result[key] = value
            return result
        
        # Pydanticモデルの場合
        if hasattr(params, 'model_dump'):
            return params.model_dump()
        elif hasattr(params, 'dict'):
            return params.dict()
        
        return params
    
    def _get_status_text(self, status_code: int) -> str:
        """HTTPステータスコードからステータステキストを取得
        
        Args:
            status_code: HTTPステータスコード
            
        Returns:
            ステータステキスト
        """
        status_texts = {
            200: "200 OK",
            201: "201 Created",
            204: "204 No Content",
            400: "400 Bad Request",
            401: "401 Unauthorized",
            403: "403 Forbidden",
            404: "404 Not Found",
            500: "500 Internal Server Error"
        }
        return status_texts.get(status_code, f"{status_code} Unknown")
    
    def _generate_json_schema(self, data: Any) -> Dict[str, Any]:
        """データからJSONスキーマを生成
        
        Args:
            data: データオブジェクト
            
        Returns:
            JSONスキーマ
        """
        if data is None:
            return {"type": "null"}
        
        if isinstance(data, bool):
            return {"type": "boolean"}
        
        if isinstance(data, int):
            return {"type": "integer"}
        
        if isinstance(data, float):
            return {"type": "number"}
        
        if isinstance(data, str):
            return {"type": "string"}
        
        if isinstance(data, list):
            if len(data) > 0:
                return {
                    "type": "array",
                    "items": self._generate_json_schema(data[0])
                }
            return {"type": "array", "items": {}}
        
        if isinstance(data, dict):
            properties = {}
            required = []
            for key, value in data.items():
                properties[key] = self._generate_json_schema(value)
                if value is not None:
                    required.append(key)
            return {
                "type": "object",
                "properties": properties,
                "required": required
            }
        
        # その他のオブジェクト
        if hasattr(data, '__dict__'):
            return self._generate_json_schema(data.__dict__)
        
        return {"type": "unknown"}
    
    def _serialize_response(self, response: Any) -> Any:
        """レスポンスをシリアライズ可能な形式に変換
        
        Args:
            response: レスポンスオブジェクト
            
        Returns:
            シリアライズ可能な形式のレスポンス
        """
        if response is None:
            return None
        
        # 辞書の場合はそのまま返す
        if isinstance(response, dict):
            return response
        
        # リストの場合は各要素を再帰的に処理
        if isinstance(response, list):
            return [self._serialize_response(item) for item in response]
        
        # オブジェクトの場合は__dict__を使用
        if hasattr(response, '__dict__'):
            return self._serialize_response(response.__dict__)
        
        # プリミティブ型はそのまま返す
        if isinstance(response, (str, int, float, bool)):
            return response
        
        # その他の場合は文字列に変換
        return str(response)

    def _get_snapshot_path(self, module: str, story_name: str) -> Path:
        """スナップショットファイルのパスを取得
        
        Args:
            module: モジュール名
            story_name: ストーリー名
            
        Returns:
            スナップショットファイルのパス
        """
        snapshot_dir = self.config.get_story_snapshots_dir(module)
        return snapshot_dir / f"{story_name}.json"
    
    def _get_comparison_path(self, module: str, story_name: str) -> Path:
        """比較結果ファイルのパスを取得
        
        Args:
            module: モジュール名
            story_name: ストーリー名
            
        Returns:
            比較結果ファイルのパス
        """
        comparison_dir = self.config.get_story_comparisons_dir(module)
        return comparison_dir / f"{story_name}_diff.json"
    
    def generate_report(self, all_diffs: List[Dict], module: Optional[str] = None) -> Optional[Dict[str, Path]]:
        """すべての差分からレポートを生成
        
        Args:
            all_diffs: すべてのストーリーの差分情報のリスト
            module: モジュール名（指定された場合、モジュール別のレポートを生成）
            
        Returns:
            生成されたレポートファイルのパスを含む辞書（"json"と"html"キー）、レポート生成が無効の場合はNone
        """
        if not self.config.report_enabled:
            return None
        
        # SnapshotReporterを使用してレポートを生成
        report_paths = self.reporter.generate(all_diffs, module)
        
        if report_paths:
            if "json" in report_paths:
                self.logger.logger.info(f"JSON report generated: {report_paths['json']}")
            if "html" in report_paths:
                self.logger.logger.info(f"HTML report generated: {report_paths['html']}")
        
        return report_paths

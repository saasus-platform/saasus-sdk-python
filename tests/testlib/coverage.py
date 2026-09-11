"""
カバレッジトラッキングモジュール

SDKメソッドの実行状況を追跡し、カバレッジレポートを生成します。
"""

import importlib
import inspect
from typing import Dict, Any, Set, List


class CoverageTracker:
    """SDKメソッドのカバレッジを追跡"""
    
    def __init__(self, sdk_modules: List[str]):
        """
        CoverageTrackerを初期化
        
        Args:
            sdk_modules: 追跡対象のSDKモジュール名のリスト（例: ['auth', 'billing', 'pricing']）
        """
        self.sdk_modules = sdk_modules
        self.executed_methods: Dict[str, Dict[str, Any]] = {}
        self.all_methods: Set[str] = self._discover_all_methods()
    
    def record(self, module: str, method_name: str, success: bool) -> None:
        """
        メソッド実行を記録
        
        Args:
            module: モジュール名（例: 'auth'）
            method_name: メソッド名（例: 'create_saas_user'）
            success: 実行が成功したかどうか
        """
        key = f"{module}.{method_name}"
        
        if key not in self.executed_methods:
            self.executed_methods[key] = {
                "count": 0,
                "success_count": 0,
                "failure_count": 0
            }
        
        self.executed_methods[key]["count"] += 1
        if success:
            self.executed_methods[key]["success_count"] += 1
        else:
            self.executed_methods[key]["failure_count"] += 1
    
    def get_coverage_report(self) -> Dict[str, Any]:
        """
        カバレッジレポートを生成
        
        Returns:
            カバレッジ統計情報を含む辞書:
            - total_methods: 全メソッド数
            - executed_methods: 実行済みメソッド数
            - not_executed_methods: 未実行メソッド数
            - coverage_percentage: カバレッジ率
            - executed_details: 実行済みメソッドの詳細
            - not_executed_list: 未実行メソッドのリスト
        """
        executed = set(self.executed_methods.keys())
        not_executed = self.all_methods - executed
        
        total_methods = len(self.all_methods)
        coverage_percentage = (len(executed) / total_methods * 100) if total_methods > 0 else 0.0
        
        return {
            "total_methods": total_methods,
            "executed_methods": len(executed),
            "not_executed_methods": len(not_executed),
            "coverage_percentage": coverage_percentage,
            "executed_details": self.executed_methods,
            "not_executed_list": sorted(list(not_executed))
        }
    
    def _discover_all_methods(self) -> Set[str]:
        """
        SDKの全メソッドを検出
        
        Returns:
            全メソッド名のセット（形式: "module.method_name"）
        """
        methods = set()
        
        for module_name in self.sdk_modules:
            try:
                # SDKクライアントモジュールを動的にインポート
                module = importlib.import_module(
                    f"saasus_sdk_python.client.{module_name}_client"
                )
                
                # クライアントクラスを取得
                client_class_name = f"{module_name.capitalize()}Client"
                if not hasattr(module, client_class_name):
                    # クラス名が見つからない場合はスキップ
                    continue
                
                client_class = getattr(module, client_class_name)
                
                # クラスの全メソッドを列挙
                for name, method in inspect.getmembers(client_class, predicate=inspect.isfunction):
                    # プライベートメソッド（_で始まる）を除外
                    if not name.startswith("_"):
                        methods.add(f"{module_name}.{name}")
                
            except (ImportError, AttributeError) as e:
                # モジュールが見つからない場合は警告を出してスキップ
                print(f"Warning: Could not import module '{module_name}': {e}")
                continue
        
        return methods

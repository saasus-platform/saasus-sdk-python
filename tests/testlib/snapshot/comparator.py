"""スナップショット間の差分を計算するモジュール"""

from typing import Dict, List
from datetime import datetime
from deepdiff import DeepDiff


class Comparator:
    """スナップショット間の差分を計算"""
    
    def compare(self, previous: Dict, current: Dict) -> Dict:
        """2つのスナップショットを比較
        
        Args:
            previous: 前回のスナップショット
            current: 現在のスナップショット
            
        Returns:
            差分情報を含む辞書
        """
        # deepdiffで差分を計算
        diff = DeepDiff(
            previous,
            current,
            ignore_order=True,
            report_repetition=True
        )
        
        # 差分を整形
        formatted_diff = {
            "has_differences": bool(diff),
            "summary": self._create_summary(diff),
            "details": self._format_diff(diff),
            "timestamp": datetime.now().isoformat()
        }
        
        return formatted_diff
    
    def _create_summary(self, diff: DeepDiff) -> Dict:
        """差分のサマリを作成
        
        Args:
            diff: DeepDiffオブジェクト
            
        Returns:
            サマリ情報を含む辞書
        """
        return {
            "values_changed": len(diff.get("values_changed", {})),
            "items_added": len(diff.get("dictionary_item_added", [])),
            "items_removed": len(diff.get("dictionary_item_removed", [])),
            "type_changes": len(diff.get("type_changes", {}))
        }
    
    def _format_diff(self, diff: DeepDiff) -> Dict:
        """差分を読みやすい形式に整形
        
        Args:
            diff: DeepDiffオブジェクト
            
        Returns:
            整形された差分情報
        """
        return {
            "values_changed": self._format_values_changed(
                diff.get("values_changed", {})
            ),
            "items_added": list(diff.get("dictionary_item_added", [])),
            "items_removed": list(diff.get("dictionary_item_removed", [])),
            "type_changes": dict(diff.get("type_changes", {}))
        }
    
    def _format_values_changed(self, values_changed: Dict) -> List[Dict]:
        """変更された値を整形
        
        Args:
            values_changed: DeepDiffの値変更情報
            
        Returns:
            整形された変更情報のリスト
        """
        return [
            {
                "path": path,
                "old_value": change.get("old_value"),
                "new_value": change.get("new_value")
            }
            for path, change in values_changed.items()
        ]

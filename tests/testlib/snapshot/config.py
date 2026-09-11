"""
スナップショット設定管理

スナップショットのキャプチャ、比較、レポート生成の動作を制御する設定を管理します。
"""

import os
import re
import subprocess
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional


@dataclass
class SnapshotConfig:
    """スナップショット設定"""
    
    # スナップショット保存先ディレクトリ
    snapshot_dir: str = "tests/snapshots"
    
    # キャプチャ機能の有効化
    capture_enabled: bool = False
    
    # 比較機能の有効化
    compare_enabled: bool = False
    
    # レポート生成の有効化
    report_enabled: bool = False
    
    # 機密情報マスキングパターン（正規表現）
    mask_patterns: List[str] = field(default_factory=lambda: [
        r"api_key",
        r"secret",
        r"password",
        r"token",
        r"authorization",
        r"credential"
    ])
    
    # キャッシュされたGitタグ
    _cached_git_tag: Optional[str] = field(default=None, repr=False)
    
    @classmethod
    def from_env(cls) -> 'SnapshotConfig':
        """環境変数からスナップショット設定を読み込む
        
        Returns:
            SnapshotConfig: スナップショット設定オブジェクト
        """
        snapshot_enabled = os.getenv("SNAPSHOT_ENABLED", "false").lower() == "true"
        snapshot_mode = os.getenv("SNAPSHOT_MODE", "capture").lower()
        
        # モードに応じて機能を有効化
        capture_enabled = snapshot_mode in ["capture", "full"] and snapshot_enabled
        compare_enabled = snapshot_mode in ["compare", "full"] and snapshot_enabled
        report_enabled = snapshot_mode in ["report", "full"] and snapshot_enabled
        
        return cls(
            snapshot_dir=os.getenv("SNAPSHOT_DIR", "tests/snapshots"),
            capture_enabled=capture_enabled,
            compare_enabled=compare_enabled,
            report_enabled=report_enabled
        )
    
    def get_snapshot_tag(self) -> str:
        """Gitタグまたはコミットハッシュを取得"""
        if self._cached_git_tag:
            return self._cached_git_tag
        
        # 1. 正確なタグを試す
        try:
            result = subprocess.run(
                ["git", "describe", "--tags", "--exact-match", "HEAD"],
                capture_output=True, text=True, check=True, timeout=5
            )
            self._cached_git_tag = result.stdout.strip()
            return self._cached_git_tag
        except (subprocess.CalledProcessError, OSError):
            pass
        
        # 2. タグ+コミット情報を試す
        try:
            result = subprocess.run(
                ["git", "describe", "--tags", "--always"],
                capture_output=True, text=True, check=True, timeout=5
            )
            self._cached_git_tag = result.stdout.strip()
            return self._cached_git_tag
        except (subprocess.CalledProcessError, OSError):
            pass
        
        # 3. コミットハッシュにフォールバック
        try:
            result = subprocess.run(
                ["git", "rev-parse", "--short", "HEAD"],
                capture_output=True, text=True, check=True, timeout=5
            )
            self._cached_git_tag = result.stdout.strip()
            return self._cached_git_tag
        except (subprocess.CalledProcessError, OSError):
            pass
        
        # 4. タイムスタンプにフォールバック
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        self._cached_git_tag = f"dev-{timestamp}"
        return self._cached_git_tag
    
    def _sanitize_story_name(self, story_name: str) -> str:
        """ストーリー名をファイル名用にサニタイズ"""
        sanitized = re.sub(r'[\s\-./\\]+', '_', story_name).lower()
        sanitized = re.sub(r'_+', '_', sanitized)
        return sanitized.strip('_')
    
    def _sanitize_tag(self, tag: str) -> str:
        """タグをファイル名用にサニタイズ"""
        return re.sub(r'[/\\:]', '_', tag)
    
    def get_snapshot_dir_path(self) -> Path:
        """スナップショットディレクトリのPathオブジェクトを取得"""
        return Path(self.snapshot_dir)
    
    def get_module_snapshot_dir(self, module: str) -> Path:
        """モジュール別のスナップショットディレクトリを取得"""
        return self.get_snapshot_dir_path() / module
    
    def get_story_snapshots_dir(self, module: str) -> Path:
        """ストーリースナップショット保存ディレクトリを取得"""
        return self.get_module_snapshot_dir(module) / "story_snapshots"
    
    def get_story_snapshot_tag_dir(self, module: str) -> Path:
        """タグ付きスナップショット保存ディレクトリを取得"""
        return self.get_story_snapshots_dir(module) / "tags"
    
    def get_tagged_snapshot_path(self, module: str, story_name: str) -> Path:
        """タグ付きスナップショットファイルのパスを取得"""
        sanitized_name = self._sanitize_story_name(story_name)
        tag = self._sanitize_tag(self.get_snapshot_tag())
        filename = f"story_snapshot_{tag}_{sanitized_name}.json"
        return self.get_story_snapshot_tag_dir(module) / filename
    
    def get_story_comparisons_dir(self, module: str) -> Path:
        """ストーリー比較結果保存ディレクトリを取得"""
        return self.get_module_snapshot_dir(module) / "story_comparisons"
    
    def get_story_validations_dir(self, module: str) -> Path:
        """ストーリーバリデーション結果保存ディレクトリを取得"""
        return self.get_module_snapshot_dir(module) / "story_validations"
    
    def get_reports_dir(self, module: str) -> Path:
        """レポート保存ディレクトリを取得"""
        return self.get_module_snapshot_dir(module) / "reports"

"""
E2Eテストフレームワークの設定管理モジュール

環境変数とCLI引数から設定を読み込み、テスト実行の動作を制御します。
"""

import os
import argparse
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any
from dotenv import load_dotenv


@dataclass
class Config:
    """テスト設定
    
    環境変数と CLI 引数から設定を読み込み、テスト実行の動作を制御します。
    
    Attributes:
        base_url: SaaSus API のベース URL
        api_key: 認証用 API キー
        secret_key: 署名生成用シークレットキー
        saas_id: SaaS ID
        dry_run: 実際の API 呼び出しを行わずにテストフローを検証するモード
        timeout: メソッド実行のタイムアウト時間（秒）
        fail_fast: 最初の失敗で即座にテストを中断するかどうか
        log_level: ログレベル（DEBUG, INFO, WARNING, ERROR）
        log_file: ログファイルのパス（オプション）
        snapshot_enabled: スナップショット機能を有効にするかどうか
        snapshot_dir: スナップショット保存先ディレクトリ
        snapshot_mode: スナップショットモード（capture, compare, report）
        mask_patterns: 機密情報マスキング用の正規表現パターンリスト
        compatibility_check: メソッドシグネチャの互換性チェックを有効にするかどうか
    """
    
    # 基本設定
    base_url: str
    api_key: str
    secret_key: str
    saas_id: str
    
    # 実行制御
    dry_run: bool = False
    timeout: int = 30
    fail_fast: bool = False
    
    # ログ設定
    log_level: str = "INFO"
    log_file: Optional[str] = None
    
    # スナップショット設定
    snapshot_enabled: bool = False
    snapshot_dir: str = "tests/snapshots"
    snapshot_mode: str = "compare"  # 'capture', 'compare', 'report'
    
    # マスキング設定
    mask_patterns: List[str] = field(default_factory=lambda: [
        r"api_key",
        r"secret",
        r"password",
        r"token",
        r"authorization"
    ])
    
    # 互換性チェック
    compatibility_check: bool = True
    
    @classmethod
    def from_env(cls, cli_args: Optional[Dict[str, Any]] = None) -> 'Config':
        """環境変数と CLI 引数から設定を読み込む
        
        .env ファイルと環境変数から設定を読み込み、CLI 引数で上書きします。
        
        Args:
            cli_args: CLI 引数の辞書（オプション）。指定された場合、環境変数の値を上書きします。
        
        Returns:
            Config: 設定オブジェクト
        
        Raises:
            ValueError: 必須の環境変数が設定されていない場合
        
        Examples:
            >>> # 環境変数のみから読み込み
            >>> config = Config.from_env()
            
            >>> # CLI 引数で上書き
            >>> config = Config.from_env(cli_args={'dry_run': True, 'log_level': 'DEBUG'})
        """
        # .env ファイルを読み込む
        load_dotenv()
        
        # 必須の環境変数を取得
        base_url = os.getenv("SAASUS_BASE_URL")
        api_key = os.getenv("SAASUS_API_KEY")
        secret_key = os.getenv("SAASUS_SECRET_KEY")
        saas_id = os.getenv("SAASUS_SAAS_ID")
        
        # 必須項目のバリデーション
        missing_vars = []
        if not base_url:
            missing_vars.append("SAASUS_BASE_URL")
        if not api_key:
            missing_vars.append("SAASUS_API_KEY")
        if not secret_key:
            missing_vars.append("SAASUS_SECRET_KEY")
        if not saas_id:
            missing_vars.append("SAASUS_SAAS_ID")
        
        if missing_vars:
            raise ValueError(
                f"必須の環境変数が設定されていません: {', '.join(missing_vars)}\n"
                f".env ファイルまたは環境変数に設定してください。"
            )
        
        # オプションの環境変数を取得（デフォルト値あり）
        dry_run = os.getenv("DRY_RUN", "false").lower() in ("true", "1", "yes")
        timeout = int(os.getenv("TIMEOUT", "30"))
        fail_fast = os.getenv("FAIL_FAST", "false").lower() in ("true", "1", "yes")
        log_level = os.getenv("LOG_LEVEL", "INFO").upper()
        log_file = os.getenv("LOG_FILE")
        snapshot_enabled = os.getenv("SNAPSHOT_ENABLED", "false").lower() in ("true", "1", "yes")
        snapshot_dir = os.getenv("SNAPSHOT_DIR", "tests/snapshots")
        snapshot_mode = os.getenv("SNAPSHOT_MODE", "compare").lower()
        compatibility_check = os.getenv("COMPATIBILITY_CHECK", "true").lower() in ("true", "1", "yes")
        
        # マスキングパターンを環境変数から読み込み（カンマ区切り）
        mask_patterns_env = os.getenv("MASK_PATTERNS")
        if mask_patterns_env:
            mask_patterns = [p.strip() for p in mask_patterns_env.split(",")]
        else:
            mask_patterns = [
                r"api_key",
                r"secret",
                r"password",
                r"token",
                r"authorization"
            ]
        
        # 設定オブジェクトを作成
        config = cls(
            base_url=base_url,
            api_key=api_key,
            secret_key=secret_key,
            saas_id=saas_id,
            dry_run=dry_run,
            timeout=timeout,
            fail_fast=fail_fast,
            log_level=log_level,
            log_file=log_file,
            snapshot_enabled=snapshot_enabled,
            snapshot_dir=snapshot_dir,
            snapshot_mode=snapshot_mode,
            mask_patterns=mask_patterns,
            compatibility_check=compatibility_check
        )
        
        # CLI 引数で上書き
        if cli_args:
            for key, value in cli_args.items():
                if hasattr(config, key) and value is not None:
                    setattr(config, key, value)
        
        return config
    
    @classmethod
    def from_cli(cls) -> 'Config':
        """CLI 引数を解析して設定を読み込む
        
        argparse を使用して CLI 引数を解析し、環境変数の値を上書きします。
        
        Returns:
            Config: 設定オブジェクト
        
        Examples:
            >>> # コマンドライン実行時
            >>> # python -m tests.e2e --dry-run --log-level DEBUG
            >>> config = Config.from_cli()
        """
        parser = argparse.ArgumentParser(
            description="SaaSus SDK E2E テストフレームワーク",
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog="""
環境変数:
  SAASUS_BASE_URL       SaaSus API のベース URL（必須）
  SAASUS_API_KEY        認証用 API キー（必須）
  SAASUS_SECRET_KEY     署名生成用シークレットキー（必須）
  SAASUS_SAAS_ID        SaaS ID（必須）
  DRY_RUN               Dry Run モードを有効にする（true/false）
  TIMEOUT               タイムアウト時間（秒）
  FAIL_FAST             Fail Fast モードを有効にする（true/false）
  LOG_LEVEL             ログレベル（DEBUG/INFO/WARNING/ERROR）
  LOG_FILE              ログファイルのパス
  SNAPSHOT_ENABLED      スナップショット機能を有効にする（true/false）
  SNAPSHOT_DIR          スナップショット保存先ディレクトリ
  SNAPSHOT_MODE         スナップショットモード（capture/compare/report）
  MASK_PATTERNS         マスキングパターン（カンマ区切り）
  COMPATIBILITY_CHECK   互換性チェックを有効にする（true/false）

使用例:
  # 環境変数のみで実行
  python -m tests.e2e
  
  # Dry Run モードで実行
  python -m tests.e2e --dry-run
  
  # デバッグログを有効にして実行
  python -m tests.e2e --log-level DEBUG
  
  # スナップショットキャプチャモードで実行
  python -m tests.e2e --snapshot-mode capture
            """
        )
        
        # 実行制御オプション
        parser.add_argument(
            "--dry-run",
            action="store_true",
            help="実際の API 呼び出しを行わずにテストフローを検証"
        )
        parser.add_argument(
            "--timeout",
            type=int,
            help="メソッド実行のタイムアウト時間（秒）"
        )
        parser.add_argument(
            "--fail-fast",
            action="store_true",
            help="最初の失敗で即座にテストを中断"
        )
        
        # ログオプション
        parser.add_argument(
            "--log-level",
            choices=["DEBUG", "INFO", "WARNING", "ERROR"],
            help="ログレベル"
        )
        parser.add_argument(
            "--log-file",
            help="ログファイルのパス"
        )
        
        # スナップショットオプション
        parser.add_argument(
            "--snapshot-enabled",
            action="store_true",
            help="スナップショット機能を有効にする"
        )
        parser.add_argument(
            "--snapshot-dir",
            help="スナップショット保存先ディレクトリ"
        )
        parser.add_argument(
            "--snapshot-mode",
            choices=["capture", "compare", "report"],
            help="スナップショットモード"
        )
        
        # その他のオプション
        parser.add_argument(
            "--no-compatibility-check",
            action="store_true",
            help="互換性チェックを無効にする"
        )
        
        args = parser.parse_args()
        
        # CLI 引数を辞書に変換
        cli_args = {}
        if args.dry_run:
            cli_args["dry_run"] = True
        if args.timeout is not None:
            cli_args["timeout"] = args.timeout
        if args.fail_fast:
            cli_args["fail_fast"] = True
        if args.log_level:
            cli_args["log_level"] = args.log_level
        if args.log_file:
            cli_args["log_file"] = args.log_file
        if args.snapshot_enabled:
            cli_args["snapshot_enabled"] = True
        if args.snapshot_dir:
            cli_args["snapshot_dir"] = args.snapshot_dir
        if args.snapshot_mode:
            cli_args["snapshot_mode"] = args.snapshot_mode
        if args.no_compatibility_check:
            cli_args["compatibility_check"] = False
        
        # 環境変数から読み込み、CLI 引数で上書き
        return cls.from_env(cli_args=cli_args)
    
    def validate(self) -> None:
        """設定の妥当性を検証
        
        Raises:
            ValueError: 設定値が不正な場合
        """
        # ログレベルの検証
        valid_log_levels = ["DEBUG", "INFO", "WARNING", "ERROR"]
        if self.log_level not in valid_log_levels:
            raise ValueError(
                f"不正なログレベル: {self.log_level}。"
                f"有効な値: {', '.join(valid_log_levels)}"
            )
        
        # スナップショットモードの検証
        valid_snapshot_modes = ["capture", "compare", "report"]
        if self.snapshot_mode not in valid_snapshot_modes:
            raise ValueError(
                f"不正なスナップショットモード: {self.snapshot_mode}。"
                f"有効な値: {', '.join(valid_snapshot_modes)}"
            )
        
        # タイムアウトの検証
        if self.timeout <= 0:
            raise ValueError(f"タイムアウトは0より大きい数値である必要があります: {self.timeout}")

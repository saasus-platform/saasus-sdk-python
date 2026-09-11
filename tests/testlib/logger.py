"""
ログ出力モジュール

E2Eテストフレームワークの標準化されたログ出力を提供します。
"""

import logging
from typing import Any, Optional
from tests.testlib.config import Config
from tests.testlib.models import Story, StoryResult, StepResult


class TestLogger:
    """
    テスト用の標準化されたロガー

    Pythonのloggingモジュールを使用して、ストーリー開始/終了、
    ステップ結果、検証失敗などを構造化されたログとして出力します。

    Attributes:
        config: テスト設定
        logger: Pythonのloggerインスタンス
    """

    def __init__(self, config: Config):
        """
        TestLoggerを初期化

        Args:
            config: テスト設定オブジェクト
        """
        self.config = config
        self.logger = self._setup_logger()

    def _setup_logger(self) -> logging.Logger:
        """
        loggingモジュールを設定

        コンソールハンドラとファイルハンドラ（設定されている場合）を追加し、
        統一されたフォーマットでログを出力します。

        Returns:
            logging.Logger: 設定済みのloggerインスタンス
        """
        logger = logging.getLogger("saasus_e2e_test")
        logger.setLevel(getattr(logging, self.config.log_level))

        # 既存のハンドラをクリア（重複を防ぐ）
        logger.handlers.clear()

        # コンソールハンドラ
        console_handler = logging.StreamHandler()
        console_handler.setLevel(getattr(logging, self.config.log_level))
        console_formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        console_handler.setFormatter(console_formatter)
        logger.addHandler(console_handler)

        # ファイルハンドラ（設定されている場合）
        if self.config.log_file:
            file_handler = logging.FileHandler(
                self.config.log_file,
                encoding='utf-8'
            )
            file_handler.setLevel(getattr(logging, self.config.log_level))
            file_formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S'
            )
            file_handler.setFormatter(file_formatter)
            logger.addHandler(file_handler)

        return logger

    def story_start(self, story: Story) -> None:
        """
        ストーリー開始をログ

        Args:
            story: 開始するストーリー
        """
        self.logger.info(
            f"Starting story: {story.name} - {story.description}"
        )
        if story.tags:
            self.logger.debug(f"Tags: {', '.join(story.tags)}")
        if story.timeout:
            self.logger.debug(f"Timeout: {story.timeout}s")

    def story_end(self, story_result: StoryResult) -> None:
        """
        ストーリー終了をログ

        Args:
            story_result: ストーリーの実行結果
        """
        status = "SUCCESS" if story_result.success else "FAILED"
        self.logger.info(
            f"Story {story_result.story.name} {status} "
            f"({story_result.execution_time:.2f}s)"
        )

        # 統計情報をデバッグログに出力
        total_steps = len(story_result.step_results)
        successful_steps = sum(
            1 for sr in story_result.step_results if sr.success
        )
        self.logger.debug(
            f"Steps: {successful_steps}/{total_steps} passed"
        )

    def step_result(self, step_result: StepResult) -> None:
        """
        ステップ結果をログ

        Args:
            step_result: ステップの実行結果
        """
        status_symbol = "✓" if step_result.success else "✗"

        # 基本情報をデバッグレベルで出力
        self.logger.debug(
            f"{status_symbol} {step_result.step.method_name} "
            f"({step_result.execution_time:.2f}s)"
        )

        # ステップの説明がある場合は出力
        if step_result.step.description:
            self.logger.debug(f"  Description: {step_result.step.description}")

        # ステータスコードがある場合は出力
        if step_result.status_code is not None:
            self.logger.debug(f"  Status Code: {step_result.status_code}")

        # エラーがある場合は警告レベルで出力
        if step_result.error:
            self.logger.warning(
                f"  Error: {type(step_result.error).__name__}: {str(step_result.error)}"
            )

        # レスポンスのサマリを出力（DEBUGレベル）
        if step_result.response is not None:
            response_summary = self._create_response_summary(step_result.response)
            self.logger.debug(f"  Response: {response_summary}")

    def validation_failed(
        self,
        step: Any,
        expected: Optional[Any] = None,
        actual: Optional[Any] = None
    ) -> None:
        """
        検証失敗をログ

        Args:
            step: 失敗したステップ（Stepオブジェクトまたはメソッド名）
            expected: 期待値（オプション）
            actual: 実際の値（オプション）
        """
        # ステップ名を取得
        if hasattr(step, 'method_name'):
            step_name = step.method_name
        else:
            step_name = str(step)

        error_message = f"Validation failed for {step_name}"

        if expected is not None:
            error_message += f"\n  Expected: {self._format_value(expected)}"

        if actual is not None:
            error_message += f"\n  Actual: {self._format_value(actual)}"

        self.logger.error(error_message)

    def _create_response_summary(self, response: Any) -> str:
        """
        レスポンスのサマリを作成

        Args:
            response: レスポンスオブジェクト

        Returns:
            str: レスポンスのサマリ文字列
        """
        if response is None:
            return "None"

        # 辞書の場合
        if isinstance(response, dict):
            keys = list(response.keys())
            if len(keys) <= 3:
                return f"dict with keys: {keys}"
            else:
                return f"dict with {len(keys)} keys: {keys[:3]}..."

        # リストの場合
        if isinstance(response, list):
            return f"list with {len(response)} items"

        # オブジェクトの場合
        if hasattr(response, '__dict__'):
            attrs = list(vars(response).keys())
            if len(attrs) <= 3:
                return f"{type(response).__name__} with attrs: {attrs}"
            else:
                return f"{type(response).__name__} with {len(attrs)} attrs"

        # その他の場合は文字列表現（長すぎる場合は切り詰める）
        str_repr = str(response)
        if len(str_repr) > 100:
            return f"{str_repr[:100]}..."
        return str_repr

    def _format_value(self, value: Any) -> str:
        """
        値を読みやすい形式にフォーマット

        Args:
            value: フォーマットする値

        Returns:
            str: フォーマットされた文字列
        """
        if value is None:
            return "None"

        # 辞書の場合は整形して出力
        if isinstance(value, dict):
            import json
            try:
                return json.dumps(value, indent=2, ensure_ascii=False)
            except (TypeError, ValueError):
                return str(value)

        # リストの場合
        if isinstance(value, list):
            if len(value) <= 5:
                return str(value)
            else:
                return f"[{', '.join(str(v) for v in value[:5])}, ... ({len(value)} items)]"

        # その他の場合
        str_repr = str(value)
        if len(str_repr) > 200:
            return f"{str_repr[:200]}..."
        return str_repr

    def debug(self, message: str) -> None:
        """DEBUGレベルのログを出力"""
        self.logger.debug(message)

    def info(self, message: str) -> None:
        """INFOレベルのログを出力"""
        self.logger.info(message)

    def warning(self, message: str) -> None:
        """WARNINGレベルのログを出力"""
        self.logger.warning(message)

    def error(self, message: str, exc_info: Optional[Exception] = None) -> None:
        """
        ERRORレベルのログを出力

        Args:
            message: エラーメッセージ
            exc_info: 例外オブジェクト（オプション）
        """
        if exc_info:
            self.logger.error(message, exc_info=exc_info)
        else:
            self.logger.error(message)

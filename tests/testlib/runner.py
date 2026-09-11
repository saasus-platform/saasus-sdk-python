"""
ストーリー実行エンジン

テストストーリーを実行し、setup → steps → cleanupの順序で処理を行います。
"""

import time
from typing import Any, List

from tests.testlib.config import Config
from tests.testlib.logger import TestLogger
from tests.testlib.method_executor import MethodExecutor
from tests.testlib.models import Step, Story, StepResult, StoryResult


class StoryRunner:
    """
    ストーリー実行エンジン
    
    テストストーリーをsetup → steps → cleanupの順序で実行し、
    各ステップの結果を記録します。Fail FastモードとDry Runモードをサポートします。
    
    Attributes:
        client: SDKクライアントオブジェクト
        config: テスト設定
        logger: ロガーインスタンス
        executor: メソッド実行エンジン
    """
    
    def __init__(self, client: Any, config: Config, logger: TestLogger):
        """
        StoryRunnerを初期化
        
        Args:
            client: SDKクライアントオブジェクト
            config: テスト設定
            logger: ロガーインスタンス
        """
        self.client = client
        self.config = config
        self.logger = logger
        self.executor = MethodExecutor(client, config, logger)
    
    def run_story(self, story: Story) -> StoryResult:
        """
        ストーリーを実行
        
        setup → steps → cleanupの順序でストーリーを実行し、
        各ステップの結果をStoryResultに記録します。
        
        Args:
            story: 実行するストーリー
        
        Returns:
            StoryResult: ストーリーの実行結果
        """
        start_time = time.time()
        
        # ストーリー開始をログ
        self.logger.story_start(story)
        
        # ステップ変数をクリア（新しいストーリーの開始）
        self.executor.clear_variables()
        
        # 結果を格納するリスト
        setup_results: List[StepResult] = []
        step_results: List[StepResult] = []
        cleanup_results: List[StepResult] = []
        
        # ストーリー全体の成功フラグ
        story_success = True
        
        try:
            # Setup実行
            if story.setup:
                self.logger.info("Executing setup steps")
                setup_results = self._execute_steps(
                    story.setup,
                    phase="setup"
                )
                
                # Setupが失敗した場合、Fail Fastに関係なく中断
                if not all(result.success for result in setup_results):
                    story_success = False
                    self.logger.error("Setup failed. Skipping main steps.")
                    return self._create_story_result(
                        story=story,
                        success=False,
                        setup_results=setup_results,
                        step_results=[],
                        cleanup_results=[],
                        start_time=start_time
                    )
            
            # Main steps実行
            self.logger.info("Executing main steps")
            step_results = self._execute_steps(
                story.steps,
                phase="steps"
            )
            
            # ステップの成功/失敗を判定
            if not all(result.success for result in step_results):
                story_success = False
        
        finally:
            # Cleanup実行（必ず実行）
            if story.cleanup:
                self.logger.info("Executing cleanup steps")
                cleanup_results = self._execute_steps(
                    story.cleanup,
                    phase="cleanup",
                    skip_fail_fast=True  # Cleanupではfail_fastを無視
                )
                
                # Cleanupの失敗もストーリー全体の失敗とみなす
                if not all(result.success for result in cleanup_results):
                    story_success = False
        
        # ストーリー結果を作成
        story_result = self._create_story_result(
            story=story,
            success=story_success,
            setup_results=setup_results,
            step_results=step_results,
            cleanup_results=cleanup_results,
            start_time=start_time
        )
        
        # ストーリー終了をログ
        self.logger.story_end(story_result)
        
        return story_result
    
    def _execute_steps(
        self,
        steps: List[Step],
        phase: str,
        skip_fail_fast: bool = False
    ) -> List[StepResult]:
        """
        ステップのリストを実行
        
        各ステップを順番に実行し、結果をリストで返します。
        Fail Fastモードが有効な場合、失敗時に即座に中断します。
        
        Args:
            steps: 実行するステップのリスト
            phase: 実行フェーズ（"setup", "steps", "cleanup"）
            skip_fail_fast: Fail Fastを無視するかどうか（Cleanup用）
        
        Returns:
            List[StepResult]: ステップの実行結果のリスト
        """
        results: List[StepResult] = []
        
        for i, step in enumerate(steps, 1):
            self.logger.debug(
                f"[{phase}] Executing step {i}/{len(steps)}: "
                f"{step.method_name}"
            )
            
            # ステップを実行
            result = self.executor.execute(step)
            
            # allow_failureの場合、失敗しても成功として扱う
            if not result.success and step.allow_failure:
                result.success = True
                self.logger.debug(f"Step failed but allow_failure=True, continuing")
            
            results.append(result)
            
            # ステップ結果をログ
            self.logger.step_result(result)
            
            # Fail Fastチェック
            if not result.success and not skip_fail_fast:
                if self.config.fail_fast:
                    self.logger.warning(
                        f"Fail fast enabled. Stopping {phase} execution "
                        f"after step {i}/{len(steps)}"
                    )
                    break
                else:
                    self.logger.debug(
                        f"Step failed but continuing execution "
                        f"(fail_fast=False)"
                    )
        
        return results
    
    def _create_story_result(
        self,
        story: Story,
        success: bool,
        setup_results: List[StepResult],
        step_results: List[StepResult],
        cleanup_results: List[StepResult],
        start_time: float
    ) -> StoryResult:
        """
        StoryResultを作成
        
        Args:
            story: 実行したストーリー
            success: ストーリー全体の成功フラグ
            setup_results: Setupステップの結果
            step_results: メインステップの結果
            cleanup_results: Cleanupステップの結果
            start_time: 開始時刻
        
        Returns:
            StoryResult: ストーリーの実行結果
        """
        execution_time = time.time() - start_time
        
        return StoryResult(
            story=story,
            success=success,
            setup_results=setup_results,
            step_results=step_results,
            cleanup_results=cleanup_results,
            execution_time=execution_time
        )

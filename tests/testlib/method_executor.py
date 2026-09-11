"""
メソッド実行エンジン

SDKメソッドを動的に実行し、レスポンスを検証するエンジンを提供します。
"""

import time
from typing import Any, Callable, Dict, Optional, Tuple, Union
from concurrent.futures import ThreadPoolExecutor, TimeoutError as FuturesTimeoutError

from tests.testlib.config import Config
from tests.testlib.logger import TestLogger
from tests.testlib.models import Step, StepResult


class MethodExecutor:
    """
    SDKメソッドを動的に実行するエンジン
    
    リフレクションを使用してSDKクライアントのメソッドを動的に呼び出し、
    パラメータ解決、タイムアウト処理、レスポンス検証を行います。
    
    Attributes:
        client: SDKクライアントオブジェクト
        config: テスト設定
        logger: ロガーインスタンス
        step_variables: ステップ間で共有される変数の辞書
    """
    
    def __init__(self, client: Any, config: Config, logger: TestLogger):
        """
        MethodExecutorを初期化
        
        Args:
            client: SDKクライアントオブジェクト
            config: テスト設定
            logger: ロガーインスタンス
        """
        self.client = client
        self.config = config
        self.logger = logger
        self.step_variables: Dict[str, Any] = {}

    def execute(self, step: Step) -> StepResult:
        """
        ステップを実行
        
        メソッドの取得、パラメータ解決、実行、検証を行い、
        結果をStepResultとして返します。
        
        Args:
            step: 実行するステップ
        
        Returns:
            StepResult: ステップの実行結果
        """
        start_time = time.time()
        
        executed_method_name: Optional[str] = None
        try:
            # スキップチェック
            if step.skip:
                self.logger.debug(
                    f"Skipping step: {step.method_name} - {step.skip_reason or 'No reason'}"
                )
                return self._create_skipped_result(step, start_time)
            
            # Dry runチェック
            if self.config.dry_run and step.skip_on_dry_run:
                self.logger.debug(
                    f"Skipping step in dry run mode: {step.method_name}"
                )
                return self._create_dry_run_result(step, start_time)
            
            # メソッド取得
            method, executed_method_name = self._get_method(step.method_name)
            
            # パラメータ解決
            params = self._resolve_params(step.params)
            
            self.logger.debug(
                f"Executing method: {step.method_name} with params: {params}"
            )
            
            # メソッド実行
            response = self._invoke_method(method, params)
            
            # ApiResponseオブジェクトからデータを抽出
            actual_data = response
            if hasattr(response, 'data'):
                actual_data = response.data
            
            # ステータスコードを抽出
            status_code = self._extract_status_code(response)
            
            # 検証
            validation_success = self._validate_response(step, actual_data)
            
            # 変数保存（データ部分のみ）
            if step.store_as:
                self.step_variables[step.store_as] = actual_data
                self.logger.debug(
                    f"Stored response as variable: {step.store_as}"
                )
            
            execution_time = time.time() - start_time
            
            return StepResult(
                step=step,
                success=validation_success,
                executed_method_name=executed_method_name,
                response=actual_data,
                status_code=status_code,
                execution_time=execution_time,
                resolved_params=params  # 解決されたパラメータを保存
            )
            
        except Exception as e:
            execution_time = time.time() - start_time
            self.logger.error(
                f"Step failed: {step.method_name}",
                exc_info=e
            )
            
            # エラー時もパラメータを解決して保存
            try:
                params = self._resolve_params(step.params)
            except Exception:
                params = {}
            
            return StepResult(
                step=step,
                success=False,
                executed_method_name=executed_method_name,
                error=e,
                execution_time=execution_time,
                resolved_params=params
            )

    def _get_method(self, method_name: str) -> Tuple[Callable, str]:
        """
        リフレクションでメソッドを取得
        
        getattrとcallable検査を使用してクライアントオブジェクトから
        メソッドを取得します。_with_http_infoバージョンを優先的に使用して
        ステータスコードを取得できるようにします。
        
        Args:
            method_name: メソッド名
        
        Returns:
            Tuple[Callable, str]: 呼び出すメソッドと実際に呼ばれるメソッド名
        
        Raises:
            AttributeError: メソッドが存在しない場合
            TypeError: メソッドが呼び出し可能でない場合
        """
        # 既に_with_http_infoが指定されている場合はそのまま使用
        if method_name.endswith("_with_http_info"):
            if hasattr(self.client, method_name):
                method = getattr(self.client, method_name)
                if callable(method):
                    return method, method_name
        else:
            # _with_http_infoバージョンを優先的に使用
            http_info_method_name = f"{method_name}_with_http_info"
            if hasattr(self.client, http_info_method_name):
                method = getattr(self.client, http_info_method_name)
                if callable(method):
                    return method, http_info_method_name
        
        if not hasattr(self.client, method_name):
            raise AttributeError(
                f"Method '{method_name}' not found on client "
                f"of type {type(self.client).__name__}"
            )
        
        method = getattr(self.client, method_name)
        
        if not callable(method):
            raise TypeError(
                f"'{method_name}' is not callable. "
                f"Type: {type(method).__name__}"
            )
        
        return method, method_name

    def _resolve_params(
        self,
        params: Union[Dict[str, Any], Callable[[Dict[str, Any]], Dict[str, Any]]]
    ) -> Dict[str, Any]:
        """
        パラメータを解決（callableの場合は実行）
        
        パラメータがcallableの場合、ステップ変数を引数として渡して実行し、
        結果を返します。辞書の場合はそのまま返します。
        
        Args:
            params: パラメータ（辞書またはcallable）
        
        Returns:
            Dict[str, Any]: 解決されたパラメータ辞書
        
        Raises:
            TypeError: callableが辞書を返さない場合
            Exception: callable実行中のエラー
        """
        if callable(params):
            try:
                self.logger.debug(
                    f"Resolving callable params with variables: "
                    f"{list(self.step_variables.keys())}"
                )
                resolved = params(self.step_variables)
                
                if not isinstance(resolved, dict):
                    raise TypeError(
                        f"Callable params must return a dict, "
                        f"got {type(resolved).__name__}"
                    )
                
                return resolved
                
            except Exception as e:
                self.logger.error(
                    f"Error resolving callable params: {e}",
                    exc_info=e
                )
                raise
        
        return params

    def _invoke_method(
        self,
        method: Callable,
        params: Dict[str, Any]
    ) -> Any:
        """
        メソッドを実行（タイムアウト付き）
        
        concurrent.futuresを使用してタイムアウト処理を実装し、
        指定時間内にメソッドを実行します。
        
        Args:
            method: 実行するメソッド
            params: メソッドのパラメータ
        
        Returns:
            Any: メソッドの実行結果
        
        Raises:
            TimeoutError: タイムアウトが発生した場合
            Exception: メソッド実行中のエラー
        """
        if self.config.timeout and self.config.timeout > 0:
            # タイムアウト付きで実行
            with ThreadPoolExecutor(max_workers=1) as executor:
                future = executor.submit(method, **params)
                try:
                    result = future.result(timeout=self.config.timeout)
                    return result
                except FuturesTimeoutError:
                    self.logger.error(
                        f"Method execution timed out after {self.config.timeout}s"
                    )
                    raise TimeoutError(
                        f"Method execution exceeded timeout of {self.config.timeout}s"
                    )
                except Exception as e:
                    self.logger.error(
                        f"Error during method execution: {e}",
                        exc_info=e
                    )
                    raise
        else:
            # タイムアウトなしで実行
            try:
                return method(**params)
            except Exception as e:
                self.logger.error(
                    f"Error during method execution: {e}",
                    exc_info=e
                )
                raise

    def _validate_response(self, step: Step, response: Any) -> bool:
        """
        レスポンスを検証
        
        ステップに検証関数が指定されている場合、それを実行して
        レスポンスを検証します。
        
        Args:
            step: 実行したステップ
            response: メソッドのレスポンス
        
        Returns:
            bool: 検証が成功した場合True、失敗した場合False
        """
        if step.validation_func:
            try:
                self.logger.debug(
                    f"Validating response for {step.method_name}"
                )
                is_valid = step.validation_func(response)
                
                if not is_valid:
                    self.logger.validation_failed(
                        step=step,
                        actual=response
                    )
                    return False
                
                self.logger.debug("Validation passed")
                return True
                
            except Exception as e:
                self.logger.error(
                    f"Error during validation: {e}",
                    exc_info=e
                )
                self.logger.validation_failed(
                    step=step,
                    actual=response
                )
                return False
        
        # 検証関数が指定されていない場合は成功とみなす
        return True
    
    def _extract_status_code(self, response: Any) -> Optional[int]:
        """
        レスポンスからHTTPステータスコードを抽出
        
        Args:
            response: メソッドのレスポンス
        
        Returns:
            Optional[int]: ステータスコード、取得できない場合はNone
        """
        # 辞書の場合、status_codeキーを探す
        if isinstance(response, dict):
            if "status_code" in response:
                return response["status_code"]
            if "statusCode" in response:
                return response["statusCode"]
        
        # オブジェクトの場合、status_code属性を探す
        if hasattr(response, "status_code"):
            return response.status_code
        if hasattr(response, "statusCode"):
            return response.statusCode
        if hasattr(response, "status"):
            status = response.status
            if isinstance(status, int):
                return status
        
        # HTTPレスポンスオブジェクトの場合
        if hasattr(response, "http_response"):
            http_resp = response.http_response
            if hasattr(http_resp, "status_code"):
                return http_resp.status_code
        
        # 取得できない場合はNone
        return None

    def _create_dry_run_result(self, step: Step, start_time: float) -> StepResult:
        """
        Dry Runモード用のモック結果を作成
        
        Args:
            step: 実行するステップ
            start_time: 開始時刻
        
        Returns:
            StepResult: モックの実行結果
        """
        execution_time = time.time() - start_time
        
        # パラメータを解決
        try:
            params = self._resolve_params(step.params)
        except Exception:
            params = {}
        
        # モックレスポンスを作成
        mock_response = {
            "dry_run": True,
            "method": step.method_name,
            "message": "This is a dry run response"
        }
        
        return StepResult(
            step=step,
            success=True,
            executed_method_name=step.method_name,
            response=mock_response,
            status_code=200,  # Dry Runモードでは200を返す
            execution_time=execution_time,
            resolved_params=params
        )

    def _create_skipped_result(self, step: Step, start_time: float) -> StepResult:
        """
        スキップされたステップの結果を作成
        
        Args:
            step: スキップされたステップ
            start_time: 開始時刻
        
        Returns:
            StepResult: スキップ結果
        """
        return StepResult(
            step=step,
            success=True,
            executed_method_name=step.method_name,
            response={"status": "SKIPPED", "reason": step.skip_reason},
            status_code=None,
            execution_time=time.time() - start_time,
            resolved_params={}
        )
    
    def clear_variables(self) -> None:
        """
        ステップ変数をクリア
        
        新しいストーリーの実行前に呼び出して、
        前のストーリーの変数をクリアします。
        """
        self.step_variables.clear()
        self.logger.debug("Cleared step variables")
    
    def get_variable(self, name: str) -> Optional[Any]:
        """
        ステップ変数を取得
        
        Args:
            name: 変数名
        
        Returns:
            Optional[Any]: 変数の値（存在しない場合はNone）
        """
        return self.step_variables.get(name)
    
    def set_variable(self, name: str, value: Any) -> None:
        """
        ステップ変数を設定
        
        Args:
            name: 変数名
            value: 変数の値
        """
        self.step_variables[name] = value
        self.logger.debug(f"Set variable: {name}")

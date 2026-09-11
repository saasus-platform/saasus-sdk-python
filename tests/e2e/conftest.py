"""
pytest設定とfixture

E2Eテストフレームワークのpytest統合を提供します。
設定読み込み、クライアント初期化、ストーリー検出などのfixtureを定義します。
"""

# .envファイルから環境変数を読み込む（テスト収集前に実行）
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    # python-dotenv がインストールされていない場合はスキップ
    pass

import sys
from pathlib import Path
from typing import Any, List

import pytest

# testlibをインポートパスに追加
sys.path.insert(0, str(Path(__file__).parent.parent))

from testlib.config import Config
from testlib.logger import TestLogger
from testlib.runner import StoryRunner
from testlib.coverage import CoverageTracker
from testlib.reporter import Reporter
from testlib.models import Story, StoryResult, StepResult


@pytest.fixture(scope="session")
def test_config() -> Config:
    """
    テスト設定をロード
    
    環境変数と.envファイルから設定を読み込みます。
    pytest実行時のコマンドライン引数も考慮します。
    
    Returns:
        Config: テスト設定オブジェクト
    """
    cli_args = {}
    config = Config.from_env(cli_args)
    return config


@pytest.fixture(scope="session")
def test_logger(test_config: Config) -> TestLogger:
    """
    テストロガーを初期化
    
    Args:
        test_config: テスト設定
    
    Returns:
        TestLogger: ロガーインスタンス
    """
    return TestLogger(test_config)


@pytest.fixture(scope="session")
def sdk_client(test_config: Config, test_logger: TestLogger) -> Any:
    """
    SDKクライアントを初期化
    
    モジュールに応じて適切なクライアントを初期化します。
    
    Args:
        test_config: テスト設定
        test_logger: ロガーインスタンス
    
    Returns:
        Any: SDKクライアントオブジェクト
    """
    test_logger.info("Initializing SDK client")
    
    # Dry runモードの場合はモッククライアントを返す
    if test_config.dry_run:
        test_logger.info("Dry run mode: using mock client")
        return MockSDKClient()
    
    # 実際のSDKクライアントを初期化
    test_logger.info("Initializing real SDK client for Auth module")
    try:
        from saasus_sdk_python.client.auth_client import SignedAuthApiClient
        from saasus_sdk_python.client.billing_client import SignedBillingApiClient
        from saasus_sdk_python.client.pricing_client import SignedPricingApiClient
        from saasus_sdk_python.src.auth.api.auth_info_api import AuthInfoApi
        from saasus_sdk_python.src.auth.api.basic_info_api import BasicInfoApi
        from saasus_sdk_python.src.auth.api.credential_api import CredentialApi
        from saasus_sdk_python.src.auth.api.env_api import EnvApi
        from saasus_sdk_python.src.auth.api.role_api import RoleApi
        from saasus_sdk_python.src.auth.api.saas_user_api import SaasUserApi
        from saasus_sdk_python.src.auth.api.tenant_api import TenantApi
        from saasus_sdk_python.src.auth.api.tenant_attribute_api import TenantAttributeApi
        from saasus_sdk_python.src.auth.api.tenant_user_api import TenantUserApi
        from saasus_sdk_python.src.auth.api.user_attribute_api import UserAttributeApi
        from saasus_sdk_python.src.auth.api.user_info_api import UserInfoApi
        from saasus_sdk_python.src.auth.api.invitation_api import InvitationApi
        from saasus_sdk_python.src.auth.api.single_tenant_api import SingleTenantApi
        from saasus_sdk_python.src.billing.api.stripe_api import StripeApi
        from saasus_sdk_python.src.pricing.api.pricing_plans_api import PricingPlansApi
        from saasus_sdk_python.src.pricing.api.pricing_menus_api import PricingMenusApi
        from saasus_sdk_python.src.pricing.api.pricing_units_api import PricingUnitsApi
        from saasus_sdk_python.src.pricing.api.metering_api import MeteringApi
        from saasus_sdk_python.src.pricing.api.tax_rate_api import TaxRateApi
        from saasus_sdk_python.client.communication_client import SignedCommunicationApiClient
        from saasus_sdk_python.client.integration_client import SignedIntegrationApiClient
        from saasus_sdk_python.client.apilog_client import SignedApilogApiClient
        from saasus_sdk_python.src.communication.api.feedback_api import FeedbackApi
        from saasus_sdk_python.src.integration.api.event_bridge_api import EventBridgeApi
        from saasus_sdk_python.src.apilog.api.api_log_api import ApiLogApi
        
        # 署名付きAPIクライアントを作成
        auth_api_client = SignedAuthApiClient()
        billing_api_client = SignedBillingApiClient()
        pricing_api_client = SignedPricingApiClient()
        communication_api_client = SignedCommunicationApiClient()
        integration_api_client = SignedIntegrationApiClient()
        apilog_api_client = SignedApilogApiClient()
        # ApiLogのget_logsはcreated_atをdatetime_formatでstrftimeして送信する。
        # 既定の "%Y-%m-%dT%H:%M:%S.%f%z" は "+0000"（コロン無し）となりサーバの
        # RFC3339パーサに拒否されるため、UTC前提のRFC3339形式に上書きする。
        apilog_api_client.configuration.datetime_format = "%Y-%m-%dT%H:%M:%SZ"
        
        # 各APIインスタンスを作成
        class RealSDKClient:
            def __init__(self, auth_api_client, billing_api_client, pricing_api_client,
                         communication_api_client, integration_api_client, apilog_api_client):
                self.api_client = auth_api_client
                self._apis = [
                    AuthInfoApi(auth_api_client),
                    BasicInfoApi(auth_api_client),
                    CredentialApi(auth_api_client),
                    EnvApi(auth_api_client),
                    RoleApi(auth_api_client),
                    SaasUserApi(auth_api_client),
                    TenantApi(auth_api_client),
                    TenantAttributeApi(auth_api_client),
                    TenantUserApi(auth_api_client),
                    UserAttributeApi(auth_api_client),
                    UserInfoApi(auth_api_client),
                    InvitationApi(auth_api_client),
                    SingleTenantApi(auth_api_client),
                    StripeApi(billing_api_client),
                    PricingPlansApi(pricing_api_client),
                    PricingMenusApi(pricing_api_client),
                    PricingUnitsApi(pricing_api_client),
                    MeteringApi(pricing_api_client),
                    TaxRateApi(pricing_api_client),
                    FeedbackApi(communication_api_client),
                    EventBridgeApi(integration_api_client),
                    ApiLogApi(apilog_api_client),
                ]
            
            def __getattr__(self, name):
                for api in self._apis:
                    if hasattr(api, name):
                        return getattr(api, name)
                raise AttributeError(f"Method '{name}' not found in SDK client")
        
        client = RealSDKClient(
            auth_api_client, billing_api_client, pricing_api_client,
            communication_api_client, integration_api_client, apilog_api_client
        )
        test_logger.info(f"SDK client initialized: {auth_api_client.base_url}/auth")
        return client
        
    except Exception as e:
        test_logger.error(f"Failed to initialize SDK client: {e}")
        raise


@pytest.fixture(scope="session")
def coverage_tracker(test_config: Config) -> CoverageTracker:
    """
    カバレッジトラッカーを初期化
    
    Args:
        test_config: テスト設定
    
    Returns:
        CoverageTracker: カバレッジトラッカーインスタンス
    """
    sdk_modules = [
        "auth",
        "billing",
        "pricing",
        "awsmarketplace",
        "integration",
        "apilog",
        "communication"
    ]
    
    return CoverageTracker(sdk_modules)


@pytest.fixture(scope="session")
def snapshot_engine(test_config: Config, test_logger: TestLogger):
    """
    スナップショットエンジンを初期化
    
    Args:
        test_config: テスト設定
        test_logger: ロガーインスタンス
    
    Returns:
        SnapshotEngine: スナップショットエンジンインスタンス（有効時のみ）
    """
    from testlib.snapshot import SnapshotEngine, SnapshotConfig
    
    snapshot_config = SnapshotConfig.from_env()
    if snapshot_config.capture_enabled or snapshot_config.compare_enabled:
        return SnapshotEngine(snapshot_config, test_logger)
    return None


@pytest.fixture(scope="session")
def story_runner(
    sdk_client: Any,
    test_config: Config,
    test_logger: TestLogger
) -> StoryRunner:
    """
    ストーリーランナーを初期化
    
    Args:
        sdk_client: SDKクライアント
        test_config: テスト設定
        test_logger: ロガーインスタンス
    
    Returns:
        StoryRunner: ストーリーランナーインスタンス
    """
    return StoryRunner(sdk_client, test_config, test_logger)


@pytest.fixture(scope="session")
def story_results() -> List[StoryResult]:
    """
    ストーリー実行結果を収集するリスト
    
    セッション全体でストーリーの実行結果を収集します。
    
    Returns:
        List[StoryResult]: ストーリー結果のリスト
    """
    return []


@pytest.fixture(scope="session", autouse=True)
def generate_report(
    request: pytest.FixtureRequest,
    test_config: Config,
    test_logger: TestLogger,
    coverage_tracker: CoverageTracker,
    story_results: List[StoryResult]
):
    """
    テスト終了時にレポートを生成
    
    すべてのテストが完了した後、レポートを生成します。
    
    Args:
        request: pytestリクエストオブジェクト
        test_config: テスト設定
        test_logger: ロガーインスタンス
        coverage_tracker: カバレッジトラッカー
        story_results: ストーリー結果のリスト
    """
    # テスト実行前の処理
    test_logger.info("=" * 80)
    test_logger.info("Starting E2E Test Suite")
    test_logger.info("=" * 80)
    
    # yieldでテスト実行を待つ
    yield
    
    # テスト実行後の処理（レポート生成）
    test_logger.info("=" * 80)
    test_logger.info("Generating Test Report")
    test_logger.info("=" * 80)
    
    # カバレッジレポートを取得
    coverage_report = coverage_tracker.get_coverage_report()
    
    # レポーターを初期化
    reporter = Reporter(test_config)
    
    # レポートを生成
    report_paths = reporter.generate(
        story_results=story_results,
        coverage_report=coverage_report,
        snapshot_diffs=None  # スナップショット機能は後で実装
    )
    
    test_logger.info(f"JSON report: {report_paths['json']}")
    test_logger.info(f"Text report: {report_paths['text']}")
    test_logger.info("=" * 80)


class MockSDKClient:
    """
    モックSDKクライアント
    
    Dry runモードや実際のクライアントが利用できない場合に使用します。
    """
    
    def __getattr__(self, name: str):
        """
        任意のメソッド呼び出しをモック
        
        Args:
            name: メソッド名
        
        Returns:
            Callable: モックメソッド
        """
        def mock_method(**kwargs):
            return {
                "id": "mock-id-12345",
                "status": "success",
                "message": f"Mock response for {name}",
                "data": kwargs
            }
        
        return mock_method


# pytestマーカーの定義
def pytest_configure(config):
    """
    pytestマーカーを登録
    
    モジュール別、ストーリー別のマーカーを定義します。
    
    Args:
        config: pytest設定オブジェクト
    """
    # モジュール別マーカー
    config.addinivalue_line("markers", "auth: Auth module tests")
    config.addinivalue_line("markers", "billing: Billing module tests")
    config.addinivalue_line("markers", "pricing: Pricing module tests")
    config.addinivalue_line("markers", "awsmarketplace: AWS Marketplace module tests")
    config.addinivalue_line("markers", "integration: Integration module tests")
    config.addinivalue_line("markers", "apilog: API Log module tests")
    config.addinivalue_line("markers", "communication: Communication module tests")
    
    # ストーリータイプ別マーカー
    config.addinivalue_line("markers", "crud: CRUD operation tests")
    config.addinivalue_line("markers", "lifecycle: Lifecycle tests")
    config.addinivalue_line("markers", "integration_test: Integration tests")
    config.addinivalue_line("markers", "smoke: Smoke tests")
    config.addinivalue_line("markers", "user: User-related tests")


def pytest_generate_tests(metafunc):
    """
    ストーリーベースのテストを動的に生成する補助関数
    
    test_story関数に対して、各ストーリーをパラメータとして渡します。
    stories.pyファイルは標準のpytest収集で読み込まれる前提で、
    各ストーリーをテストとしてパラメータ化します。
    
    Args:
        metafunc: pytestのメタ関数オブジェクト
    """
    if "story" in metafunc.fixturenames and "module_name" in metafunc.fixturenames:
        # ストーリーファイルのパスを取得
        test_file = Path(metafunc.module.__file__)
        
        # stories.pyファイルの場合のみ処理
        if test_file.name == "stories.py":
            # モジュール名を取得
            module_name = test_file.parent.name
            
            # get_<module>_stories()関数を呼び出し
            stories_func_name = f"get_{module_name}_stories"
            
            if hasattr(metafunc.module, stories_func_name):
                stories_func = getattr(metafunc.module, stories_func_name)
                stories = stories_func()
                
                # 各ストーリーをテストパラメータとして登録
                metafunc.parametrize(
                    "story,module_name",
                    [(story, module_name) for story in stories],
                    ids=[story.name for story in stories]
                )


def pytest_collection_modifyitems(config, items):
    """
    収集されたテストアイテムにマーカーを追加
    
    各ストーリーのモジュール名とタグに基づいてマーカーを追加します。
    
    Args:
        config: pytest設定オブジェクト
        items: 収集されたテストアイテムのリスト
    """
    for item in items:
        # test_story関数の場合のみ処理
        if item.name.startswith("test_story["):
            # パラメータからstoryとmodule_nameを取得
            if hasattr(item, 'callspec'):
                story = item.callspec.params.get('story')
                module_name = item.callspec.params.get('module_name')
                
                if story and module_name:
                    # モジュール別マーカーを追加
                    item.add_marker(getattr(pytest.mark, module_name))
                    
                    # タグベースのマーカーを追加
                    for tag in story.tags:
                        item.add_marker(getattr(pytest.mark, tag))


def test_story(
    story: Story,
    module_name: str,
    story_runner: StoryRunner,
    coverage_tracker: CoverageTracker,
    story_results: List[StoryResult],
    test_config: Config,
    snapshot_engine: Any,
    request: pytest.FixtureRequest
):
    """
    ストーリーを実行するテスト関数
    
    pytest_generate_testsによって動的に生成されたパラメータを使用して、
    各ストーリーを実行します。
    
    Args:
        story: 実行するストーリー
        module_name: モジュール名
        story_runner: ストーリーランナー
        coverage_tracker: カバレッジトラッカー
        story_results: ストーリー結果のリスト
        test_config: テスト設定
        snapshot_engine: スナップショットエンジン
        request: pytestリクエスト
    """
    # 詳細モードの確認
    verbose = request.config.option.verbose > 0
    
    # 詳細モードの場合、ストーリー情報を出力
    if verbose:
        print(f"\n{'=' * 80}")
        print(f"Story: {story.name}")
        print(f"Module: {module_name}")
        print(f"Description: {story.description}")
        if story.tags:
            print(f"Tags: {', '.join(story.tags)}")
        print(f"{'=' * 80}")
    
    # ストーリーを実行
    result = story_runner.run_story(story)
    
    # 詳細モードの場合、ステップ情報を出力
    if verbose:
        _print_step_results(result, request.config.option.verbose)
    
    # 結果を記録
    story_results.append(result)
    
    # カバレッジを記録
    for step_result in result.step_results:
        coverage_tracker.record(
            module=module_name,
            method_name=step_result.step.method_name,
            success=step_result.success
        )
    
    # スナップショット処理
    if snapshot_engine:
        # スナップショットをキャプチャ（失敗してもキャプチャ）
        if hasattr(snapshot_engine.config, 'capture_enabled') and snapshot_engine.config.capture_enabled:
            snapshot_path = snapshot_engine.capture(result, story_runner.client)
            if snapshot_path and verbose:
                print(f"\n📸 Snapshot captured: {snapshot_path}")
        
        # スナップショットを比較（成功時のみ）
        if result.success and hasattr(snapshot_engine.config, 'compare_enabled') and snapshot_engine.config.compare_enabled:
            diff = snapshot_engine.compare(result, story_runner.client)
            if diff and verbose:
                print(f"\n🔍 Snapshot differences detected for story: {story.name}")
    
    # 失敗した場合はアサーションエラーを発生
    if not result.success:
        failed_steps = [sr for sr in result.step_results if not sr.success]
        error_messages = []
        
        for step_result in failed_steps:
            msg = f"Step '{step_result.step.method_name}' failed"
            if step_result.error:
                msg += f": {step_result.error}"
            error_messages.append(msg)
        
        pytest.fail(
            f"Story '{story.name}' failed:\n" + "\n".join(error_messages)
        )


def _print_step_results(result: StoryResult, verbose_level: int):
    """
    ステップ結果を出力（詳細モード用）
    
    Args:
        result: ストーリー実行結果
        verbose_level: 詳細レベル
    """
    print(f"\n{'-' * 80}")
    print("Step Results:")
    print(f"{'-' * 80}")
    
    # Setup steps
    if result.setup_results:
        print("\nSetup Steps:")
        for i, step_result in enumerate(result.setup_results, 1):
            _print_step_result(i, step_result, verbose_level)
    
    # Main steps
    if result.step_results:
        print("\nMain Steps:")
        for i, step_result in enumerate(result.step_results, 1):
            _print_step_result(i, step_result, verbose_level)
    
    # Cleanup steps
    if result.cleanup_results:
        print("\nCleanup Steps:")
        for i, step_result in enumerate(result.cleanup_results, 1):
            _print_step_result(i, step_result, verbose_level)
    
    # サマリ
    print(f"\n{'-' * 80}")
    print(f"Total Execution Time: {result.execution_time:.2f}s")
    print(f"Status: {'✓ PASSED' if result.success else '✗ FAILED'}")
    print(f"{'-' * 80}\n")


def _print_step_result(index: int, step_result: StepResult, verbose_level: int):
    """
    個別のステップ結果を出力
    
    Args:
        index: ステップ番号
        step_result: ステップ実行結果
        verbose_level: 詳細レベル
    """
    status_icon = "✓" if step_result.success else "✗"
    status_text = "PASS" if step_result.success else "FAIL"
    
    print(
        f"  {index}. [{status_icon}] {step_result.step.method_name} "
        f"({step_result.execution_time:.2f}s) - {status_text}"
    )
    
    if step_result.step.description:
        print(f"      Description: {step_result.step.description}")
    
    if not step_result.success and step_result.error:
        print(f"      Error: {step_result.error}")
    
    # 超詳細モード（-vv）の場合、レスポンスも表示
    if verbose_level > 1 and step_result.response:
        print(f"      Response: {step_result.response}")

# TestLib - E2Eテストフレームワーク共通ライブラリ

TestLibは、SaaSus SDK PythonのE2Eテストフレームワークで使用される共通ライブラリです。

## コンポーネント

### models.py - データモデル

テストストーリーとステップを定義するためのデータモデルを提供します。

```python
from tests.testlib.models import Story, Step

# ステップの定義
step = Step(
    method_name="create_saas_user",
    params={"email": "test@example.com", "password": "Pass123!"},
    description="新規ユーザーを作成",
    store_as="created_user"
)

# ストーリーの定義
story = Story(
    name="user_lifecycle",
    description="ユーザーのライフサイクルテスト",
    module="auth",
    steps=[step]
)
```

### config.py - 設定管理

環境変数とCLI引数から設定を読み込みます。

```python
from tests.testlib.config import Config

# 環境変数から設定を読み込み
config = Config.from_env()

# CLI引数で上書き
config = Config.from_env(cli_args={
    "dry_run": True,
    "log_level": "DEBUG"
})

# CLI引数を解析
config = Config.from_cli()
```

### logger.py - ログ出力

構造化されたログ出力を提供します。

```python
from tests.testlib.logger import TestLogger
from tests.testlib.config import Config

config = Config.from_env()
logger = TestLogger(config)

# ストーリー開始
logger.story_start(story)

# ステップ結果
logger.step_result(step_result)

# ストーリー終了
logger.story_end(story_result)
```

### method_executor.py - メソッド実行エンジン

SDKメソッドを動的に実行します。

```python
from tests.testlib.method_executor import MethodExecutor
from SDK.auth_client import AuthClient

client = AuthClient(
    base_url=config.base_url,
    api_key=config.api_key,
    secret_key=config.secret_key,
    saas_id=config.saas_id
)

executor = MethodExecutor(client, config, logger)

# ステップを実行
step_result = executor.execute(step)

# ステップ変数を取得
user = executor.get_variable("created_user")

# ステップ変数を設定
executor.set_variable("test_data", {"key": "value"})

# ステップ変数をクリア
executor.clear_variables()
```

### coverage.py - カバレッジトラッキング

実行されたSDKメソッドを追跡します。

```python
from tests.testlib.coverage import CoverageTracker

# トラッカーを初期化
tracker = CoverageTracker(sdk_modules=["auth", "billing", "pricing"])

# メソッド実行を記録
tracker.record(module="auth", method_name="create_saas_user", success=True)
tracker.record(module="auth", method_name="get_saas_user", success=True)
tracker.record(module="auth", method_name="delete_saas_user", success=False)

# カバレッジレポートを取得
report = tracker.get_coverage_report()

print(f"総メソッド数: {report['total_methods']}")
print(f"実行済みメソッド数: {report['executed_methods']}")
print(f"カバレッジ率: {report['coverage_percentage']:.2f}%")
print(f"未実行メソッド: {report['not_executed_list']}")
```

### reporter.py - レポート生成

テスト結果のレポートを生成します。

```python
from tests.testlib.reporter import Reporter

reporter = Reporter(config)

# レポートを生成
report_paths = reporter.generate(
    story_results=[story_result1, story_result2],
    coverage_report=coverage_report
)

# 生成されたレポートのパス
print(f"JSONレポート: {report_paths['json']}")
print(f"テキストレポート: {report_paths['text']}")
```

### runner.py - ストーリー実行エンジン

テストストーリーを実行します。

```python
from tests.testlib.runner import StoryRunner

runner = StoryRunner(client, config, logger)

# ストーリーを実行
story_result = runner.run_story(story)

# 結果を確認
if story_result.success:
    print("ストーリーが成功しました")
else:
    print("ストーリーが失敗しました")
    for step_result in story_result.step_results:
        if not step_result.success:
            print(f"  失敗したステップ: {step_result.step.method_name}")
            print(f"  エラー: {step_result.error}")
```

## 完全な使用例

```python
from tests.testlib.config import Config
from tests.testlib.logger import TestLogger
from tests.testlib.coverage import CoverageTracker
from tests.testlib.runner import StoryRunner
from tests.testlib.reporter import Reporter
from tests.testlib.models import Story, Step
from SDK.auth_client import AuthClient

# 1. 設定を読み込み
config = Config.from_env()

# 2. ロガーを初期化
logger = TestLogger(config)

# 3. カバレッジトラッカーを初期化
tracker = CoverageTracker(sdk_modules=["auth"])

# 4. SDKクライアントを初期化
client = AuthClient(
    base_url=config.base_url,
    api_key=config.api_key,
    secret_key=config.secret_key,
    saas_id=config.saas_id
)

# 5. ストーリーを定義
story = Story(
    name="user_creation",
    description="ユーザー作成テスト",
    module="auth",
    steps=[
        Step(
            method_name="create_saas_user",
            params={"email": "test@example.com", "password": "Pass123!"},
            description="新規ユーザーを作成",
            store_as="created_user"
        ),
        Step(
            method_name="get_saas_user",
            params=lambda vars: {"user_id": vars["created_user"]["id"]},
            description="作成したユーザーを取得"
        )
    ],
    cleanup=[
        Step(
            method_name="delete_saas_user",
            params=lambda vars: {"user_id": vars["created_user"]["id"]},
            description="ユーザーを削除"
        )
    ]
)

# 6. ストーリーを実行
runner = StoryRunner(client, config, logger)
story_result = runner.run_story(story)

# 7. カバレッジを記録
for step_result in story_result.step_results:
    tracker.record(
        module=story.module,
        method_name=step_result.step.method_name,
        success=step_result.success
    )

# 8. レポートを生成
reporter = Reporter(config)
coverage_report = tracker.get_coverage_report()
report_paths = reporter.generate(
    story_results=[story_result],
    coverage_report=coverage_report
)

print(f"レポートが生成されました: {report_paths['json']}")
```

## 環境変数

TestLibは以下の環境変数を使用します：

### 必須

- `SAASUS_BASE_URL`: SaaSus APIのベースURL
- `SAASUS_API_KEY`: 認証用APIキー
- `SAASUS_SECRET_KEY`: 署名生成用シークレットキー
- `SAASUS_SAAS_ID`: SaaS ID

### オプション

- `DRY_RUN`: Dry Runモードを有効にする（true/false、デフォルト: false）
- `TIMEOUT`: メソッド実行のタイムアウト時間（秒、デフォルト: 30）
- `FAIL_FAST`: Fail Fastモードを有効にする（true/false、デフォルト: false）
- `LOG_LEVEL`: ログレベル（DEBUG/INFO/WARNING/ERROR、デフォルト: INFO）
- `LOG_FILE`: ログファイルのパス（オプション）
- `SNAPSHOT_ENABLED`: スナップショット機能を有効にする（true/false、デフォルト: false）
- `SNAPSHOT_DIR`: スナップショット保存先ディレクトリ（デフォルト: tests/snapshots）
- `SNAPSHOT_MODE`: スナップショットモード（capture/compare/report、デフォルト: compare）
- `MASK_PATTERNS`: マスキングパターン（カンマ区切り）
- `COMPATIBILITY_CHECK`: 互換性チェックを有効にする（true/false、デフォルト: true）

## 開発状況

### 実装済み

- ✅ データモデル（Story, Step, StepResult, StoryResult）
- ✅ 設定管理（Config）
- ✅ ログ出力（TestLogger）
- ✅ メソッド実行エンジン（MethodExecutor）
- ✅ カバレッジトラッキング（CoverageTracker）
- ✅ レポート生成（Reporter）
- ✅ ストーリー実行エンジン（StoryRunner）

### 実装予定

- ⏳ スナップショット機能（snapshot/）
  - engine.py: スナップショットエンジン
  - masker.py: 機密情報マスキング
  - comparator.py: 差分比較
  - reporter.py: スナップショットレポート

## 参考資料

- [E2Eテストフレームワーク全体のドキュメント](../README.md)
- [要件定義書](../../.kiro/specs/e2e-snapshot-testing/requirements.md)
- [設計書](../../.kiro/specs/e2e-snapshot-testing/design.md)
- [実装計画](../../.kiro/specs/e2e-snapshot-testing/tasks.md)

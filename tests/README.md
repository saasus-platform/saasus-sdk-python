# SaaSus SDK Python - E2Eテストフレームワーク

SaaSus SDK Python向けのE2Eテストフレームワークとスナップショットテスト機能のドキュメントです。

## 概要

このE2Eテストフレームワークは、SDK全体の動作を実際のAPIエンドポイントに対して検証するテストシステムです。以下の機能を提供します：

- **ストーリーベースのテスト**: 一連の関連するAPIコールをストーリーとして定義
- **カバレッジトラッキング**: 実行されたSDKメソッドを追跡し、カバレッジレポートを生成
- **スナップショットテスト**: APIレスポンスを記録し、後続の実行で比較して互換性を検証
- **機密情報のマスキング**: スナップショットに機密情報が含まれないように自動マスキング
- **詳細なレポート**: JSON/テキスト形式での実行結果レポート

## ディレクトリ構造

```
tests/
├── testlib/                    # 共通テストライブラリ
│   ├── __init__.py
│   ├── config.py              # 設定管理
│   ├── logger.py              # ログ出力
│   ├── coverage.py            # カバレッジトラッキング
│   ├── method_executor.py     # メソッド実行エンジン
│   ├── reporter.py            # レポート生成
│   ├── runner.py              # ストーリー実行エンジン
│   ├── models.py              # データモデル（Story, Step, Result）
│   └── snapshot/              # スナップショット機能
│       ├── __init__.py
│       ├── engine.py          # スナップショットエンジン
│       ├── config.py          # スナップショット設定
│       ├── masker.py          # 機密情報マスキング
│       ├── comparator.py      # 差分比較
│       └── reporter.py        # スナップショットレポート
├── e2e/                       # E2Eテスト定義
│   ├── conftest.py           # pytest設定とfixture
│   ├── auth/                 # authモジュールのテスト
│   │   ├── stories.py        # ストーリー定義
│   │   ├── validators.py     # 検証関数
│   │   └── helpers.py        # ヘルパー関数
│   ├── billing/              # billingモジュールのテスト
│   └── pricing/              # pricingモジュールのテスト
└── snapshots/                # スナップショット保存先（.gitignore）
    ├── auth/
    │   ├── story_snapshots/
    │   ├── story_comparisons/
    │   └── reports/
    └── ...
```

## インストール

テスト用の依存関係をインストールします：

```bash
poetry install --with test
```

## 環境設定

`.env`ファイルに以下の環境変数を設定します：

```bash
# 必須設定
SAASUS_API_KEY=your_api_key
SAASUS_SECRET_KEY=your_secret_key
SAASUS_SAAS_ID=your_saas_id
SAASUS_BASE_URL=https://api.saasus.io/v1

# テスト実行制御（オプション）
DRY_RUN=false                    # true: API呼び出しをスキップ
TIMEOUT=30                       # メソッド実行のタイムアウト（秒）
FAIL_FAST=false                  # true: 失敗時に即座に中断
LOG_LEVEL=INFO                   # DEBUG, INFO, WARNING, ERROR

# スナップショット設定（オプション）
SNAPSHOT_ENABLED=false           # スナップショット機能の有効化
SNAPSHOT_MODE=compare            # capture, compare, report
SNAPSHOT_DIR=tests/snapshots     # スナップショット保存先
COMPATIBILITY_CHECK=true         # メソッドシグネチャの互換性チェック
```

## 基本的な使い方

### テストの実行

```bash
# すべてのE2Eテストを実行
poetry run pytest tests/e2e/ -v

# 特定のモジュールのテストを実行
poetry run pytest tests/e2e/auth/ -v

# Dry Runモード（API呼び出しなし）
DRY_RUN=true poetry run pytest tests/e2e/ -v
```

### ストーリーの定義

ストーリーは、一連の関連するAPIコールをまとめたテストシナリオです。

```python
# tests/e2e/auth/stories.py

from tests.testlib.models import Story, Step
from tests.e2e.auth.validators import validate_user_created
from tests.e2e.auth.helpers import generate_test_email

def get_auth_stories():
    """Authモジュールのストーリー定義"""
    
    return [
        Story(
            name="user_lifecycle",
            description="ユーザーのライフサイクル（作成→取得→更新→削除）",
            module="auth",
            steps=[
                Step(
                    method_name="create_saas_user",
                    params=lambda vars: {
                        "email": generate_test_email(),
                        "password": "TestPass123!"
                    },
                    validation_func=validate_user_created,
                    description="新規ユーザーを作成",
                    store_as="created_user"
                ),
                Step(
                    method_name="get_saas_user",
                    params=lambda vars: {
                        "user_id": vars["created_user"]["id"]
                    },
                    description="作成したユーザーを取得"
                ),
                Step(
                    method_name="delete_saas_user",
                    params=lambda vars: {
                        "user_id": vars["created_user"]["id"]
                    },
                    description="ユーザーを削除"
                )
            ],
            tags=["auth", "user", "crud"]
        )
    ]
```

### 検証関数の定義

```python
# tests/e2e/auth/validators.py

def validate_user_created(response) -> bool:
    """ユーザー作成レスポンスを検証"""
    if not response:
        return False
    
    required_fields = ["id", "email"]
    return all(field in response for field in required_fields)
```

### ヘルパー関数の定義

```python
# tests/e2e/auth/helpers.py

import uuid
from datetime import datetime

def generate_test_email() -> str:
    """テスト用のユニークなメールアドレスを生成"""
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    unique_id = str(uuid.uuid4())[:8]
    return f"test_{timestamp}_{unique_id}@example.com"
```

## コアコンポーネント

### Config（設定管理）

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
```

### TestLogger（ログ出力）

構造化されたログ出力を提供します。

```python
from tests.testlib.logger import TestLogger

logger = TestLogger(config)
logger.story_start(story)
logger.step_result(step_result)
logger.story_end(story_result)
```

### MethodExecutor（メソッド実行エンジン）

SDKメソッドを動的に実行します。

```python
from tests.testlib.method_executor import MethodExecutor

executor = MethodExecutor(client, config, logger)
step_result = executor.execute(step)
```

### CoverageTracker（カバレッジトラッキング）

実行されたSDKメソッドを追跡します。

```python
from tests.testlib.coverage import CoverageTracker

tracker = CoverageTracker(sdk_modules=["auth", "billing", "pricing"])
tracker.record(module="auth", method_name="create_saas_user", success=True)

# カバレッジレポートを取得
report = tracker.get_coverage_report()
print(f"カバレッジ: {report['coverage_percentage']:.2f}%")
```

### Reporter（レポート生成）

テスト結果のレポートを生成します。

```python
from tests.testlib.reporter import Reporter

reporter = Reporter(config)
report_paths = reporter.generate(
    story_results=story_results,
    coverage_report=coverage_report
)

# reports/e2e_report.json
# reports/e2e_report.txt
```

## 実行モード

### 通常モード

実際のAPIエンドポイントに対してテストを実行します。

```bash
poetry run pytest tests/e2e/ -v
```

### Dry Runモード

API呼び出しをスキップし、テストフローのみを検証します。

```bash
DRY_RUN=true poetry run pytest tests/e2e/ -v
```

### Fail Fastモード

最初の失敗で即座にテストを中断します。

```bash
FAIL_FAST=true poetry run pytest tests/e2e/ -v
```

## レポート

テスト実行後、以下のレポートが生成されます：

### JSONレポート

`reports/e2e_report.json`に詳細な実行結果が保存されます。

```json
{
  "summary": {
    "total_stories": 5,
    "successful_stories": 4,
    "failed_stories": 1,
    "success_rate": 80.0,
    "total_execution_time": 12.34,
    "coverage_percentage": 65.5
  },
  "story_results": [...],
  "coverage": {...}
}
```

### テキストレポート

`reports/e2e_report.txt`に人間が読みやすい形式で結果が保存されます。

```
================================================================================
E2E Test Report
================================================================================

Summary:
  Total Stories: 5
  Successful: 4
  Failed: 1
  Success Rate: 80.00%
  Total Time: 12.34s
  Coverage: 65.50%

================================================================================
```

## スナップショット機能

APIレスポンスをスナップショットとして保存し、後続の実行で比較することで互換性を検証します。

### Captureモード（初回実行）

```bash
SNAPSHOT_MODE=capture poetry run pytest tests/e2e/
```

### Compareモード（通常実行）

```bash
SNAPSHOT_MODE=compare poetry run pytest tests/e2e/
```

### 機密情報のマスキング

スナップショットには機密情報が自動的にマスキングされます：

- `api_key`
- `secret`
- `password`
- `token`
- `authorization`

カスタムパターンも追加可能です。

## CI/CD統合

GitHub Actionsでの実行例：

```yaml
name: E2E Tests

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  e2e-tests:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: |
          pip install poetry
          poetry install --with test
      
      - name: Run E2E tests
        env:
          SAASUS_API_KEY: ${{ secrets.SAASUS_API_KEY }}
          SAASUS_SECRET_KEY: ${{ secrets.SAASUS_SECRET_KEY }}
          SAASUS_SAAS_ID: ${{ secrets.SAASUS_SAAS_ID }}
          SAASUS_BASE_URL: ${{ secrets.SAASUS_BASE_URL }}
        run: |
          poetry run pytest tests/e2e/ -v --tb=short
      
      - name: Upload test reports
        if: always()
        uses: actions/upload-artifact@v3
        with:
          name: e2e-reports
          path: reports/
```

## 新規モジュールの追加

新しいAPIモジュールのテストを追加する手順：

1. **ディレクトリ構造を作成**

```bash
mkdir -p tests/e2e/new_module
touch tests/e2e/new_module/stories.py
touch tests/e2e/new_module/validators.py
touch tests/e2e/new_module/helpers.py
```

2. **ストーリーを定義**

```python
# tests/e2e/new_module/stories.py
from tests.testlib.models import Story, Step

def get_new_module_stories():
    return [
        Story(
            name="basic_flow",
            description="基本的なフロー",
            module="new_module",
            steps=[
                # ステップを定義
            ]
        )
    ]
```

3. **pytest fixtureに追加**

```python
# tests/e2e/conftest.py
from tests.e2e.new_module.stories import get_new_module_stories

@pytest.fixture
def new_module_stories():
    return get_new_module_stories()
```

## トラブルシューティング

### 環境変数が読み込まれない

`.env`ファイルがプロジェクトルートに配置されていることを確認してください。

```bash
# .envファイルの確認
cat .env
```

### タイムアウトエラー

`TIMEOUT`環境変数を増やしてください。

```bash
TIMEOUT=60 poetry run pytest tests/e2e/ -v
```

### カバレッジが0%

SDKモジュール名が正しく設定されているか確認してください。

```python
tracker = CoverageTracker(sdk_modules=["auth", "billing", "pricing"])
```

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

- ✅ スナップショットエンジン
- ✅ 機密情報マスキング
- ✅ 差分比較
- ✅ pytest統合
- ✅ Authモジュールのストーリー定義
- ⏳ Billing/Pricingモジュールのストーリー定義
- ⏳ HTMLレポート生成
- ⏳ 並列実行機能

## 参考資料

- [要件定義書](.kiro/specs/e2e-snapshot-testing/requirements.md)
- [設計書](.kiro/specs/e2e-snapshot-testing/design.md)
- [実装計画](.kiro/specs/e2e-snapshot-testing/tasks.md)

## ライセンス

このプロジェクトのライセンスに従います。

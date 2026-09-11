# Auth E2E スナップショットテスト

SaaSus Auth API の包括的なE2Eスナップショットテストスイートです。JavaScriptの実装をPythonに移植しました。

## 📁 ディレクトリ構成

```
tests/e2e/auth/
├── cognito/
│   ├── __init__.py
│   ├── token_provider.py    # Cognitoトークン取得とキャッシュ
│   └── mfa.py                # TOTP生成
├── integrations/
│   ├── __init__.py
│   ├── stripe.py             # Stripe統合
│   └── aws_marketplace.py    # AWS Marketplace統合
├── helpers.py                # ヘルパー関数
├── validation.py             # レスポンス検証関数
├── state.py                  # State管理
├── stories.py                # ストーリー定義
├── test_auth_snapshot.py     # スナップショットテスト実行
└── README.md                 # このファイル
```

## 🚀 実行方法

### 基本実行コマンド

```bash
# 全ストーリーを実行
pytest tests/e2e/auth/

# 特定のストーリーのみ実行
pytest tests/e2e/auth/ -k saas_user_attributes_management
pytest tests/e2e/auth/ -k basic_user_flow

# スナップショットテストを実行
pytest tests/e2e/auth/test_auth_snapshot.py

# スナップショットモード指定実行
SNAPSHOT_MODE=capture pytest tests/e2e/auth/test_auth_snapshot.py    # キャプチャ
SNAPSHOT_MODE=compare pytest tests/e2e/auth/test_auth_snapshot.py    # 比較
SNAPSHOT_MODE=report pytest tests/e2e/auth/test_auth_snapshot.py     # レポート
SNAPSHOT_MODE=full pytest tests/e2e/auth/test_auth_snapshot.py       # 完全実行

# 詳細モード
pytest tests/e2e/auth/ -v
pytest tests/e2e/auth/ -vv  # 超詳細モード
```

## 🔐 環境変数設定

### 必須環境変数

```bash
# SaaSus Platform 認証情報（必須）
SAASUS_SAAS_ID=your-saas-id
SAASUS_API_KEY=your-api-key
SAASUS_SECRET_KEY=your-secret-key

# AWS認証情報（Cognito統合に必須）
AWS_ACCESS_KEY_ID=YOUR_AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY=YOUR_AWS_SECRET_ACCESS_KEY
AWS_SESSION_TOKEN=YOUR_AWS_SESSION_TOKEN

# Cognito設定（必須）
E2E_COGNITO_USER_POOL_ID=ap-northeast-1_xxxxxxxxx
E2E_COGNITO_CLIENT_ID=xxxxxxxxxxxxxxxxxxxxxxxxxx
E2E_COGNITO_REGION=ap-northeast-1
E2E_COGNITO_USERNAME=your-test-username
E2E_COGNITO_PASSWORD=your-test-password
```

### オプション環境変数

```bash
# SaaSus Platform API URL（オプション）
SAASUS_BASE_URL=https://api.saasus.io/v1

# Stripe統合テスト用（Stripe統合テスト実行時のみ必要）
STRIPE_SECRET_KEY=sk_test_xxxxxxxxxxxxxxxxxxxxxxxxxx

# AWS Marketplace統合テスト用（AWS Marketplace統合テスト実行時のみ必要）
AWS_MARKETPLACE_REGISTRATION_TOKEN=your-registration-token

# テスト用設定（オプション）
AUTH_E2E_DEFAULT_PASSWORD=Passw0rd!
DRY_RUN=false
LOG_LEVEL=INFO

# スナップショット設定（オプション）
SNAPSHOT_MODE=capture           # capture, compare, report, full
SNAPSHOT_ENABLED=true
SNAPSHOT_DIR=tests/snapshots
```

## 📚 ストーリー概要

### 実装済みストーリー

1. **basic_user_flow**
   - 基本的なユーザーフロー（ユーザー一覧取得）
   - タグ: `auth`, `user`, `smoke`

2. **user_lifecycle**
   - ユーザーのライフサイクル（作成→取得→削除）
   - タグ: `auth`, `user`, `crud`, `lifecycle`

3. **saas_user_attributes_management**
   - SaaSユーザー属性の管理（作成→取得→削除）
   - タグ: `auth`, `attributes`, `crud`

### 今後実装予定のストーリー

4. **external_user_link_and_email_update**
   - 外部ユーザーリンクとメール更新機能
   - RequestExternalUserLink → RequestEmailUpdate

5. **postman_collection_story**
   - 包括的なAuth APIテスト
   - 基本設定、ユーザー管理、ロール管理、環境管理、テナント管理
   - MFAフロー（CreateSecretCode → UpdateSoftwareToken → UpdateUserMfaPreference）
   - Stripe統合（条件付き）

## 🔧 依存関係のインストール

```bash
# Poetry環境で依存関係をインストール
poetry install --with test

# boto3とpyotpが追加されます
# boto3: Cognito統合用
# pyotp: TOTP生成用
```

## ⚠️ 既知の問題

### AWS認証情報の有効期限
- AWS_SESSION_TOKENは短期間（1時間程度）で期限切れになります
- テスト実行前に新しいトークンを取得してください

### Cognitoトークンキャッシュ
- トークンは30分間メモリにキャッシュされます
- キャッシュをクリアする場合は、Pythonプロセスを再起動してください

### Stripe統合
- Stripe統合テストは `STRIPE_SECRET_KEY` 環境変数が設定されている場合のみ実行されます
- 未設定の場合は自動的にスキップされます

### AWS Marketplace統合
- AWS Marketplace統合テストは有効な登録トークンが必要です
- テスト環境では実際のマーケットプレイス連携は困難なため、基本的な設定更新のみをテストします

## 📊 スナップショット機能

### スナップショットモード

- **capture**: APIレスポンスをスナップショットとして保存
- **compare**: 前回のスナップショットと現在の結果を比較
- **report**: 差分レポートを生成
- **full**: capture + compare + report を実行

### スナップショット保存先

```
tests/snapshots/auth/
├── story_snapshots/
│   ├── basic_user_flow.json
│   ├── user_lifecycle.json
│   └── saas_user_attributes_management.json
├── story_comparisons/
│   └── (差分ファイル)
└── reports/
    └── (レポートファイル)
```

## 🧪 テスト実行例

```bash
# 1. 環境変数を設定
export SAASUS_SAAS_ID=your-saas-id
export SAASUS_API_KEY=your-api-key
export SAASUS_SECRET_KEY=your-secret-key
export AWS_ACCESS_KEY_ID=ASIA...
export AWS_SECRET_ACCESS_KEY=vTpe...
export AWS_SESSION_TOKEN=IQoJ...
export E2E_COGNITO_USER_POOL_ID=ap-northeast-1_xxx
export E2E_COGNITO_CLIENT_ID=xxx
export E2E_COGNITO_USERNAME=test-user
export E2E_COGNITO_PASSWORD=TestPass123!

# 2. スナップショットをキャプチャ
SNAPSHOT_MODE=capture pytest tests/e2e/auth/test_auth_snapshot.py -v

# 3. スナップショットを比較
SNAPSHOT_MODE=compare pytest tests/e2e/auth/test_auth_snapshot.py -v

# 4. レポートを確認
cat tests/snapshots/auth/reports/snapshot_report.json
```

## 📖 JavaScriptとの対応表

| JavaScript | Python | 説明 |
|------------|--------|------|
| `helpers.ts` | `helpers.py` | ヘルパー関数 |
| `validation.ts` | `validation.py` | レスポンス検証 |
| `state.ts` | `state.py` | State管理 |
| `stories.ts` | `stories.py` | ストーリー定義 |
| `cognito/token-provider.ts` | `cognito/token_provider.py` | Cognitoトークン取得 |
| `cognito/mfa.ts` | `cognito/mfa.py` | TOTP生成 |
| `integrations/stripe.ts` | `integrations/stripe.py` | Stripe統合 |
| `integrations/aws-marketplace.ts` | `integrations/aws_marketplace.py` | AWS Marketplace統合 |
| `auth.snapshot.test.ts` | `test_auth_snapshot.py` | スナップショットテスト |

## 🤝 貢献

新しいストーリーを追加する場合は、`stories.py`に追加してください。

```python
Story(
    name="your_story_name",
    description="ストーリーの説明",
    module="auth",
    steps=[
        Step(
            method_name="method_name",
            params={},
            description="ステップの説明"
        )
    ],
    tags=["auth", "your-tag"]
)
```

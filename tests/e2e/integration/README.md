# Integration (EventBridge) E2E スナップショットテスト

SaaSus Integration (EventBridge) API のE2Eスナップショットテストです。`saasus-sdk-javascript` の `tests/e2e/integration` を Python に移植しました。

## 📁 ディレクトリ構成

```
tests/e2e/integration/
├── __init__.py
├── helpers.py                      # EventBridge設定 / イベントのペイロードビルダー
├── validation.py                   # レスポンス検証関数
├── state.py                        # 前処理/後処理（設定削除, 404は無視）
├── stories.py                      # ストーリー定義
├── test_integration_snapshot.py    # スナップショットテスト実行
└── README.md                       # このファイル
```

## 🧩 カバーするメソッド

- `save_event_bridge_settings`（SaveEventBridgeSettings）
- `get_event_bridge_settings`（GetEventBridgeSettings_AfterSave）
- `create_event_bridge_test_event`（CreateEventBridgeTestEvent）
- `create_event_bridge_event`（CreateEventBridgeEvent, 環境依存の失敗を許容 = `allow_failure=True`）
- `delete_event_bridge_settings`（DeleteEventBridgeSettings）

## 🚀 実行方法

```bash
SNAPSHOT_MODE=capture pytest tests/e2e/integration/test_integration_snapshot.py
SNAPSHOT_MODE=compare pytest tests/e2e/integration/test_integration_snapshot.py
SNAPSHOT_MODE=report  pytest tests/e2e/integration/test_integration_snapshot.py
SNAPSHOT_MODE=full    pytest tests/e2e/integration/test_integration_snapshot.py
```

スナップショットは `tests/snapshots/integration/` 配下に出力されます。

## 🔐 必須環境変数

```bash
SAASUS_SAAS_ID=your-saas-id
SAASUS_API_KEY=your-api-key
SAASUS_SECRET_KEY=your-secret-key
SAASUS_BASE_URL=https://api.saasus.io/v1
```

## ⚙️ 任意環境変数（EventBridge設定）

```bash
TEST_AWS_ACCOUNT_ID=267185063265   # 既定値
TEST_AWS_REGION=ap-northeast-1     # 既定値（AwsRegion enumで受理される値）
```

## 🧹 クリーンアップ

テスト前後で `delete_event_bridge_settings` を実行し、未設定(404)は無視します。

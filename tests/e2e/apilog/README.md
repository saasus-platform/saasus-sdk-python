# ApiLog E2E スナップショットテスト

SaaSus ApiLog API のE2Eスナップショットテストです。`saasus-sdk-javascript` の `tests/e2e/apilogs` を Python に移植しました。

## 📁 ディレクトリ構成

```
tests/e2e/apilog/
├── __init__.py
├── helpers.py                 # パラメータビルダー / ログ情報抽出
├── validation.py              # レスポンス検証関数
├── state.py                   # State管理（参照系のためクリーンアップは無し）
├── stories.py                 # ストーリー定義
├── test_apilog_snapshot.py    # スナップショットテスト実行
└── README.md                  # このファイル
```

## 🧩 カバーするメソッド

- `get_logs`（Pre_GetApiLogs / GetApiLogs / GetApiLogs With QueryParameters）
- `get_log`（GetApiLog）

## 🚀 実行方法

```bash
# キャプチャ
SNAPSHOT_MODE=capture pytest tests/e2e/apilog/test_apilog_snapshot.py
# 比較 / レポート / 完全
SNAPSHOT_MODE=compare pytest tests/e2e/apilog/test_apilog_snapshot.py
SNAPSHOT_MODE=report  pytest tests/e2e/apilog/test_apilog_snapshot.py
SNAPSHOT_MODE=full    pytest tests/e2e/apilog/test_apilog_snapshot.py
```

スナップショットは `tests/snapshots/apilog/` 配下に出力されます。

## 🔐 必須環境変数

```bash
SAASUS_SAAS_ID=your-saas-id
SAASUS_API_KEY=your-api-key
SAASUS_SECRET_KEY=your-secret-key
SAASUS_BASE_URL=https://api.saasus.io/v1
```

## ⚠️ 前提条件

`get_logs` は少なくとも1件のAPIログが存在することを前提に検証します（`api_logs` が空だと失敗）。
テナントにAPIログが無い場合は、他のAPI呼び出しを行ってログを生成してから実行してください。

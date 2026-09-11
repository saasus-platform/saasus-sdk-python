# Communication (Feedback) E2E スナップショットテスト

SaaSus Communication (Feedback) API のE2Eスナップショットテストです。`saasus-sdk-javascript` の `tests/e2e/communication` を Python に移植しました。

## 📁 ディレクトリ構成

```
tests/e2e/communication/
├── __init__.py
├── helpers.py                        # パラメータビルダー / user_id取得 / タイトルprefix
├── validation.py                     # レスポンス検証関数
├── state.py                          # テストフィードバックのクリーンアップ
├── stories.py                        # ストーリー定義（12ステップ）
├── test_communication_snapshot.py    # スナップショットテスト実行
└── README.md                         # このファイル
```

## 🧩 カバーするメソッド（12種）

`get_feedbacks` → `create_feedback` → `get_feedback` → `update_feedback` →
`update_feedback_status` → `create_feedback_comment` → `get_feedback_comment` →
`update_feedback_comment` → `create_vote_user` → `delete_vote_for_feedback` →
`delete_feedback_comment` → `delete_feedback`

`create_feedback` / `create_feedback_comment` のレスポンスを `store_as` で保存し、
後続ステップで `feedback_id` / `comment_id` を再利用します。

## 🚀 実行方法

```bash
SNAPSHOT_MODE=capture pytest tests/e2e/communication/test_communication_snapshot.py
SNAPSHOT_MODE=compare pytest tests/e2e/communication/test_communication_snapshot.py
SNAPSHOT_MODE=report  pytest tests/e2e/communication/test_communication_snapshot.py
SNAPSHOT_MODE=full    pytest tests/e2e/communication/test_communication_snapshot.py
```

スナップショットは `tests/snapshots/communication/` 配下に出力されます。

## 🔐 必須環境変数

```bash
SAASUS_SAAS_ID=your-saas-id
SAASUS_API_KEY=your-api-key
SAASUS_SECRET_KEY=your-secret-key
SAASUS_BASE_URL=https://api.saasus.io/v1
```

## ⚙️ 任意環境変数

```bash
TEST_USER_ID=00000000-0000-0000-0000-000000000000   # 既定値。フィードバック/投票のuser_id
```

## 🧹 クリーンアップ

テスト前後で、タイトルが `py-sdk-e2e-feedback` で始まるテスト用フィードバックを一覧取得して削除します。

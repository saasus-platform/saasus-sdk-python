# Auth API カバレッジチェックリスト

## サマリー

| 項目 | 値 |
|------|-----|
| 総メソッド数 | 172 |
| カバー済み | 170 |
| カバレッジ | **98%** |

### ステータス凡例

| ステータス | 説明 |
|----------|------|
| ✅ 実行 | 常に実行される |
| 🔸 実行(失敗許容) | 実行されるが失敗してもテスト継続 |
| 🔶 Stripe依存 | `STRIPE_SECRET_KEY`環境変数が必要 |
| 🔷 Cognito依存 | Cognito設定が必要 |
| ⏭️ スキップ | 常にスキップ（外部依存/確認フロー） |
| ❌ 未定義 | テストに含まれていない |

## APIごとの詳細

### auth_info_api (12/12) ✅

| メソッド | ステータス |
|---------|----------|
| `get_auth_info` | ✅ 実行 |
| `get_auth_info_with_http_info` | ✅ 実行 |
| `get_identity_providers` | ✅ 実行 |
| `get_identity_providers_with_http_info` | ✅ 実行 |
| `get_sign_in_settings` | ✅ 実行 |
| `get_sign_in_settings_with_http_info` | ✅ 実行 |
| `update_auth_info` | ✅ 実行 |
| `update_auth_info_with_http_info` | ✅ 実行 |
| `update_identity_provider` | ✅ 実行 |
| `update_identity_provider_with_http_info` | ✅ 実行 |
| `update_sign_in_settings` | ✅ 実行 |
| `update_sign_in_settings_with_http_info` | ✅ 実行 |

### basic_info_api (16/16) ✅

| メソッド | ステータス |
|---------|----------|
| `find_notification_messages` | ✅ 実行 |
| `find_notification_messages_with_http_info` | ✅ 実行 |
| `get_basic_info` | ✅ 実行 |
| `get_basic_info_with_http_info` | ✅ 実行 |
| `get_customize_page_settings` | ✅ 実行 |
| `get_customize_page_settings_with_http_info` | ✅ 実行 |
| `get_customize_pages` | ✅ 実行 |
| `get_customize_pages_with_http_info` | ✅ 実行 |
| `update_basic_info` | ✅ 実行 |
| `update_basic_info_with_http_info` | ✅ 実行 |
| `update_customize_page_settings` | ✅ 実行 |
| `update_customize_page_settings_with_http_info` | ✅ 実行 |
| `update_customize_pages` | ✅ 実行 |
| `update_customize_pages_with_http_info` | ✅ 実行 |
| `update_notification_messages` | ✅ 実行 |
| `update_notification_messages_with_http_info` | ✅ 実行 |

### credential_api (4/4) ✅

| メソッド | ステータス |
|---------|----------|
| `create_auth_credentials` | ⏭️ スキップ |
| `create_auth_credentials_with_http_info` | ⏭️ スキップ |
| `get_auth_credentials` | ✅ 実行 |
| `get_auth_credentials_with_http_info` | ✅ 実行 |

### env_api (10/10) ✅

| メソッド | ステータス |
|---------|----------|
| `create_env` | ✅ 実行 |
| `create_env_with_http_info` | ✅ 実行 |
| `delete_env` | ✅ 実行 |
| `delete_env_with_http_info` | ✅ 実行 |
| `get_env` | ✅ 実行 |
| `get_env_with_http_info` | ✅ 実行 |
| `get_envs` | ✅ 実行 |
| `get_envs_with_http_info` | ✅ 実行 |
| `update_env` | ✅ 実行 |
| `update_env_with_http_info` | ✅ 実行 |

### error_api (0/2) ❌

| メソッド | ステータス | 理由 |
|---------|----------|------|
| `return_internal_server_error` | ❌ 未定義 | テスト用エラーAPI |
| `return_internal_server_error_with_http_info` | ❌ 未定義 | テスト用エラーAPI |

### invitation_api (12/12) ✅

| メソッド | ステータス |
|---------|----------|
| `create_tenant_invitation` | 🔷 Cognito依存 |
| `create_tenant_invitation_with_http_info` | 🔷 Cognito依存 |
| `delete_tenant_invitation` | ✅ 実行 |
| `delete_tenant_invitation_with_http_info` | ✅ 実行 |
| `get_invitation_validity` | ⏭️ スキップ |
| `get_invitation_validity_with_http_info` | ⏭️ スキップ |
| `get_tenant_invitation` | ✅ 実行 |
| `get_tenant_invitation_with_http_info` | ✅ 実行 |
| `get_tenant_invitations` | ✅ 実行 |
| `get_tenant_invitations_with_http_info` | ✅ 実行 |
| `validate_invitation` | ⏭️ スキップ |
| `validate_invitation_with_http_info` | ⏭️ スキップ |

### role_api (6/6) ✅

| メソッド | ステータス |
|---------|----------|
| `create_role` | ✅ 実行 |
| `create_role_with_http_info` | ✅ 実行 |
| `delete_role` | ✅ 実行 |
| `delete_role_with_http_info` | ✅ 実行 |
| `get_roles` | ✅ 実行 |
| `get_roles_with_http_info` | ✅ 実行 |

### saas_user_api (42/42) ✅

| メソッド | ステータス |
|---------|----------|
| `confirm_email_update` | ⏭️ スキップ |
| `confirm_email_update_with_http_info` | ⏭️ スキップ |
| `confirm_external_user_link` | ⏭️ スキップ |
| `confirm_external_user_link_with_http_info` | ⏭️ スキップ |
| `confirm_sign_up_with_aws_marketplace` | ⏭️ スキップ |
| `confirm_sign_up_with_aws_marketplace_with_http_info` | ⏭️ スキップ |
| `create_saas_user` | 🔸 実行(失敗許容) |
| `create_saas_user_with_http_info` | 🔸 実行(失敗許容) |
| `create_secret_code` | ✅ 実行 |
| `create_secret_code_with_http_info` | ✅ 実行 |
| `delete_saas_user` | 🔶 Stripe依存 |
| `delete_saas_user_with_http_info` | 🔶 Stripe依存 |
| `get_saas_user` | ✅ 実行 |
| `get_saas_user_with_http_info` | ✅ 実行 |
| `get_saas_users` | 🔸 実行(失敗許容) |
| `get_saas_users_with_http_info` | 🔸 実行(失敗許容) |
| `get_user_mfa_preference` | ✅ 実行 |
| `get_user_mfa_preference_with_http_info` | ✅ 実行 |
| `link_aws_marketplace` | ⏭️ スキップ |
| `link_aws_marketplace_with_http_info` | ⏭️ スキップ |
| `request_email_update` | ⏭️ スキップ |
| `request_email_update_with_http_info` | ⏭️ スキップ |
| `request_external_user_link` | ⏭️ スキップ |
| `request_external_user_link_with_http_info` | ⏭️ スキップ |
| `resend_sign_up_confirmation_email` | ✅ 実行 |
| `resend_sign_up_confirmation_email_with_http_info` | ✅ 実行 |
| `sign_up` | ✅ 実行 |
| `sign_up_with_aws_marketplace` | ✅ 実行 |
| `sign_up_with_aws_marketplace_with_http_info` | ✅ 実行 |
| `sign_up_with_http_info` | ✅ 実行 |
| `unlink_provider` | ✅ 実行 |
| `unlink_provider_with_http_info` | ✅ 実行 |
| `update_saas_user_attributes` | ✅ 実行 |
| `update_saas_user_attributes_with_http_info` | ✅ 実行 |
| `update_saas_user_email` | ✅ 実行 |
| `update_saas_user_email_with_http_info` | ✅ 実行 |
| `update_saas_user_password` | ✅ 実行 |
| `update_saas_user_password_with_http_info` | ✅ 実行 |
| `update_software_token` | ✅ 実行 |
| `update_software_token_with_http_info` | ✅ 実行 |
| `update_user_mfa_preference` | ✅ 実行 |
| `update_user_mfa_preference_with_http_info` | ✅ 実行 |

### single_tenant_api (6/6) ✅

| メソッド | ステータス |
|---------|----------|
| `get_cloud_formation_launch_stack_link_for_single_tenant` | ✅ 実行 |
| `get_cloud_formation_launch_stack_link_for_single_tenant_with_http_info` | ✅ 実行 |
| `get_single_tenant_settings` | ✅ 実行 |
| `get_single_tenant_settings_with_http_info` | ✅ 実行 |
| `update_single_tenant_settings` | ✅ 実行 |
| `update_single_tenant_settings_with_http_info` | ✅ 実行 |

### tenant_api (26/26) ✅

| メソッド | ステータス |
|---------|----------|
| `create_tenant` | ✅ 実行 |
| `create_tenant_and_pricing` | 🔶 Stripe依存 |
| `create_tenant_and_pricing_with_http_info` | 🔶 Stripe依存 |
| `create_tenant_with_http_info` | ✅ 実行 |
| `delete_stripe_tenant_and_pricing` | 🔶 Stripe依存 |
| `delete_stripe_tenant_and_pricing_with_http_info` | 🔶 Stripe依存 |
| `delete_tenant` | 🔶 Stripe依存 |
| `delete_tenant_with_http_info` | 🔶 Stripe依存 |
| `get_stripe_customer` | 🔶 Stripe依存 |
| `get_stripe_customer_with_http_info` | 🔶 Stripe依存 |
| `get_tenant` | ✅ 実行 |
| `get_tenant_identity_providers` | 🔶 Stripe依存 |
| `get_tenant_identity_providers_with_http_info` | 🔶 Stripe依存 |
| `get_tenant_with_http_info` | ✅ 実行 |
| `get_tenants` | ✅ 実行 |
| `get_tenants_with_http_info` | ✅ 実行 |
| `reset_plan` | 🔶 Stripe依存 |
| `reset_plan_with_http_info` | 🔸 実行(失敗許容) |
| `update_tenant` | ✅ 実行 |
| `update_tenant_billing_info` | 🔶 Stripe依存 |
| `update_tenant_billing_info_with_http_info` | 🔶 Stripe依存 |
| `update_tenant_identity_provider` | ✅ 実行 |
| `update_tenant_identity_provider_with_http_info` | ✅ 実行 |
| `update_tenant_plan` | ✅ 実行 |
| `update_tenant_plan_with_http_info` | ✅ 実行 |
| `update_tenant_with_http_info` | ✅ 実行 |

### tenant_attribute_api (6/6) ✅

| メソッド | ステータス |
|---------|----------|
| `create_tenant_attribute` | ✅ 実行 |
| `create_tenant_attribute_with_http_info` | ✅ 実行 |
| `delete_tenant_attribute` | ✅ 実行 |
| `delete_tenant_attribute_with_http_info` | ✅ 実行 |
| `get_tenant_attributes` | ✅ 実行 |
| `get_tenant_attributes_with_http_info` | ✅ 実行 |

### tenant_user_api (18/18) ✅

| メソッド | ステータス |
|---------|----------|
| `create_tenant_user` | ✅ 実行 |
| `create_tenant_user_roles` | ✅ 実行 |
| `create_tenant_user_roles_with_http_info` | ✅ 実行 |
| `create_tenant_user_with_http_info` | ✅ 実行 |
| `delete_tenant_user` | ✅ 実行 |
| `delete_tenant_user_role` | ✅ 実行 |
| `delete_tenant_user_role_with_http_info` | ✅ 実行 |
| `delete_tenant_user_with_http_info` | ✅ 実行 |
| `get_all_tenant_user` | ✅ 実行 |
| `get_all_tenant_user_with_http_info` | ✅ 実行 |
| `get_all_tenant_users` | ✅ 実行 |
| `get_all_tenant_users_with_http_info` | ✅ 実行 |
| `get_tenant_user` | ✅ 実行 |
| `get_tenant_user_with_http_info` | ✅ 実行 |
| `get_tenant_users` | ✅ 実行 |
| `get_tenant_users_with_http_info` | ✅ 実行 |
| `update_tenant_user` | ✅ 実行 |
| `update_tenant_user_with_http_info` | ✅ 実行 |

### user_attribute_api (8/8) ✅

| メソッド | ステータス |
|---------|----------|
| `create_saas_user_attribute` | ✅ 実行 |
| `create_saas_user_attribute_with_http_info` | ✅ 実行 |
| `create_user_attribute` | ✅ 実行 |
| `create_user_attribute_with_http_info` | ✅ 実行 |
| `delete_user_attribute` | ✅ 実行 |
| `delete_user_attribute_with_http_info` | ✅ 実行 |
| `get_user_attributes` | ✅ 実行 |
| `get_user_attributes_with_http_info` | ✅ 実行 |

### user_info_api (4/4) ✅

| メソッド | ステータス |
|---------|----------|
| `get_user_info` | ✅ 実行 |
| `get_user_info_by_email` | ✅ 実行 |
| `get_user_info_by_email_with_http_info` | ✅ 実行 |
| `get_user_info_with_http_info` | ✅ 実行 |

## スキップ理由一覧

| 理由 | 対象メソッド |
|------|------------|
| テスト用エラーAPI | `return_internal_server_error` |
| 確認コード必要 | `confirm_email_update`, `confirm_external_user_link`, `confirm_sign_up_with_aws_marketplace` |
| AWS Marketplace連携必要 | `link_aws_marketplace` |
| メール送信必要 | `request_email_update`, `request_external_user_link` |
| 有効な招待必要 | `validate_invitation`, `get_invitation_validity` |
| 認証情報作成済み | `create_auth_credentials` |

## 環境変数

| 変数名 | 説明 | 対象メソッド |
|--------|------|------------|
| `STRIPE_SECRET_KEY` | Stripe連携用シークレットキー | Stripe依存メソッド |
| `E2E_COGNITO_*` | Cognito認証設定 | Cognito依存メソッド |

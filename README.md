# saasus-sdk-python
スキーマ

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import saasus_sdk_python
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import saasus_sdk_python
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import saasus_sdk_python
from saasus_sdk_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.saasus.io/v1/auth
# See configuration.py for a list of all supported configuration parameters.
configuration = saasus_sdk_python.Configuration(
    host = "https://api.saasus.io/v1/auth"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = saasus_sdk_python.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)


# Enter a context with an instance of the API client
with saasus_sdk_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = saasus_sdk_python.AuthInfoApi(api_client)

    try:
        # 認証情報を取得(Get Authentication Info)
        api_response = api_instance.get_auth_info()
        print("The response of AuthInfoApi->get_auth_info:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthInfoApi->get_auth_info: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.saasus.io/v1/auth*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthInfoApi* | [**get_auth_info**](docs/AuthInfoApi.md#get_auth_info) | **GET** /auth-info | 認証情報を取得(Get Authentication Info)
*AuthInfoApi* | [**get_identity_providers**](docs/AuthInfoApi.md#get_identity_providers) | **GET** /identity-providers | 
*AuthInfoApi* | [**get_sign_in_settings**](docs/AuthInfoApi.md#get_sign_in_settings) | **GET** /sign-in-settings | パスワード要件を取得(Get Password Requirements)
*AuthInfoApi* | [**update_auth_info**](docs/AuthInfoApi.md#update_auth_info) | **PUT** /auth-info | 認証情報を更新(Update Authentication Info)
*AuthInfoApi* | [**update_identity_provider**](docs/AuthInfoApi.md#update_identity_provider) | **PUT** /identity-providers | 
*AuthInfoApi* | [**update_sign_in_settings**](docs/AuthInfoApi.md#update_sign_in_settings) | **PUT** /sign-in-settings | パスワード要件を更新(Update Password Requirements)
*BasicInfoApi* | [**find_notification_messages**](docs/BasicInfoApi.md#find_notification_messages) | **GET** /notification-messages | 通知メールテンプレートを取得(Get Notification Email Templates)
*BasicInfoApi* | [**get_basic_info**](docs/BasicInfoApi.md#get_basic_info) | **GET** /basic-info | 基本設定情報の取得(Get Basic Configurations)
*BasicInfoApi* | [**get_customize_page_settings**](docs/BasicInfoApi.md#get_customize_page_settings) | **GET** /customize-page-settings | 認証認可基本情報取得(Get Authentication Authorization Basic Information)
*BasicInfoApi* | [**get_customize_pages**](docs/BasicInfoApi.md#get_customize_pages) | **GET** /customize-pages | 認証系画面設定情報取得(Get Authentication Page Setting)
*BasicInfoApi* | [**update_basic_info**](docs/BasicInfoApi.md#update_basic_info) | **PUT** /basic-info | 基本設定情報の更新(Update Basic Configurations)
*BasicInfoApi* | [**update_customize_page_settings**](docs/BasicInfoApi.md#update_customize_page_settings) | **PATCH** /customize-page-settings | 認証認可基本情報更新(Update Authentication Authorization Basic Information)
*BasicInfoApi* | [**update_customize_pages**](docs/BasicInfoApi.md#update_customize_pages) | **PATCH** /customize-pages | 認証系画面設定情報設定(Authentication Page Setting)
*BasicInfoApi* | [**update_notification_messages**](docs/BasicInfoApi.md#update_notification_messages) | **PUT** /notification-messages | 通知メールテンプレートを更新(Update Notification Email Template)
*CredentialApi* | [**create_auth_credentials**](docs/CredentialApi.md#create_auth_credentials) | **POST** /credentials | 認証・認可情報の保存(Save Authentication/Authorization Information)
*CredentialApi* | [**get_auth_credentials**](docs/CredentialApi.md#get_auth_credentials) | **GET** /credentials | 認証・認可情報の取得(Get Authentication/Authorization Information)
*EnvApi* | [**create_env**](docs/EnvApi.md#create_env) | **POST** /envs | 環境情報を作成(Create Env Info)
*EnvApi* | [**delete_env**](docs/EnvApi.md#delete_env) | **DELETE** /envs/{env_id} | 環境情報を削除(Delete Env Info)
*EnvApi* | [**get_env**](docs/EnvApi.md#get_env) | **GET** /envs/{env_id} | 環境情報を取得(Get Env Details)
*EnvApi* | [**get_envs**](docs/EnvApi.md#get_envs) | **GET** /envs | 環境情報一覧を取得(Get Env Info)
*EnvApi* | [**update_env**](docs/EnvApi.md#update_env) | **PATCH** /envs/{env_id} | 環境情報を更新(Update Env Info)
*ErrorApi* | [**return_internal_server_error**](docs/ErrorApi.md#return_internal_server_error) | **GET** /errors/internal-server-error | ステータスコード500でサーバーエラーを返却(Return Internal Server Error)
*RoleApi* | [**create_role**](docs/RoleApi.md#create_role) | **POST** /roles | 役割(ロール)を作成(Create Role)
*RoleApi* | [**delete_role**](docs/RoleApi.md#delete_role) | **DELETE** /roles/{role_name} | 役割(ロール)を削除(Delete Role)
*RoleApi* | [**get_roles**](docs/RoleApi.md#get_roles) | **GET** /roles | 役割(ロール)一覧を取得(Get Roles)
*SaasUserApi* | [**confirm_sign_up_with_aws_marketplace**](docs/SaasUserApi.md#confirm_sign_up_with_aws_marketplace) | **POST** /aws-marketplace/sign-up-confirm | AWS Marketplaceによるユーザー新規登録の確定(Confirm Sign Up with AWS Marketplace)
*SaasUserApi* | [**create_saas_user**](docs/SaasUserApi.md#create_saas_user) | **POST** /users | SaaSにユーザーを作成(Create SaaS User)
*SaasUserApi* | [**create_secret_code**](docs/SaasUserApi.md#create_secret_code) | **POST** /users/{user_id}/mfa/software-token/secret-code | 認証アプリケーション登録用のシークレットコードを作成(Creates secret code for authentication application registration)
*SaasUserApi* | [**delete_saas_user**](docs/SaasUserApi.md#delete_saas_user) | **DELETE** /users/{user_id} | ユーザー情報を削除(Delete User)
*SaasUserApi* | [**get_saas_user**](docs/SaasUserApi.md#get_saas_user) | **GET** /users/{user_id} | ユーザー情報を取得(Get User)
*SaasUserApi* | [**get_saas_users**](docs/SaasUserApi.md#get_saas_users) | **GET** /users | ユーザー一覧を取得(Get Users)
*SaasUserApi* | [**get_user_mfa_preference**](docs/SaasUserApi.md#get_user_mfa_preference) | **GET** /users/{user_id}/mfa/preference | ユーザーのMFA設定を取得(Get User&#39;s MFA Settings)
*SaasUserApi* | [**link_aws_marketplace**](docs/SaasUserApi.md#link_aws_marketplace) | **PATCH** /aws-marketplace/link | AWS Marketplaceと既存のテナントの連携(Link an existing tenant with AWS Marketplace)
*SaasUserApi* | [**resend_sign_up_confirmation_email**](docs/SaasUserApi.md#resend_sign_up_confirmation_email) | **POST** /sign-up/resend | 新規登録時の確認メール再送信(Resend Sign Up Confirmation Email)
*SaasUserApi* | [**sign_up**](docs/SaasUserApi.md#sign_up) | **POST** /sign-up | 新規登録(Sign Up)
*SaasUserApi* | [**sign_up_with_aws_marketplace**](docs/SaasUserApi.md#sign_up_with_aws_marketplace) | **POST** /aws-marketplace/sign-up | AWS Marketplaceによるユーザー新規登録(Sign Up with AWS Marketplace)
*SaasUserApi* | [**unlink_provider**](docs/SaasUserApi.md#unlink_provider) | **DELETE** /users/{user_id}/providers/{provider_name} | 外部IDプロバイダの連携解除(Unlink external identity providers)
*SaasUserApi* | [**update_saas_user_email**](docs/SaasUserApi.md#update_saas_user_email) | **PATCH** /users/{user_id}/email | メールアドレスを変更(Change Email)
*SaasUserApi* | [**update_saas_user_password**](docs/SaasUserApi.md#update_saas_user_password) | **PATCH** /users/{user_id}/password | パスワードを変更(Change Password)
*SaasUserApi* | [**update_software_token**](docs/SaasUserApi.md#update_software_token) | **PUT** /users/{user_id}/mfa/software-token | 認証アプリケーションを登録(Register Authentication Application)
*SaasUserApi* | [**update_user_mfa_preference**](docs/SaasUserApi.md#update_user_mfa_preference) | **PATCH** /users/{user_id}/mfa/preference | ユーザーのMFA設定を更新(Update User&#39;s MFA Settings)
*SaasusTenantApi* | [**create_api_key**](docs/SaasusTenantApi.md#create_api_key) | **POST** /apikeys | APIキーを作成(Create API Key)
*SaasusTenantApi* | [**delete_api_key**](docs/SaasusTenantApi.md#delete_api_key) | **DELETE** /apikeys/{api_key} | APIキーを削除(Delete API Key)
*SaasusTenantApi* | [**get_api_keys**](docs/SaasusTenantApi.md#get_api_keys) | **GET** /apikeys | APIキー一覧を取得(Get API Keys)
*SaasusTenantApi* | [**get_client_secret**](docs/SaasusTenantApi.md#get_client_secret) | **GET** /client-secret | クライアントシークレットを取得(Get Client Secret)
*SaasusTenantApi* | [**get_saas_id**](docs/SaasusTenantApi.md#get_saas_id) | **GET** /saasid | SaasIDを取得(Get SaasID)
*SaasusTenantApi* | [**update_client_secret**](docs/SaasusTenantApi.md#update_client_secret) | **PATCH** /client-secret | クライアントシークレットを更新(Update Client Secret)
*SaasusTenantApi* | [**update_saas_id**](docs/SaasusTenantApi.md#update_saas_id) | **PATCH** /saasid | SaasIDを更新(Update SaasID)
*TenantApi* | [**create_tenant**](docs/TenantApi.md#create_tenant) | **POST** /tenants | テナントを作成(Create Tenant)
*TenantApi* | [**create_tenant_and_pricing**](docs/TenantApi.md#create_tenant_and_pricing) | **PATCH** /stripe/init | stripe初期設定(Stripe Initial Setting)
*TenantApi* | [**delete_stripe_tenant_and_pricing**](docs/TenantApi.md#delete_stripe_tenant_and_pricing) | **DELETE** /stripe | stripe上の顧客情報・商品情報の削除(Delete Customer and Product From Stripe)
*TenantApi* | [**delete_tenant**](docs/TenantApi.md#delete_tenant) | **DELETE** /tenants/{tenant_id} | テナント情報を削除(Delete Tenant)
*TenantApi* | [**get_tenant**](docs/TenantApi.md#get_tenant) | **GET** /tenants/{tenant_id} | テナント情報を取得(Get Tenant Details)
*TenantApi* | [**get_tenants**](docs/TenantApi.md#get_tenants) | **GET** /tenants | テナント一覧取得(Get Tenants)
*TenantApi* | [**reset_plan**](docs/TenantApi.md#reset_plan) | **PUT** /plans/reset | プランに関わる情報を全削除
*TenantApi* | [**update_tenant**](docs/TenantApi.md#update_tenant) | **PATCH** /tenants/{tenant_id} | テナント情報を更新(Update Tenant Details)
*TenantApi* | [**update_tenant_billing_info**](docs/TenantApi.md#update_tenant_billing_info) | **PUT** /tenants/{tenant_id}/billing-info | テナントの請求先情報を更新(Update Tenant Billing Information)
*TenantApi* | [**update_tenant_plan**](docs/TenantApi.md#update_tenant_plan) | **PUT** /tenants/{tenant_id}/plans | テナントのプラン情報を更新(Update Tenant Plan Information)
*TenantAttributeApi* | [**create_tenant_attribute**](docs/TenantAttributeApi.md#create_tenant_attribute) | **POST** /tenant-attributes | テナント属性の作成(Create Tenant Attribute)
*TenantAttributeApi* | [**delete_tenant_attribute**](docs/TenantAttributeApi.md#delete_tenant_attribute) | **DELETE** /tenant-attributes/{attribute_name} | テナント属性の削除(Delete Tenant Attribute)
*TenantAttributeApi* | [**get_tenant_attributes**](docs/TenantAttributeApi.md#get_tenant_attributes) | **GET** /tenant-attributes | テナント属性の一覧を取得(Get Tenant Attributes)
*TenantUserApi* | [**create_tenant_user**](docs/TenantUserApi.md#create_tenant_user) | **POST** /tenants/{tenant_id}/users | テナントにユーザーを作成(Create Tenant User)
*TenantUserApi* | [**create_tenant_user_roles**](docs/TenantUserApi.md#create_tenant_user_roles) | **POST** /tenants/{tenant_id}/users/{user_id}/envs/{env_id}/roles | テナントのユーザー情報に役割(ロール)を作成(Create Tenant User Role)
*TenantUserApi* | [**delete_tenant_user**](docs/TenantUserApi.md#delete_tenant_user) | **DELETE** /tenants/{tenant_id}/users/{user_id} | テナントのユーザー情報を削除(Delete Tenant User)
*TenantUserApi* | [**delete_tenant_user_role**](docs/TenantUserApi.md#delete_tenant_user_role) | **DELETE** /tenants/{tenant_id}/users/{user_id}/envs/{env_id}/roles/{role_name} | テナントのユーザーから役割(ロール)を削除(Remove Role From Tenant User)
*TenantUserApi* | [**get_all_tenant_user**](docs/TenantUserApi.md#get_all_tenant_user) | **GET** /tenants/all/users/{user_id} | ユーザー情報を取得(Get User Info)
*TenantUserApi* | [**get_all_tenant_users**](docs/TenantUserApi.md#get_all_tenant_users) | **GET** /tenants/all/users | ユーザー一覧を取得(Get Users)
*TenantUserApi* | [**get_tenant_user**](docs/TenantUserApi.md#get_tenant_user) | **GET** /tenants/{tenant_id}/users/{user_id} | テナントのユーザー情報を取得(Get Tenant User)
*TenantUserApi* | [**get_tenant_users**](docs/TenantUserApi.md#get_tenant_users) | **GET** /tenants/{tenant_id}/users | テナントのユーザー一覧を取得(Get Tenant Users)
*TenantUserApi* | [**update_tenant_user**](docs/TenantUserApi.md#update_tenant_user) | **PATCH** /tenants/{tenant_id}/users/{user_id} | テナントのユーザー属性情報を更新(Update Tenant User Attribute)
*UserAttributeApi* | [**create_user_attribute**](docs/UserAttributeApi.md#create_user_attribute) | **POST** /user-attributes | ユーザー属性の作成(Create User Attributes)
*UserAttributeApi* | [**delete_user_attribute**](docs/UserAttributeApi.md#delete_user_attribute) | **DELETE** /user-attributes/{attribute_name} | ユーザー属性の削除(Delete User Attribute)
*UserAttributeApi* | [**get_user_attributes**](docs/UserAttributeApi.md#get_user_attributes) | **GET** /user-attributes | ユーザー属性の一覧を取得(Get User Attributes)
*UserInfoApi* | [**get_user_info**](docs/UserInfoApi.md#get_user_info) | **GET** /userinfo | ユーザー情報取得(Get User Info)


## Documentation For Models

 - [AccountVerification](docs/AccountVerification.md)
 - [ApiKeys](docs/ApiKeys.md)
 - [Attribute](docs/Attribute.md)
 - [AttributeType](docs/AttributeType.md)
 - [AuthInfo](docs/AuthInfo.md)
 - [AuthorizationTempCode](docs/AuthorizationTempCode.md)
 - [BasicInfo](docs/BasicInfo.md)
 - [BillingAddress](docs/BillingAddress.md)
 - [BillingInfo](docs/BillingInfo.md)
 - [ClientSecret](docs/ClientSecret.md)
 - [ConfirmSignUpWithAwsMarketplaceParam](docs/ConfirmSignUpWithAwsMarketplaceParam.md)
 - [CreateSaasUserParam](docs/CreateSaasUserParam.md)
 - [CreateSecretCodeParam](docs/CreateSecretCodeParam.md)
 - [CreateTenantUserParam](docs/CreateTenantUserParam.md)
 - [CreateTenantUserRolesParam](docs/CreateTenantUserRolesParam.md)
 - [Credentials](docs/Credentials.md)
 - [CustomizePageProps](docs/CustomizePageProps.md)
 - [CustomizePageSettings](docs/CustomizePageSettings.md)
 - [CustomizePageSettingsProps](docs/CustomizePageSettingsProps.md)
 - [CustomizePages](docs/CustomizePages.md)
 - [DeviceConfiguration](docs/DeviceConfiguration.md)
 - [DnsRecord](docs/DnsRecord.md)
 - [Env](docs/Env.md)
 - [Envs](docs/Envs.md)
 - [Error](docs/Error.md)
 - [IdentityProviderConfiguration](docs/IdentityProviderConfiguration.md)
 - [IdentityProviderProps](docs/IdentityProviderProps.md)
 - [IdentityProviders](docs/IdentityProviders.md)
 - [InvoiceLanguage](docs/InvoiceLanguage.md)
 - [LinkAwsMarketplaceParam](docs/LinkAwsMarketplaceParam.md)
 - [MessageTemplate](docs/MessageTemplate.md)
 - [MfaConfiguration](docs/MfaConfiguration.md)
 - [MfaPreference](docs/MfaPreference.md)
 - [NotificationMessages](docs/NotificationMessages.md)
 - [PasswordPolicy](docs/PasswordPolicy.md)
 - [PlanHistories](docs/PlanHistories.md)
 - [PlanHistory](docs/PlanHistory.md)
 - [PlanReservation](docs/PlanReservation.md)
 - [ProviderName](docs/ProviderName.md)
 - [RecaptchaProps](docs/RecaptchaProps.md)
 - [ResendSignUpConfirmationEmailParam](docs/ResendSignUpConfirmationEmailParam.md)
 - [Role](docs/Role.md)
 - [Roles](docs/Roles.md)
 - [SaasId](docs/SaasId.md)
 - [SaasUser](docs/SaasUser.md)
 - [SaasUsers](docs/SaasUsers.md)
 - [SelfRegist](docs/SelfRegist.md)
 - [SignInSettings](docs/SignInSettings.md)
 - [SignUpParam](docs/SignUpParam.md)
 - [SignUpWithAwsMarketplaceParam](docs/SignUpWithAwsMarketplaceParam.md)
 - [SoftwareTokenSecretCode](docs/SoftwareTokenSecretCode.md)
 - [Tenant](docs/Tenant.md)
 - [TenantAttributes](docs/TenantAttributes.md)
 - [TenantDetail](docs/TenantDetail.md)
 - [TenantProps](docs/TenantProps.md)
 - [Tenants](docs/Tenants.md)
 - [UpdateBasicInfoParam](docs/UpdateBasicInfoParam.md)
 - [UpdateCustomizePageSettingsParam](docs/UpdateCustomizePageSettingsParam.md)
 - [UpdateCustomizePagesParam](docs/UpdateCustomizePagesParam.md)
 - [UpdateEnvParam](docs/UpdateEnvParam.md)
 - [UpdateIdentityProviderParam](docs/UpdateIdentityProviderParam.md)
 - [UpdateNotificationMessagesParam](docs/UpdateNotificationMessagesParam.md)
 - [UpdateSaasUserEmailParam](docs/UpdateSaasUserEmailParam.md)
 - [UpdateSaasUserPasswordParam](docs/UpdateSaasUserPasswordParam.md)
 - [UpdateSignInSettingsParam](docs/UpdateSignInSettingsParam.md)
 - [UpdateSoftwareTokenParam](docs/UpdateSoftwareTokenParam.md)
 - [UpdateTenantUserParam](docs/UpdateTenantUserParam.md)
 - [User](docs/User.md)
 - [UserAttributes](docs/UserAttributes.md)
 - [UserAvailableEnv](docs/UserAvailableEnv.md)
 - [UserAvailableTenant](docs/UserAvailableTenant.md)
 - [UserInfo](docs/UserInfo.md)
 - [Users](docs/Users.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="Bearer"></a>
### Bearer

- **Type**: Bearer authentication


## Author

--- 

## 新しいモジュールの追加方法

例えばhogeモジュールを追加したい時

1. モジュールのymlファイルをsaasus_sdk_python直下に配置する
2. `generate.sh`のMODULESにモジュール名を追加する
```shell
MODULES=("auth" "pricing" "billing" "hoge")
```
3. `hoge_client.py`を`saasus_sdk_python/client`配下に作成する
   1. auth_client.pyはconfiguration.default_headersがなかったりして少し特殊なため**pricing_client.py**をコピーして作成するのが望ましい
   2. 適宜Client名を変更する
   3. hoge_client.pyを一部修正する
```python
   # このhost名を修正
    self.configuration.host = f"{self.base_url}/hoge"
```
4. 必要に応じてSDK呼び出し側のサンプル(__main__.py)も変更する
   



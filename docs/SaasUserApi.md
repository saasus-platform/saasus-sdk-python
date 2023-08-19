# saasus_sdk_python.SaasUserApi

All URIs are relative to *https://api.saasus.io/v1/auth*

Method | HTTP request | Description
------------- | ------------- | -------------
[**confirm_sign_up_with_aws_marketplace**](SaasUserApi.md#confirm_sign_up_with_aws_marketplace) | **POST** /aws-marketplace/sign-up-confirm | AWS Marketplaceによるユーザー新規登録の確定(Confirm Sign Up with AWS Marketplace)
[**create_saas_user**](SaasUserApi.md#create_saas_user) | **POST** /users | SaaSにユーザーを作成(Create SaaS User)
[**create_secret_code**](SaasUserApi.md#create_secret_code) | **POST** /users/{user_id}/mfa/software-token/secret-code | 認証アプリケーション登録用のシークレットコードを作成(Creates secret code for authentication application registration)
[**delete_saas_user**](SaasUserApi.md#delete_saas_user) | **DELETE** /users/{user_id} | ユーザー情報を削除(Delete User)
[**get_saas_user**](SaasUserApi.md#get_saas_user) | **GET** /users/{user_id} | ユーザー情報を取得(Get User)
[**get_saas_users**](SaasUserApi.md#get_saas_users) | **GET** /users | ユーザー一覧を取得(Get Users)
[**get_user_mfa_preference**](SaasUserApi.md#get_user_mfa_preference) | **GET** /users/{user_id}/mfa/preference | ユーザーのMFA設定を取得(Get User&#39;s MFA Settings)
[**link_aws_marketplace**](SaasUserApi.md#link_aws_marketplace) | **PATCH** /aws-marketplace/link | AWS Marketplaceと既存のテナントの連携(Link an existing tenant with AWS Marketplace)
[**resend_sign_up_confirmation_email**](SaasUserApi.md#resend_sign_up_confirmation_email) | **POST** /sign-up/resend | 新規登録時の確認メール再送信(Resend Sign Up Confirmation Email)
[**sign_up**](SaasUserApi.md#sign_up) | **POST** /sign-up | 新規登録(Sign Up)
[**sign_up_with_aws_marketplace**](SaasUserApi.md#sign_up_with_aws_marketplace) | **POST** /aws-marketplace/sign-up | AWS Marketplaceによるユーザー新規登録(Sign Up with AWS Marketplace)
[**unlink_provider**](SaasUserApi.md#unlink_provider) | **DELETE** /users/{user_id}/providers/{provider_name} | 外部IDプロバイダの連携解除(Unlink external identity providers)
[**update_saas_user_email**](SaasUserApi.md#update_saas_user_email) | **PATCH** /users/{user_id}/email | メールアドレスを変更(Change Email)
[**update_saas_user_password**](SaasUserApi.md#update_saas_user_password) | **PATCH** /users/{user_id}/password | パスワードを変更(Change Password)
[**update_software_token**](SaasUserApi.md#update_software_token) | **PUT** /users/{user_id}/mfa/software-token | 認証アプリケーションを登録(Register Authentication Application)
[**update_user_mfa_preference**](SaasUserApi.md#update_user_mfa_preference) | **PATCH** /users/{user_id}/mfa/preference | ユーザーのMFA設定を更新(Update User&#39;s MFA Settings)


# **confirm_sign_up_with_aws_marketplace**
> Tenant confirm_sign_up_with_aws_marketplace(confirm_sign_up_with_aws_marketplace_param=confirm_sign_up_with_aws_marketplace_param)

AWS Marketplaceによるユーザー新規登録の確定(Confirm Sign Up with AWS Marketplace)

AWS Marketplaceと連携したユーザー新規登録を確定します。AWS Marketplaceと連携したテナントを新規作成します。 Registration Tokenが有効でない場合はエラーを返却します。  Confirm a new use registeration linked to AWS Marketplace. Create a new tenant linked to AWS Marketplace. If the Registration Token is not valid, an error is returned. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python
from saasus_sdk_python.models.confirm_sign_up_with_aws_marketplace_param import ConfirmSignUpWithAwsMarketplaceParam
from saasus_sdk_python.models.tenant import Tenant
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
    api_instance = saasus_sdk_python.SaasUserApi(api_client)
    confirm_sign_up_with_aws_marketplace_param = saasus_sdk_python.ConfirmSignUpWithAwsMarketplaceParam() # ConfirmSignUpWithAwsMarketplaceParam |  (optional)

    try:
        # AWS Marketplaceによるユーザー新規登録の確定(Confirm Sign Up with AWS Marketplace)
        api_response = api_instance.confirm_sign_up_with_aws_marketplace(confirm_sign_up_with_aws_marketplace_param=confirm_sign_up_with_aws_marketplace_param)
        print("The response of SaasUserApi->confirm_sign_up_with_aws_marketplace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SaasUserApi->confirm_sign_up_with_aws_marketplace: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **confirm_sign_up_with_aws_marketplace_param** | [**ConfirmSignUpWithAwsMarketplaceParam**](ConfirmSignUpWithAwsMarketplaceParam.md)|  | [optional] 

### Return type

[**Tenant**](Tenant.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_saas_user**
> SaasUser create_saas_user(create_saas_user_param=create_saas_user_param)

SaaSにユーザーを作成(Create SaaS User)

SaaSにユーザーを作成します。  Create SaaS User. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python
from saasus_sdk_python.models.create_saas_user_param import CreateSaasUserParam
from saasus_sdk_python.models.saas_user import SaasUser
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
    api_instance = saasus_sdk_python.SaasUserApi(api_client)
    create_saas_user_param = saasus_sdk_python.CreateSaasUserParam() # CreateSaasUserParam |  (optional)

    try:
        # SaaSにユーザーを作成(Create SaaS User)
        api_response = api_instance.create_saas_user(create_saas_user_param=create_saas_user_param)
        print("The response of SaasUserApi->create_saas_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SaasUserApi->create_saas_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_saas_user_param** | [**CreateSaasUserParam**](CreateSaasUserParam.md)|  | [optional] 

### Return type

[**SaasUser**](SaasUser.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_secret_code**
> SoftwareTokenSecretCode create_secret_code(user_id, create_secret_code_param=create_secret_code_param)

認証アプリケーション登録用のシークレットコードを作成(Creates secret code for authentication application registration)

認証アプリケーション登録用のシークレットコードを作成します。  Create a secret code for authentication application registration. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python
from saasus_sdk_python.models.create_secret_code_param import CreateSecretCodeParam
from saasus_sdk_python.models.software_token_secret_code import SoftwareTokenSecretCode
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
    api_instance = saasus_sdk_python.SaasUserApi(api_client)
    user_id = 'f94bfffc-8be2-11ec-b41a-0242ac120004' # str | ユーザーID(User ID)
    create_secret_code_param = saasus_sdk_python.CreateSecretCodeParam() # CreateSecretCodeParam |  (optional)

    try:
        # 認証アプリケーション登録用のシークレットコードを作成(Creates secret code for authentication application registration)
        api_response = api_instance.create_secret_code(user_id, create_secret_code_param=create_secret_code_param)
        print("The response of SaasUserApi->create_secret_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SaasUserApi->create_secret_code: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ユーザーID(User ID) | 
 **create_secret_code_param** | [**CreateSecretCodeParam**](CreateSecretCodeParam.md)|  | [optional] 

### Return type

[**SoftwareTokenSecretCode**](SoftwareTokenSecretCode.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_saas_user**
> delete_saas_user(user_id)

ユーザー情報を削除(Delete User)

ユーザーIDを元に一致するユーザーをテナントからすべて削除し、SaaSからも削除します。  Delete all users with matching user ID from the tenant and SaaS. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
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
    api_instance = saasus_sdk_python.SaasUserApi(api_client)
    user_id = 'f94bfffc-8be2-11ec-b41a-0242ac120004' # str | ユーザーID(User ID)

    try:
        # ユーザー情報を削除(Delete User)
        api_instance.delete_saas_user(user_id)
    except Exception as e:
        print("Exception when calling SaasUserApi->delete_saas_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ユーザーID(User ID) | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_saas_user**
> SaasUser get_saas_user(user_id)

ユーザー情報を取得(Get User)

ユーザーIDからユーザー情報を取得します。  Get user information based on user ID. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python
from saasus_sdk_python.models.saas_user import SaasUser
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
    api_instance = saasus_sdk_python.SaasUserApi(api_client)
    user_id = 'f94bfffc-8be2-11ec-b41a-0242ac120004' # str | ユーザーID(User ID)

    try:
        # ユーザー情報を取得(Get User)
        api_response = api_instance.get_saas_user(user_id)
        print("The response of SaasUserApi->get_saas_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SaasUserApi->get_saas_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ユーザーID(User ID) | 

### Return type

[**SaasUser**](SaasUser.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_saas_users**
> SaasUsers get_saas_users()

ユーザー一覧を取得(Get Users)

SaaSのユーザー全件を取得します。  Get all SaaS users. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python
from saasus_sdk_python.models.saas_users import SaasUsers
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
    api_instance = saasus_sdk_python.SaasUserApi(api_client)

    try:
        # ユーザー一覧を取得(Get Users)
        api_response = api_instance.get_saas_users()
        print("The response of SaasUserApi->get_saas_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SaasUserApi->get_saas_users: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**SaasUsers**](SaasUsers.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_mfa_preference**
> MfaPreference get_user_mfa_preference(user_id)

ユーザーのMFA設定を取得(Get User's MFA Settings)

ユーザーのMFA設定を取得します。  Get the user's MFA settings. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python
from saasus_sdk_python.models.mfa_preference import MfaPreference
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
    api_instance = saasus_sdk_python.SaasUserApi(api_client)
    user_id = 'f94bfffc-8be2-11ec-b41a-0242ac120004' # str | ユーザーID(User ID)

    try:
        # ユーザーのMFA設定を取得(Get User's MFA Settings)
        api_response = api_instance.get_user_mfa_preference(user_id)
        print("The response of SaasUserApi->get_user_mfa_preference:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SaasUserApi->get_user_mfa_preference: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ユーザーID(User ID) | 

### Return type

[**MfaPreference**](MfaPreference.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_aws_marketplace**
> link_aws_marketplace(link_aws_marketplace_param=link_aws_marketplace_param)

AWS Marketplaceと既存のテナントの連携(Link an existing tenant with AWS Marketplace)

AWS Marketplaceと既存のテナントを連携します。 Registration Tokenが有効でない場合はエラーを返却します。  Link an existing tenant with AWS Marketplace. If the Registration Token is not valid, an error is returned. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python
from saasus_sdk_python.models.link_aws_marketplace_param import LinkAwsMarketplaceParam
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
    api_instance = saasus_sdk_python.SaasUserApi(api_client)
    link_aws_marketplace_param = saasus_sdk_python.LinkAwsMarketplaceParam() # LinkAwsMarketplaceParam |  (optional)

    try:
        # AWS Marketplaceと既存のテナントの連携(Link an existing tenant with AWS Marketplace)
        api_instance.link_aws_marketplace(link_aws_marketplace_param=link_aws_marketplace_param)
    except Exception as e:
        print("Exception when calling SaasUserApi->link_aws_marketplace: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **link_aws_marketplace_param** | [**LinkAwsMarketplaceParam**](LinkAwsMarketplaceParam.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resend_sign_up_confirmation_email**
> resend_sign_up_confirmation_email(resend_sign_up_confirmation_email_param=resend_sign_up_confirmation_email_param)

新規登録時の確認メール再送信(Resend Sign Up Confirmation Email)

新規登録時の仮パスワードを再送信します。  Resend temporary password for the new registered user. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python
from saasus_sdk_python.models.resend_sign_up_confirmation_email_param import ResendSignUpConfirmationEmailParam
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
    api_instance = saasus_sdk_python.SaasUserApi(api_client)
    resend_sign_up_confirmation_email_param = saasus_sdk_python.ResendSignUpConfirmationEmailParam() # ResendSignUpConfirmationEmailParam |  (optional)

    try:
        # 新規登録時の確認メール再送信(Resend Sign Up Confirmation Email)
        api_instance.resend_sign_up_confirmation_email(resend_sign_up_confirmation_email_param=resend_sign_up_confirmation_email_param)
    except Exception as e:
        print("Exception when calling SaasUserApi->resend_sign_up_confirmation_email: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resend_sign_up_confirmation_email_param** | [**ResendSignUpConfirmationEmailParam**](ResendSignUpConfirmationEmailParam.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sign_up**
> SaasUser sign_up(sign_up_param=sign_up_param)

新規登録(Sign Up)

ユーザーを新規登録します。登録されたメールアドレスに対して仮パスワードを送信します。  Register a new user. A temporary password will be sent to the registered email. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python
from saasus_sdk_python.models.saas_user import SaasUser
from saasus_sdk_python.models.sign_up_param import SignUpParam
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
    api_instance = saasus_sdk_python.SaasUserApi(api_client)
    sign_up_param = saasus_sdk_python.SignUpParam() # SignUpParam |  (optional)

    try:
        # 新規登録(Sign Up)
        api_response = api_instance.sign_up(sign_up_param=sign_up_param)
        print("The response of SaasUserApi->sign_up:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SaasUserApi->sign_up: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sign_up_param** | [**SignUpParam**](SignUpParam.md)|  | [optional] 

### Return type

[**SaasUser**](SaasUser.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sign_up_with_aws_marketplace**
> SaasUser sign_up_with_aws_marketplace(sign_up_with_aws_marketplace_param=sign_up_with_aws_marketplace_param)

AWS Marketplaceによるユーザー新規登録(Sign Up with AWS Marketplace)

AWS Marketplaceと連携したユーザーを新規登録します。登録されたメールアドレスに対して仮パスワードを送信します。 Registration Tokenが有効でない場合はエラーを返却します。  Register a new user linked to AWS Marketplace. A temporary password will be sent to the registered email. If the Registration Token is not valid, an error is returned. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python
from saasus_sdk_python.models.saas_user import SaasUser
from saasus_sdk_python.models.sign_up_with_aws_marketplace_param import SignUpWithAwsMarketplaceParam
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
    api_instance = saasus_sdk_python.SaasUserApi(api_client)
    sign_up_with_aws_marketplace_param = saasus_sdk_python.SignUpWithAwsMarketplaceParam() # SignUpWithAwsMarketplaceParam |  (optional)

    try:
        # AWS Marketplaceによるユーザー新規登録(Sign Up with AWS Marketplace)
        api_response = api_instance.sign_up_with_aws_marketplace(sign_up_with_aws_marketplace_param=sign_up_with_aws_marketplace_param)
        print("The response of SaasUserApi->sign_up_with_aws_marketplace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SaasUserApi->sign_up_with_aws_marketplace: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sign_up_with_aws_marketplace_param** | [**SignUpWithAwsMarketplaceParam**](SignUpWithAwsMarketplaceParam.md)|  | [optional] 

### Return type

[**SaasUser**](SaasUser.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unlink_provider**
> unlink_provider(provider_name, user_id)

外部IDプロバイダの連携解除(Unlink external identity providers)

外部IDプロバイダの連携を解除します。  Unlink external identity providers. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
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
    api_instance = saasus_sdk_python.SaasUserApi(api_client)
    provider_name = 'Google' # str | 
    user_id = 'f94bfffc-8be2-11ec-b41a-0242ac120004' # str | ユーザーID(User ID)

    try:
        # 外部IDプロバイダの連携解除(Unlink external identity providers)
        api_instance.unlink_provider(provider_name, user_id)
    except Exception as e:
        print("Exception when calling SaasUserApi->unlink_provider: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_name** | **str**|  | 
 **user_id** | **str**| ユーザーID(User ID) | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_saas_user_email**
> update_saas_user_email(user_id, update_saas_user_email_param=update_saas_user_email_param)

メールアドレスを変更(Change Email)

ユーザーのメールアドレスを変更します。  Change user's email. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python
from saasus_sdk_python.models.update_saas_user_email_param import UpdateSaasUserEmailParam
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
    api_instance = saasus_sdk_python.SaasUserApi(api_client)
    user_id = 'f94bfffc-8be2-11ec-b41a-0242ac120004' # str | ユーザーID(User ID)
    update_saas_user_email_param = saasus_sdk_python.UpdateSaasUserEmailParam() # UpdateSaasUserEmailParam |  (optional)

    try:
        # メールアドレスを変更(Change Email)
        api_instance.update_saas_user_email(user_id, update_saas_user_email_param=update_saas_user_email_param)
    except Exception as e:
        print("Exception when calling SaasUserApi->update_saas_user_email: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ユーザーID(User ID) | 
 **update_saas_user_email_param** | [**UpdateSaasUserEmailParam**](UpdateSaasUserEmailParam.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_saas_user_password**
> update_saas_user_password(user_id, update_saas_user_password_param=update_saas_user_password_param)

パスワードを変更(Change Password)

ユーザーのログインパスワードを変更します。  Change user's login password. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python
from saasus_sdk_python.models.update_saas_user_password_param import UpdateSaasUserPasswordParam
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
    api_instance = saasus_sdk_python.SaasUserApi(api_client)
    user_id = 'f94bfffc-8be2-11ec-b41a-0242ac120004' # str | ユーザーID(User ID)
    update_saas_user_password_param = saasus_sdk_python.UpdateSaasUserPasswordParam() # UpdateSaasUserPasswordParam |  (optional)

    try:
        # パスワードを変更(Change Password)
        api_instance.update_saas_user_password(user_id, update_saas_user_password_param=update_saas_user_password_param)
    except Exception as e:
        print("Exception when calling SaasUserApi->update_saas_user_password: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ユーザーID(User ID) | 
 **update_saas_user_password_param** | [**UpdateSaasUserPasswordParam**](UpdateSaasUserPasswordParam.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_software_token**
> update_software_token(user_id, update_software_token_param=update_software_token_param)

認証アプリケーションを登録(Register Authentication Application)

認証アプリケーションを登録します。  Register an authentication application. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python
from saasus_sdk_python.models.update_software_token_param import UpdateSoftwareTokenParam
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
    api_instance = saasus_sdk_python.SaasUserApi(api_client)
    user_id = 'f94bfffc-8be2-11ec-b41a-0242ac120004' # str | ユーザーID(User ID)
    update_software_token_param = saasus_sdk_python.UpdateSoftwareTokenParam() # UpdateSoftwareTokenParam |  (optional)

    try:
        # 認証アプリケーションを登録(Register Authentication Application)
        api_instance.update_software_token(user_id, update_software_token_param=update_software_token_param)
    except Exception as e:
        print("Exception when calling SaasUserApi->update_software_token: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ユーザーID(User ID) | 
 **update_software_token_param** | [**UpdateSoftwareTokenParam**](UpdateSoftwareTokenParam.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_mfa_preference**
> update_user_mfa_preference(user_id, body=body)

ユーザーのMFA設定を更新(Update User's MFA Settings)

ユーザーのMFA設定を更新します。  Update user's MFA settings. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python
from saasus_sdk_python.models.mfa_preference import MfaPreference
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
    api_instance = saasus_sdk_python.SaasUserApi(api_client)
    user_id = 'f94bfffc-8be2-11ec-b41a-0242ac120004' # str | ユーザーID(User ID)
    body = saasus_sdk_python.MfaPreference() # MfaPreference |  (optional)

    try:
        # ユーザーのMFA設定を更新(Update User's MFA Settings)
        api_instance.update_user_mfa_preference(user_id, body=body)
    except Exception as e:
        print("Exception when calling SaasUserApi->update_user_mfa_preference: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ユーザーID(User ID) | 
 **body** | **MfaPreference**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


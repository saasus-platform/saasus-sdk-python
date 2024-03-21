# saasus_sdk_python.src.auth.SaasUserApi

All URIs are relative to *https://api.saasus.io/v1/auth*

Method | HTTP request | Description
------------- | ------------- | -------------
[**confirm_email_update**](SaasUserApi.md#confirm_email_update) | **POST** /users/{user_id}/email/confirm | Confirm User Email Update
[**confirm_external_user_link**](SaasUserApi.md#confirm_external_user_link) | **POST** /external-users/confirm | Confirm External User Account Link
[**confirm_sign_up_with_aws_marketplace**](SaasUserApi.md#confirm_sign_up_with_aws_marketplace) | **POST** /aws-marketplace/sign-up-confirm | Confirm Sign Up with AWS Marketplace
[**create_saas_user**](SaasUserApi.md#create_saas_user) | **POST** /users | Create SaaS User
[**create_secret_code**](SaasUserApi.md#create_secret_code) | **POST** /users/{user_id}/mfa/software-token/secret-code | Create secret code for authentication application registration
[**delete_saas_user**](SaasUserApi.md#delete_saas_user) | **DELETE** /users/{user_id} | Delete User
[**get_saas_user**](SaasUserApi.md#get_saas_user) | **GET** /users/{user_id} | Get User
[**get_saas_users**](SaasUserApi.md#get_saas_users) | **GET** /users | Get Users
[**get_user_mfa_preference**](SaasUserApi.md#get_user_mfa_preference) | **GET** /users/{user_id}/mfa/preference | Get User&#39;s MFA Settings
[**link_aws_marketplace**](SaasUserApi.md#link_aws_marketplace) | **PATCH** /aws-marketplace/link | Link an existing tenant with AWS Marketplace
[**request_email_update**](SaasUserApi.md#request_email_update) | **POST** /users/{user_id}/email/request | Request User Email Update
[**request_external_user_link**](SaasUserApi.md#request_external_user_link) | **POST** /external-users/request | Request External User Account Link
[**resend_sign_up_confirmation_email**](SaasUserApi.md#resend_sign_up_confirmation_email) | **POST** /sign-up/resend | Resend Sign Up Confirmation Email
[**sign_up**](SaasUserApi.md#sign_up) | **POST** /sign-up | Sign Up
[**sign_up_with_aws_marketplace**](SaasUserApi.md#sign_up_with_aws_marketplace) | **POST** /aws-marketplace/sign-up | Sign Up with AWS Marketplace
[**unlink_provider**](SaasUserApi.md#unlink_provider) | **DELETE** /users/{user_id}/providers/{provider_name} | Unlink external identity providers
[**update_saas_user_email**](SaasUserApi.md#update_saas_user_email) | **PATCH** /users/{user_id}/email | Change Email
[**update_saas_user_password**](SaasUserApi.md#update_saas_user_password) | **PATCH** /users/{user_id}/password | Change Password
[**update_software_token**](SaasUserApi.md#update_software_token) | **PUT** /users/{user_id}/mfa/software-token | Register Authentication Application
[**update_user_mfa_preference**](SaasUserApi.md#update_user_mfa_preference) | **PATCH** /users/{user_id}/mfa/preference | Update User&#39;s MFA Settings


# **confirm_email_update**
> confirm_email_update(user_id, confirm_email_update_param=confirm_email_update_param)

Confirm User Email Update

Verify the code to confirm the user's email address update. Requires the user's access token. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.auth
from saasus_sdk_python.src.auth.models.confirm_email_update_param import ConfirmEmailUpdateParam
from saasus_sdk_python.src.auth.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.saasus.io/v1/auth
# See configuration.py for a list of all supported configuration parameters.
configuration = saasus_sdk_python.src.auth.Configuration(
    host = "https://api.saasus.io/v1/auth"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = saasus_sdk_python.src.auth.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with saasus_sdk_python.src.auth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = saasus_sdk_python.src.auth.SaasUserApi(api_client)
    user_id = 'f94bfffc-8be2-11ec-b41a-0242ac120004' # str | User ID
    confirm_email_update_param = saasus_sdk_python.src.auth.ConfirmEmailUpdateParam() # ConfirmEmailUpdateParam |  (optional)

    try:
        # Confirm User Email Update
        api_instance.confirm_email_update(user_id, confirm_email_update_param=confirm_email_update_param)
    except Exception as e:
        print("Exception when calling SaasUserApi->confirm_email_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User ID | 
 **confirm_email_update_param** | [**ConfirmEmailUpdateParam**](ConfirmEmailUpdateParam.md)|  | [optional] 

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

# **confirm_external_user_link**
> confirm_external_user_link(confirm_external_user_link_param=confirm_external_user_link_param)

Confirm External User Account Link

Verify the code for external account user link confirmation. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.auth
from saasus_sdk_python.src.auth.models.confirm_external_user_link_param import ConfirmExternalUserLinkParam
from saasus_sdk_python.src.auth.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.saasus.io/v1/auth
# See configuration.py for a list of all supported configuration parameters.
configuration = saasus_sdk_python.src.auth.Configuration(
    host = "https://api.saasus.io/v1/auth"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = saasus_sdk_python.src.auth.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with saasus_sdk_python.src.auth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = saasus_sdk_python.src.auth.SaasUserApi(api_client)
    confirm_external_user_link_param = saasus_sdk_python.src.auth.ConfirmExternalUserLinkParam() # ConfirmExternalUserLinkParam |  (optional)

    try:
        # Confirm External User Account Link
        api_instance.confirm_external_user_link(confirm_external_user_link_param=confirm_external_user_link_param)
    except Exception as e:
        print("Exception when calling SaasUserApi->confirm_external_user_link: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **confirm_external_user_link_param** | [**ConfirmExternalUserLinkParam**](ConfirmExternalUserLinkParam.md)|  | [optional] 

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
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **confirm_sign_up_with_aws_marketplace**
> Tenant confirm_sign_up_with_aws_marketplace(confirm_sign_up_with_aws_marketplace_param=confirm_sign_up_with_aws_marketplace_param)

Confirm Sign Up with AWS Marketplace

Confirm a new use registeration linked to AWS Marketplace. Create a new tenant linked to AWS Marketplace. If the Registration Token is not valid, an error is returned. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.auth
from saasus_sdk_python.src.auth.models.confirm_sign_up_with_aws_marketplace_param import ConfirmSignUpWithAwsMarketplaceParam
from saasus_sdk_python.src.auth.models.tenant import Tenant
from saasus_sdk_python.src.auth.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.saasus.io/v1/auth
# See configuration.py for a list of all supported configuration parameters.
configuration = saasus_sdk_python.src.auth.Configuration(
    host = "https://api.saasus.io/v1/auth"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = saasus_sdk_python.src.auth.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with saasus_sdk_python.src.auth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = saasus_sdk_python.src.auth.SaasUserApi(api_client)
    confirm_sign_up_with_aws_marketplace_param = saasus_sdk_python.src.auth.ConfirmSignUpWithAwsMarketplaceParam() # ConfirmSignUpWithAwsMarketplaceParam |  (optional)

    try:
        # Confirm Sign Up with AWS Marketplace
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

Create SaaS User

Create SaaS User. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.auth
from saasus_sdk_python.src.auth.models.create_saas_user_param import CreateSaasUserParam
from saasus_sdk_python.src.auth.models.saas_user import SaasUser
from saasus_sdk_python.src.auth.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.saasus.io/v1/auth
# See configuration.py for a list of all supported configuration parameters.
configuration = saasus_sdk_python.src.auth.Configuration(
    host = "https://api.saasus.io/v1/auth"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = saasus_sdk_python.src.auth.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with saasus_sdk_python.src.auth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = saasus_sdk_python.src.auth.SaasUserApi(api_client)
    create_saas_user_param = saasus_sdk_python.src.auth.CreateSaasUserParam() # CreateSaasUserParam |  (optional)

    try:
        # Create SaaS User
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

Create secret code for authentication application registration

Create a secret code for authentication application registration. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.auth
from saasus_sdk_python.src.auth.models.create_secret_code_param import CreateSecretCodeParam
from saasus_sdk_python.src.auth.models.software_token_secret_code import SoftwareTokenSecretCode
from saasus_sdk_python.src.auth.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.saasus.io/v1/auth
# See configuration.py for a list of all supported configuration parameters.
configuration = saasus_sdk_python.src.auth.Configuration(
    host = "https://api.saasus.io/v1/auth"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = saasus_sdk_python.src.auth.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with saasus_sdk_python.src.auth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = saasus_sdk_python.src.auth.SaasUserApi(api_client)
    user_id = 'f94bfffc-8be2-11ec-b41a-0242ac120004' # str | User ID
    create_secret_code_param = saasus_sdk_python.src.auth.CreateSecretCodeParam() # CreateSecretCodeParam |  (optional)

    try:
        # Create secret code for authentication application registration
        api_response = api_instance.create_secret_code(user_id, create_secret_code_param=create_secret_code_param)
        print("The response of SaasUserApi->create_secret_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SaasUserApi->create_secret_code: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User ID | 
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

Delete User

Delete all users with matching user ID from the tenant and SaaS. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.auth
from saasus_sdk_python.src.auth.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.saasus.io/v1/auth
# See configuration.py for a list of all supported configuration parameters.
configuration = saasus_sdk_python.src.auth.Configuration(
    host = "https://api.saasus.io/v1/auth"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = saasus_sdk_python.src.auth.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with saasus_sdk_python.src.auth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = saasus_sdk_python.src.auth.SaasUserApi(api_client)
    user_id = 'f94bfffc-8be2-11ec-b41a-0242ac120004' # str | User ID

    try:
        # Delete User
        api_instance.delete_saas_user(user_id)
    except Exception as e:
        print("Exception when calling SaasUserApi->delete_saas_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User ID | 

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

Get User

Get user information based on user ID. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.auth
from saasus_sdk_python.src.auth.models.saas_user import SaasUser
from saasus_sdk_python.src.auth.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.saasus.io/v1/auth
# See configuration.py for a list of all supported configuration parameters.
configuration = saasus_sdk_python.src.auth.Configuration(
    host = "https://api.saasus.io/v1/auth"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = saasus_sdk_python.src.auth.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with saasus_sdk_python.src.auth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = saasus_sdk_python.src.auth.SaasUserApi(api_client)
    user_id = 'f94bfffc-8be2-11ec-b41a-0242ac120004' # str | User ID

    try:
        # Get User
        api_response = api_instance.get_saas_user(user_id)
        print("The response of SaasUserApi->get_saas_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SaasUserApi->get_saas_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User ID | 

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

Get Users

Get all SaaS users. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.auth
from saasus_sdk_python.src.auth.models.saas_users import SaasUsers
from saasus_sdk_python.src.auth.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.saasus.io/v1/auth
# See configuration.py for a list of all supported configuration parameters.
configuration = saasus_sdk_python.src.auth.Configuration(
    host = "https://api.saasus.io/v1/auth"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = saasus_sdk_python.src.auth.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with saasus_sdk_python.src.auth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = saasus_sdk_python.src.auth.SaasUserApi(api_client)

    try:
        # Get Users
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

Get User's MFA Settings

Get the user's MFA settings. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.auth
from saasus_sdk_python.src.auth.models.mfa_preference import MfaPreference
from saasus_sdk_python.src.auth.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.saasus.io/v1/auth
# See configuration.py for a list of all supported configuration parameters.
configuration = saasus_sdk_python.src.auth.Configuration(
    host = "https://api.saasus.io/v1/auth"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = saasus_sdk_python.src.auth.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with saasus_sdk_python.src.auth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = saasus_sdk_python.src.auth.SaasUserApi(api_client)
    user_id = 'f94bfffc-8be2-11ec-b41a-0242ac120004' # str | User ID

    try:
        # Get User's MFA Settings
        api_response = api_instance.get_user_mfa_preference(user_id)
        print("The response of SaasUserApi->get_user_mfa_preference:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SaasUserApi->get_user_mfa_preference: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User ID | 

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

Link an existing tenant with AWS Marketplace

Link an existing tenant with AWS Marketplace. If the Registration Token is not valid, an error is returned. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.auth
from saasus_sdk_python.src.auth.models.link_aws_marketplace_param import LinkAwsMarketplaceParam
from saasus_sdk_python.src.auth.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.saasus.io/v1/auth
# See configuration.py for a list of all supported configuration parameters.
configuration = saasus_sdk_python.src.auth.Configuration(
    host = "https://api.saasus.io/v1/auth"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = saasus_sdk_python.src.auth.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with saasus_sdk_python.src.auth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = saasus_sdk_python.src.auth.SaasUserApi(api_client)
    link_aws_marketplace_param = saasus_sdk_python.src.auth.LinkAwsMarketplaceParam() # LinkAwsMarketplaceParam |  (optional)

    try:
        # Link an existing tenant with AWS Marketplace
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

# **request_email_update**
> request_email_update(user_id, request_email_update_param=request_email_update_param)

Request User Email Update

Request to update the user's email address. Sends a verification code to the requested email address. Requires the user's access token. The verification code is valid for 24 hours. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.auth
from saasus_sdk_python.src.auth.models.request_email_update_param import RequestEmailUpdateParam
from saasus_sdk_python.src.auth.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.saasus.io/v1/auth
# See configuration.py for a list of all supported configuration parameters.
configuration = saasus_sdk_python.src.auth.Configuration(
    host = "https://api.saasus.io/v1/auth"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = saasus_sdk_python.src.auth.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with saasus_sdk_python.src.auth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = saasus_sdk_python.src.auth.SaasUserApi(api_client)
    user_id = 'f94bfffc-8be2-11ec-b41a-0242ac120004' # str | User ID
    request_email_update_param = saasus_sdk_python.src.auth.RequestEmailUpdateParam() # RequestEmailUpdateParam |  (optional)

    try:
        # Request User Email Update
        api_instance.request_email_update(user_id, request_email_update_param=request_email_update_param)
    except Exception as e:
        print("Exception when calling SaasUserApi->request_email_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User ID | 
 **request_email_update_param** | [**RequestEmailUpdateParam**](RequestEmailUpdateParam.md)|  | [optional] 

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

# **request_external_user_link**
> request_external_user_link(request_external_user_link_param=request_external_user_link_param)

Request External User Account Link

Request to link an external account user. Get the email address of the user to be linked from the access token and send a verification code to that email address. The verification code is valid for 24 hours. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.auth
from saasus_sdk_python.src.auth.models.request_external_user_link_param import RequestExternalUserLinkParam
from saasus_sdk_python.src.auth.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.saasus.io/v1/auth
# See configuration.py for a list of all supported configuration parameters.
configuration = saasus_sdk_python.src.auth.Configuration(
    host = "https://api.saasus.io/v1/auth"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = saasus_sdk_python.src.auth.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with saasus_sdk_python.src.auth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = saasus_sdk_python.src.auth.SaasUserApi(api_client)
    request_external_user_link_param = saasus_sdk_python.src.auth.RequestExternalUserLinkParam() # RequestExternalUserLinkParam |  (optional)

    try:
        # Request External User Account Link
        api_instance.request_external_user_link(request_external_user_link_param=request_external_user_link_param)
    except Exception as e:
        print("Exception when calling SaasUserApi->request_external_user_link: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_external_user_link_param** | [**RequestExternalUserLinkParam**](RequestExternalUserLinkParam.md)|  | [optional] 

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
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resend_sign_up_confirmation_email**
> resend_sign_up_confirmation_email(resend_sign_up_confirmation_email_param=resend_sign_up_confirmation_email_param)

Resend Sign Up Confirmation Email

Resend temporary password for the new registered user. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.auth
from saasus_sdk_python.src.auth.models.resend_sign_up_confirmation_email_param import ResendSignUpConfirmationEmailParam
from saasus_sdk_python.src.auth.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.saasus.io/v1/auth
# See configuration.py for a list of all supported configuration parameters.
configuration = saasus_sdk_python.src.auth.Configuration(
    host = "https://api.saasus.io/v1/auth"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = saasus_sdk_python.src.auth.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with saasus_sdk_python.src.auth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = saasus_sdk_python.src.auth.SaasUserApi(api_client)
    resend_sign_up_confirmation_email_param = saasus_sdk_python.src.auth.ResendSignUpConfirmationEmailParam() # ResendSignUpConfirmationEmailParam |  (optional)

    try:
        # Resend Sign Up Confirmation Email
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

Sign Up

Register a new user. A temporary password will be sent to the registered email. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.auth
from saasus_sdk_python.src.auth.models.saas_user import SaasUser
from saasus_sdk_python.src.auth.models.sign_up_param import SignUpParam
from saasus_sdk_python.src.auth.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.saasus.io/v1/auth
# See configuration.py for a list of all supported configuration parameters.
configuration = saasus_sdk_python.src.auth.Configuration(
    host = "https://api.saasus.io/v1/auth"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = saasus_sdk_python.src.auth.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with saasus_sdk_python.src.auth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = saasus_sdk_python.src.auth.SaasUserApi(api_client)
    sign_up_param = saasus_sdk_python.src.auth.SignUpParam() # SignUpParam |  (optional)

    try:
        # Sign Up
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

Sign Up with AWS Marketplace

Register a new user linked to AWS Marketplace. A temporary password will be sent to the registered email. If the Registration Token is not valid, an error is returned. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.auth
from saasus_sdk_python.src.auth.models.saas_user import SaasUser
from saasus_sdk_python.src.auth.models.sign_up_with_aws_marketplace_param import SignUpWithAwsMarketplaceParam
from saasus_sdk_python.src.auth.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.saasus.io/v1/auth
# See configuration.py for a list of all supported configuration parameters.
configuration = saasus_sdk_python.src.auth.Configuration(
    host = "https://api.saasus.io/v1/auth"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = saasus_sdk_python.src.auth.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with saasus_sdk_python.src.auth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = saasus_sdk_python.src.auth.SaasUserApi(api_client)
    sign_up_with_aws_marketplace_param = saasus_sdk_python.src.auth.SignUpWithAwsMarketplaceParam() # SignUpWithAwsMarketplaceParam |  (optional)

    try:
        # Sign Up with AWS Marketplace
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

Unlink external identity providers

Unlink external identity providers. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.auth
from saasus_sdk_python.src.auth.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.saasus.io/v1/auth
# See configuration.py for a list of all supported configuration parameters.
configuration = saasus_sdk_python.src.auth.Configuration(
    host = "https://api.saasus.io/v1/auth"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = saasus_sdk_python.src.auth.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with saasus_sdk_python.src.auth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = saasus_sdk_python.src.auth.SaasUserApi(api_client)
    provider_name = 'Google' # str | 
    user_id = 'f94bfffc-8be2-11ec-b41a-0242ac120004' # str | User ID

    try:
        # Unlink external identity providers
        api_instance.unlink_provider(provider_name, user_id)
    except Exception as e:
        print("Exception when calling SaasUserApi->unlink_provider: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_name** | **str**|  | 
 **user_id** | **str**| User ID | 

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_saas_user_email**
> update_saas_user_email(user_id, update_saas_user_email_param=update_saas_user_email_param)

Change Email

Change user's email. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.auth
from saasus_sdk_python.src.auth.models.update_saas_user_email_param import UpdateSaasUserEmailParam
from saasus_sdk_python.src.auth.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.saasus.io/v1/auth
# See configuration.py for a list of all supported configuration parameters.
configuration = saasus_sdk_python.src.auth.Configuration(
    host = "https://api.saasus.io/v1/auth"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = saasus_sdk_python.src.auth.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with saasus_sdk_python.src.auth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = saasus_sdk_python.src.auth.SaasUserApi(api_client)
    user_id = 'f94bfffc-8be2-11ec-b41a-0242ac120004' # str | User ID
    update_saas_user_email_param = saasus_sdk_python.src.auth.UpdateSaasUserEmailParam() # UpdateSaasUserEmailParam |  (optional)

    try:
        # Change Email
        api_instance.update_saas_user_email(user_id, update_saas_user_email_param=update_saas_user_email_param)
    except Exception as e:
        print("Exception when calling SaasUserApi->update_saas_user_email: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User ID | 
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

Change Password

Change user's login password. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.auth
from saasus_sdk_python.src.auth.models.update_saas_user_password_param import UpdateSaasUserPasswordParam
from saasus_sdk_python.src.auth.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.saasus.io/v1/auth
# See configuration.py for a list of all supported configuration parameters.
configuration = saasus_sdk_python.src.auth.Configuration(
    host = "https://api.saasus.io/v1/auth"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = saasus_sdk_python.src.auth.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with saasus_sdk_python.src.auth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = saasus_sdk_python.src.auth.SaasUserApi(api_client)
    user_id = 'f94bfffc-8be2-11ec-b41a-0242ac120004' # str | User ID
    update_saas_user_password_param = saasus_sdk_python.src.auth.UpdateSaasUserPasswordParam() # UpdateSaasUserPasswordParam |  (optional)

    try:
        # Change Password
        api_instance.update_saas_user_password(user_id, update_saas_user_password_param=update_saas_user_password_param)
    except Exception as e:
        print("Exception when calling SaasUserApi->update_saas_user_password: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User ID | 
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

Register Authentication Application

Register an authentication application. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.auth
from saasus_sdk_python.src.auth.models.update_software_token_param import UpdateSoftwareTokenParam
from saasus_sdk_python.src.auth.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.saasus.io/v1/auth
# See configuration.py for a list of all supported configuration parameters.
configuration = saasus_sdk_python.src.auth.Configuration(
    host = "https://api.saasus.io/v1/auth"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = saasus_sdk_python.src.auth.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with saasus_sdk_python.src.auth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = saasus_sdk_python.src.auth.SaasUserApi(api_client)
    user_id = 'f94bfffc-8be2-11ec-b41a-0242ac120004' # str | User ID
    update_software_token_param = saasus_sdk_python.src.auth.UpdateSoftwareTokenParam() # UpdateSoftwareTokenParam |  (optional)

    try:
        # Register Authentication Application
        api_instance.update_software_token(user_id, update_software_token_param=update_software_token_param)
    except Exception as e:
        print("Exception when calling SaasUserApi->update_software_token: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User ID | 
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

Update User's MFA Settings

Update user's MFA settings. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.auth
from saasus_sdk_python.src.auth.models.mfa_preference import MfaPreference
from saasus_sdk_python.src.auth.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.saasus.io/v1/auth
# See configuration.py for a list of all supported configuration parameters.
configuration = saasus_sdk_python.src.auth.Configuration(
    host = "https://api.saasus.io/v1/auth"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = saasus_sdk_python.src.auth.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with saasus_sdk_python.src.auth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = saasus_sdk_python.src.auth.SaasUserApi(api_client)
    user_id = 'f94bfffc-8be2-11ec-b41a-0242ac120004' # str | User ID
    body = saasus_sdk_python.src.auth.MfaPreference() # MfaPreference |  (optional)

    try:
        # Update User's MFA Settings
        api_instance.update_user_mfa_preference(user_id, body=body)
    except Exception as e:
        print("Exception when calling SaasUserApi->update_user_mfa_preference: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User ID | 
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


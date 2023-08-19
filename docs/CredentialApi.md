# saasus_sdk_python.CredentialApi

All URIs are relative to *https://api.saasus.io/v1/auth*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_auth_credentials**](CredentialApi.md#create_auth_credentials) | **POST** /credentials | 認証・認可情報の保存(Save Authentication/Authorization Information)
[**get_auth_credentials**](CredentialApi.md#get_auth_credentials) | **GET** /credentials | 認証・認可情報の取得(Get Authentication/Authorization Information)


# **create_auth_credentials**
> AuthorizationTempCode create_auth_credentials(body=body)

認証・認可情報の保存(Save Authentication/Authorization Information)

引数のIDトークン・アクセストークン・リフレッシュトークンを一時保存し取得用の一時コードを返却する。 一時コードの有効期間は発行から10秒です。  Temporarily save the parameter for the ID token, access token, and refresh token and return a temporary code for obtaining. Temporary codes are valid for 10 seconds from issuance. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python
from saasus_sdk_python.models.authorization_temp_code import AuthorizationTempCode
from saasus_sdk_python.models.credentials import Credentials
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
    api_instance = saasus_sdk_python.CredentialApi(api_client)
    body = saasus_sdk_python.Credentials() # Credentials |  (optional)

    try:
        # 認証・認可情報の保存(Save Authentication/Authorization Information)
        api_response = api_instance.create_auth_credentials(body=body)
        print("The response of CredentialApi->create_auth_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialApi->create_auth_credentials: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Credentials**|  | [optional] 

### Return type

[**AuthorizationTempCode**](AuthorizationTempCode.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auth_credentials**
> Credentials get_auth_credentials(code=code, auth_flow=auth_flow, refresh_token=refresh_token)

認証・認可情報の取得(Get Authentication/Authorization Information)

一時コードまたはリフレッシュトークンを利用してIDトークン・アクセストークン・リフレッシュトークンを取得する。  Get ID token, access token, and refresh token using a temporary code or a refresh token. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python
from saasus_sdk_python.models.credentials import Credentials
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
    api_instance = saasus_sdk_python.CredentialApi(api_client)
    code = 'code_example' # str | 一時コード(Temp Code) (optional)
    auth_flow = 'auth_flow_example' # str | 認証フロー（Authentication Flow） tempCodeAuth: 一時コードを利用した認証情報の取得 refreshTokenAuth: リフレッシュトークンを利用した認証情報の取得 指定されていない場合は tempCodeAuth になります  (optional)
    refresh_token = 'refresh_token_example' # str | リフレッシュトークン(Refresh Token) (optional)

    try:
        # 認証・認可情報の取得(Get Authentication/Authorization Information)
        api_response = api_instance.get_auth_credentials(code=code, auth_flow=auth_flow, refresh_token=refresh_token)
        print("The response of CredentialApi->get_auth_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialApi->get_auth_credentials: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| 一時コード(Temp Code) | [optional] 
 **auth_flow** | **str**| 認証フロー（Authentication Flow） tempCodeAuth: 一時コードを利用した認証情報の取得 refreshTokenAuth: リフレッシュトークンを利用した認証情報の取得 指定されていない場合は tempCodeAuth になります  | [optional] 
 **refresh_token** | **str**| リフレッシュトークン(Refresh Token) | [optional] 

### Return type

[**Credentials**](Credentials.md)

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


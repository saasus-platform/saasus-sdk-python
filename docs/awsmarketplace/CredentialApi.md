# saasus_sdk_python.src.auth.CredentialApi

All URIs are relative to *https://api.saasus.io/v1/auth*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_auth_credentials**](CredentialApi.md#create_auth_credentials) | **POST** /credentials | Save Authentication/Authorization Information
[**get_auth_credentials**](CredentialApi.md#get_auth_credentials) | **GET** /credentials | Get Authentication/Authorization Information


# **create_auth_credentials**
> AuthorizationTempCode create_auth_credentials(body=body)

Save Authentication/Authorization Information

Temporarily save the parameter for the ID token, access token, and refresh token and return a temporary code for obtaining. Temporary codes are valid for 10 seconds from issuance. 

### Example

* Bearer Authentication (Bearer):

```python
import time
import os
import saasus_sdk_python.src.auth
from saasus_sdk_python.src.auth.models.authorization_temp_code import AuthorizationTempCode
from saasus_sdk_python.src.auth.models.credentials import Credentials
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
    api_instance = saasus_sdk_python.src.auth.CredentialApi(api_client)
    body = saasus_sdk_python.src.auth.Credentials() # Credentials |  (optional)

    try:
        # Save Authentication/Authorization Information
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

Get Authentication/Authorization Information

Get ID token, access token, and refresh token using a temporary code or a refresh token. 

### Example

* Bearer Authentication (Bearer):

```python
import time
import os
import saasus_sdk_python.src.auth
from saasus_sdk_python.src.auth.models.credentials import Credentials
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
    api_instance = saasus_sdk_python.src.auth.CredentialApi(api_client)
    code = 'code_example' # str | Temp Code (optional)
    auth_flow = 'auth_flow_example' # str | Authentication Flow tempCodeAuth: Getting authentication information using a temporary code refreshTokenAuth: Getting authentication information using a refresh token If not specified, it will be tempCodeAuth  (optional)
    refresh_token = 'refresh_token_example' # str | Refresh Token (optional)

    try:
        # Get Authentication/Authorization Information
        api_response = api_instance.get_auth_credentials(code=code, auth_flow=auth_flow, refresh_token=refresh_token)
        print("The response of CredentialApi->get_auth_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialApi->get_auth_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| Temp Code | [optional] 
 **auth_flow** | **str**| Authentication Flow tempCodeAuth: Getting authentication information using a temporary code refreshTokenAuth: Getting authentication information using a refresh token If not specified, it will be tempCodeAuth  | [optional] 
 **refresh_token** | **str**| Refresh Token | [optional] 

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


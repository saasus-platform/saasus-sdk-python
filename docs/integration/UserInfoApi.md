# saasus_sdk_python.src.auth.UserInfoApi

All URIs are relative to *https://api.saasus.io/v1/auth*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user_info**](UserInfoApi.md#get_user_info) | **GET** /userinfo | Get User Info
[**get_user_info_by_email**](UserInfoApi.md#get_user_info_by_email) | **GET** /userinfo/search/email | Get User Info by Email


# **get_user_info**
> UserInfo get_user_info(token)

Get User Info

User information is obtained based on the ID token of the SaaS user (registered user). The ID token is passed to the Callback URL during login from the SaaSus Platform generated login screen. User information can be obtained from calling this API with an ID token from the URL on the server side. Since the acquired tenant, role (role), price plan, etc. are included, it is possible to implement authorization based on it. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.auth
from saasus_sdk_python.src.auth.models.user_info import UserInfo
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
    api_instance = saasus_sdk_python.src.auth.UserInfoApi(api_client)
    token = 'token_example' # str | ID Token

    try:
        # Get User Info
        api_response = api_instance.get_user_info(token)
        print("The response of UserInfoApi->get_user_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserInfoApi->get_user_info: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| ID Token | 

### Return type

[**UserInfo**](UserInfo.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_info_by_email**
> UserInfo get_user_info_by_email(email)

Get User Info by Email

Get user information by email address. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.auth
from saasus_sdk_python.src.auth.models.user_info import UserInfo
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
    api_instance = saasus_sdk_python.src.auth.UserInfoApi(api_client)
    email = 'email_example' # str | Email

    try:
        # Get User Info by Email
        api_response = api_instance.get_user_info_by_email(email)
        print("The response of UserInfoApi->get_user_info_by_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserInfoApi->get_user_info_by_email: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Email | 

### Return type

[**UserInfo**](UserInfo.md)

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


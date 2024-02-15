# saasus_sdk_python.src.communication.ErrorApi

All URIs are relative to *https://api.saasus.io/v1/communication*

Method | HTTP request | Description
------------- | ------------- | -------------
[**return_internal_server_error**](ErrorApi.md#return_internal_server_error) | **GET** /errors/internal-server-error | ステータスコード500でサーバーエラーを返却(Return Internal Server Error)


# **return_internal_server_error**
> return_internal_server_error()

ステータスコード500でサーバーエラーを返却(Return Internal Server Error)

テスト用途で使用するエンドポイントです。ステータスコード500でサーバーエラーを返却します。  This endpoint is used for testing purposes. Returns a server error with status code 500. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.communication
from saasus_sdk_python.src.communication.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.saasus.io/v1/communication
# See configuration.py for a list of all supported configuration parameters.
configuration = saasus_sdk_python.src.communication.Configuration(
    host = "https://api.saasus.io/v1/communication"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = saasus_sdk_python.src.communication.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with saasus_sdk_python.src.communication.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = saasus_sdk_python.src.communication.ErrorApi(api_client)

    try:
        # ステータスコード500でサーバーエラーを返却(Return Internal Server Error)
        api_instance.return_internal_server_error()
    except Exception as e:
        print("Exception when calling ErrorApi->return_internal_server_error: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# saasus_sdk_python.src.apilog.ApiLogApi

All URIs are relative to *https://api.saasus.io/v1/apilog*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_log**](ApiLogApi.md#get_log) | **GET** /logs/{api_log_id} | Get API execution log
[**get_logs**](ApiLogApi.md#get_logs) | **GET** /logs | Get API execution log list


# **get_log**
> ApiLog get_log(api_log_id)

Get API execution log

Retrieve the log of the API execution with the specified ID.

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.apilog
from saasus_sdk_python.src.apilog.models.api_log import ApiLog
from saasus_sdk_python.src.apilog.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.saasus.io/v1/apilog
# See configuration.py for a list of all supported configuration parameters.
configuration = saasus_sdk_python.src.apilog.Configuration(
    host = "https://api.saasus.io/v1/apilog"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = saasus_sdk_python.src.apilog.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with saasus_sdk_python.src.apilog.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = saasus_sdk_python.src.apilog.ApiLogApi(api_client)
    api_log_id = 'api_log_id_example' # str | API Log ID

    try:
        # Get API execution log
        api_response = api_instance.get_log(api_log_id)
        print("The response of ApiLogApi->get_log:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiLogApi->get_log: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_log_id** | **str**| API Log ID | 

### Return type

[**ApiLog**](ApiLog.md)

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

# **get_logs**
> ApiLogs get_logs(created_date=created_date, created_at=created_at, limit=limit, cursor=cursor)

Get API execution log list

Retrieve the log of all API executions.

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.apilog
from saasus_sdk_python.src.apilog.models.api_logs import ApiLogs
from saasus_sdk_python.src.apilog.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.saasus.io/v1/apilog
# See configuration.py for a list of all supported configuration parameters.
configuration = saasus_sdk_python.src.apilog.Configuration(
    host = "https://api.saasus.io/v1/apilog"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = saasus_sdk_python.src.apilog.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with saasus_sdk_python.src.apilog.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = saasus_sdk_python.src.apilog.ApiLogApi(api_client)
    created_date = '2013-10-20' # date | The date, in format of YYYY-MM-DD, to retrieve the log. (optional)
    created_at = '2013-10-20T19:20:30+01:00' # datetime | The datetime, in ISO 8601 format, to retrieve the log. (optional)
    limit = 56 # int | Maximum number of logs to retrieve. (optional)
    cursor = 'cursor_example' # str | Cursor for cursor pagination. (optional)

    try:
        # Get API execution log list
        api_response = api_instance.get_logs(created_date=created_date, created_at=created_at, limit=limit, cursor=cursor)
        print("The response of ApiLogApi->get_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiLogApi->get_logs: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **created_date** | **date**| The date, in format of YYYY-MM-DD, to retrieve the log. | [optional] 
 **created_at** | **datetime**| The datetime, in ISO 8601 format, to retrieve the log. | [optional] 
 **limit** | **int**| Maximum number of logs to retrieve. | [optional] 
 **cursor** | **str**| Cursor for cursor pagination. | [optional] 

### Return type

[**ApiLogs**](ApiLogs.md)

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


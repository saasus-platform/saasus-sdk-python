# saasus_sdk_python.src.integration.EventBridgeApi

All URIs are relative to *https://api.saasus.io/v1/integration*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_event_bridge_event**](EventBridgeApi.md#create_event_bridge_event) | **POST** /eventbridge/event | イベント連携の送信(Send Events)
[**create_event_bridge_test_event**](EventBridgeApi.md#create_event_bridge_test_event) | **POST** /eventbridge/test-event | イベント連携のテスト送信(Test EventBridge Connection)
[**delete_event_bridge_settings**](EventBridgeApi.md#delete_event_bridge_settings) | **DELETE** /eventbridge/info | イベント連携設定を削除(Delete EventBridge Settings)
[**get_event_bridge_settings**](EventBridgeApi.md#get_event_bridge_settings) | **GET** /eventbridge/info | イベント連携設定を取得(Get EventBridge Settings)
[**save_event_bridge_settings**](EventBridgeApi.md#save_event_bridge_settings) | **PUT** /eventbridge/info | イベント連携設定を更新(Update EventBridge Settings)


# **create_event_bridge_event**
> create_event_bridge_event(create_event_bridge_event_param=create_event_bridge_event_param)

イベント連携の送信(Send Events)

Amazon EventBridge へイベントを送信します。  Send events to Amazon EventBridge. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.integration
from saasus_sdk_python.src.integration.models.create_event_bridge_event_param import CreateEventBridgeEventParam
from saasus_sdk_python.src.integration.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.saasus.io/v1/integration
# See configuration.py for a list of all supported configuration parameters.
configuration = saasus_sdk_python.src.integration.Configuration(
    host = "https://api.saasus.io/v1/integration"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = saasus_sdk_python.src.integration.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with saasus_sdk_python.src.integration.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = saasus_sdk_python.src.integration.EventBridgeApi(api_client)
    create_event_bridge_event_param = saasus_sdk_python.src.integration.CreateEventBridgeEventParam() # CreateEventBridgeEventParam |  (optional)

    try:
        # イベント連携の送信(Send Events)
        api_instance.create_event_bridge_event(create_event_bridge_event_param=create_event_bridge_event_param)
    except Exception as e:
        print("Exception when calling EventBridgeApi->create_event_bridge_event: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_event_bridge_event_param** | [**CreateEventBridgeEventParam**](CreateEventBridgeEventParam.md)|  | [optional] 

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
**201** | Created |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_event_bridge_test_event**
> create_event_bridge_test_event()

イベント連携のテスト送信(Test EventBridge Connection)

Amazon EventBridge との連携をテストする為のイベントを送信します。  Send events to test the connection with Amazon EventBridge. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.integration
from saasus_sdk_python.src.integration.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.saasus.io/v1/integration
# See configuration.py for a list of all supported configuration parameters.
configuration = saasus_sdk_python.src.integration.Configuration(
    host = "https://api.saasus.io/v1/integration"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = saasus_sdk_python.src.integration.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with saasus_sdk_python.src.integration.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = saasus_sdk_python.src.integration.EventBridgeApi(api_client)

    try:
        # イベント連携のテスト送信(Test EventBridge Connection)
        api_instance.create_event_bridge_test_event()
    except Exception as e:
        print("Exception when calling EventBridgeApi->create_event_bridge_test_event: %s\n" % e)
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
**201** | Created |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_event_bridge_settings**
> delete_event_bridge_settings()

イベント連携設定を削除(Delete EventBridge Settings)

ホストの状態を Amazon EventBridge 経由で提供するための設定を解除します。  Delete settings used to provide host state via Amazon EventBridge. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.integration
from saasus_sdk_python.src.integration.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.saasus.io/v1/integration
# See configuration.py for a list of all supported configuration parameters.
configuration = saasus_sdk_python.src.integration.Configuration(
    host = "https://api.saasus.io/v1/integration"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = saasus_sdk_python.src.integration.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with saasus_sdk_python.src.integration.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = saasus_sdk_python.src.integration.EventBridgeApi(api_client)

    try:
        # イベント連携設定を削除(Delete EventBridge Settings)
        api_instance.delete_event_bridge_settings()
    except Exception as e:
        print("Exception when calling EventBridgeApi->delete_event_bridge_settings: %s\n" % e)
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
**200** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_bridge_settings**
> EventBridgeSettings get_event_bridge_settings()

イベント連携設定を取得(Get EventBridge Settings)

監視対象となっている全ホストの状態をリアルタイムにAmazon EventBridge 経由で提供するための設定を取得します。  Gets the settings for providing real-time status of all monitored hosts via Amazon EventBridge. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.integration
from saasus_sdk_python.src.integration.models.event_bridge_settings import EventBridgeSettings
from saasus_sdk_python.src.integration.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.saasus.io/v1/integration
# See configuration.py for a list of all supported configuration parameters.
configuration = saasus_sdk_python.src.integration.Configuration(
    host = "https://api.saasus.io/v1/integration"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = saasus_sdk_python.src.integration.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with saasus_sdk_python.src.integration.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = saasus_sdk_python.src.integration.EventBridgeApi(api_client)

    try:
        # イベント連携設定を取得(Get EventBridge Settings)
        api_response = api_instance.get_event_bridge_settings()
        print("The response of EventBridgeApi->get_event_bridge_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventBridgeApi->get_event_bridge_settings: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**EventBridgeSettings**](EventBridgeSettings.md)

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

# **save_event_bridge_settings**
> save_event_bridge_settings(body=body)

イベント連携設定を更新(Update EventBridge Settings)

ホストの状態を Amazon EventBridge 経由で提供するための設定を更新します。  Update configuration used to provide the host state via Amazon EventBridge. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.integration
from saasus_sdk_python.src.integration.models.event_bridge_settings import EventBridgeSettings
from saasus_sdk_python.src.integration.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.saasus.io/v1/integration
# See configuration.py for a list of all supported configuration parameters.
configuration = saasus_sdk_python.src.integration.Configuration(
    host = "https://api.saasus.io/v1/integration"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = saasus_sdk_python.src.integration.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with saasus_sdk_python.src.integration.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = saasus_sdk_python.src.integration.EventBridgeApi(api_client)
    body = saasus_sdk_python.src.integration.EventBridgeSettings() # EventBridgeSettings |  (optional)

    try:
        # イベント連携設定を更新(Update EventBridge Settings)
        api_instance.save_event_bridge_settings(body=body)
    except Exception as e:
        print("Exception when calling EventBridgeApi->save_event_bridge_settings: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **EventBridgeSettings**|  | [optional] 

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


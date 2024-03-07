# saasus_sdk_python.src.integration.EventBridgeApi

All URIs are relative to *https://api.saasus.io/v1/integration*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_event_bridge_event**](EventBridgeApi.md#create_event_bridge_event) | **POST** /eventbridge/event | Send Events
[**create_event_bridge_test_event**](EventBridgeApi.md#create_event_bridge_test_event) | **POST** /eventbridge/test-event | Test EventBridge Connection
[**delete_event_bridge_settings**](EventBridgeApi.md#delete_event_bridge_settings) | **DELETE** /eventbridge/info | Delete EventBridge Settings
[**get_event_bridge_settings**](EventBridgeApi.md#get_event_bridge_settings) | **GET** /eventbridge/info | Get EventBridge Settings
[**save_event_bridge_settings**](EventBridgeApi.md#save_event_bridge_settings) | **PUT** /eventbridge/info | Update EventBridge Settings


# **create_event_bridge_event**
> create_event_bridge_event(create_event_bridge_event_param=create_event_bridge_event_param)

Send Events

Send events to Amazon EventBridge. 

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
        # Send Events
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

Test EventBridge Connection

Send events to test the connection with Amazon EventBridge. 

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
        # Test EventBridge Connection
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

Delete EventBridge Settings

Delete settings used to provide host state via Amazon EventBridge. 

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
        # Delete EventBridge Settings
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

Get EventBridge Settings

Gets the settings for providing real-time status of all monitored hosts via Amazon EventBridge. 

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
        # Get EventBridge Settings
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

Update EventBridge Settings

Update configuration used to provide the host state via Amazon EventBridge. 

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
        # Update EventBridge Settings
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


# saasus_sdk_python.src.auth.BasicInfoApi

All URIs are relative to *https://api.saasus.io/v1/auth*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_notification_messages**](BasicInfoApi.md#find_notification_messages) | **GET** /notification-messages | Get Notification Email Templates
[**get_basic_info**](BasicInfoApi.md#get_basic_info) | **GET** /basic-info | Get Basic Configurations
[**get_customize_page_settings**](BasicInfoApi.md#get_customize_page_settings) | **GET** /customize-page-settings | Get Authentication Authorization Basic Information
[**get_customize_pages**](BasicInfoApi.md#get_customize_pages) | **GET** /customize-pages | Get Authentication Page Setting
[**update_basic_info**](BasicInfoApi.md#update_basic_info) | **PUT** /basic-info | Update Basic Configurations
[**update_customize_page_settings**](BasicInfoApi.md#update_customize_page_settings) | **PATCH** /customize-page-settings | Update Authentication Authorization Basic Information
[**update_customize_pages**](BasicInfoApi.md#update_customize_pages) | **PATCH** /customize-pages | Authentication Page Setting
[**update_notification_messages**](BasicInfoApi.md#update_notification_messages) | **PUT** /notification-messages | Update Notification Email Template


# **find_notification_messages**
> NotificationMessages find_notification_messages()

Get Notification Email Templates

Get notification email templates. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.auth
from saasus_sdk_python.src.auth.models.notification_messages import NotificationMessages
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
    api_instance = saasus_sdk_python.src.auth.BasicInfoApi(api_client)

    try:
        # Get Notification Email Templates
        api_response = api_instance.find_notification_messages()
        print("The response of BasicInfoApi->find_notification_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BasicInfoApi->find_notification_messages: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**NotificationMessages**](NotificationMessages.md)

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

# **get_basic_info**
> BasicInfo get_basic_info()

Get Basic Configurations

Get the domain name and CNAME record based on the SaaS ID. By setting the CNAME record on the DNS the login screen will be generated. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.auth
from saasus_sdk_python.src.auth.models.basic_info import BasicInfo
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
    api_instance = saasus_sdk_python.src.auth.BasicInfoApi(api_client)

    try:
        # Get Basic Configurations
        api_response = api_instance.get_basic_info()
        print("The response of BasicInfoApi->get_basic_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BasicInfoApi->get_basic_info: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**BasicInfo**](BasicInfo.md)

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

# **get_customize_page_settings**
> CustomizePageSettings get_customize_page_settings()

Get Authentication Authorization Basic Information

Get authentication authorization basic information. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.auth
from saasus_sdk_python.src.auth.models.customize_page_settings import CustomizePageSettings
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
    api_instance = saasus_sdk_python.src.auth.BasicInfoApi(api_client)

    try:
        # Get Authentication Authorization Basic Information
        api_response = api_instance.get_customize_page_settings()
        print("The response of BasicInfoApi->get_customize_page_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BasicInfoApi->get_customize_page_settings: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**CustomizePageSettings**](CustomizePageSettings.md)

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

# **get_customize_pages**
> CustomizePages get_customize_pages()

Get Authentication Page Setting

Get the authentication screen setting information (new registration, login, password reset, etc.). 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.auth
from saasus_sdk_python.src.auth.models.customize_pages import CustomizePages
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
    api_instance = saasus_sdk_python.src.auth.BasicInfoApi(api_client)

    try:
        # Get Authentication Page Setting
        api_response = api_instance.get_customize_pages()
        print("The response of BasicInfoApi->get_customize_pages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BasicInfoApi->get_customize_pages: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**CustomizePages**](CustomizePages.md)

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

# **update_basic_info**
> update_basic_info(update_basic_info_param=update_basic_info_param)

Update Basic Configurations

Update the domain name that was set as a parameter based on the SaaS ID. After the CNAME record is generated, set it in your DNS. If it is set on a SaaS application that is already running, it will affect the behavior. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.auth
from saasus_sdk_python.src.auth.models.update_basic_info_param import UpdateBasicInfoParam
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
    api_instance = saasus_sdk_python.src.auth.BasicInfoApi(api_client)
    update_basic_info_param = saasus_sdk_python.src.auth.UpdateBasicInfoParam() # UpdateBasicInfoParam |  (optional)

    try:
        # Update Basic Configurations
        api_instance.update_basic_info(update_basic_info_param=update_basic_info_param)
    except Exception as e:
        print("Exception when calling BasicInfoApi->update_basic_info: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_basic_info_param** | [**UpdateBasicInfoParam**](UpdateBasicInfoParam.md)|  | [optional] 

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

# **update_customize_page_settings**
> update_customize_page_settings(update_customize_page_settings_param=update_customize_page_settings_param)

Update Authentication Authorization Basic Information

Update authentication authorization basic information. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.auth
from saasus_sdk_python.src.auth.models.update_customize_page_settings_param import UpdateCustomizePageSettingsParam
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
    api_instance = saasus_sdk_python.src.auth.BasicInfoApi(api_client)
    update_customize_page_settings_param = saasus_sdk_python.src.auth.UpdateCustomizePageSettingsParam() # UpdateCustomizePageSettingsParam |  (optional)

    try:
        # Update Authentication Authorization Basic Information
        api_instance.update_customize_page_settings(update_customize_page_settings_param=update_customize_page_settings_param)
    except Exception as e:
        print("Exception when calling BasicInfoApi->update_customize_page_settings: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_customize_page_settings_param** | [**UpdateCustomizePageSettingsParam**](UpdateCustomizePageSettingsParam.md)|  | [optional] 

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

# **update_customize_pages**
> update_customize_pages(update_customize_pages_param=update_customize_pages_param)

Authentication Page Setting

Update the authentication page setting information (new registration, login, password reset, etc.). 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.auth
from saasus_sdk_python.src.auth.models.update_customize_pages_param import UpdateCustomizePagesParam
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
    api_instance = saasus_sdk_python.src.auth.BasicInfoApi(api_client)
    update_customize_pages_param = saasus_sdk_python.src.auth.UpdateCustomizePagesParam() # UpdateCustomizePagesParam |  (optional)

    try:
        # Authentication Page Setting
        api_instance.update_customize_pages(update_customize_pages_param=update_customize_pages_param)
    except Exception as e:
        print("Exception when calling BasicInfoApi->update_customize_pages: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_customize_pages_param** | [**UpdateCustomizePagesParam**](UpdateCustomizePagesParam.md)|  | [optional] 

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

# **update_notification_messages**
> update_notification_messages(update_notification_messages_param=update_notification_messages_param)

Update Notification Email Template

Update notification email template. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.auth
from saasus_sdk_python.src.auth.models.update_notification_messages_param import UpdateNotificationMessagesParam
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
    api_instance = saasus_sdk_python.src.auth.BasicInfoApi(api_client)
    update_notification_messages_param = saasus_sdk_python.src.auth.UpdateNotificationMessagesParam() # UpdateNotificationMessagesParam |  (optional)

    try:
        # Update Notification Email Template
        api_instance.update_notification_messages(update_notification_messages_param=update_notification_messages_param)
    except Exception as e:
        print("Exception when calling BasicInfoApi->update_notification_messages: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_notification_messages_param** | [**UpdateNotificationMessagesParam**](UpdateNotificationMessagesParam.md)|  | [optional] 

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


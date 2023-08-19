# saasus_sdk_python.BasicInfoApi

All URIs are relative to *https://api.saasus.io/v1/auth*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_notification_messages**](BasicInfoApi.md#find_notification_messages) | **GET** /notification-messages | 通知メールテンプレートを取得(Get Notification Email Templates)
[**get_basic_info**](BasicInfoApi.md#get_basic_info) | **GET** /basic-info | 基本設定情報の取得(Get Basic Configurations)
[**get_customize_page_settings**](BasicInfoApi.md#get_customize_page_settings) | **GET** /customize-page-settings | 認証認可基本情報取得(Get Authentication Authorization Basic Information)
[**get_customize_pages**](BasicInfoApi.md#get_customize_pages) | **GET** /customize-pages | 認証系画面設定情報取得(Get Authentication Page Setting)
[**update_basic_info**](BasicInfoApi.md#update_basic_info) | **PUT** /basic-info | 基本設定情報の更新(Update Basic Configurations)
[**update_customize_page_settings**](BasicInfoApi.md#update_customize_page_settings) | **PATCH** /customize-page-settings | 認証認可基本情報更新(Update Authentication Authorization Basic Information)
[**update_customize_pages**](BasicInfoApi.md#update_customize_pages) | **PATCH** /customize-pages | 認証系画面設定情報設定(Authentication Page Setting)
[**update_notification_messages**](BasicInfoApi.md#update_notification_messages) | **PUT** /notification-messages | 通知メールテンプレートを更新(Update Notification Email Template)


# **find_notification_messages**
> NotificationMessages find_notification_messages()

通知メールテンプレートを取得(Get Notification Email Templates)

各種通知メールテンプレートを取得します。  Get notification email templates. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python
from saasus_sdk_python.models.notification_messages import NotificationMessages
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
    api_instance = saasus_sdk_python.BasicInfoApi(api_client)

    try:
        # 通知メールテンプレートを取得(Get Notification Email Templates)
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

基本設定情報の取得(Get Basic Configurations)

SaaS ID を元に設定されているドメイン名と CNAME レコードを取得します。 取得した CNAME レコードを DNS に設定することで、ログイン画面を生成します。  Get the domain name and CNAME record based on the SaaS ID. By setting the CNAME record on the DNS the login screen will be generated. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python
from saasus_sdk_python.models.basic_info import BasicInfo
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
    api_instance = saasus_sdk_python.BasicInfoApi(api_client)

    try:
        # 基本設定情報の取得(Get Basic Configurations)
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

認証認可基本情報取得(Get Authentication Authorization Basic Information)

認証認可基本情報を取得します。  Get authentication authorization basic information. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python
from saasus_sdk_python.models.customize_page_settings import CustomizePageSettings
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
    api_instance = saasus_sdk_python.BasicInfoApi(api_client)

    try:
        # 認証認可基本情報取得(Get Authentication Authorization Basic Information)
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

認証系画面設定情報取得(Get Authentication Page Setting)

認証系画面設定情報（新規登録・ログイン・パスワードリセット等）を取得します。  Get the authentication screen setting information (new registration, login, password reset, etc.). 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python
from saasus_sdk_python.models.customize_pages import CustomizePages
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
    api_instance = saasus_sdk_python.BasicInfoApi(api_client)

    try:
        # 認証系画面設定情報取得(Get Authentication Page Setting)
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

基本設定情報の更新(Update Basic Configurations)

SaaS ID を元にパラメータとして設定したドメイン名を設定更新します。 CNAME レコードが生成されますので、 DNS に設定して下さい。 既に稼働中の SaaS アプリケーションに設定している場合には、動作に影響があります。  Update the domain name that was set as a parameter based on the SaaS ID. After the CNAME record is generated, set it in your DNS. If it is set on a SaaS application that is already running, it will affect the behavior. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python
from saasus_sdk_python.models.update_basic_info_param import UpdateBasicInfoParam
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
    api_instance = saasus_sdk_python.BasicInfoApi(api_client)
    update_basic_info_param = saasus_sdk_python.UpdateBasicInfoParam() # UpdateBasicInfoParam |  (optional)

    try:
        # 基本設定情報の更新(Update Basic Configurations)
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

認証認可基本情報更新(Update Authentication Authorization Basic Information)

認証認可基本情報を更新します。  Update authentication authorization basic information. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python
from saasus_sdk_python.models.update_customize_page_settings_param import UpdateCustomizePageSettingsParam
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
    api_instance = saasus_sdk_python.BasicInfoApi(api_client)
    update_customize_page_settings_param = saasus_sdk_python.UpdateCustomizePageSettingsParam() # UpdateCustomizePageSettingsParam |  (optional)

    try:
        # 認証認可基本情報更新(Update Authentication Authorization Basic Information)
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

認証系画面設定情報設定(Authentication Page Setting)

認証系画面設定情報（新規登録・ログイン・パスワードリセット等）を更新します。  Update the authentication page setting information (new registration, login, password reset, etc.). 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python
from saasus_sdk_python.models.update_customize_pages_param import UpdateCustomizePagesParam
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
    api_instance = saasus_sdk_python.BasicInfoApi(api_client)
    update_customize_pages_param = saasus_sdk_python.UpdateCustomizePagesParam() # UpdateCustomizePagesParam |  (optional)

    try:
        # 認証系画面設定情報設定(Authentication Page Setting)
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

通知メールテンプレートを更新(Update Notification Email Template)

各種通知メールテンプレート更新します。  Update notification email template. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python
from saasus_sdk_python.models.update_notification_messages_param import UpdateNotificationMessagesParam
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
    api_instance = saasus_sdk_python.BasicInfoApi(api_client)
    update_notification_messages_param = saasus_sdk_python.UpdateNotificationMessagesParam() # UpdateNotificationMessagesParam |  (optional)

    try:
        # 通知メールテンプレートを更新(Update Notification Email Template)
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


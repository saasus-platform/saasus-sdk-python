# saasus_sdk_python.src.pricing.PricingMenusApi

All URIs are relative to *https://api.saasus.io/v1/pricing*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_pricing_menu**](PricingMenusApi.md#create_pricing_menu) | **POST** /menus | プライシング機能メニューを作成
[**delete_pricing_menu**](PricingMenusApi.md#delete_pricing_menu) | **DELETE** /menus/{menu_id} | プライシング機能メニューを削除
[**get_pricing_menu**](PricingMenusApi.md#get_pricing_menu) | **GET** /menus/{menu_id} | プライシング機能メニューを取得
[**get_pricing_menus**](PricingMenusApi.md#get_pricing_menus) | **GET** /menus | プライシング機能メニュー一覧を取得
[**update_pricing_menu**](PricingMenusApi.md#update_pricing_menu) | **PATCH** /menus/{menu_id} | プライシング機能メニューを更新


# **create_pricing_menu**
> PricingMenu create_pricing_menu(body=body)

プライシング機能メニューを作成

プライシング機能メニューを作成します。 

### Example

* Bearer Authentication (Bearer):

```python
import time
import os
import saasus_sdk_python.src.pricing
from saasus_sdk_python.src.pricing.models.pricing_menu import PricingMenu
from saasus_sdk_python.src.pricing.models.save_pricing_menu_param import SavePricingMenuParam
from saasus_sdk_python.src.pricing.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.saasus.io/v1/pricing
# See configuration.py for a list of all supported configuration parameters.
configuration = saasus_sdk_python.src.pricing.Configuration(
    host = "https://api.saasus.io/v1/pricing"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = saasus_sdk_python.src.pricing.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with saasus_sdk_python.src.pricing.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = saasus_sdk_python.src.pricing.PricingMenusApi(api_client)
    body = saasus_sdk_python.src.pricing.SavePricingMenuParam() # SavePricingMenuParam |  (optional)

    try:
        # プライシング機能メニューを作成
        api_response = api_instance.create_pricing_menu(body=body)
        print("The response of PricingMenusApi->create_pricing_menu:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricingMenusApi->create_pricing_menu: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **SavePricingMenuParam**|  | [optional] 

### Return type

[**PricingMenu**](PricingMenu.md)

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

# **delete_pricing_menu**
> delete_pricing_menu(menu_id)

プライシング機能メニューを削除

プライシング機能メニューを削除します。 

### Example

* Bearer Authentication (Bearer):

```python
import time
import os
import saasus_sdk_python.src.pricing
from saasus_sdk_python.src.pricing.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.saasus.io/v1/pricing
# See configuration.py for a list of all supported configuration parameters.
configuration = saasus_sdk_python.src.pricing.Configuration(
    host = "https://api.saasus.io/v1/pricing"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = saasus_sdk_python.src.pricing.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with saasus_sdk_python.src.pricing.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = saasus_sdk_python.src.pricing.PricingMenusApi(api_client)
    menu_id = 'menu_id_example' # str | メニューID

    try:
        # プライシング機能メニューを削除
        api_instance.delete_pricing_menu(menu_id)
    except Exception as e:
        print("Exception when calling PricingMenusApi->delete_pricing_menu: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **menu_id** | **str**| メニューID | 

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

# **get_pricing_menu**
> PricingMenu get_pricing_menu(menu_id)

プライシング機能メニューを取得

プライシング機能メニューを取得します。 

### Example

* Bearer Authentication (Bearer):

```python
import time
import os
import saasus_sdk_python.src.pricing
from saasus_sdk_python.src.pricing.models.pricing_menu import PricingMenu
from saasus_sdk_python.src.pricing.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.saasus.io/v1/pricing
# See configuration.py for a list of all supported configuration parameters.
configuration = saasus_sdk_python.src.pricing.Configuration(
    host = "https://api.saasus.io/v1/pricing"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = saasus_sdk_python.src.pricing.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with saasus_sdk_python.src.pricing.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = saasus_sdk_python.src.pricing.PricingMenusApi(api_client)
    menu_id = 'menu_id_example' # str | メニューID

    try:
        # プライシング機能メニューを取得
        api_response = api_instance.get_pricing_menu(menu_id)
        print("The response of PricingMenusApi->get_pricing_menu:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricingMenusApi->get_pricing_menu: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **menu_id** | **str**| メニューID | 

### Return type

[**PricingMenu**](PricingMenu.md)

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

# **get_pricing_menus**
> PricingMenus get_pricing_menus()

プライシング機能メニュー一覧を取得

機能メニュー一覧を取得します。計測単位を複数まとめて、１つの機能メニューとして定義します。ここで定義した機能メニューを複数合わせ１つの料金プランとします。 

### Example

* Bearer Authentication (Bearer):

```python
import time
import os
import saasus_sdk_python.src.pricing
from saasus_sdk_python.src.pricing.models.pricing_menus import PricingMenus
from saasus_sdk_python.src.pricing.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.saasus.io/v1/pricing
# See configuration.py for a list of all supported configuration parameters.
configuration = saasus_sdk_python.src.pricing.Configuration(
    host = "https://api.saasus.io/v1/pricing"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = saasus_sdk_python.src.pricing.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with saasus_sdk_python.src.pricing.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = saasus_sdk_python.src.pricing.PricingMenusApi(api_client)

    try:
        # プライシング機能メニュー一覧を取得
        api_response = api_instance.get_pricing_menus()
        print("The response of PricingMenusApi->get_pricing_menus:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricingMenusApi->get_pricing_menus: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PricingMenus**](PricingMenus.md)

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

# **update_pricing_menu**
> update_pricing_menu(menu_id, body=body)

プライシング機能メニューを更新

プライシング機能メニューを更新します。 

### Example

* Bearer Authentication (Bearer):

```python
import time
import os
import saasus_sdk_python.src.pricing
from saasus_sdk_python.src.pricing.models.save_pricing_menu_param import SavePricingMenuParam
from saasus_sdk_python.src.pricing.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.saasus.io/v1/pricing
# See configuration.py for a list of all supported configuration parameters.
configuration = saasus_sdk_python.src.pricing.Configuration(
    host = "https://api.saasus.io/v1/pricing"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = saasus_sdk_python.src.pricing.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with saasus_sdk_python.src.pricing.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = saasus_sdk_python.src.pricing.PricingMenusApi(api_client)
    menu_id = 'menu_id_example' # str | メニューID
    body = saasus_sdk_python.src.pricing.SavePricingMenuParam() # SavePricingMenuParam |  (optional)

    try:
        # プライシング機能メニューを更新
        api_instance.update_pricing_menu(menu_id, body=body)
    except Exception as e:
        print("Exception when calling PricingMenusApi->update_pricing_menu: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **menu_id** | **str**| メニューID | 
 **body** | **SavePricingMenuParam**|  | [optional] 

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


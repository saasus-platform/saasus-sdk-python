# saasus_sdk_python.src.pricing.PricingMenusApi

All URIs are relative to *https://api.saasus.io/v1/pricing*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_pricing_menu**](PricingMenusApi.md#create_pricing_menu) | **POST** /menus | Create a Pricing Feature Menu
[**delete_pricing_menu**](PricingMenusApi.md#delete_pricing_menu) | **DELETE** /menus/{menu_id} | Delete Pricing Feature Menu
[**get_pricing_menu**](PricingMenusApi.md#get_pricing_menu) | **GET** /menus/{menu_id} | Get Pricing Feature Menu
[**get_pricing_menus**](PricingMenusApi.md#get_pricing_menus) | **GET** /menus | Get Pricing Feature Menus
[**update_pricing_menu**](PricingMenusApi.md#update_pricing_menu) | **PATCH** /menus/{menu_id} | Update Pricing Feature Menu


# **create_pricing_menu**
> PricingMenu create_pricing_menu(body=body)

Create a Pricing Feature Menu

Create a pricing feature menu. 

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
        # Create a Pricing Feature Menu
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

Delete Pricing Feature Menu

Delete pricing feature menu. 

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
    menu_id = 'menu_id_example' # str | Menu ID

    try:
        # Delete Pricing Feature Menu
        api_instance.delete_pricing_menu(menu_id)
    except Exception as e:
        print("Exception when calling PricingMenusApi->delete_pricing_menu: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **menu_id** | **str**| Menu ID | 

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

Get Pricing Feature Menu

Get a pricing feature menu. 

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
    menu_id = 'menu_id_example' # str | Menu ID

    try:
        # Get Pricing Feature Menu
        api_response = api_instance.get_pricing_menu(menu_id)
        print("The response of PricingMenusApi->get_pricing_menu:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricingMenusApi->get_pricing_menu: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **menu_id** | **str**| Menu ID | 

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

Get Pricing Feature Menus

Get the feature menu list. Multiple measurement units are grouped together and defined as one feature menu. Multiple feature menus defined here are combined into one billing plan. 

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
        # Get Pricing Feature Menus
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

Update Pricing Feature Menu

Update pricing feature menu. 

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
    menu_id = 'menu_id_example' # str | Menu ID
    body = saasus_sdk_python.src.pricing.SavePricingMenuParam() # SavePricingMenuParam |  (optional)

    try:
        # Update Pricing Feature Menu
        api_instance.update_pricing_menu(menu_id, body=body)
    except Exception as e:
        print("Exception when calling PricingMenusApi->update_pricing_menu: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **menu_id** | **str**| Menu ID | 
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


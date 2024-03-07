# saasus_sdk_python.src.pricing.PricingUnitsApi

All URIs are relative to *https://api.saasus.io/v1/pricing*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_pricing_unit**](PricingUnitsApi.md#create_pricing_unit) | **POST** /units | Create Pricing Unit
[**delete_pricing_unit**](PricingUnitsApi.md#delete_pricing_unit) | **DELETE** /units/{pricing_unit_id} | Delete Pricing Unit
[**get_pricing_unit**](PricingUnitsApi.md#get_pricing_unit) | **GET** /units/{pricing_unit_id} | Get Pricing Unit
[**get_pricing_units**](PricingUnitsApi.md#get_pricing_units) | **GET** /units | Get Pricing Units
[**update_pricing_unit**](PricingUnitsApi.md#update_pricing_unit) | **PATCH** /units/{pricing_unit_id} | Update Pricing Unit


# **create_pricing_unit**
> PricingUnit create_pricing_unit(body=body)

Create Pricing Unit

Create a pricing unit. 

### Example

* Bearer Authentication (Bearer):

```python
import time
import os
import saasus_sdk_python.src.pricing
from saasus_sdk_python.src.pricing.models.pricing_unit import PricingUnit
from saasus_sdk_python.src.pricing.models.pricing_unit_for_save import PricingUnitForSave
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
    api_instance = saasus_sdk_python.src.pricing.PricingUnitsApi(api_client)
    body = saasus_sdk_python.src.pricing.PricingUnitForSave() # PricingUnitForSave |  (optional)

    try:
        # Create Pricing Unit
        api_response = api_instance.create_pricing_unit(body=body)
        print("The response of PricingUnitsApi->create_pricing_unit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricingUnitsApi->create_pricing_unit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **PricingUnitForSave**|  | [optional] 

### Return type

[**PricingUnit**](PricingUnit.md)

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

# **delete_pricing_unit**
> delete_pricing_unit(pricing_unit_id)

Delete Pricing Unit

Delete a pricing unit. 

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
    api_instance = saasus_sdk_python.src.pricing.PricingUnitsApi(api_client)
    pricing_unit_id = 'pricing_unit_id_example' # str | Unit ID

    try:
        # Delete Pricing Unit
        api_instance.delete_pricing_unit(pricing_unit_id)
    except Exception as e:
        print("Exception when calling PricingUnitsApi->delete_pricing_unit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pricing_unit_id** | **str**| Unit ID | 

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

# **get_pricing_unit**
> PricingUnit get_pricing_unit(pricing_unit_id)

Get Pricing Unit

Get a pricing unit. 

### Example

* Bearer Authentication (Bearer):

```python
import time
import os
import saasus_sdk_python.src.pricing
from saasus_sdk_python.src.pricing.models.pricing_unit import PricingUnit
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
    api_instance = saasus_sdk_python.src.pricing.PricingUnitsApi(api_client)
    pricing_unit_id = 'pricing_unit_id_example' # str | Unit ID

    try:
        # Get Pricing Unit
        api_response = api_instance.get_pricing_unit(pricing_unit_id)
        print("The response of PricingUnitsApi->get_pricing_unit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricingUnitsApi->get_pricing_unit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pricing_unit_id** | **str**| Unit ID | 

### Return type

[**PricingUnit**](PricingUnit.md)

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

# **get_pricing_units**
> PricingUnits get_pricing_units()

Get Pricing Units

Gets the smallest unit of measure on which the charges are based. \"Fixed Unit\" (type=fixed) is a unit of a monthly fixed charge such as a basic charge, \"Usage Unit\" (type=usage) is a unit in which a charge is generated per unit such as billing for the number of users, \"Tiered Unit\" (type=tiered) is a fixed charge unit for each tier of usage, such as the tiered packet charge for mobile phones, \"Tiered Usage Unit\" (type=tiered_usage) is a unit where the charge per unit changes according to the usage amount, such as a volume discount. 

### Example

* Bearer Authentication (Bearer):

```python
import time
import os
import saasus_sdk_python.src.pricing
from saasus_sdk_python.src.pricing.models.pricing_units import PricingUnits
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
    api_instance = saasus_sdk_python.src.pricing.PricingUnitsApi(api_client)

    try:
        # Get Pricing Units
        api_response = api_instance.get_pricing_units()
        print("The response of PricingUnitsApi->get_pricing_units:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricingUnitsApi->get_pricing_units: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PricingUnits**](PricingUnits.md)

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

# **update_pricing_unit**
> update_pricing_unit(pricing_unit_id, body=body)

Update Pricing Unit

Update pricing unit. 

### Example

* Bearer Authentication (Bearer):

```python
import time
import os
import saasus_sdk_python.src.pricing
from saasus_sdk_python.src.pricing.models.pricing_unit_for_save import PricingUnitForSave
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
    api_instance = saasus_sdk_python.src.pricing.PricingUnitsApi(api_client)
    pricing_unit_id = 'pricing_unit_id_example' # str | Unit ID
    body = saasus_sdk_python.src.pricing.PricingUnitForSave() # PricingUnitForSave |  (optional)

    try:
        # Update Pricing Unit
        api_instance.update_pricing_unit(pricing_unit_id, body=body)
    except Exception as e:
        print("Exception when calling PricingUnitsApi->update_pricing_unit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pricing_unit_id** | **str**| Unit ID | 
 **body** | **PricingUnitForSave**|  | [optional] 

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


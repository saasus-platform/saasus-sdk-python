# saasus_sdk_python.src.pricing.TaxRateApi

All URIs are relative to *https://api.saasus.io/v1/pricing*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tax_rate**](TaxRateApi.md#create_tax_rate) | **POST** /tax-rates | 税率の作成
[**get_tax_rates**](TaxRateApi.md#get_tax_rates) | **GET** /tax-rates | 税率を取得します
[**update_tax_rate**](TaxRateApi.md#update_tax_rate) | **PATCH** /tax-rates/{tax_rate_id} | 税率を更新


# **create_tax_rate**
> TaxRate create_tax_rate(body=body)

税率の作成

税率を作成します。 

### Example

* Bearer Authentication (Bearer):

```python
import time
import os
import saasus_sdk_python.src.pricing
from saasus_sdk_python.src.pricing.models.tax_rate import TaxRate
from saasus_sdk_python.src.pricing.models.tax_rate_props import TaxRateProps
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
    api_instance = saasus_sdk_python.src.pricing.TaxRateApi(api_client)
    body = saasus_sdk_python.src.pricing.TaxRateProps() # TaxRateProps |  (optional)

    try:
        # 税率の作成
        api_response = api_instance.create_tax_rate(body=body)
        print("The response of TaxRateApi->create_tax_rate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxRateApi->create_tax_rate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **TaxRateProps**|  | [optional] 

### Return type

[**TaxRate**](TaxRate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tax_rates**
> TaxRates get_tax_rates()

税率を取得します

税率を取得します。 

### Example

* Bearer Authentication (Bearer):

```python
import time
import os
import saasus_sdk_python.src.pricing
from saasus_sdk_python.src.pricing.models.tax_rates import TaxRates
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
    api_instance = saasus_sdk_python.src.pricing.TaxRateApi(api_client)

    try:
        # 税率を取得します
        api_response = api_instance.get_tax_rates()
        print("The response of TaxRateApi->get_tax_rates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxRateApi->get_tax_rates: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**TaxRates**](TaxRates.md)

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

# **update_tax_rate**
> update_tax_rate(tax_rate_id, update_tax_rate_param=update_tax_rate_param)

税率を更新

税率を更新します。 

### Example

* Bearer Authentication (Bearer):

```python
import time
import os
import saasus_sdk_python.src.pricing
from saasus_sdk_python.src.pricing.models.update_tax_rate_param import UpdateTaxRateParam
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
    api_instance = saasus_sdk_python.src.pricing.TaxRateApi(api_client)
    tax_rate_id = 'tax_rate_id_example' # str | 税率ID
    update_tax_rate_param = saasus_sdk_python.src.pricing.UpdateTaxRateParam() # UpdateTaxRateParam |  (optional)

    try:
        # 税率を更新
        api_instance.update_tax_rate(tax_rate_id, update_tax_rate_param=update_tax_rate_param)
    except Exception as e:
        print("Exception when calling TaxRateApi->update_tax_rate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tax_rate_id** | **str**| 税率ID | 
 **update_tax_rate_param** | [**UpdateTaxRateParam**](UpdateTaxRateParam.md)|  | [optional] 

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
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


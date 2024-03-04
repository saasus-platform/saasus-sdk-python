# saasus_sdk_python.src.billing.StripeApi

All URIs are relative to *https://api.saasus.io/v1/billing*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_stripe_info**](StripeApi.md#delete_stripe_info) | **DELETE** /stripe/info | Delete Stripe Connection
[**get_stripe_info**](StripeApi.md#get_stripe_info) | **GET** /stripe/info | Get Stripe Connection information
[**update_stripe_info**](StripeApi.md#update_stripe_info) | **PUT** /stripe/info | Update Stripe Connection Info


# **delete_stripe_info**
> delete_stripe_info()

Delete Stripe Connection

Delete connection with external billing SaaS 

### Example

* Bearer Authentication (Bearer):

```python
import time
import os
import saasus_sdk_python.src.billing
from saasus_sdk_python.src.billing.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.saasus.io/v1/billing
# See configuration.py for a list of all supported configuration parameters.
configuration = saasus_sdk_python.src.billing.Configuration(
    host = "https://api.saasus.io/v1/billing"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = saasus_sdk_python.src.billing.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with saasus_sdk_python.src.billing.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = saasus_sdk_python.src.billing.StripeApi(api_client)

    try:
        # Delete Stripe Connection
        api_instance.delete_stripe_info()
    except Exception as e:
        print("Exception when calling StripeApi->delete_stripe_info: %s\n" % e)
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

# **get_stripe_info**
> StripeInfo get_stripe_info()

Get Stripe Connection information

Get information on connnections with external billing SaaS. Currently possible to integrate with Stripe. Without integration, you will need to implement billing using the SaaSus SDK/API. 

### Example

* Bearer Authentication (Bearer):

```python
import time
import os
import saasus_sdk_python.src.billing
from saasus_sdk_python.src.billing.models.stripe_info import StripeInfo
from saasus_sdk_python.src.billing.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.saasus.io/v1/billing
# See configuration.py for a list of all supported configuration parameters.
configuration = saasus_sdk_python.src.billing.Configuration(
    host = "https://api.saasus.io/v1/billing"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = saasus_sdk_python.src.billing.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with saasus_sdk_python.src.billing.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = saasus_sdk_python.src.billing.StripeApi(api_client)

    try:
        # Get Stripe Connection information
        api_response = api_instance.get_stripe_info()
        print("The response of StripeApi->get_stripe_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StripeApi->get_stripe_info: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**StripeInfo**](StripeInfo.md)

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

# **update_stripe_info**
> update_stripe_info(update_stripe_info_param=update_stripe_info_param)

Update Stripe Connection Info

Updates information on connection with external billing SaaS. Currently possible to connect to Stripe. 

### Example

* Bearer Authentication (Bearer):

```python
import time
import os
import saasus_sdk_python.src.billing
from saasus_sdk_python.src.billing.models.update_stripe_info_param import UpdateStripeInfoParam
from saasus_sdk_python.src.billing.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.saasus.io/v1/billing
# See configuration.py for a list of all supported configuration parameters.
configuration = saasus_sdk_python.src.billing.Configuration(
    host = "https://api.saasus.io/v1/billing"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = saasus_sdk_python.src.billing.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with saasus_sdk_python.src.billing.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = saasus_sdk_python.src.billing.StripeApi(api_client)
    update_stripe_info_param = saasus_sdk_python.src.billing.UpdateStripeInfoParam() # UpdateStripeInfoParam |  (optional)

    try:
        # Update Stripe Connection Info
        api_instance.update_stripe_info(update_stripe_info_param=update_stripe_info_param)
    except Exception as e:
        print("Exception when calling StripeApi->update_stripe_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_stripe_info_param** | [**UpdateStripeInfoParam**](UpdateStripeInfoParam.md)|  | [optional] 

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


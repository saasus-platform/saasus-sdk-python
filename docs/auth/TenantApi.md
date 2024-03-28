# saasus_sdk_python.src.auth.TenantApi

All URIs are relative to *https://api.saasus.io/v1/auth*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tenant**](TenantApi.md#create_tenant) | **POST** /tenants | Create Tenant
[**create_tenant_and_pricing**](TenantApi.md#create_tenant_and_pricing) | **PATCH** /stripe/init | Stripe Initial Setting
[**delete_stripe_tenant_and_pricing**](TenantApi.md#delete_stripe_tenant_and_pricing) | **DELETE** /stripe | Delete Customer and Product From Stripe
[**delete_tenant**](TenantApi.md#delete_tenant) | **DELETE** /tenants/{tenant_id} | Delete Tenant
[**get_tenant**](TenantApi.md#get_tenant) | **GET** /tenants/{tenant_id} | Get Tenant Details
[**get_tenant_identity_providers**](TenantApi.md#get_tenant_identity_providers) | **GET** /tenants/{tenant_id}/identity-providers | Get identity provider per tenant
[**get_tenants**](TenantApi.md#get_tenants) | **GET** /tenants | Get Tenants
[**reset_plan**](TenantApi.md#reset_plan) | **PUT** /plans/reset | Delete all information related to rate plans
[**update_tenant**](TenantApi.md#update_tenant) | **PATCH** /tenants/{tenant_id} | Update Tenant Details
[**update_tenant_billing_info**](TenantApi.md#update_tenant_billing_info) | **PUT** /tenants/{tenant_id}/billing-info | Update Tenant Billing Information
[**update_tenant_identity_provider**](TenantApi.md#update_tenant_identity_provider) | **PUT** /tenants/{tenant_id}/identity-providers | Update identity provider per tenant
[**update_tenant_plan**](TenantApi.md#update_tenant_plan) | **PUT** /tenants/{tenant_id}/plans | Update Tenant Plan Information


# **create_tenant**
> Tenant create_tenant(body=body)

Create Tenant

Create a tenant managed by the SaaSus Platform. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.auth
from saasus_sdk_python.src.auth.models.tenant import Tenant
from saasus_sdk_python.src.auth.models.tenant_props import TenantProps
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
    api_instance = saasus_sdk_python.src.auth.TenantApi(api_client)
    body = saasus_sdk_python.src.auth.TenantProps() # TenantProps |  (optional)

    try:
        # Create Tenant
        api_response = api_instance.create_tenant(body=body)
        print("The response of TenantApi->create_tenant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->create_tenant: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **TenantProps**|  | [optional] 

### Return type

[**Tenant**](Tenant.md)

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

# **create_tenant_and_pricing**
> create_tenant_and_pricing()

Stripe Initial Setting

Set Stripe initial information via billing 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.auth
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
    api_instance = saasus_sdk_python.src.auth.TenantApi(api_client)

    try:
        # Stripe Initial Setting
        api_instance.create_tenant_and_pricing()
    except Exception as e:
        print("Exception when calling TenantApi->create_tenant_and_pricing: %s\n" % e)
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

# **delete_stripe_tenant_and_pricing**
> delete_stripe_tenant_and_pricing()

Delete Customer and Product From Stripe

Delete customer and product from Stripe. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.auth
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
    api_instance = saasus_sdk_python.src.auth.TenantApi(api_client)

    try:
        # Delete Customer and Product From Stripe
        api_instance.delete_stripe_tenant_and_pricing()
    except Exception as e:
        print("Exception when calling TenantApi->delete_stripe_tenant_and_pricing: %s\n" % e)
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

# **delete_tenant**
> delete_tenant(tenant_id)

Delete Tenant

Delete SaaSus Platform tenant. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.auth
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
    api_instance = saasus_sdk_python.src.auth.TenantApi(api_client)
    tenant_id = 'tenant_id_example' # str | Tenant ID

    try:
        # Delete Tenant
        api_instance.delete_tenant(tenant_id)
    except Exception as e:
        print("Exception when calling TenantApi->delete_tenant: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant ID | 

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

# **get_tenant**
> TenantDetail get_tenant(tenant_id)

Get Tenant Details

Get the details of tenant managed on the SaaSus Platform. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.auth
from saasus_sdk_python.src.auth.models.tenant_detail import TenantDetail
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
    api_instance = saasus_sdk_python.src.auth.TenantApi(api_client)
    tenant_id = 'tenant_id_example' # str | Tenant ID

    try:
        # Get Tenant Details
        api_response = api_instance.get_tenant(tenant_id)
        print("The response of TenantApi->get_tenant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->get_tenant: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant ID | 

### Return type

[**TenantDetail**](TenantDetail.md)

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

# **get_tenant_identity_providers**
> TenantIdentityProviders get_tenant_identity_providers(tenant_id)

Get identity provider per tenant

Get sign-in information via external identity provider per tenant. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.auth
from saasus_sdk_python.src.auth.models.tenant_identity_providers import TenantIdentityProviders
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
    api_instance = saasus_sdk_python.src.auth.TenantApi(api_client)
    tenant_id = 'tenant_id_example' # str | Tenant ID

    try:
        # Get identity provider per tenant
        api_response = api_instance.get_tenant_identity_providers(tenant_id)
        print("The response of TenantApi->get_tenant_identity_providers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->get_tenant_identity_providers: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant ID | 

### Return type

[**TenantIdentityProviders**](TenantIdentityProviders.md)

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

# **get_tenants**
> Tenants get_tenants()

Get Tenants

Get tenants managed by SaaSus Platform. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.auth
from saasus_sdk_python.src.auth.models.tenants import Tenants
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
    api_instance = saasus_sdk_python.src.auth.TenantApi(api_client)

    try:
        # Get Tenants
        api_response = api_instance.get_tenants()
        print("The response of TenantApi->get_tenants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->get_tenants: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**Tenants**](Tenants.md)

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

# **reset_plan**
> reset_plan()

Delete all information related to rate plans

Delete all information related to rate plans. Delete plans linked to tenants and plan definitions. If you are using the Stripe linkage, the linkage will be removed. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.auth
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
    api_instance = saasus_sdk_python.src.auth.TenantApi(api_client)

    try:
        # Delete all information related to rate plans
        api_instance.reset_plan()
    except Exception as e:
        print("Exception when calling TenantApi->reset_plan: %s\n" % e)
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

# **update_tenant**
> update_tenant(tenant_id, body=body)

Update Tenant Details

Update SaaSus Platform tenant details. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.auth
from saasus_sdk_python.src.auth.models.tenant_props import TenantProps
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
    api_instance = saasus_sdk_python.src.auth.TenantApi(api_client)
    tenant_id = 'tenant_id_example' # str | Tenant ID
    body = saasus_sdk_python.src.auth.TenantProps() # TenantProps |  (optional)

    try:
        # Update Tenant Details
        api_instance.update_tenant(tenant_id, body=body)
    except Exception as e:
        print("Exception when calling TenantApi->update_tenant: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant ID | 
 **body** | **TenantProps**|  | [optional] 

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
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tenant_billing_info**
> update_tenant_billing_info(tenant_id, body=body)

Update Tenant Billing Information

Update SaaSus Platform tenant billing information. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.auth
from saasus_sdk_python.src.auth.models.billing_info import BillingInfo
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
    api_instance = saasus_sdk_python.src.auth.TenantApi(api_client)
    tenant_id = 'tenant_id_example' # str | Tenant ID
    body = saasus_sdk_python.src.auth.BillingInfo() # BillingInfo |  (optional)

    try:
        # Update Tenant Billing Information
        api_instance.update_tenant_billing_info(tenant_id, body=body)
    except Exception as e:
        print("Exception when calling TenantApi->update_tenant_billing_info: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant ID | 
 **body** | **BillingInfo**|  | [optional] 

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
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tenant_identity_provider**
> update_tenant_identity_provider(tenant_id, update_tenant_identity_provider_param=update_tenant_identity_provider_param)

Update identity provider per tenant

Update sign-in information via external identity provider per tenant. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.auth
from saasus_sdk_python.src.auth.models.update_tenant_identity_provider_param import UpdateTenantIdentityProviderParam
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
    api_instance = saasus_sdk_python.src.auth.TenantApi(api_client)
    tenant_id = 'tenant_id_example' # str | Tenant ID
    update_tenant_identity_provider_param = saasus_sdk_python.src.auth.UpdateTenantIdentityProviderParam() # UpdateTenantIdentityProviderParam |  (optional)

    try:
        # Update identity provider per tenant
        api_instance.update_tenant_identity_provider(tenant_id, update_tenant_identity_provider_param=update_tenant_identity_provider_param)
    except Exception as e:
        print("Exception when calling TenantApi->update_tenant_identity_provider: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant ID | 
 **update_tenant_identity_provider_param** | [**UpdateTenantIdentityProviderParam**](UpdateTenantIdentityProviderParam.md)|  | [optional] 

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

# **update_tenant_plan**
> update_tenant_plan(tenant_id, body=body)

Update Tenant Plan Information

Update SaaSus Platform tenant plan information. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.auth
from saasus_sdk_python.src.auth.models.plan_reservation import PlanReservation
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
    api_instance = saasus_sdk_python.src.auth.TenantApi(api_client)
    tenant_id = 'tenant_id_example' # str | Tenant ID
    body = saasus_sdk_python.src.auth.PlanReservation() # PlanReservation |  (optional)

    try:
        # Update Tenant Plan Information
        api_instance.update_tenant_plan(tenant_id, body=body)
    except Exception as e:
        print("Exception when calling TenantApi->update_tenant_plan: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant ID | 
 **body** | **PlanReservation**|  | [optional] 

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
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# saasus_sdk_python.src.auth.TenantApi

All URIs are relative to *https://api.saasus.io/v1/auth*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tenant**](TenantApi.md#create_tenant) | **POST** /tenants | テナントを作成(Create Tenant)
[**create_tenant_and_pricing**](TenantApi.md#create_tenant_and_pricing) | **PATCH** /stripe/init | stripe初期設定(Stripe Initial Setting)
[**delete_stripe_tenant_and_pricing**](TenantApi.md#delete_stripe_tenant_and_pricing) | **DELETE** /stripe | stripe上の顧客情報・商品情報の削除(Delete Customer and Product From Stripe)
[**delete_tenant**](TenantApi.md#delete_tenant) | **DELETE** /tenants/{tenant_id} | テナント情報を削除(Delete Tenant)
[**get_tenant**](TenantApi.md#get_tenant) | **GET** /tenants/{tenant_id} | テナント情報を取得(Get Tenant Details)
[**get_tenant_identity_providers**](TenantApi.md#get_tenant_identity_providers) | **GET** /tenants/{tenant_id}/identity-providers | テナント毎の外部IDプロバイダ取得(Get identity provider per tenant)
[**get_tenants**](TenantApi.md#get_tenants) | **GET** /tenants | テナント一覧取得(Get Tenants)
[**reset_plan**](TenantApi.md#reset_plan) | **PUT** /plans/reset | プランに関わる情報を全削除
[**update_tenant**](TenantApi.md#update_tenant) | **PATCH** /tenants/{tenant_id} | テナント情報を更新(Update Tenant Details)
[**update_tenant_billing_info**](TenantApi.md#update_tenant_billing_info) | **PUT** /tenants/{tenant_id}/billing-info | テナントの請求先情報を更新(Update Tenant Billing Information)
[**update_tenant_identity_provider**](TenantApi.md#update_tenant_identity_provider) | **PUT** /tenants/{tenant_id}/identity-providers | テナント毎の外部IDプロバイダ更新(Update identity provider per tenant)
[**update_tenant_plan**](TenantApi.md#update_tenant_plan) | **PUT** /tenants/{tenant_id}/plans | テナントのプラン情報を更新(Update Tenant Plan Information)


# **create_tenant**
> Tenant create_tenant(body=body)

テナントを作成(Create Tenant)

SaaSus Platform で管理する、テナント情報を作成します。  Create a tenant managed by the SaaSus Platform. 

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
        # テナントを作成(Create Tenant)
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

stripe初期設定(Stripe Initial Setting)

billing経由でstripeへ初期情報を設定  Set Stripe initial information via billing 

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
        # stripe初期設定(Stripe Initial Setting)
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

stripe上の顧客情報・商品情報の削除(Delete Customer and Product From Stripe)

stripe上の顧客情報・商品情報を削除します  Delete customer and product from Stripe. 

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
        # stripe上の顧客情報・商品情報の削除(Delete Customer and Product From Stripe)
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

テナント情報を削除(Delete Tenant)

SaaSus Platform で管理する、テナントの詳細情報を削除します。  Delete SaaSus Platform tenant. 

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
    tenant_id = 'tenant_id_example' # str | テナントID(Tenant ID)

    try:
        # テナント情報を削除(Delete Tenant)
        api_instance.delete_tenant(tenant_id)
    except Exception as e:
        print("Exception when calling TenantApi->delete_tenant: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| テナントID(Tenant ID) | 

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

テナント情報を取得(Get Tenant Details)

SaaSus Platform で管理する、テナントの詳細情報を取得します。  Get the details of tenant managed on the SaaSus Platform. 

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
    tenant_id = 'tenant_id_example' # str | テナントID(Tenant ID)

    try:
        # テナント情報を取得(Get Tenant Details)
        api_response = api_instance.get_tenant(tenant_id)
        print("The response of TenantApi->get_tenant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->get_tenant: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| テナントID(Tenant ID) | 

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

テナント毎の外部IDプロバイダ取得(Get identity provider per tenant)

テナント毎の外部IDプロバイダ経由のサインイン情報を取得します。  Get sign-in information via external identity provider per tenant. 

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
    tenant_id = 'tenant_id_example' # str | テナントID(Tenant ID)

    try:
        # テナント毎の外部IDプロバイダ取得(Get identity provider per tenant)
        api_response = api_instance.get_tenant_identity_providers(tenant_id)
        print("The response of TenantApi->get_tenant_identity_providers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->get_tenant_identity_providers: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| テナントID(Tenant ID) | 

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

テナント一覧取得(Get Tenants)

SaaSus Platform で管理する、テナント情報の取得を行います。  Get tenants managed by SaaSus Platform. 

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
        # テナント一覧取得(Get Tenants)
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

プランに関わる情報を全削除

料金プランに関わる情報を全削除します。 テナントに連携されたプランとプラン定義を削除します。 Stripe連携している場合、連携が解除されます。  Delete all information related to rate plans. Delete plans linked to tenants and plan definitions. If you are using the Stripe linkage, the linkage will be removed. 

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
        # プランに関わる情報を全削除
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

テナント情報を更新(Update Tenant Details)

SaaSus Platform で管理する、テナントの詳細情報を更新します。  Update SaaSus Platform tenant details. 

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
    tenant_id = 'tenant_id_example' # str | テナントID(Tenant ID)
    body = saasus_sdk_python.src.auth.TenantProps() # TenantProps |  (optional)

    try:
        # テナント情報を更新(Update Tenant Details)
        api_instance.update_tenant(tenant_id, body=body)
    except Exception as e:
        print("Exception when calling TenantApi->update_tenant: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| テナントID(Tenant ID) | 
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

テナントの請求先情報を更新(Update Tenant Billing Information)

SaaSus Platform で管理しているテナントの請求先情報を更新します。  Update SaaSus Platform tenant billing information. 

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
    tenant_id = 'tenant_id_example' # str | テナントID(Tenant ID)
    body = saasus_sdk_python.src.auth.BillingInfo() # BillingInfo |  (optional)

    try:
        # テナントの請求先情報を更新(Update Tenant Billing Information)
        api_instance.update_tenant_billing_info(tenant_id, body=body)
    except Exception as e:
        print("Exception when calling TenantApi->update_tenant_billing_info: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| テナントID(Tenant ID) | 
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

テナント毎の外部IDプロバイダ更新(Update identity provider per tenant)

テナント毎の外部IDプロバイダ経由のサインイン情報を更新します。  Update sign-in information via external identity provider per tenant. 

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
    tenant_id = 'tenant_id_example' # str | テナントID(Tenant ID)
    update_tenant_identity_provider_param = saasus_sdk_python.src.auth.UpdateTenantIdentityProviderParam() # UpdateTenantIdentityProviderParam |  (optional)

    try:
        # テナント毎の外部IDプロバイダ更新(Update identity provider per tenant)
        api_instance.update_tenant_identity_provider(tenant_id, update_tenant_identity_provider_param=update_tenant_identity_provider_param)
    except Exception as e:
        print("Exception when calling TenantApi->update_tenant_identity_provider: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| テナントID(Tenant ID) | 
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

テナントのプラン情報を更新(Update Tenant Plan Information)

SaaSus Platform で管理しているテナントのプラン情報を更新します。  Update SaaSus Platform tenant plan information. 

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
    tenant_id = 'tenant_id_example' # str | テナントID(Tenant ID)
    body = saasus_sdk_python.src.auth.PlanReservation() # PlanReservation |  (optional)

    try:
        # テナントのプラン情報を更新(Update Tenant Plan Information)
        api_instance.update_tenant_plan(tenant_id, body=body)
    except Exception as e:
        print("Exception when calling TenantApi->update_tenant_plan: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| テナントID(Tenant ID) | 
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


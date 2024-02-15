# saasus_sdk_python.src.pricing.PricingPlansApi

All URIs are relative to *https://api.saasus.io/v1/pricing*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_pricing_plan**](PricingPlansApi.md#create_pricing_plan) | **POST** /plans | 料金プランを作成(Create Pricing Plan)
[**delete_all_plans_and_menus_and_units_and_meters_and_tax_rates**](PricingPlansApi.md#delete_all_plans_and_menus_and_units_and_meters_and_tax_rates) | **DELETE** /plans-initialization | 全てのPlans,Menus,Units,Metersの削除(Delete all Plans, Menus, Units, Meters and Tax Rates)
[**delete_pricing_plan**](PricingPlansApi.md#delete_pricing_plan) | **DELETE** /plans/{plan_id} | 料金プランを削除(Delete Pricing Plan)
[**delete_stripe_plan**](PricingPlansApi.md#delete_stripe_plan) | **DELETE** /stripe | stripe上の商品情報を削除(Delete Product Data from Stripe)
[**get_pricing_plan**](PricingPlansApi.md#get_pricing_plan) | **GET** /plans/{plan_id} | 料金プランを取得(Get Pricing Plan)
[**get_pricing_plans**](PricingPlansApi.md#get_pricing_plans) | **GET** /plans | 料金プラン一覧を取得(Get pricing plan list)
[**link_plan_to_stripe**](PricingPlansApi.md#link_plan_to_stripe) | **PATCH** /stripe/init | stripe連携(Connect to Stripe)
[**update_pricing_plan**](PricingPlansApi.md#update_pricing_plan) | **PATCH** /plans/{plan_id} | 料金プランを更新(Update Pricing Plan)
[**update_pricing_plans_used**](PricingPlansApi.md#update_pricing_plans_used) | **PATCH** /plans/used | 使用済みフラグ更新(Update Used Flag)


# **create_pricing_plan**
> PricingPlan create_pricing_plan(body=body)

料金プランを作成(Create Pricing Plan)

料金プランを作成します。  Create pricing plan. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.pricing
from saasus_sdk_python.src.pricing.models.pricing_plan import PricingPlan
from saasus_sdk_python.src.pricing.models.save_pricing_plan_param import SavePricingPlanParam
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
    api_instance = saasus_sdk_python.src.pricing.PricingPlansApi(api_client)
    body = saasus_sdk_python.src.pricing.SavePricingPlanParam() # SavePricingPlanParam |  (optional)

    try:
        # 料金プランを作成(Create Pricing Plan)
        api_response = api_instance.create_pricing_plan(body=body)
        print("The response of PricingPlansApi->create_pricing_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricingPlansApi->create_pricing_plan: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **SavePricingPlanParam**|  | [optional] 

### Return type

[**PricingPlan**](PricingPlan.md)

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

# **delete_all_plans_and_menus_and_units_and_meters_and_tax_rates**
> delete_all_plans_and_menus_and_units_and_meters_and_tax_rates()

全てのPlans,Menus,Units,Metersの削除(Delete all Plans, Menus, Units, Meters and Tax Rates)

無条件に全料金プラン、メニュー、ユニット、メーター、税率を削除します。  Unconditionally remove all rate plans, menus, units, meters and tax rates. 

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
    api_instance = saasus_sdk_python.src.pricing.PricingPlansApi(api_client)

    try:
        # 全てのPlans,Menus,Units,Metersの削除(Delete all Plans, Menus, Units, Meters and Tax Rates)
        api_instance.delete_all_plans_and_menus_and_units_and_meters_and_tax_rates()
    except Exception as e:
        print("Exception when calling PricingPlansApi->delete_all_plans_and_menus_and_units_and_meters_and_tax_rates: %s\n" % e)
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

# **delete_pricing_plan**
> delete_pricing_plan(plan_id)

料金プランを削除(Delete Pricing Plan)

料金プランを削除します。  Delete pricing plan. 

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
    api_instance = saasus_sdk_python.src.pricing.PricingPlansApi(api_client)
    plan_id = 'plan_id_example' # str | 料金プランID(price plan ID)

    try:
        # 料金プランを削除(Delete Pricing Plan)
        api_instance.delete_pricing_plan(plan_id)
    except Exception as e:
        print("Exception when calling PricingPlansApi->delete_pricing_plan: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **str**| 料金プランID(price plan ID) | 

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

# **delete_stripe_plan**
> delete_stripe_plan()

stripe上の商品情報を削除(Delete Product Data from Stripe)

stripe上の商品情報を削除します。  Delete product data from Stripe. 

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
    api_instance = saasus_sdk_python.src.pricing.PricingPlansApi(api_client)

    try:
        # stripe上の商品情報を削除(Delete Product Data from Stripe)
        api_instance.delete_stripe_plan()
    except Exception as e:
        print("Exception when calling PricingPlansApi->delete_stripe_plan: %s\n" % e)
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

# **get_pricing_plan**
> PricingPlan get_pricing_plan(plan_id)

料金プランを取得(Get Pricing Plan)

料金プランを取得します。  Get pricing plan. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.pricing
from saasus_sdk_python.src.pricing.models.pricing_plan import PricingPlan
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
    api_instance = saasus_sdk_python.src.pricing.PricingPlansApi(api_client)
    plan_id = 'plan_id_example' # str | 料金プランID(price plan ID)

    try:
        # 料金プランを取得(Get Pricing Plan)
        api_response = api_instance.get_pricing_plan(plan_id)
        print("The response of PricingPlansApi->get_pricing_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricingPlansApi->get_pricing_plan: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **str**| 料金プランID(price plan ID) | 

### Return type

[**PricingPlan**](PricingPlan.md)

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

# **get_pricing_plans**
> PricingPlans get_pricing_plans()

料金プラン一覧を取得(Get pricing plan list)

料金プラン一覧を取得します。 機能メニューを複数まとめて、１つの料金プランとして定義します。 ここで定義した料金プランを各テナントは選ぶことができます。 もし特定テナント特有の料金（プライベートプライシング）がある場合は、そのテナント専用の料金プランを作成して結びつけます。  Get pricing plans. Multiple feature menus are grouped together and defined as one pricing plan. Each tenant can choose a pricing plan defined here. If you have a specific tenant-specific rate (private pricing), create and connect the pricing plan specifically for that tenant. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.pricing
from saasus_sdk_python.src.pricing.models.pricing_plans import PricingPlans
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
    api_instance = saasus_sdk_python.src.pricing.PricingPlansApi(api_client)

    try:
        # 料金プラン一覧を取得(Get pricing plan list)
        api_response = api_instance.get_pricing_plans()
        print("The response of PricingPlansApi->get_pricing_plans:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricingPlansApi->get_pricing_plans: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**PricingPlans**](PricingPlans.md)

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

# **link_plan_to_stripe**
> link_plan_to_stripe()

stripe連携(Connect to Stripe)

stripeへ情報を連携します。  Connect information to Stripe. 

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
    api_instance = saasus_sdk_python.src.pricing.PricingPlansApi(api_client)

    try:
        # stripe連携(Connect to Stripe)
        api_instance.link_plan_to_stripe()
    except Exception as e:
        print("Exception when calling PricingPlansApi->link_plan_to_stripe: %s\n" % e)
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

# **update_pricing_plan**
> update_pricing_plan(plan_id, body=body)

料金プランを更新(Update Pricing Plan)

料金プランを更新します。  Update pricing plan. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.pricing
from saasus_sdk_python.src.pricing.models.save_pricing_plan_param import SavePricingPlanParam
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
    api_instance = saasus_sdk_python.src.pricing.PricingPlansApi(api_client)
    plan_id = 'plan_id_example' # str | 料金プランID(price plan ID)
    body = saasus_sdk_python.src.pricing.SavePricingPlanParam() # SavePricingPlanParam |  (optional)

    try:
        # 料金プランを更新(Update Pricing Plan)
        api_instance.update_pricing_plan(plan_id, body=body)
    except Exception as e:
        print("Exception when calling PricingPlansApi->update_pricing_plan: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **str**| 料金プランID(price plan ID) | 
 **body** | **SavePricingPlanParam**|  | [optional] 

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

# **update_pricing_plans_used**
> update_pricing_plans_used(update_pricing_plans_used_param=update_pricing_plans_used_param)

使用済みフラグ更新(Update Used Flag)

料金プランと配下のメニュー・ユニットを使用済みに更新します。  Update price plan and feature menu/pricing unit to used. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.pricing
from saasus_sdk_python.src.pricing.models.update_pricing_plans_used_param import UpdatePricingPlansUsedParam
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
    api_instance = saasus_sdk_python.src.pricing.PricingPlansApi(api_client)
    update_pricing_plans_used_param = saasus_sdk_python.src.pricing.UpdatePricingPlansUsedParam() # UpdatePricingPlansUsedParam |  (optional)

    try:
        # 使用済みフラグ更新(Update Used Flag)
        api_instance.update_pricing_plans_used(update_pricing_plans_used_param=update_pricing_plans_used_param)
    except Exception as e:
        print("Exception when calling PricingPlansApi->update_pricing_plans_used: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_pricing_plans_used_param** | [**UpdatePricingPlansUsedParam**](UpdatePricingPlansUsedParam.md)|  | [optional] 

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


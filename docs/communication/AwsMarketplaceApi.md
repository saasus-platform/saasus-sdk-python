# saasus_sdk_python.src.awsmarketplace.AwsMarketplaceApi

All URIs are relative to *https://api.saasus.io/v1/awsmarketplace*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_customer**](AwsMarketplaceApi.md#create_customer) | **POST** /customers | AWS Marketplaceに連携する顧客情報を新規作成(Create customer information to be linked to AWS Marketplace)
[**get_catalog_entity_visibility**](AwsMarketplaceApi.md#get_catalog_entity_visibility) | **GET** /catalog-entity/visibility | AWS Marketplaceから商品の公開状況を取得(Obtain product publication status from AWS Marketplace)
[**get_cloud_formation_launch_stack_link**](AwsMarketplaceApi.md#get_cloud_formation_launch_stack_link) | **GET** /cloudformation-launch-stack-link | AWS CloudFormationのスタック作成リンクを取得(Get the link to create the AWS CloudFormation stack)
[**get_customer**](AwsMarketplaceApi.md#get_customer) | **GET** /customers/{customer_identifier} | AWS Marketplaceに連携する顧客情報を取得(Get customer information to be linked to AWS Marketplace)
[**get_customers**](AwsMarketplaceApi.md#get_customers) | **GET** /customers | AWS Marketplaceに連携する顧客情報の一覧を取得(Get a list of customer information to be linked to AWS Marketplace)
[**get_listing_status**](AwsMarketplaceApi.md#get_listing_status) | **GET** /listing-status | AWS Marketplaceの出品状況を取得(Get AWS Marketplace Listing Status)
[**get_plan_by_plan_name**](AwsMarketplaceApi.md#get_plan_by_plan_name) | **GET** /plans/{plan_name} | AWSMarketplaceに連携するプラン情報を取得(Obtain plan information to link to AWS Marketplace)
[**get_plans**](AwsMarketplaceApi.md#get_plans) | **GET** /plans | AWS Marketplaceに連携するプラン情報を取得(Obtain plan information to link to AWS Marketplace)
[**get_settings**](AwsMarketplaceApi.md#get_settings) | **GET** /settings | AWS Marketplaceの設定を取得(Get AWS Marketplace Settings)
[**save_plan**](AwsMarketplaceApi.md#save_plan) | **PUT** /plans | AWS Marketplaceに連携するプラン情報を登録(Save plan information to be linked to AWSMarketplace)
[**sync_customer**](AwsMarketplaceApi.md#sync_customer) | **POST** /customers/{customer_identifier}/sync | AWS Marketplaceの顧客情報をSaaSusに同期します(Sync AWS Marketplace customer information to SaaSus)
[**update_listing_status**](AwsMarketplaceApi.md#update_listing_status) | **PUT** /listing-status | AWS Marketplaceの出品状況を更新(Update AWS Marketplace Listing Status)
[**update_settings**](AwsMarketplaceApi.md#update_settings) | **PUT** /settings | AWS Marketplaceの設定を更新(Update AWS Marketplace Settings)
[**verify_registration_token**](AwsMarketplaceApi.md#verify_registration_token) | **POST** /registration-token/verify | Registration Tokenを検証(Verify Registration Token)


# **create_customer**
> Customer create_customer(create_customer_param=create_customer_param)

AWS Marketplaceに連携する顧客情報を新規作成(Create customer information to be linked to AWS Marketplace)

AWS Marketplaceに連携する顧客情報を新規作成します。  Create customer information to be linked to AWS Marketplace. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.awsmarketplace
from saasus_sdk_python.src.awsmarketplace.models.create_customer_param import CreateCustomerParam
from saasus_sdk_python.src.awsmarketplace.models.customer import Customer
from saasus_sdk_python.src.awsmarketplace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.saasus.io/v1/awsmarketplace
# See configuration.py for a list of all supported configuration parameters.
configuration = saasus_sdk_python.src.awsmarketplace.Configuration(
    host = "https://api.saasus.io/v1/awsmarketplace"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = saasus_sdk_python.src.awsmarketplace.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with saasus_sdk_python.src.awsmarketplace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = saasus_sdk_python.src.awsmarketplace.AwsMarketplaceApi(api_client)
    create_customer_param = saasus_sdk_python.src.awsmarketplace.CreateCustomerParam() # CreateCustomerParam |  (optional)

    try:
        # AWS Marketplaceに連携する顧客情報を新規作成(Create customer information to be linked to AWS Marketplace)
        api_response = api_instance.create_customer(create_customer_param=create_customer_param)
        print("The response of AwsMarketplaceApi->create_customer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AwsMarketplaceApi->create_customer: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_customer_param** | [**CreateCustomerParam**](CreateCustomerParam.md)|  | [optional] 

### Return type

[**Customer**](Customer.md)

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

# **get_catalog_entity_visibility**
> CatalogEntityVisibility get_catalog_entity_visibility()

AWS Marketplaceから商品の公開状況を取得(Obtain product publication status from AWS Marketplace)

AWS Marketplaceから商品の公開状況を取得します。  Retrieve the product's publication status from AWS Marketplace. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.awsmarketplace
from saasus_sdk_python.src.awsmarketplace.models.catalog_entity_visibility import CatalogEntityVisibility
from saasus_sdk_python.src.awsmarketplace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.saasus.io/v1/awsmarketplace
# See configuration.py for a list of all supported configuration parameters.
configuration = saasus_sdk_python.src.awsmarketplace.Configuration(
    host = "https://api.saasus.io/v1/awsmarketplace"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = saasus_sdk_python.src.awsmarketplace.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with saasus_sdk_python.src.awsmarketplace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = saasus_sdk_python.src.awsmarketplace.AwsMarketplaceApi(api_client)

    try:
        # AWS Marketplaceから商品の公開状況を取得(Obtain product publication status from AWS Marketplace)
        api_response = api_instance.get_catalog_entity_visibility()
        print("The response of AwsMarketplaceApi->get_catalog_entity_visibility:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AwsMarketplaceApi->get_catalog_entity_visibility: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**CatalogEntityVisibility**](CatalogEntityVisibility.md)

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

# **get_cloud_formation_launch_stack_link**
> CloudFormationLaunchStackLink get_cloud_formation_launch_stack_link()

AWS CloudFormationのスタック作成リンクを取得(Get the link to create the AWS CloudFormation stack)

CloudFormationのクイック作成リンクを取得します。  Get the CloudFormation Quick Create link. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.awsmarketplace
from saasus_sdk_python.src.awsmarketplace.models.cloud_formation_launch_stack_link import CloudFormationLaunchStackLink
from saasus_sdk_python.src.awsmarketplace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.saasus.io/v1/awsmarketplace
# See configuration.py for a list of all supported configuration parameters.
configuration = saasus_sdk_python.src.awsmarketplace.Configuration(
    host = "https://api.saasus.io/v1/awsmarketplace"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = saasus_sdk_python.src.awsmarketplace.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with saasus_sdk_python.src.awsmarketplace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = saasus_sdk_python.src.awsmarketplace.AwsMarketplaceApi(api_client)

    try:
        # AWS CloudFormationのスタック作成リンクを取得(Get the link to create the AWS CloudFormation stack)
        api_response = api_instance.get_cloud_formation_launch_stack_link()
        print("The response of AwsMarketplaceApi->get_cloud_formation_launch_stack_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AwsMarketplaceApi->get_cloud_formation_launch_stack_link: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**CloudFormationLaunchStackLink**](CloudFormationLaunchStackLink.md)

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

# **get_customer**
> Customer get_customer(customer_identifier)

AWS Marketplaceに連携する顧客情報を取得(Get customer information to be linked to AWS Marketplace)

AWS Marketplaceに連携する顧客情報を取得します。  Get customer information to be linked to AWS Marketplace. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.awsmarketplace
from saasus_sdk_python.src.awsmarketplace.models.customer import Customer
from saasus_sdk_python.src.awsmarketplace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.saasus.io/v1/awsmarketplace
# See configuration.py for a list of all supported configuration parameters.
configuration = saasus_sdk_python.src.awsmarketplace.Configuration(
    host = "https://api.saasus.io/v1/awsmarketplace"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = saasus_sdk_python.src.awsmarketplace.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with saasus_sdk_python.src.awsmarketplace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = saasus_sdk_python.src.awsmarketplace.AwsMarketplaceApi(api_client)
    customer_identifier = '123456789012' # str | 顧客ID

    try:
        # AWS Marketplaceに連携する顧客情報を取得(Get customer information to be linked to AWS Marketplace)
        api_response = api_instance.get_customer(customer_identifier)
        print("The response of AwsMarketplaceApi->get_customer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AwsMarketplaceApi->get_customer: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_identifier** | **str**| 顧客ID | 

### Return type

[**Customer**](Customer.md)

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

# **get_customers**
> Customers get_customers(tenant_ids=tenant_ids)

AWS Marketplaceに連携する顧客情報の一覧を取得(Get a list of customer information to be linked to AWS Marketplace)

AWS Marketplaceに連携する顧客情報の一覧を取得します。  Get a list of customer information to be linked to AWS Marketplace. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.awsmarketplace
from saasus_sdk_python.src.awsmarketplace.models.customers import Customers
from saasus_sdk_python.src.awsmarketplace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.saasus.io/v1/awsmarketplace
# See configuration.py for a list of all supported configuration parameters.
configuration = saasus_sdk_python.src.awsmarketplace.Configuration(
    host = "https://api.saasus.io/v1/awsmarketplace"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = saasus_sdk_python.src.awsmarketplace.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with saasus_sdk_python.src.awsmarketplace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = saasus_sdk_python.src.awsmarketplace.AwsMarketplaceApi(api_client)
    tenant_ids = ['tenant_ids_example'] # List[str] | 指定したテナントIDの顧客を取得する(Get customers with the specified tenant ID) (optional)

    try:
        # AWS Marketplaceに連携する顧客情報の一覧を取得(Get a list of customer information to be linked to AWS Marketplace)
        api_response = api_instance.get_customers(tenant_ids=tenant_ids)
        print("The response of AwsMarketplaceApi->get_customers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AwsMarketplaceApi->get_customers: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_ids** | [**List[str]**](str.md)| 指定したテナントIDの顧客を取得する(Get customers with the specified tenant ID) | [optional] 

### Return type

[**Customers**](Customers.md)

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

# **get_listing_status**
> GetListingStatusResult get_listing_status()

AWS Marketplaceの出品状況を取得(Get AWS Marketplace Listing Status)

AWS Marketplaceの出品状況を取得します。  Get AWS Marketplace Listing Status. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.awsmarketplace
from saasus_sdk_python.src.awsmarketplace.models.get_listing_status_result import GetListingStatusResult
from saasus_sdk_python.src.awsmarketplace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.saasus.io/v1/awsmarketplace
# See configuration.py for a list of all supported configuration parameters.
configuration = saasus_sdk_python.src.awsmarketplace.Configuration(
    host = "https://api.saasus.io/v1/awsmarketplace"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = saasus_sdk_python.src.awsmarketplace.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with saasus_sdk_python.src.awsmarketplace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = saasus_sdk_python.src.awsmarketplace.AwsMarketplaceApi(api_client)

    try:
        # AWS Marketplaceの出品状況を取得(Get AWS Marketplace Listing Status)
        api_response = api_instance.get_listing_status()
        print("The response of AwsMarketplaceApi->get_listing_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AwsMarketplaceApi->get_listing_status: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**GetListingStatusResult**](GetListingStatusResult.md)

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

# **get_plan_by_plan_name**
> Plan get_plan_by_plan_name(plan_name)

AWSMarketplaceに連携するプラン情報を取得(Obtain plan information to link to AWS Marketplace)

Marketplaceと連携するプラン情報を取得します。  Obtain plan information to link to AWS Marketplace. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.awsmarketplace
from saasus_sdk_python.src.awsmarketplace.models.plan import Plan
from saasus_sdk_python.src.awsmarketplace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.saasus.io/v1/awsmarketplace
# See configuration.py for a list of all supported configuration parameters.
configuration = saasus_sdk_python.src.awsmarketplace.Configuration(
    host = "https://api.saasus.io/v1/awsmarketplace"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = saasus_sdk_python.src.awsmarketplace.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with saasus_sdk_python.src.awsmarketplace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = saasus_sdk_python.src.awsmarketplace.AwsMarketplaceApi(api_client)
    plan_name = 'normal_plan_name_month' # str | AWS Marketplace連携プラン名

    try:
        # AWSMarketplaceに連携するプラン情報を取得(Obtain plan information to link to AWS Marketplace)
        api_response = api_instance.get_plan_by_plan_name(plan_name)
        print("The response of AwsMarketplaceApi->get_plan_by_plan_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AwsMarketplaceApi->get_plan_by_plan_name: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_name** | **str**| AWS Marketplace連携プラン名 | 

### Return type

[**Plan**](Plan.md)

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

# **get_plans**
> Plans get_plans()

AWS Marketplaceに連携するプラン情報を取得(Obtain plan information to link to AWS Marketplace)

Marketplaceと連携するプラン情報を取得します。  Obtain plan information to link to AWS Marketplace. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.awsmarketplace
from saasus_sdk_python.src.awsmarketplace.models.plans import Plans
from saasus_sdk_python.src.awsmarketplace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.saasus.io/v1/awsmarketplace
# See configuration.py for a list of all supported configuration parameters.
configuration = saasus_sdk_python.src.awsmarketplace.Configuration(
    host = "https://api.saasus.io/v1/awsmarketplace"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = saasus_sdk_python.src.awsmarketplace.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with saasus_sdk_python.src.awsmarketplace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = saasus_sdk_python.src.awsmarketplace.AwsMarketplaceApi(api_client)

    try:
        # AWS Marketplaceに連携するプラン情報を取得(Obtain plan information to link to AWS Marketplace)
        api_response = api_instance.get_plans()
        print("The response of AwsMarketplaceApi->get_plans:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AwsMarketplaceApi->get_plans: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**Plans**](Plans.md)

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

# **get_settings**
> Settings get_settings()

AWS Marketplaceの設定を取得(Get AWS Marketplace Settings)

AWS Marketplaceの設定を取得します。  Get AWS Marketplace Settings. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.awsmarketplace
from saasus_sdk_python.src.awsmarketplace.models.settings import Settings
from saasus_sdk_python.src.awsmarketplace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.saasus.io/v1/awsmarketplace
# See configuration.py for a list of all supported configuration parameters.
configuration = saasus_sdk_python.src.awsmarketplace.Configuration(
    host = "https://api.saasus.io/v1/awsmarketplace"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = saasus_sdk_python.src.awsmarketplace.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with saasus_sdk_python.src.awsmarketplace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = saasus_sdk_python.src.awsmarketplace.AwsMarketplaceApi(api_client)

    try:
        # AWS Marketplaceの設定を取得(Get AWS Marketplace Settings)
        api_response = api_instance.get_settings()
        print("The response of AwsMarketplaceApi->get_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AwsMarketplaceApi->get_settings: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**Settings**](Settings.md)

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

# **save_plan**
> save_plan(save_plan_param=save_plan_param)

AWS Marketplaceに連携するプラン情報を登録(Save plan information to be linked to AWSMarketplace)

AWSMarketplaceに連携するプラン情報を登録します。  Save plan information to be linked to AWSMarketplace. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.awsmarketplace
from saasus_sdk_python.src.awsmarketplace.models.save_plan_param import SavePlanParam
from saasus_sdk_python.src.awsmarketplace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.saasus.io/v1/awsmarketplace
# See configuration.py for a list of all supported configuration parameters.
configuration = saasus_sdk_python.src.awsmarketplace.Configuration(
    host = "https://api.saasus.io/v1/awsmarketplace"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = saasus_sdk_python.src.awsmarketplace.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with saasus_sdk_python.src.awsmarketplace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = saasus_sdk_python.src.awsmarketplace.AwsMarketplaceApi(api_client)
    save_plan_param = saasus_sdk_python.src.awsmarketplace.SavePlanParam() # SavePlanParam |  (optional)

    try:
        # AWS Marketplaceに連携するプラン情報を登録(Save plan information to be linked to AWSMarketplace)
        api_instance.save_plan(save_plan_param=save_plan_param)
    except Exception as e:
        print("Exception when calling AwsMarketplaceApi->save_plan: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **save_plan_param** | [**SavePlanParam**](SavePlanParam.md)|  | [optional] 

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

# **sync_customer**
> sync_customer(customer_identifier)

AWS Marketplaceの顧客情報をSaaSusに同期します(Sync AWS Marketplace customer information to SaaSus)

AWS Marketplaceの顧客情報をSaaSusに同期します。  Sync AWS Marketplace customer information to SaaSus. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.awsmarketplace
from saasus_sdk_python.src.awsmarketplace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.saasus.io/v1/awsmarketplace
# See configuration.py for a list of all supported configuration parameters.
configuration = saasus_sdk_python.src.awsmarketplace.Configuration(
    host = "https://api.saasus.io/v1/awsmarketplace"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = saasus_sdk_python.src.awsmarketplace.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with saasus_sdk_python.src.awsmarketplace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = saasus_sdk_python.src.awsmarketplace.AwsMarketplaceApi(api_client)
    customer_identifier = '123456789012' # str | 顧客ID

    try:
        # AWS Marketplaceの顧客情報をSaaSusに同期します(Sync AWS Marketplace customer information to SaaSus)
        api_instance.sync_customer(customer_identifier)
    except Exception as e:
        print("Exception when calling AwsMarketplaceApi->sync_customer: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_identifier** | **str**| 顧客ID | 

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

# **update_listing_status**
> update_listing_status(update_listing_status_param=update_listing_status_param)

AWS Marketplaceの出品状況を更新(Update AWS Marketplace Listing Status)

AWS Marketplaceの出品状況を更新します。  Update AWS Marketplace Listing Status. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.awsmarketplace
from saasus_sdk_python.src.awsmarketplace.models.update_listing_status_param import UpdateListingStatusParam
from saasus_sdk_python.src.awsmarketplace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.saasus.io/v1/awsmarketplace
# See configuration.py for a list of all supported configuration parameters.
configuration = saasus_sdk_python.src.awsmarketplace.Configuration(
    host = "https://api.saasus.io/v1/awsmarketplace"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = saasus_sdk_python.src.awsmarketplace.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with saasus_sdk_python.src.awsmarketplace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = saasus_sdk_python.src.awsmarketplace.AwsMarketplaceApi(api_client)
    update_listing_status_param = saasus_sdk_python.src.awsmarketplace.UpdateListingStatusParam() # UpdateListingStatusParam |  (optional)

    try:
        # AWS Marketplaceの出品状況を更新(Update AWS Marketplace Listing Status)
        api_instance.update_listing_status(update_listing_status_param=update_listing_status_param)
    except Exception as e:
        print("Exception when calling AwsMarketplaceApi->update_listing_status: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_listing_status_param** | [**UpdateListingStatusParam**](UpdateListingStatusParam.md)|  | [optional] 

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

# **update_settings**
> update_settings(update_settings_param=update_settings_param)

AWS Marketplaceの設定を更新(Update AWS Marketplace Settings)

AWS Marketplaceの設定を更新します。  Update AWS Marketplace Settings. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.awsmarketplace
from saasus_sdk_python.src.awsmarketplace.models.update_settings_param import UpdateSettingsParam
from saasus_sdk_python.src.awsmarketplace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.saasus.io/v1/awsmarketplace
# See configuration.py for a list of all supported configuration parameters.
configuration = saasus_sdk_python.src.awsmarketplace.Configuration(
    host = "https://api.saasus.io/v1/awsmarketplace"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = saasus_sdk_python.src.awsmarketplace.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with saasus_sdk_python.src.awsmarketplace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = saasus_sdk_python.src.awsmarketplace.AwsMarketplaceApi(api_client)
    update_settings_param = saasus_sdk_python.src.awsmarketplace.UpdateSettingsParam() # UpdateSettingsParam |  (optional)

    try:
        # AWS Marketplaceの設定を更新(Update AWS Marketplace Settings)
        api_instance.update_settings(update_settings_param=update_settings_param)
    except Exception as e:
        print("Exception when calling AwsMarketplaceApi->update_settings: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_settings_param** | [**UpdateSettingsParam**](UpdateSettingsParam.md)|  | [optional] 

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

# **verify_registration_token**
> verify_registration_token(verify_registration_token_param=verify_registration_token_param)

Registration Tokenを検証(Verify Registration Token)

Registration Tokenを検証します。  Verify Registration Token. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.awsmarketplace
from saasus_sdk_python.src.awsmarketplace.models.verify_registration_token_param import VerifyRegistrationTokenParam
from saasus_sdk_python.src.awsmarketplace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.saasus.io/v1/awsmarketplace
# See configuration.py for a list of all supported configuration parameters.
configuration = saasus_sdk_python.src.awsmarketplace.Configuration(
    host = "https://api.saasus.io/v1/awsmarketplace"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = saasus_sdk_python.src.awsmarketplace.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with saasus_sdk_python.src.awsmarketplace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = saasus_sdk_python.src.awsmarketplace.AwsMarketplaceApi(api_client)
    verify_registration_token_param = saasus_sdk_python.src.awsmarketplace.VerifyRegistrationTokenParam() # VerifyRegistrationTokenParam |  (optional)

    try:
        # Registration Tokenを検証(Verify Registration Token)
        api_instance.verify_registration_token(verify_registration_token_param=verify_registration_token_param)
    except Exception as e:
        print("Exception when calling AwsMarketplaceApi->verify_registration_token: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **verify_registration_token_param** | [**VerifyRegistrationTokenParam**](VerifyRegistrationTokenParam.md)|  | [optional] 

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


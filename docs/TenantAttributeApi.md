# saasus_sdk_python.TenantAttributeApi

All URIs are relative to *https://api.saasus.io/v1/auth*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tenant_attribute**](TenantAttributeApi.md#create_tenant_attribute) | **POST** /tenant-attributes | テナント属性の作成(Create Tenant Attribute)
[**delete_tenant_attribute**](TenantAttributeApi.md#delete_tenant_attribute) | **DELETE** /tenant-attributes/{attribute_name} | テナント属性の削除(Delete Tenant Attribute)
[**get_tenant_attributes**](TenantAttributeApi.md#get_tenant_attributes) | **GET** /tenant-attributes | テナント属性の一覧を取得(Get Tenant Attributes)


# **create_tenant_attribute**
> Attribute create_tenant_attribute(body=body)

テナント属性の作成(Create Tenant Attribute)

SaaSus Platform で管理する、テナントの追加属性の登録を行います。 例えばテナントの呼び名やメモなどをを持たせることができ、SaaSからSaaSus SDK/APIを利用して取得することができます。  Register additional tenant attributes to be managed by SaaSus Platform. For example, tenant name, memo, etc., then get the attributes from SaaS using the SaaSus SDK/API. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python
from saasus_sdk_python.models.attribute import Attribute
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
    api_instance = saasus_sdk_python.TenantAttributeApi(api_client)
    body = saasus_sdk_python.Attribute() # Attribute |  (optional)

    try:
        # テナント属性の作成(Create Tenant Attribute)
        api_response = api_instance.create_tenant_attribute(body=body)
        print("The response of TenantAttributeApi->create_tenant_attribute:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantAttributeApi->create_tenant_attribute: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Attribute**|  | [optional] 

### Return type

[**Attribute**](Attribute.md)

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

# **delete_tenant_attribute**
> delete_tenant_attribute(attribute_name)

テナント属性の削除(Delete Tenant Attribute)

SaaSus Platform で管理する、テナントの追加属性の削除を行います。  Deletes tenant attributes managed by SaaSus Platform. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python
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
    api_instance = saasus_sdk_python.TenantAttributeApi(api_client)
    attribute_name = 'birthday' # str | 属性名(Attribute Name)

    try:
        # テナント属性の削除(Delete Tenant Attribute)
        api_instance.delete_tenant_attribute(attribute_name)
    except Exception as e:
        print("Exception when calling TenantAttributeApi->delete_tenant_attribute: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute_name** | **str**| 属性名(Attribute Name) | 

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

# **get_tenant_attributes**
> TenantAttributes get_tenant_attributes()

テナント属性の一覧を取得(Get Tenant Attributes)

SaaSus Platform で管理する、テナントの追加属性の定義を取得します。 例えばテナントの呼び名やメモなどをを持たせることができ、SaaSからSaaSus SDK/APIを利用して取得することができます。  Get definitions for additional tenant attributes managed by the SaaSus Platform. For example, tenant name, memo, etc., then get the attributes from SaaS using the SaaSus SDK/API. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python
from saasus_sdk_python.models.tenant_attributes import TenantAttributes
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
    api_instance = saasus_sdk_python.TenantAttributeApi(api_client)

    try:
        # テナント属性の一覧を取得(Get Tenant Attributes)
        api_response = api_instance.get_tenant_attributes()
        print("The response of TenantAttributeApi->get_tenant_attributes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantAttributeApi->get_tenant_attributes: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**TenantAttributes**](TenantAttributes.md)

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


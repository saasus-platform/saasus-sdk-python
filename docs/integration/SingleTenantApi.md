# saasus_sdk_python.src.auth.SingleTenantApi

All URIs are relative to *https://api.saasus.io/v1/auth*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cloud_formation_launch_stack_link_for_single_tenant**](SingleTenantApi.md#get_cloud_formation_launch_stack_link_for_single_tenant) | **GET** /single-tenant/cloudformation-launch-stack-link | Get CloudFormation Stack Launch Link For SaaS Infrastructure Management
[**get_single_tenant_settings**](SingleTenantApi.md#get_single_tenant_settings) | **GET** /single-tenant/settings | Retrieve the settings of the SaaS Infrastructure Management.
[**update_single_tenant_settings**](SingleTenantApi.md#update_single_tenant_settings) | **PATCH** /single-tenant/settings | Update configuration information for SaaS Infrastructure Management


# **get_cloud_formation_launch_stack_link_for_single_tenant**
> CloudFormationLaunchStackLink get_cloud_formation_launch_stack_link_for_single_tenant()

Get CloudFormation Stack Launch Link For SaaS Infrastructure Management

Get the CloudFormation stack activation link for SaaS Infrastructure Management. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.auth
from saasus_sdk_python.src.auth.models.cloud_formation_launch_stack_link import CloudFormationLaunchStackLink
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
    api_instance = saasus_sdk_python.src.auth.SingleTenantApi(api_client)

    try:
        # Get CloudFormation Stack Launch Link For SaaS Infrastructure Management
        api_response = api_instance.get_cloud_formation_launch_stack_link_for_single_tenant()
        print("The response of SingleTenantApi->get_cloud_formation_launch_stack_link_for_single_tenant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SingleTenantApi->get_cloud_formation_launch_stack_link_for_single_tenant: %s\n" % e)
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

# **get_single_tenant_settings**
> SingleTenantSettings get_single_tenant_settings()

Retrieve the settings of the SaaS Infrastructure Management.

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.auth
from saasus_sdk_python.src.auth.models.single_tenant_settings import SingleTenantSettings
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
    api_instance = saasus_sdk_python.src.auth.SingleTenantApi(api_client)

    try:
        # Retrieve the settings of the SaaS Infrastructure Management.
        api_response = api_instance.get_single_tenant_settings()
        print("The response of SingleTenantApi->get_single_tenant_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SingleTenantApi->get_single_tenant_settings: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**SingleTenantSettings**](SingleTenantSettings.md)

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

# **update_single_tenant_settings**
> update_single_tenant_settings(update_single_tenant_settings_param=update_single_tenant_settings_param)

Update configuration information for SaaS Infrastructure Management

Updates configuration information for SaaS Infrastructure Management Returns error if SaaS Infrastructure Management feature cannot be enabled. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.auth
from saasus_sdk_python.src.auth.models.update_single_tenant_settings_param import UpdateSingleTenantSettingsParam
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
    api_instance = saasus_sdk_python.src.auth.SingleTenantApi(api_client)
    update_single_tenant_settings_param = saasus_sdk_python.src.auth.UpdateSingleTenantSettingsParam() # UpdateSingleTenantSettingsParam |  (optional)

    try:
        # Update configuration information for SaaS Infrastructure Management
        api_instance.update_single_tenant_settings(update_single_tenant_settings_param=update_single_tenant_settings_param)
    except Exception as e:
        print("Exception when calling SingleTenantApi->update_single_tenant_settings: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_single_tenant_settings_param** | [**UpdateSingleTenantSettingsParam**](UpdateSingleTenantSettingsParam.md)|  | [optional] 

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


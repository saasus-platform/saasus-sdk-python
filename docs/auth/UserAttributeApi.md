# saasus_sdk_python.src.auth.UserAttributeApi

All URIs are relative to *https://api.saasus.io/v1/auth*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_saas_user_attribute**](UserAttributeApi.md#create_saas_user_attribute) | **POST** /saas-user-attributes | Create SaaS User Attributes
[**create_user_attribute**](UserAttributeApi.md#create_user_attribute) | **POST** /user-attributes | Create User Attributes
[**delete_user_attribute**](UserAttributeApi.md#delete_user_attribute) | **DELETE** /user-attributes/{attribute_name} | Delete User Attribute
[**get_user_attributes**](UserAttributeApi.md#get_user_attributes) | **GET** /user-attributes | Get User Attributes


# **create_saas_user_attribute**
> Attribute create_saas_user_attribute(body=body)

Create SaaS User Attributes

Create additional SaaS user attributes to be kept on the SaaSus Platform. You can give common values to all tenants. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.auth
from saasus_sdk_python.src.auth.models.attribute import Attribute
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
    api_instance = saasus_sdk_python.src.auth.UserAttributeApi(api_client)
    body = saasus_sdk_python.src.auth.Attribute() # Attribute |  (optional)

    try:
        # Create SaaS User Attributes
        api_response = api_instance.create_saas_user_attribute(body=body)
        print("The response of UserAttributeApi->create_saas_user_attribute:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserAttributeApi->create_saas_user_attribute: %s\n" % e)
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

# **create_user_attribute**
> Attribute create_user_attribute(body=body)

Create User Attributes

Create additional user attributes to be kept on the SaaSus Platform. You can give different values to each tenant. For example, you can define items associated with a user, such as user name, birthday, etc. If you don't want personal information on the SaaS Platform side, personal information can be kept on the SaaS side without user attribute definition. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.auth
from saasus_sdk_python.src.auth.models.attribute import Attribute
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
    api_instance = saasus_sdk_python.src.auth.UserAttributeApi(api_client)
    body = saasus_sdk_python.src.auth.Attribute() # Attribute |  (optional)

    try:
        # Create User Attributes
        api_response = api_instance.create_user_attribute(body=body)
        print("The response of UserAttributeApi->create_user_attribute:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserAttributeApi->create_user_attribute: %s\n" % e)
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

# **delete_user_attribute**
> delete_user_attribute(attribute_name)

Delete User Attribute

Delete user attributes kept on the SaaSus Platform. 

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
    api_instance = saasus_sdk_python.src.auth.UserAttributeApi(api_client)
    attribute_name = 'birthday' # str | Attribute Name

    try:
        # Delete User Attribute
        api_instance.delete_user_attribute(attribute_name)
    except Exception as e:
        print("Exception when calling UserAttributeApi->delete_user_attribute: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute_name** | **str**| Attribute Name | 

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

# **get_user_attributes**
> UserAttributes get_user_attributes()

Get User Attributes

Get additional attributes of the user saved in the SaaSus Platform. For example, you can define items associated with a user, such as user name, birthday, etc. If you don't want personal information on the SaaS Platform side, personal information can be kept on the SaaS side without user attribute definition. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.auth
from saasus_sdk_python.src.auth.models.user_attributes import UserAttributes
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
    api_instance = saasus_sdk_python.src.auth.UserAttributeApi(api_client)

    try:
        # Get User Attributes
        api_response = api_instance.get_user_attributes()
        print("The response of UserAttributeApi->get_user_attributes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserAttributeApi->get_user_attributes: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**UserAttributes**](UserAttributes.md)

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


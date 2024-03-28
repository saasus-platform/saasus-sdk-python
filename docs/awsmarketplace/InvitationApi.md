# saasus_sdk_python.src.auth.InvitationApi

All URIs are relative to *https://api.saasus.io/v1/auth*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tenant_invitation**](InvitationApi.md#create_tenant_invitation) | **POST** /tenants/{tenant_id}/invitations | Create Tenant Invitation
[**delete_tenant_invitation**](InvitationApi.md#delete_tenant_invitation) | **DELETE** /tenants/{tenant_id}/invitations/{invitation_id} | Delete Tenant Invitation
[**get_invitation_validity**](InvitationApi.md#get_invitation_validity) | **GET** /invitations/{invitation_id}/validity | Get Invitation Validity
[**get_tenant_invitation**](InvitationApi.md#get_tenant_invitation) | **GET** /tenants/{tenant_id}/invitations/{invitation_id} | Get Tenant Invitation
[**get_tenant_invitations**](InvitationApi.md#get_tenant_invitations) | **GET** /tenants/{tenant_id}/invitations | Get Tenant Invitations
[**validate_invitation**](InvitationApi.md#validate_invitation) | **PATCH** /invitations/{invitation_id}/validate | Validate Invitation


# **create_tenant_invitation**
> Invitation create_tenant_invitation(tenant_id, create_tenant_invitation_param=create_tenant_invitation_param)

Create Tenant Invitation

Create an invitation to the tenant. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.auth
from saasus_sdk_python.src.auth.models.create_tenant_invitation_param import CreateTenantInvitationParam
from saasus_sdk_python.src.auth.models.invitation import Invitation
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
    api_instance = saasus_sdk_python.src.auth.InvitationApi(api_client)
    tenant_id = 'tenant_id_example' # str | Tenant ID
    create_tenant_invitation_param = saasus_sdk_python.src.auth.CreateTenantInvitationParam() # CreateTenantInvitationParam |  (optional)

    try:
        # Create Tenant Invitation
        api_response = api_instance.create_tenant_invitation(tenant_id, create_tenant_invitation_param=create_tenant_invitation_param)
        print("The response of InvitationApi->create_tenant_invitation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvitationApi->create_tenant_invitation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant ID | 
 **create_tenant_invitation_param** | [**CreateTenantInvitationParam**](CreateTenantInvitationParam.md)|  | [optional] 

### Return type

[**Invitation**](Invitation.md)

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

# **delete_tenant_invitation**
> delete_tenant_invitation(tenant_id, invitation_id)

Delete Tenant Invitation

Delete an invitation for the tenant. 

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
    api_instance = saasus_sdk_python.src.auth.InvitationApi(api_client)
    tenant_id = 'tenant_id_example' # str | Tenant ID
    invitation_id = 'invitation_id_example' # str | Invitation ID

    try:
        # Delete Tenant Invitation
        api_instance.delete_tenant_invitation(tenant_id, invitation_id)
    except Exception as e:
        print("Exception when calling InvitationApi->delete_tenant_invitation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant ID | 
 **invitation_id** | **str**| Invitation ID | 

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

# **get_invitation_validity**
> InvitationValidity get_invitation_validity(invitation_id)

Get Invitation Validity

Get the validity of an invitation to the tenant. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.auth
from saasus_sdk_python.src.auth.models.invitation_validity import InvitationValidity
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
    api_instance = saasus_sdk_python.src.auth.InvitationApi(api_client)
    invitation_id = 'invitation_id_example' # str | Invitation ID

    try:
        # Get Invitation Validity
        api_response = api_instance.get_invitation_validity(invitation_id)
        print("The response of InvitationApi->get_invitation_validity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvitationApi->get_invitation_validity: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invitation_id** | **str**| Invitation ID | 

### Return type

[**InvitationValidity**](InvitationValidity.md)

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

# **get_tenant_invitation**
> Invitation get_tenant_invitation(tenant_id, invitation_id)

Get Tenant Invitation

Get invitation information for the tenant. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.auth
from saasus_sdk_python.src.auth.models.invitation import Invitation
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
    api_instance = saasus_sdk_python.src.auth.InvitationApi(api_client)
    tenant_id = 'tenant_id_example' # str | Tenant ID
    invitation_id = 'invitation_id_example' # str | Invitation ID

    try:
        # Get Tenant Invitation
        api_response = api_instance.get_tenant_invitation(tenant_id, invitation_id)
        print("The response of InvitationApi->get_tenant_invitation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvitationApi->get_tenant_invitation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant ID | 
 **invitation_id** | **str**| Invitation ID | 

### Return type

[**Invitation**](Invitation.md)

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

# **get_tenant_invitations**
> Invitations get_tenant_invitations(tenant_id)

Get Tenant Invitations

Get a list of invitations to the tenant. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.auth
from saasus_sdk_python.src.auth.models.invitations import Invitations
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
    api_instance = saasus_sdk_python.src.auth.InvitationApi(api_client)
    tenant_id = 'tenant_id_example' # str | Tenant ID

    try:
        # Get Tenant Invitations
        api_response = api_instance.get_tenant_invitations(tenant_id)
        print("The response of InvitationApi->get_tenant_invitations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvitationApi->get_tenant_invitations: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant ID | 

### Return type

[**Invitations**](Invitations.md)

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

# **validate_invitation**
> validate_invitation(invitation_id, validate_invitation_param=validate_invitation_param)

Validate Invitation

Validate an invitation to the tenant. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.auth
from saasus_sdk_python.src.auth.models.validate_invitation_param import ValidateInvitationParam
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
    api_instance = saasus_sdk_python.src.auth.InvitationApi(api_client)
    invitation_id = 'invitation_id_example' # str | Invitation ID
    validate_invitation_param = saasus_sdk_python.src.auth.ValidateInvitationParam() # ValidateInvitationParam |  (optional)

    try:
        # Validate Invitation
        api_instance.validate_invitation(invitation_id, validate_invitation_param=validate_invitation_param)
    except Exception as e:
        print("Exception when calling InvitationApi->validate_invitation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invitation_id** | **str**| Invitation ID | 
 **validate_invitation_param** | [**ValidateInvitationParam**](ValidateInvitationParam.md)|  | [optional] 

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


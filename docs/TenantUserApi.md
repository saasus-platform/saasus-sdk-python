# saasus_sdk_python.TenantUserApi

All URIs are relative to *https://api.saasus.io/v1/auth*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tenant_user**](TenantUserApi.md#create_tenant_user) | **POST** /tenants/{tenant_id}/users | テナントにユーザーを作成(Create Tenant User)
[**create_tenant_user_roles**](TenantUserApi.md#create_tenant_user_roles) | **POST** /tenants/{tenant_id}/users/{user_id}/envs/{env_id}/roles | テナントのユーザー情報に役割(ロール)を作成(Create Tenant User Role)
[**delete_tenant_user**](TenantUserApi.md#delete_tenant_user) | **DELETE** /tenants/{tenant_id}/users/{user_id} | テナントのユーザー情報を削除(Delete Tenant User)
[**delete_tenant_user_role**](TenantUserApi.md#delete_tenant_user_role) | **DELETE** /tenants/{tenant_id}/users/{user_id}/envs/{env_id}/roles/{role_name} | テナントのユーザーから役割(ロール)を削除(Remove Role From Tenant User)
[**get_all_tenant_user**](TenantUserApi.md#get_all_tenant_user) | **GET** /tenants/all/users/{user_id} | ユーザー情報を取得(Get User Info)
[**get_all_tenant_users**](TenantUserApi.md#get_all_tenant_users) | **GET** /tenants/all/users | ユーザー一覧を取得(Get Users)
[**get_tenant_user**](TenantUserApi.md#get_tenant_user) | **GET** /tenants/{tenant_id}/users/{user_id} | テナントのユーザー情報を取得(Get Tenant User)
[**get_tenant_users**](TenantUserApi.md#get_tenant_users) | **GET** /tenants/{tenant_id}/users | テナントのユーザー一覧を取得(Get Tenant Users)
[**update_tenant_user**](TenantUserApi.md#update_tenant_user) | **PATCH** /tenants/{tenant_id}/users/{user_id} | テナントのユーザー属性情報を更新(Update Tenant User Attribute)


# **create_tenant_user**
> User create_tenant_user(tenant_id, create_tenant_user_param=create_tenant_user_param)

テナントにユーザーを作成(Create Tenant User)

テナントにユーザーを作成します。 attributesを空のオブジェクトにした場合、追加属性は空で作成されます。  Create a tenant user. If attributes is empty, the additional attributes will be created empty. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python
from saasus_sdk_python.models.create_tenant_user_param import CreateTenantUserParam
from saasus_sdk_python.models.user import User
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
    api_instance = saasus_sdk_python.TenantUserApi(api_client)
    tenant_id = 'tenant_id_example' # str | テナントID(Tenant ID)
    create_tenant_user_param = saasus_sdk_python.CreateTenantUserParam() # CreateTenantUserParam |  (optional)

    try:
        # テナントにユーザーを作成(Create Tenant User)
        api_response = api_instance.create_tenant_user(tenant_id, create_tenant_user_param=create_tenant_user_param)
        print("The response of TenantUserApi->create_tenant_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantUserApi->create_tenant_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| テナントID(Tenant ID) | 
 **create_tenant_user_param** | [**CreateTenantUserParam**](CreateTenantUserParam.md)|  | [optional] 

### Return type

[**User**](User.md)

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

# **create_tenant_user_roles**
> create_tenant_user_roles(tenant_id, user_id, env_id, create_tenant_user_roles_param=create_tenant_user_roles_param)

テナントのユーザー情報に役割(ロール)を作成(Create Tenant User Role)

テナントのユーザーに役割(ロール)を作成します。  Create roles on tenant users. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python
from saasus_sdk_python.models.create_tenant_user_roles_param import CreateTenantUserRolesParam
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
    api_instance = saasus_sdk_python.TenantUserApi(api_client)
    tenant_id = 'tenant_id_example' # str | テナントID(Tenant ID)
    user_id = 'f94bfffc-8be2-11ec-b41a-0242ac120004' # str | ユーザーID(User ID)
    env_id = 56 # int | 環境ID(Env ID)
    create_tenant_user_roles_param = saasus_sdk_python.CreateTenantUserRolesParam() # CreateTenantUserRolesParam |  (optional)

    try:
        # テナントのユーザー情報に役割(ロール)を作成(Create Tenant User Role)
        api_instance.create_tenant_user_roles(tenant_id, user_id, env_id, create_tenant_user_roles_param=create_tenant_user_roles_param)
    except Exception as e:
        print("Exception when calling TenantUserApi->create_tenant_user_roles: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| テナントID(Tenant ID) | 
 **user_id** | **str**| ユーザーID(User ID) | 
 **env_id** | **int**| 環境ID(Env ID) | 
 **create_tenant_user_roles_param** | [**CreateTenantUserRolesParam**](CreateTenantUserRolesParam.md)|  | [optional] 

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
**201** | Created |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tenant_user**
> delete_tenant_user(tenant_id, user_id)

テナントのユーザー情報を削除(Delete Tenant User)

テナントからユーザーを削除します。  Delete a user from your tenant. 

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
    api_instance = saasus_sdk_python.TenantUserApi(api_client)
    tenant_id = 'tenant_id_example' # str | テナントID(Tenant ID)
    user_id = 'f94bfffc-8be2-11ec-b41a-0242ac120004' # str | ユーザーID(User ID)

    try:
        # テナントのユーザー情報を削除(Delete Tenant User)
        api_instance.delete_tenant_user(tenant_id, user_id)
    except Exception as e:
        print("Exception when calling TenantUserApi->delete_tenant_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| テナントID(Tenant ID) | 
 **user_id** | **str**| ユーザーID(User ID) | 

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

# **delete_tenant_user_role**
> delete_tenant_user_role(tenant_id, user_id, env_id, role_name)

テナントのユーザーから役割(ロール)を削除(Remove Role From Tenant User)

テナントのユーザーから役割(ロール)を削除します。  Remove a role from a tenant user. 

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
    api_instance = saasus_sdk_python.TenantUserApi(api_client)
    tenant_id = 'tenant_id_example' # str | テナントID(Tenant ID)
    user_id = 'f94bfffc-8be2-11ec-b41a-0242ac120004' # str | ユーザーID(User ID)
    env_id = 56 # int | 環境ID(Env ID)
    role_name = 'admin' # str | 役割(ロール)名(role name)

    try:
        # テナントのユーザーから役割(ロール)を削除(Remove Role From Tenant User)
        api_instance.delete_tenant_user_role(tenant_id, user_id, env_id, role_name)
    except Exception as e:
        print("Exception when calling TenantUserApi->delete_tenant_user_role: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| テナントID(Tenant ID) | 
 **user_id** | **str**| ユーザーID(User ID) | 
 **env_id** | **int**| 環境ID(Env ID) | 
 **role_name** | **str**| 役割(ロール)名(role name) | 

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

# **get_all_tenant_user**
> Users get_all_tenant_user(user_id)

ユーザー情報を取得(Get User Info)

ユーザーIDからテナントに所属しているユーザー情報を取得します。 複数テナントに所属している場合は別のオブジェクトとして返却されます。  Get information on user belonging to the tenant from the user ID. If the user belongs to multiple tenants, it will be returned as another object. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python
from saasus_sdk_python.models.users import Users
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
    api_instance = saasus_sdk_python.TenantUserApi(api_client)
    user_id = 'f94bfffc-8be2-11ec-b41a-0242ac120004' # str | ユーザーID(User ID)

    try:
        # ユーザー情報を取得(Get User Info)
        api_response = api_instance.get_all_tenant_user(user_id)
        print("The response of TenantUserApi->get_all_tenant_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantUserApi->get_all_tenant_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ユーザーID(User ID) | 

### Return type

[**Users**](Users.md)

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

# **get_all_tenant_users**
> Users get_all_tenant_users()

ユーザー一覧を取得(Get Users)

テナントに所属しているユーザー全件を取得します。 複数テナントに所属する同一ユーザーは別のオブジェクトとして返却されます。 idは一意ではありません。  Get all users belonging to the tenant. The same user belonging to multiple tenants will be returned as a different object. Id is not unique. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python
from saasus_sdk_python.models.users import Users
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
    api_instance = saasus_sdk_python.TenantUserApi(api_client)

    try:
        # ユーザー一覧を取得(Get Users)
        api_response = api_instance.get_all_tenant_users()
        print("The response of TenantUserApi->get_all_tenant_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantUserApi->get_all_tenant_users: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**Users**](Users.md)

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

# **get_tenant_user**
> User get_tenant_user(tenant_id, user_id)

テナントのユーザー情報を取得(Get Tenant User)

テナントのユーザーをIDから一件取得します。  Get one tenant user by specific ID. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python
from saasus_sdk_python.models.user import User
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
    api_instance = saasus_sdk_python.TenantUserApi(api_client)
    tenant_id = 'tenant_id_example' # str | テナントID(Tenant ID)
    user_id = 'f94bfffc-8be2-11ec-b41a-0242ac120004' # str | ユーザーID(User ID)

    try:
        # テナントのユーザー情報を取得(Get Tenant User)
        api_response = api_instance.get_tenant_user(tenant_id, user_id)
        print("The response of TenantUserApi->get_tenant_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantUserApi->get_tenant_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| テナントID(Tenant ID) | 
 **user_id** | **str**| ユーザーID(User ID) | 

### Return type

[**User**](User.md)

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

# **get_tenant_users**
> Users get_tenant_users(tenant_id)

テナントのユーザー一覧を取得(Get Tenant Users)

テナントに所属するユーザーを全件取得します。 idは一意です。  Get all the users belonging to the tenant. Id is unique. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python
from saasus_sdk_python.models.users import Users
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
    api_instance = saasus_sdk_python.TenantUserApi(api_client)
    tenant_id = 'tenant_id_example' # str | テナントID(Tenant ID)

    try:
        # テナントのユーザー一覧を取得(Get Tenant Users)
        api_response = api_instance.get_tenant_users(tenant_id)
        print("The response of TenantUserApi->get_tenant_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantUserApi->get_tenant_users: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| テナントID(Tenant ID) | 

### Return type

[**Users**](Users.md)

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

# **update_tenant_user**
> update_tenant_user(tenant_id, user_id, update_tenant_user_param=update_tenant_user_param)

テナントのユーザー属性情報を更新(Update Tenant User Attribute)

テナントのユーザー属性情報を更新します。  Update tenant user attributes. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python
from saasus_sdk_python.models.update_tenant_user_param import UpdateTenantUserParam
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
    api_instance = saasus_sdk_python.TenantUserApi(api_client)
    tenant_id = 'tenant_id_example' # str | テナントID(Tenant ID)
    user_id = 'f94bfffc-8be2-11ec-b41a-0242ac120004' # str | ユーザーID(User ID)
    update_tenant_user_param = saasus_sdk_python.UpdateTenantUserParam() # UpdateTenantUserParam |  (optional)

    try:
        # テナントのユーザー属性情報を更新(Update Tenant User Attribute)
        api_instance.update_tenant_user(tenant_id, user_id, update_tenant_user_param=update_tenant_user_param)
    except Exception as e:
        print("Exception when calling TenantUserApi->update_tenant_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| テナントID(Tenant ID) | 
 **user_id** | **str**| ユーザーID(User ID) | 
 **update_tenant_user_param** | [**UpdateTenantUserParam**](UpdateTenantUserParam.md)|  | [optional] 

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


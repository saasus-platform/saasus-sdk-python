# saasus_sdk_python.SaasusTenantApi

All URIs are relative to *https://api.saasus.io/v1/auth*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_api_key**](SaasusTenantApi.md#create_api_key) | **POST** /apikeys | APIキーを作成(Create API Key)
[**delete_api_key**](SaasusTenantApi.md#delete_api_key) | **DELETE** /apikeys/{api_key} | APIキーを削除(Delete API Key)
[**get_api_keys**](SaasusTenantApi.md#get_api_keys) | **GET** /apikeys | APIキー一覧を取得(Get API Keys)
[**get_client_secret**](SaasusTenantApi.md#get_client_secret) | **GET** /client-secret | クライアントシークレットを取得(Get Client Secret)
[**get_saas_id**](SaasusTenantApi.md#get_saas_id) | **GET** /saasid | SaasIDを取得(Get SaasID)
[**update_client_secret**](SaasusTenantApi.md#update_client_secret) | **PATCH** /client-secret | クライアントシークレットを更新(Update Client Secret)
[**update_saas_id**](SaasusTenantApi.md#update_saas_id) | **PATCH** /saasid | SaasIDを更新(Update SaasID)


# **create_api_key**
> create_api_key()

APIキーを作成(Create API Key)

サーバサイド用に API キーを発行します。 最大 2 つまで発行できます。  Generate an API key for the server side. Up to 2 can be generated. 

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
    api_instance = saasus_sdk_python.SaasusTenantApi(api_client)

    try:
        # APIキーを作成(Create API Key)
        api_instance.create_api_key()
    except Exception as e:
        print("Exception when calling SaasusTenantApi->create_api_key: %s\n" % e)
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
**201** | Created |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_api_key**
> delete_api_key(api_key)

APIキーを削除(Delete API Key)

サーバサイド用の API キーを削除します。  Delete API Key. 

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
    api_instance = saasus_sdk_python.SaasusTenantApi(api_client)
    api_key = 'ZDMiIHN0UmVmOmRvY3VtZW50SUQ9Inhtc' # str | APIキー(API key)

    try:
        # APIキーを削除(Delete API Key)
        api_instance.delete_api_key(api_key)
    except Exception as e:
        print("Exception when calling SaasusTenantApi->delete_api_key: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| APIキー(API key) | 

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

# **get_api_keys**
> ApiKeys get_api_keys()

APIキー一覧を取得(Get API Keys)

サーバサイド用に API キーを取得します。 最大 2 つまで発行できます。  Get API key for the server side. Up to 2 can be generated. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python
from saasus_sdk_python.models.api_keys import ApiKeys
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
    api_instance = saasus_sdk_python.SaasusTenantApi(api_client)

    try:
        # APIキー一覧を取得(Get API Keys)
        api_response = api_instance.get_api_keys()
        print("The response of SaasusTenantApi->get_api_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SaasusTenantApi->get_api_keys: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiKeys**](ApiKeys.md)

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

# **get_client_secret**
> ClientSecret get_client_secret()

クライアントシークレットを取得(Get Client Secret)

API リクエストでアプリが使用する固定文字列を取得します。  Gets the fixed string that the app uses in API requests. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python
from saasus_sdk_python.models.client_secret import ClientSecret
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
    api_instance = saasus_sdk_python.SaasusTenantApi(api_client)

    try:
        # クライアントシークレットを取得(Get Client Secret)
        api_response = api_instance.get_client_secret()
        print("The response of SaasusTenantApi->get_client_secret:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SaasusTenantApi->get_client_secret: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**ClientSecret**](ClientSecret.md)

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

# **get_saas_id**
> SaasId get_saas_id()

SaasIDを取得(Get SaasID)

テナントのSaasIDを取得します。 SaaSus API および SaaSus SDK にて利用します。  Get the tenant's SaasID. Used by SaaSus API and SaaSus SDK. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python
from saasus_sdk_python.models.saas_id import SaasId
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
    api_instance = saasus_sdk_python.SaasusTenantApi(api_client)

    try:
        # SaasIDを取得(Get SaasID)
        api_response = api_instance.get_saas_id()
        print("The response of SaasusTenantApi->get_saas_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SaasusTenantApi->get_saas_id: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**SaasId**](SaasId.md)

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

# **update_client_secret**
> update_client_secret()

クライアントシークレットを更新(Update Client Secret)

API リクエストでアプリが使用する固定文字列を再発行します。 既に稼働中のSaaSアプリケーションに設定している場合には、動作に影響があります。  Reissue fixed strings that apps use in API requests. If changed on a SaaS application that is already running, it will affect the behavior. 

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
    api_instance = saasus_sdk_python.SaasusTenantApi(api_client)

    try:
        # クライアントシークレットを更新(Update Client Secret)
        api_instance.update_client_secret()
    except Exception as e:
        print("Exception when calling SaasusTenantApi->update_client_secret: %s\n" % e)
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

# **update_saas_id**
> update_saas_id()

SaasIDを更新(Update SaasID)

テナントのSaasIDを更新します。 SaaSus API および SaaSus SDK にて利用します。 既に稼働中の SaaS アプリケーションに設定している場合には、動作に影響があります。  Update the tenant's SaasID. Used by SaaSus API and SaaSus SDK. If changed on an SaaS application that is already running, it will affect the behavior. 

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
    api_instance = saasus_sdk_python.SaasusTenantApi(api_client)

    try:
        # SaasIDを更新(Update SaasID)
        api_instance.update_saas_id()
    except Exception as e:
        print("Exception when calling SaasusTenantApi->update_saas_id: %s\n" % e)
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


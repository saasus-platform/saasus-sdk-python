# saasus_sdk_python.src.pricing.MeteringApi

All URIs are relative to *https://api.saasus.io/v1/pricing*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_metering_unit**](MeteringApi.md#create_metering_unit) | **POST** /metering/units | メータリングユニットの作成
[**delete_metering_unit_by_id**](MeteringApi.md#delete_metering_unit_by_id) | **DELETE** /metering/units/{metering_unit_id} | メータリングユニットを削除
[**delete_metering_unit_timestamp_count**](MeteringApi.md#delete_metering_unit_timestamp_count) | **DELETE** /metering/tenants/{tenant_id}/units/{metering_unit_name}/timestamp/{timestamp} | 指定したタイムスタンプのメータリングユニットカウントを削除
[**get_metering_unit_date_count_by_tenant_id_and_unit_name_and_date**](MeteringApi.md#get_metering_unit_date_count_by_tenant_id_and_unit_name_and_date) | **GET** /metering/tenants/{tenant_id}/units/{metering_unit_name}/date/{date} | 指定した日付のメータリングユニットカウントを取得
[**get_metering_unit_date_count_by_tenant_id_and_unit_name_and_date_period**](MeteringApi.md#get_metering_unit_date_count_by_tenant_id_and_unit_name_and_date_period) | **GET** /metering/tenants/{tenant_id}/units/{metering_unit_name}/date-period | 指定した日時期間のメータリングユニットカウントを取得
[**get_metering_unit_date_count_by_tenant_id_and_unit_name_today**](MeteringApi.md#get_metering_unit_date_count_by_tenant_id_and_unit_name_today) | **GET** /metering/tenants/{tenant_id}/units/{metering_unit_name}/today | 当日のメータリングユニットカウントを取得
[**get_metering_unit_date_counts_by_tenant_id_and_date**](MeteringApi.md#get_metering_unit_date_counts_by_tenant_id_and_date) | **GET** /metering/tenants/{tenant_id}/units/date/{date} | 指定日の全メータリングユニットカウントを取得
[**get_metering_unit_month_count_by_tenant_id_and_unit_name_and_month**](MeteringApi.md#get_metering_unit_month_count_by_tenant_id_and_unit_name_and_month) | **GET** /metering/tenants/{tenant_id}/units/{metering_unit_name}/month/{month} | 指定月のメータリングユニットカウントを取得
[**get_metering_unit_month_count_by_tenant_id_and_unit_name_this_month**](MeteringApi.md#get_metering_unit_month_count_by_tenant_id_and_unit_name_this_month) | **GET** /metering/tenants/{tenant_id}/units/{metering_unit_name}/thismonth | 当月のメータリングユニットカウントを取得
[**get_metering_unit_month_counts_by_tenant_id_and_month**](MeteringApi.md#get_metering_unit_month_counts_by_tenant_id_and_month) | **GET** /metering/tenants/{tenant_id}/units/month/{month} | 指定月の全メータリングユニットカウントを取得
[**get_metering_units**](MeteringApi.md#get_metering_units) | **GET** /metering/units | メータリングユニットを取得
[**update_metering_unit_by_id**](MeteringApi.md#update_metering_unit_by_id) | **PATCH** /metering/units/{metering_unit_id} | メータリングユニットを更新
[**update_metering_unit_timestamp_count**](MeteringApi.md#update_metering_unit_timestamp_count) | **PUT** /metering/tenants/{tenant_id}/units/{metering_unit_name}/timestamp/{timestamp} | 指定したタイムスタンプのメータリングユニットカウントを更新
[**update_metering_unit_timestamp_count_now**](MeteringApi.md#update_metering_unit_timestamp_count_now) | **PUT** /metering/tenants/{tenant_id}/units/{metering_unit_name}/now | 現在時刻のメータリングユニットカウントを更新


# **create_metering_unit**
> MeteringUnit create_metering_unit(body=body)

メータリングユニットの作成

メータリングユニットを作成します。 

### Example

* Bearer Authentication (Bearer):

```python
import time
import os
import saasus_sdk_python.src.pricing
from saasus_sdk_python.src.pricing.models.metering_unit import MeteringUnit
from saasus_sdk_python.src.pricing.models.metering_unit_props import MeteringUnitProps
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
    api_instance = saasus_sdk_python.src.pricing.MeteringApi(api_client)
    body = saasus_sdk_python.src.pricing.MeteringUnitProps() # MeteringUnitProps |  (optional)

    try:
        # メータリングユニットの作成
        api_response = api_instance.create_metering_unit(body=body)
        print("The response of MeteringApi->create_metering_unit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeteringApi->create_metering_unit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **MeteringUnitProps**|  | [optional] 

### Return type

[**MeteringUnit**](MeteringUnit.md)

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

# **delete_metering_unit_by_id**
> delete_metering_unit_by_id(metering_unit_id)

メータリングユニットを削除

メータリングユニットを削除します。 

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
    api_instance = saasus_sdk_python.src.pricing.MeteringApi(api_client)
    metering_unit_id = '46af35b5-60de-4cd8-9412-19a3a5d1f838' # str | メータリングユニットID

    try:
        # メータリングユニットを削除
        api_instance.delete_metering_unit_by_id(metering_unit_id)
    except Exception as e:
        print("Exception when calling MeteringApi->delete_metering_unit_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metering_unit_id** | **str**| メータリングユニットID | 

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

# **delete_metering_unit_timestamp_count**
> delete_metering_unit_timestamp_count(tenant_id, metering_unit_name, timestamp)

指定したタイムスタンプのメータリングユニットカウントを削除

指定したタイムスタンプのメータリングユニットカウントを削除します。

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
    api_instance = saasus_sdk_python.src.pricing.MeteringApi(api_client)
    tenant_id = '46af35b5-60de-4cd8-9412-19a3a5d1f838' # str | テナントID
    metering_unit_name = 'storage_unit' # str | 計測ユニット名
    timestamp = 1640995200 # int | タイムスタンプ

    try:
        # 指定したタイムスタンプのメータリングユニットカウントを削除
        api_instance.delete_metering_unit_timestamp_count(tenant_id, metering_unit_name, timestamp)
    except Exception as e:
        print("Exception when calling MeteringApi->delete_metering_unit_timestamp_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| テナントID | 
 **metering_unit_name** | **str**| 計測ユニット名 | 
 **timestamp** | **int**| タイムスタンプ | 

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

# **get_metering_unit_date_count_by_tenant_id_and_unit_name_and_date**
> MeteringUnitDateCount get_metering_unit_date_count_by_tenant_id_and_unit_name_and_date(tenant_id, metering_unit_name, var_date)

指定した日付のメータリングユニットカウントを取得

指定した日付のメータリングユニットカウントを取得します。 

### Example

* Bearer Authentication (Bearer):

```python
import time
import os
import saasus_sdk_python.src.pricing
from saasus_sdk_python.src.pricing.models.metering_unit_date_count import MeteringUnitDateCount
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
    api_instance = saasus_sdk_python.src.pricing.MeteringApi(api_client)
    tenant_id = '46af35b5-60de-4cd8-9412-19a3a5d1f838' # str | テナントID
    metering_unit_name = 'storage_unit' # str | 計測ユニット名
    var_date = '2022-01-01' # str | 日

    try:
        # 指定した日付のメータリングユニットカウントを取得
        api_response = api_instance.get_metering_unit_date_count_by_tenant_id_and_unit_name_and_date(tenant_id, metering_unit_name, var_date)
        print("The response of MeteringApi->get_metering_unit_date_count_by_tenant_id_and_unit_name_and_date:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeteringApi->get_metering_unit_date_count_by_tenant_id_and_unit_name_and_date: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| テナントID | 
 **metering_unit_name** | **str**| 計測ユニット名 | 
 **var_date** | **str**| 日 | 

### Return type

[**MeteringUnitDateCount**](MeteringUnitDateCount.md)

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

# **get_metering_unit_date_count_by_tenant_id_and_unit_name_and_date_period**
> MeteringUnitDatePeriodCounts get_metering_unit_date_count_by_tenant_id_and_unit_name_and_date_period(tenant_id, metering_unit_name, start_timestamp=start_timestamp, end_timestamp=end_timestamp)

指定した日時期間のメータリングユニットカウントを取得

指定した日時期間のメータリングユニットカウントを取得します。 

### Example

* Bearer Authentication (Bearer):

```python
import time
import os
import saasus_sdk_python.src.pricing
from saasus_sdk_python.src.pricing.models.metering_unit_date_period_counts import MeteringUnitDatePeriodCounts
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
    api_instance = saasus_sdk_python.src.pricing.MeteringApi(api_client)
    tenant_id = '46af35b5-60de-4cd8-9412-19a3a5d1f838' # str | テナントID
    metering_unit_name = 'storage_unit' # str | 計測ユニット名
    start_timestamp = 1640995200 # int | 開始日時 (optional)
    end_timestamp = 1640995200 # int | 終了日時 (optional)

    try:
        # 指定した日時期間のメータリングユニットカウントを取得
        api_response = api_instance.get_metering_unit_date_count_by_tenant_id_and_unit_name_and_date_period(tenant_id, metering_unit_name, start_timestamp=start_timestamp, end_timestamp=end_timestamp)
        print("The response of MeteringApi->get_metering_unit_date_count_by_tenant_id_and_unit_name_and_date_period:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeteringApi->get_metering_unit_date_count_by_tenant_id_and_unit_name_and_date_period: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| テナントID | 
 **metering_unit_name** | **str**| 計測ユニット名 | 
 **start_timestamp** | **int**| 開始日時 | [optional] 
 **end_timestamp** | **int**| 終了日時 | [optional] 

### Return type

[**MeteringUnitDatePeriodCounts**](MeteringUnitDatePeriodCounts.md)

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

# **get_metering_unit_date_count_by_tenant_id_and_unit_name_today**
> MeteringUnitDateCount get_metering_unit_date_count_by_tenant_id_and_unit_name_today(tenant_id, metering_unit_name)

当日のメータリングユニットカウントを取得

当日のメータリングユニットカウントを取得します。

### Example

* Bearer Authentication (Bearer):

```python
import time
import os
import saasus_sdk_python.src.pricing
from saasus_sdk_python.src.pricing.models.metering_unit_date_count import MeteringUnitDateCount
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
    api_instance = saasus_sdk_python.src.pricing.MeteringApi(api_client)
    tenant_id = '46af35b5-60de-4cd8-9412-19a3a5d1f838' # str | テナントID
    metering_unit_name = 'storage_unit' # str | 計測ユニット名

    try:
        # 当日のメータリングユニットカウントを取得
        api_response = api_instance.get_metering_unit_date_count_by_tenant_id_and_unit_name_today(tenant_id, metering_unit_name)
        print("The response of MeteringApi->get_metering_unit_date_count_by_tenant_id_and_unit_name_today:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeteringApi->get_metering_unit_date_count_by_tenant_id_and_unit_name_today: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| テナントID | 
 **metering_unit_name** | **str**| 計測ユニット名 | 

### Return type

[**MeteringUnitDateCount**](MeteringUnitDateCount.md)

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

# **get_metering_unit_date_counts_by_tenant_id_and_date**
> MeteringUnitDateCounts get_metering_unit_date_counts_by_tenant_id_and_date(tenant_id, var_date)

指定日の全メータリングユニットカウントを取得

指定した日の全メータリングユニットカウントを取得します。 

### Example

* Bearer Authentication (Bearer):

```python
import time
import os
import saasus_sdk_python.src.pricing
from saasus_sdk_python.src.pricing.models.metering_unit_date_counts import MeteringUnitDateCounts
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
    api_instance = saasus_sdk_python.src.pricing.MeteringApi(api_client)
    tenant_id = '46af35b5-60de-4cd8-9412-19a3a5d1f838' # str | テナントID
    var_date = '2022-01-01' # str | 日

    try:
        # 指定日の全メータリングユニットカウントを取得
        api_response = api_instance.get_metering_unit_date_counts_by_tenant_id_and_date(tenant_id, var_date)
        print("The response of MeteringApi->get_metering_unit_date_counts_by_tenant_id_and_date:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeteringApi->get_metering_unit_date_counts_by_tenant_id_and_date: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| テナントID | 
 **var_date** | **str**| 日 | 

### Return type

[**MeteringUnitDateCounts**](MeteringUnitDateCounts.md)

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

# **get_metering_unit_month_count_by_tenant_id_and_unit_name_and_month**
> MeteringUnitMonthCount get_metering_unit_month_count_by_tenant_id_and_unit_name_and_month(tenant_id, metering_unit_name, month)

指定月のメータリングユニットカウントを取得

指定した月のメータリングユニットカウントを取得します。 

### Example

* Bearer Authentication (Bearer):

```python
import time
import os
import saasus_sdk_python.src.pricing
from saasus_sdk_python.src.pricing.models.metering_unit_month_count import MeteringUnitMonthCount
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
    api_instance = saasus_sdk_python.src.pricing.MeteringApi(api_client)
    tenant_id = '46af35b5-60de-4cd8-9412-19a3a5d1f838' # str | テナントID
    metering_unit_name = 'storage_unit' # str | 計測ユニット名
    month = '2022-01' # str | 月

    try:
        # 指定月のメータリングユニットカウントを取得
        api_response = api_instance.get_metering_unit_month_count_by_tenant_id_and_unit_name_and_month(tenant_id, metering_unit_name, month)
        print("The response of MeteringApi->get_metering_unit_month_count_by_tenant_id_and_unit_name_and_month:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeteringApi->get_metering_unit_month_count_by_tenant_id_and_unit_name_and_month: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| テナントID | 
 **metering_unit_name** | **str**| 計測ユニット名 | 
 **month** | **str**| 月 | 

### Return type

[**MeteringUnitMonthCount**](MeteringUnitMonthCount.md)

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

# **get_metering_unit_month_count_by_tenant_id_and_unit_name_this_month**
> MeteringUnitMonthCount get_metering_unit_month_count_by_tenant_id_and_unit_name_this_month(tenant_id, metering_unit_name)

当月のメータリングユニットカウントを取得

当月のメータリングユニットカウントを取得します。

### Example

* Bearer Authentication (Bearer):

```python
import time
import os
import saasus_sdk_python.src.pricing
from saasus_sdk_python.src.pricing.models.metering_unit_month_count import MeteringUnitMonthCount
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
    api_instance = saasus_sdk_python.src.pricing.MeteringApi(api_client)
    tenant_id = '46af35b5-60de-4cd8-9412-19a3a5d1f838' # str | テナントID
    metering_unit_name = 'storage_unit' # str | 計測ユニット名

    try:
        # 当月のメータリングユニットカウントを取得
        api_response = api_instance.get_metering_unit_month_count_by_tenant_id_and_unit_name_this_month(tenant_id, metering_unit_name)
        print("The response of MeteringApi->get_metering_unit_month_count_by_tenant_id_and_unit_name_this_month:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeteringApi->get_metering_unit_month_count_by_tenant_id_and_unit_name_this_month: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| テナントID | 
 **metering_unit_name** | **str**| 計測ユニット名 | 

### Return type

[**MeteringUnitMonthCount**](MeteringUnitMonthCount.md)

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

# **get_metering_unit_month_counts_by_tenant_id_and_month**
> MeteringUnitMonthCounts get_metering_unit_month_counts_by_tenant_id_and_month(tenant_id, month)

指定月の全メータリングユニットカウントを取得

指定した月の全メータリングユニットカウントを取得します。 

### Example

* Bearer Authentication (Bearer):

```python
import time
import os
import saasus_sdk_python.src.pricing
from saasus_sdk_python.src.pricing.models.metering_unit_month_counts import MeteringUnitMonthCounts
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
    api_instance = saasus_sdk_python.src.pricing.MeteringApi(api_client)
    tenant_id = '46af35b5-60de-4cd8-9412-19a3a5d1f838' # str | テナントID
    month = '2022-01' # str | 月

    try:
        # 指定月の全メータリングユニットカウントを取得
        api_response = api_instance.get_metering_unit_month_counts_by_tenant_id_and_month(tenant_id, month)
        print("The response of MeteringApi->get_metering_unit_month_counts_by_tenant_id_and_month:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeteringApi->get_metering_unit_month_counts_by_tenant_id_and_month: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| テナントID | 
 **month** | **str**| 月 | 

### Return type

[**MeteringUnitMonthCounts**](MeteringUnitMonthCounts.md)

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

# **get_metering_units**
> MeteringUnits get_metering_units()

メータリングユニットを取得

全てのメータリングユニットを取得します。 

### Example

* Bearer Authentication (Bearer):

```python
import time
import os
import saasus_sdk_python.src.pricing
from saasus_sdk_python.src.pricing.models.metering_units import MeteringUnits
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
    api_instance = saasus_sdk_python.src.pricing.MeteringApi(api_client)

    try:
        # メータリングユニットを取得
        api_response = api_instance.get_metering_units()
        print("The response of MeteringApi->get_metering_units:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeteringApi->get_metering_units: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**MeteringUnits**](MeteringUnits.md)

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

# **update_metering_unit_by_id**
> update_metering_unit_by_id(metering_unit_id, body=body)

メータリングユニットを更新

メータリングユニットを更新します。 

### Example

* Bearer Authentication (Bearer):

```python
import time
import os
import saasus_sdk_python.src.pricing
from saasus_sdk_python.src.pricing.models.metering_unit_props import MeteringUnitProps
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
    api_instance = saasus_sdk_python.src.pricing.MeteringApi(api_client)
    metering_unit_id = '46af35b5-60de-4cd8-9412-19a3a5d1f838' # str | メータリングユニットID
    body = saasus_sdk_python.src.pricing.MeteringUnitProps() # MeteringUnitProps |  (optional)

    try:
        # メータリングユニットを更新
        api_instance.update_metering_unit_by_id(metering_unit_id, body=body)
    except Exception as e:
        print("Exception when calling MeteringApi->update_metering_unit_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metering_unit_id** | **str**| メータリングユニットID | 
 **body** | **MeteringUnitProps**|  | [optional] 

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

# **update_metering_unit_timestamp_count**
> MeteringUnitTimestampCount update_metering_unit_timestamp_count(tenant_id, metering_unit_name, timestamp, update_metering_unit_timestamp_count_param=update_metering_unit_timestamp_count_param)

指定したタイムスタンプのメータリングユニットカウントを更新

指定したタイムスタンプのメータリングユニットカウントを更新します。

### Example

* Bearer Authentication (Bearer):

```python
import time
import os
import saasus_sdk_python.src.pricing
from saasus_sdk_python.src.pricing.models.metering_unit_timestamp_count import MeteringUnitTimestampCount
from saasus_sdk_python.src.pricing.models.update_metering_unit_timestamp_count_param import UpdateMeteringUnitTimestampCountParam
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
    api_instance = saasus_sdk_python.src.pricing.MeteringApi(api_client)
    tenant_id = '46af35b5-60de-4cd8-9412-19a3a5d1f838' # str | テナントID
    metering_unit_name = 'storage_unit' # str | 計測ユニット名
    timestamp = 1640995200 # int | タイムスタンプ
    update_metering_unit_timestamp_count_param = saasus_sdk_python.src.pricing.UpdateMeteringUnitTimestampCountParam() # UpdateMeteringUnitTimestampCountParam |  (optional)

    try:
        # 指定したタイムスタンプのメータリングユニットカウントを更新
        api_response = api_instance.update_metering_unit_timestamp_count(tenant_id, metering_unit_name, timestamp, update_metering_unit_timestamp_count_param=update_metering_unit_timestamp_count_param)
        print("The response of MeteringApi->update_metering_unit_timestamp_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeteringApi->update_metering_unit_timestamp_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| テナントID | 
 **metering_unit_name** | **str**| 計測ユニット名 | 
 **timestamp** | **int**| タイムスタンプ | 
 **update_metering_unit_timestamp_count_param** | [**UpdateMeteringUnitTimestampCountParam**](UpdateMeteringUnitTimestampCountParam.md)|  | [optional] 

### Return type

[**MeteringUnitTimestampCount**](MeteringUnitTimestampCount.md)

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

# **update_metering_unit_timestamp_count_now**
> MeteringUnitTimestampCount update_metering_unit_timestamp_count_now(tenant_id, metering_unit_name, update_metering_unit_timestamp_count_now_param=update_metering_unit_timestamp_count_now_param)

現在時刻のメータリングユニットカウントを更新

現在時刻のメータリングユニットカウントを更新します。

### Example

* Bearer Authentication (Bearer):

```python
import time
import os
import saasus_sdk_python.src.pricing
from saasus_sdk_python.src.pricing.models.metering_unit_timestamp_count import MeteringUnitTimestampCount
from saasus_sdk_python.src.pricing.models.update_metering_unit_timestamp_count_now_param import UpdateMeteringUnitTimestampCountNowParam
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
    api_instance = saasus_sdk_python.src.pricing.MeteringApi(api_client)
    tenant_id = '46af35b5-60de-4cd8-9412-19a3a5d1f838' # str | テナントID
    metering_unit_name = 'storage_unit' # str | 計測ユニット名
    update_metering_unit_timestamp_count_now_param = saasus_sdk_python.src.pricing.UpdateMeteringUnitTimestampCountNowParam() # UpdateMeteringUnitTimestampCountNowParam |  (optional)

    try:
        # 現在時刻のメータリングユニットカウントを更新
        api_response = api_instance.update_metering_unit_timestamp_count_now(tenant_id, metering_unit_name, update_metering_unit_timestamp_count_now_param=update_metering_unit_timestamp_count_now_param)
        print("The response of MeteringApi->update_metering_unit_timestamp_count_now:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeteringApi->update_metering_unit_timestamp_count_now: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| テナントID | 
 **metering_unit_name** | **str**| 計測ユニット名 | 
 **update_metering_unit_timestamp_count_now_param** | [**UpdateMeteringUnitTimestampCountNowParam**](UpdateMeteringUnitTimestampCountNowParam.md)|  | [optional] 

### Return type

[**MeteringUnitTimestampCount**](MeteringUnitTimestampCount.md)

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


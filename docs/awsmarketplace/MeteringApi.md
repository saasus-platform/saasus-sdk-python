# saasus_sdk_python.src.pricing.MeteringApi

All URIs are relative to *https://api.saasus.io/v1/pricing*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_metering_unit**](MeteringApi.md#create_metering_unit) | **POST** /metering/units | Create Metering Unit
[**delete_metering_unit_by_id**](MeteringApi.md#delete_metering_unit_by_id) | **DELETE** /metering/units/{metering_unit_id} | Delete Metering Unit
[**delete_metering_unit_timestamp_count**](MeteringApi.md#delete_metering_unit_timestamp_count) | **DELETE** /metering/tenants/{tenant_id}/units/{metering_unit_name}/timestamp/{timestamp} | Delete Metering Unit Count for Specified Timestamp
[**get_metering_unit_date_count_by_tenant_id_and_unit_name_and_date**](MeteringApi.md#get_metering_unit_date_count_by_tenant_id_and_unit_name_and_date) | **GET** /metering/tenants/{tenant_id}/units/{metering_unit_name}/date/{date} | Get Metering Unit Count for Specific Date
[**get_metering_unit_date_count_by_tenant_id_and_unit_name_and_date_period**](MeteringApi.md#get_metering_unit_date_count_by_tenant_id_and_unit_name_and_date_period) | **GET** /metering/tenants/{tenant_id}/units/{metering_unit_name}/date-period | Obtain metering unit counts for a specified date/time period
[**get_metering_unit_date_count_by_tenant_id_and_unit_name_today**](MeteringApi.md#get_metering_unit_date_count_by_tenant_id_and_unit_name_today) | **GET** /metering/tenants/{tenant_id}/units/{metering_unit_name}/today | Get Metering Unit Count for the Current Day
[**get_metering_unit_date_counts_by_tenant_id_and_date**](MeteringApi.md#get_metering_unit_date_counts_by_tenant_id_and_date) | **GET** /metering/tenants/{tenant_id}/units/date/{date} | Get All Metering Unit Counts for a Specified Date
[**get_metering_unit_month_count_by_tenant_id_and_unit_name_and_month**](MeteringApi.md#get_metering_unit_month_count_by_tenant_id_and_unit_name_and_month) | **GET** /metering/tenants/{tenant_id}/units/{metering_unit_name}/month/{month} | Get the Metering Unit Count for the Specified Month
[**get_metering_unit_month_count_by_tenant_id_and_unit_name_this_month**](MeteringApi.md#get_metering_unit_month_count_by_tenant_id_and_unit_name_this_month) | **GET** /metering/tenants/{tenant_id}/units/{metering_unit_name}/thismonth | Get Metering Unit Count for the Current Month
[**get_metering_unit_month_counts_by_tenant_id_and_month**](MeteringApi.md#get_metering_unit_month_counts_by_tenant_id_and_month) | **GET** /metering/tenants/{tenant_id}/units/month/{month} | Get All Metering Unit Counts for the Specified Month
[**get_metering_units**](MeteringApi.md#get_metering_units) | **GET** /metering/units | Get all metering units
[**update_metering_unit_by_id**](MeteringApi.md#update_metering_unit_by_id) | **PATCH** /metering/units/{metering_unit_id} | Update Metering Unit
[**update_metering_unit_timestamp_count**](MeteringApi.md#update_metering_unit_timestamp_count) | **PUT** /metering/tenants/{tenant_id}/units/{metering_unit_name}/timestamp/{timestamp} | Update Metering Unit Count for Specified Timestamp
[**update_metering_unit_timestamp_count_now**](MeteringApi.md#update_metering_unit_timestamp_count_now) | **PUT** /metering/tenants/{tenant_id}/units/{metering_unit_name}/now | Update Metering Unit Count for Current Time


# **create_metering_unit**
> MeteringUnit create_metering_unit(body=body)

Create Metering Unit

Create a metering unit. 

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
        # Create Metering Unit
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

Delete Metering Unit

Delete metering unit. 

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
    metering_unit_id = '46af35b5-60de-4cd8-9412-19a3a5d1f838' # str | Metering Unit ID

    try:
        # Delete Metering Unit
        api_instance.delete_metering_unit_by_id(metering_unit_id)
    except Exception as e:
        print("Exception when calling MeteringApi->delete_metering_unit_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metering_unit_id** | **str**| Metering Unit ID | 

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

Delete Metering Unit Count for Specified Timestamp

Deletes metering unit count for the specified timestamp. 

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
    tenant_id = '46af35b5-60de-4cd8-9412-19a3a5d1f838' # str | Tenant ID
    metering_unit_name = 'storage_unit' # str | Metering Unit Name
    timestamp = 1640995200 # int | Timestamp

    try:
        # Delete Metering Unit Count for Specified Timestamp
        api_instance.delete_metering_unit_timestamp_count(tenant_id, metering_unit_name, timestamp)
    except Exception as e:
        print("Exception when calling MeteringApi->delete_metering_unit_timestamp_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant ID | 
 **metering_unit_name** | **str**| Metering Unit Name | 
 **timestamp** | **int**| Timestamp | 

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

Get Metering Unit Count for Specific Date

Gets the metering unit count for a specific date. 

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
    tenant_id = '46af35b5-60de-4cd8-9412-19a3a5d1f838' # str | Tenant ID
    metering_unit_name = 'storage_unit' # str | Metering Unit Name
    var_date = '2022-01-01' # str | Date

    try:
        # Get Metering Unit Count for Specific Date
        api_response = api_instance.get_metering_unit_date_count_by_tenant_id_and_unit_name_and_date(tenant_id, metering_unit_name, var_date)
        print("The response of MeteringApi->get_metering_unit_date_count_by_tenant_id_and_unit_name_and_date:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeteringApi->get_metering_unit_date_count_by_tenant_id_and_unit_name_and_date: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant ID | 
 **metering_unit_name** | **str**| Metering Unit Name | 
 **var_date** | **str**| Date | 

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

Obtain metering unit counts for a specified date/time period

Obtain metering unit counts for a specified date/time period. 

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
    tenant_id = '46af35b5-60de-4cd8-9412-19a3a5d1f838' # str | Tenant ID
    metering_unit_name = 'storage_unit' # str | Metering Unit Name
    start_timestamp = 1640995200 # int | Start Date-Time (optional)
    end_timestamp = 1640995200 # int | End Date-Time (optional)

    try:
        # Obtain metering unit counts for a specified date/time period
        api_response = api_instance.get_metering_unit_date_count_by_tenant_id_and_unit_name_and_date_period(tenant_id, metering_unit_name, start_timestamp=start_timestamp, end_timestamp=end_timestamp)
        print("The response of MeteringApi->get_metering_unit_date_count_by_tenant_id_and_unit_name_and_date_period:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeteringApi->get_metering_unit_date_count_by_tenant_id_and_unit_name_and_date_period: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant ID | 
 **metering_unit_name** | **str**| Metering Unit Name | 
 **start_timestamp** | **int**| Start Date-Time | [optional] 
 **end_timestamp** | **int**| End Date-Time | [optional] 

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

Get Metering Unit Count for the Current Day

Get the metering unit count for the current day. 

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
    tenant_id = '46af35b5-60de-4cd8-9412-19a3a5d1f838' # str | Tenant ID
    metering_unit_name = 'storage_unit' # str | Metering Unit Name

    try:
        # Get Metering Unit Count for the Current Day
        api_response = api_instance.get_metering_unit_date_count_by_tenant_id_and_unit_name_today(tenant_id, metering_unit_name)
        print("The response of MeteringApi->get_metering_unit_date_count_by_tenant_id_and_unit_name_today:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeteringApi->get_metering_unit_date_count_by_tenant_id_and_unit_name_today: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant ID | 
 **metering_unit_name** | **str**| Metering Unit Name | 

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

Get All Metering Unit Counts for a Specified Date

Gets the total metering unit count for the specified date. 

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
    tenant_id = '46af35b5-60de-4cd8-9412-19a3a5d1f838' # str | Tenant ID
    var_date = '2022-01-01' # str | Date

    try:
        # Get All Metering Unit Counts for a Specified Date
        api_response = api_instance.get_metering_unit_date_counts_by_tenant_id_and_date(tenant_id, var_date)
        print("The response of MeteringApi->get_metering_unit_date_counts_by_tenant_id_and_date:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeteringApi->get_metering_unit_date_counts_by_tenant_id_and_date: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant ID | 
 **var_date** | **str**| Date | 

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

Get the Metering Unit Count for the Specified Month

Gets the metering unit count for the specified month. 

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
    tenant_id = '46af35b5-60de-4cd8-9412-19a3a5d1f838' # str | Tenant ID
    metering_unit_name = 'storage_unit' # str | Metering Unit Name
    month = '2022-01' # str | Month

    try:
        # Get the Metering Unit Count for the Specified Month
        api_response = api_instance.get_metering_unit_month_count_by_tenant_id_and_unit_name_and_month(tenant_id, metering_unit_name, month)
        print("The response of MeteringApi->get_metering_unit_month_count_by_tenant_id_and_unit_name_and_month:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeteringApi->get_metering_unit_month_count_by_tenant_id_and_unit_name_and_month: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant ID | 
 **metering_unit_name** | **str**| Metering Unit Name | 
 **month** | **str**| Month | 

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

Get Metering Unit Count for the Current Month

Get the metering unit count for the current month. 

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
    tenant_id = '46af35b5-60de-4cd8-9412-19a3a5d1f838' # str | Tenant ID
    metering_unit_name = 'storage_unit' # str | Metering Unit Name

    try:
        # Get Metering Unit Count for the Current Month
        api_response = api_instance.get_metering_unit_month_count_by_tenant_id_and_unit_name_this_month(tenant_id, metering_unit_name)
        print("The response of MeteringApi->get_metering_unit_month_count_by_tenant_id_and_unit_name_this_month:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeteringApi->get_metering_unit_month_count_by_tenant_id_and_unit_name_this_month: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant ID | 
 **metering_unit_name** | **str**| Metering Unit Name | 

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

Get All Metering Unit Counts for the Specified Month

Gets all metering unit counts for the specified month. 

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
    tenant_id = '46af35b5-60de-4cd8-9412-19a3a5d1f838' # str | Tenant ID
    month = '2022-01' # str | Month

    try:
        # Get All Metering Unit Counts for the Specified Month
        api_response = api_instance.get_metering_unit_month_counts_by_tenant_id_and_month(tenant_id, month)
        print("The response of MeteringApi->get_metering_unit_month_counts_by_tenant_id_and_month:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeteringApi->get_metering_unit_month_counts_by_tenant_id_and_month: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant ID | 
 **month** | **str**| Month | 

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

Get all metering units

Get all metering units. 

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
        # Get all metering units
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

Update Metering Unit

Update metering unit. 

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
    metering_unit_id = '46af35b5-60de-4cd8-9412-19a3a5d1f838' # str | Metering Unit ID
    body = saasus_sdk_python.src.pricing.MeteringUnitProps() # MeteringUnitProps |  (optional)

    try:
        # Update Metering Unit
        api_instance.update_metering_unit_by_id(metering_unit_id, body=body)
    except Exception as e:
        print("Exception when calling MeteringApi->update_metering_unit_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metering_unit_id** | **str**| Metering Unit ID | 
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

Update Metering Unit Count for Specified Timestamp

Update metering unit count for the specified timestamp. 

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
    tenant_id = '46af35b5-60de-4cd8-9412-19a3a5d1f838' # str | Tenant ID
    metering_unit_name = 'storage_unit' # str | Metering Unit Name
    timestamp = 1640995200 # int | Timestamp
    update_metering_unit_timestamp_count_param = saasus_sdk_python.src.pricing.UpdateMeteringUnitTimestampCountParam() # UpdateMeteringUnitTimestampCountParam |  (optional)

    try:
        # Update Metering Unit Count for Specified Timestamp
        api_response = api_instance.update_metering_unit_timestamp_count(tenant_id, metering_unit_name, timestamp, update_metering_unit_timestamp_count_param=update_metering_unit_timestamp_count_param)
        print("The response of MeteringApi->update_metering_unit_timestamp_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeteringApi->update_metering_unit_timestamp_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant ID | 
 **metering_unit_name** | **str**| Metering Unit Name | 
 **timestamp** | **int**| Timestamp | 
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

Update Metering Unit Count for Current Time

Update the metering unit count for the current time. 

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
    tenant_id = '46af35b5-60de-4cd8-9412-19a3a5d1f838' # str | Tenant ID
    metering_unit_name = 'storage_unit' # str | Metering Unit Name
    update_metering_unit_timestamp_count_now_param = saasus_sdk_python.src.pricing.UpdateMeteringUnitTimestampCountNowParam() # UpdateMeteringUnitTimestampCountNowParam |  (optional)

    try:
        # Update Metering Unit Count for Current Time
        api_response = api_instance.update_metering_unit_timestamp_count_now(tenant_id, metering_unit_name, update_metering_unit_timestamp_count_now_param=update_metering_unit_timestamp_count_now_param)
        print("The response of MeteringApi->update_metering_unit_timestamp_count_now:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeteringApi->update_metering_unit_timestamp_count_now: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant ID | 
 **metering_unit_name** | **str**| Metering Unit Name | 
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


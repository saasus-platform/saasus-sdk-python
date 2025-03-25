# ApiLog


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trace_id** | **str** | Trace ID | 
**api_log_id** | **str** |  | 
**created_at** | **int** | Epoch second of API log registration timestamp | 
**created_date** | **str** | API log registration date | 
**ttl** | **int** | Epoch second of planned API log deletion | 
**request_method** | **str** | Request method | 
**saas_id** | **str** |  | 
**api_key** | **str** | API Key | 
**response_status** | **str** | Response status | 
**request_uri** | **str** | Request URI | 
**remote_address** | **str** | Client IP Address | 
**referer** | **str** | The referrer of the request | 
**request_body** | **str** | The body of the request | 
**response_body** | **str** | The body of the response | 

## Example

```python
from saasus_sdk_python.src.apilog.models.api_log import ApiLog

# TODO update the JSON string below
json = "{}"
# create an instance of ApiLog from a JSON string
api_log_instance = ApiLog.from_json(json)
# print the JSON string representation of the object
print ApiLog.to_json()

# convert the object into a dict
api_log_dict = api_log_instance.to_dict()
# create an instance of ApiLog from a dict
api_log_form_dict = api_log.from_dict(api_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



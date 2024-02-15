# ApiLog


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trace_id** | **str** | トレースID | 
**api_log_id** | **str** |  | 
**created_at** | **int** | APIログ登録日時のエポック秒 | 
**created_date** | **str** | APIログ登録日 | 
**ttl** | **int** | APIログ削除予定エポック秒 | 
**request_method** | **str** | リクエストメソッド | 
**saas_id** | **str** |  | 
**api_key** | **str** | APIキー | 
**response_status** | **str** | レスポンスステータス | 
**request_uri** | **str** | リクエストURI | 
**remote_address** | **str** | クライアントIPアドレス | 
**referer** | **str** | リクエストリファラー | 
**request_body** | **str** | リクエストボディー | 
**response_body** | **str** | レスポンスボディー | 

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



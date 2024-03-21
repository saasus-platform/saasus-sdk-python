# UpdateSettingsParam


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_code** | **str** |  | [optional] 
**role_arn** | **str** |  | [optional] 
**role_external_id** | **str** |  | [optional] 
**sns_topic_arn** | **str** |  | [optional] 
**cas_bucket_name** | **str** |  | [optional] 
**cas_sns_topic_arn** | **str** |  | [optional] 
**seller_sns_topic_arn** | **str** |  | [optional] 
**sqs_arn** | **str** |  | [optional] 

## Example

```python
from saasus_sdk_python.src.awsmarketplace.models.update_settings_param import UpdateSettingsParam

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSettingsParam from a JSON string
update_settings_param_instance = UpdateSettingsParam.from_json(json)
# print the JSON string representation of the object
print UpdateSettingsParam.to_json()

# convert the object into a dict
update_settings_param_dict = update_settings_param_instance.to_dict()
# create an instance of UpdateSettingsParam from a dict
update_settings_param_form_dict = update_settings_param.from_dict(update_settings_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# Settings


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_code** | **str** |  | 
**role_arn** | **str** |  | 
**role_external_id** | **str** |  | 
**sns_topic_arn** | **str** |  | 
**cas_bucket_name** | **str** |  | 
**cas_sns_topic_arn** | **str** |  | 
**seller_sns_topic_arn** | **str** |  | 
**redirect_sign_up_page_function_url** | **str** |  | 
**sqs_arn** | **str** |  | 

## Example

```python
from saasus_sdk_python.src.awsmarketplace.models.settings import Settings

# TODO update the JSON string below
json = "{}"
# create an instance of Settings from a JSON string
settings_instance = Settings.from_json(json)
# print the JSON string representation of the object
print Settings.to_json()

# convert the object into a dict
settings_dict = settings_instance.to_dict()
# create an instance of Settings from a dict
settings_form_dict = settings.from_dict(settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



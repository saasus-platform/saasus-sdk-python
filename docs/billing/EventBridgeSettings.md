# EventBridgeSettings


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_account_id** | **str** | AWS Account ID | 
**aws_region** | [**AwsRegion**](AwsRegion.md) |  | 

## Example

```python
from saasus_sdk_python.src.integration.models.event_bridge_settings import EventBridgeSettings

# TODO update the JSON string below
json = "{}"
# create an instance of EventBridgeSettings from a JSON string
event_bridge_settings_instance = EventBridgeSettings.from_json(json)
# print the JSON string representation of the object
print EventBridgeSettings.to_json()

# convert the object into a dict
event_bridge_settings_dict = event_bridge_settings_instance.to_dict()
# create an instance of EventBridgeSettings from a dict
event_bridge_settings_form_dict = event_bridge_settings.from_dict(event_bridge_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



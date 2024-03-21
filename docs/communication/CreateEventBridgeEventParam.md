# CreateEventBridgeEventParam


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_messages** | [**List[EventMessage]**](EventMessage.md) | event message | 

## Example

```python
from saasus_sdk_python.src.integration.models.create_event_bridge_event_param import CreateEventBridgeEventParam

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEventBridgeEventParam from a JSON string
create_event_bridge_event_param_instance = CreateEventBridgeEventParam.from_json(json)
# print the JSON string representation of the object
print CreateEventBridgeEventParam.to_json()

# convert the object into a dict
create_event_bridge_event_param_dict = create_event_bridge_event_param_instance.to_dict()
# create an instance of CreateEventBridgeEventParam from a dict
create_event_bridge_event_param_form_dict = create_event_bridge_event_param.from_dict(create_event_bridge_event_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



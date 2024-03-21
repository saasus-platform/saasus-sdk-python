# MessageTemplate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject** | **str** | Title | 
**message** | **str** | Message | 

## Example

```python
from saasus_sdk_python.src.auth.models.message_template import MessageTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of MessageTemplate from a JSON string
message_template_instance = MessageTemplate.from_json(json)
# print the JSON string representation of the object
print MessageTemplate.to_json()

# convert the object into a dict
message_template_dict = message_template_instance.to_dict()
# create an instance of MessageTemplate from a dict
message_template_form_dict = message_template.from_dict(message_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



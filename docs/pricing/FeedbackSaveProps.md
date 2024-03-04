# FeedbackSaveProps


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feedback_title** | **str** |  | 
**feedback_description** | **str** |  | 

## Example

```python
from saasus_sdk_python.src.communication.models.feedback_save_props import FeedbackSaveProps

# TODO update the JSON string below
json = "{}"
# create an instance of FeedbackSaveProps from a JSON string
feedback_save_props_instance = FeedbackSaveProps.from_json(json)
# print the JSON string representation of the object
print FeedbackSaveProps.to_json()

# convert the object into a dict
feedback_save_props_dict = feedback_save_props_instance.to_dict()
# create an instance of FeedbackSaveProps from a dict
feedback_save_props_form_dict = feedback_save_props.from_dict(feedback_save_props_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# UpdateFeedbackParam


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feedback_title** | **str** |  | 
**feedback_description** | **str** |  | 

## Example

```python
from saasus_sdk_python.src.communication.models.update_feedback_param import UpdateFeedbackParam

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateFeedbackParam from a JSON string
update_feedback_param_instance = UpdateFeedbackParam.from_json(json)
# print the JSON string representation of the object
print UpdateFeedbackParam.to_json()

# convert the object into a dict
update_feedback_param_dict = update_feedback_param_instance.to_dict()
# create an instance of UpdateFeedbackParam from a dict
update_feedback_param_form_dict = update_feedback_param.from_dict(update_feedback_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# CreateFeedbackParam


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feedback_title** | **str** |  | 
**feedback_description** | **str** |  | 
**user_id** | **str** |  | 

## Example

```python
from saasus_sdk_python.src.communication.models.create_feedback_param import CreateFeedbackParam

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFeedbackParam from a JSON string
create_feedback_param_instance = CreateFeedbackParam.from_json(json)
# print the JSON string representation of the object
print CreateFeedbackParam.to_json()

# convert the object into a dict
create_feedback_param_dict = create_feedback_param_instance.to_dict()
# create an instance of CreateFeedbackParam from a dict
create_feedback_param_form_dict = create_feedback_param.from_dict(create_feedback_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



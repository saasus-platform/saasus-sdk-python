# UpdateFeedbackStatusParam


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | 

## Example

```python
from saasus_sdk_python.src.communication.models.update_feedback_status_param import UpdateFeedbackStatusParam

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateFeedbackStatusParam from a JSON string
update_feedback_status_param_instance = UpdateFeedbackStatusParam.from_json(json)
# print the JSON string representation of the object
print UpdateFeedbackStatusParam.to_json()

# convert the object into a dict
update_feedback_status_param_dict = update_feedback_status_param_instance.to_dict()
# create an instance of UpdateFeedbackStatusParam from a dict
update_feedback_status_param_form_dict = update_feedback_status_param.from_dict(update_feedback_status_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



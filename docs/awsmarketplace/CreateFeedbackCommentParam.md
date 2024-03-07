# CreateFeedbackCommentParam


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**body** | **str** |  | 

## Example

```python
from saasus_sdk_python.src.communication.models.create_feedback_comment_param import CreateFeedbackCommentParam

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFeedbackCommentParam from a JSON string
create_feedback_comment_param_instance = CreateFeedbackCommentParam.from_json(json)
# print the JSON string representation of the object
print CreateFeedbackCommentParam.to_json()

# convert the object into a dict
create_feedback_comment_param_dict = create_feedback_comment_param_instance.to_dict()
# create an instance of CreateFeedbackCommentParam from a dict
create_feedback_comment_param_form_dict = create_feedback_comment_param.from_dict(create_feedback_comment_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



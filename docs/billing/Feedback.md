# Feedback


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feedback_title** | **str** |  | 
**feedback_description** | **str** |  | 
**comments** | [**List[Comment]**](Comment.md) |  | 
**count** | **int** |  | 
**users** | [**List[User]**](User.md) |  | 
**id** | **str** |  | 
**user_id** | **str** |  | 
**created_at** | **int** |  | 
**status** | **int** |  | 

## Example

```python
from saasus_sdk_python.src.communication.models.feedback import Feedback

# TODO update the JSON string below
json = "{}"
# create an instance of Feedback from a JSON string
feedback_instance = Feedback.from_json(json)
# print the JSON string representation of the object
print Feedback.to_json()

# convert the object into a dict
feedback_dict = feedback_instance.to_dict()
# create an instance of Feedback from a dict
feedback_form_dict = feedback.from_dict(feedback_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



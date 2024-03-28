# Feedbacks


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feedbacks** | [**List[Feedback]**](Feedback.md) |  | 

## Example

```python
from saasus_sdk_python.src.communication.models.feedbacks import Feedbacks

# TODO update the JSON string below
json = "{}"
# create an instance of Feedbacks from a JSON string
feedbacks_instance = Feedbacks.from_json(json)
# print the JSON string representation of the object
print Feedbacks.to_json()

# convert the object into a dict
feedbacks_dict = feedbacks_instance.to_dict()
# create an instance of Feedbacks from a dict
feedbacks_form_dict = feedbacks.from_dict(feedbacks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# Votes


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | [**List[User]**](User.md) |  | 
**count** | **int** |  | 

## Example

```python
from saasus_sdk_python.src.communication.models.votes import Votes

# TODO update the JSON string below
json = "{}"
# create an instance of Votes from a JSON string
votes_instance = Votes.from_json(json)
# print the JSON string representation of the object
print Votes.to_json()

# convert the object into a dict
votes_dict = votes_instance.to_dict()
# create an instance of Votes from a dict
votes_form_dict = votes.from_dict(votes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



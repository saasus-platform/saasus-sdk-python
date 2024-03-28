# CreateVoteUserParam


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 

## Example

```python
from saasus_sdk_python.src.communication.models.create_vote_user_param import CreateVoteUserParam

# TODO update the JSON string below
json = "{}"
# create an instance of CreateVoteUserParam from a JSON string
create_vote_user_param_instance = CreateVoteUserParam.from_json(json)
# print the JSON string representation of the object
print CreateVoteUserParam.to_json()

# convert the object into a dict
create_vote_user_param_dict = create_vote_user_param_instance.to_dict()
# create an instance of CreateVoteUserParam from a dict
create_vote_user_param_form_dict = create_vote_user_param.from_dict(create_vote_user_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



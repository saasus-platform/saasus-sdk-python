# UserAvailableEnv


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** | env name | 
**display_name** | **str** | env display name | [optional] 
**roles** | [**List[Role]**](Role.md) | role info | 

## Example

```python
from saasus_sdk_python.src.auth.models.user_available_env import UserAvailableEnv

# TODO update the JSON string below
json = "{}"
# create an instance of UserAvailableEnv from a JSON string
user_available_env_instance = UserAvailableEnv.from_json(json)
# print the JSON string representation of the object
print UserAvailableEnv.to_json()

# convert the object into a dict
user_available_env_dict = user_available_env_instance.to_dict()
# create an instance of UserAvailableEnv from a dict
user_available_env_form_dict = user_available_env.from_dict(user_available_env_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



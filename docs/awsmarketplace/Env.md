# Env

env info

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** | env name | 
**display_name** | **str** | env display name | [optional] 

## Example

```python
from saasus_sdk_python.src.auth.models.env import Env

# TODO update the JSON string below
json = "{}"
# create an instance of Env from a JSON string
env_instance = Env.from_json(json)
# print the JSON string representation of the object
print Env.to_json()

# convert the object into a dict
env_dict = env_instance.to_dict()
# create an instance of Env from a dict
env_form_dict = env.from_dict(env_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



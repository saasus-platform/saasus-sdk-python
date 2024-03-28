# Envs

env list

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**envs** | [**List[Env]**](Env.md) |  | 

## Example

```python
from saasus_sdk_python.src.auth.models.envs import Envs

# TODO update the JSON string below
json = "{}"
# create an instance of Envs from a JSON string
envs_instance = Envs.from_json(json)
# print the JSON string representation of the object
print Envs.to_json()

# convert the object into a dict
envs_dict = envs_instance.to_dict()
# create an instance of Envs from a dict
envs_form_dict = envs.from_dict(envs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



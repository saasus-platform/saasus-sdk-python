# UpdateEnvParam


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | env name | 
**display_name** | **str** | env display name | [optional] 

## Example

```python
from saasus_sdk_python.src.auth.models.update_env_param import UpdateEnvParam

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateEnvParam from a JSON string
update_env_param_instance = UpdateEnvParam.from_json(json)
# print the JSON string representation of the object
print UpdateEnvParam.to_json()

# convert the object into a dict
update_env_param_dict = update_env_param_instance.to_dict()
# create an instance of UpdateEnvParam from a dict
update_env_param_form_dict = update_env_param.from_dict(update_env_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



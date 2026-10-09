# UpdateRoleParam


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | role display name | 

## Example

```python
from saasus_sdk_python.src.auth.models.update_role_param import UpdateRoleParam

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRoleParam from a JSON string
update_role_param_instance = UpdateRoleParam.from_json(json)
# print the JSON string representation of the object
print UpdateRoleParam.to_json()

# convert the object into a dict
update_role_param_dict = update_role_param_instance.to_dict()
# create an instance of UpdateRoleParam from a dict
update_role_param_form_dict = update_role_param.from_dict(update_role_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



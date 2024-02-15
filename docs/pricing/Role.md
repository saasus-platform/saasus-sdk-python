# Role

役割(ロール)情報(role info)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_name** | **str** | 役割(ロール)名(role name) | 
**display_name** | **str** | 役割(ロール)表示名(role display name) | 

## Example

```python
from saasus_sdk_python.src.auth.models.role import Role

# TODO update the JSON string below
json = "{}"
# create an instance of Role from a JSON string
role_instance = Role.from_json(json)
# print the JSON string representation of the object
print Role.to_json()

# convert the object into a dict
role_dict = role_instance.to_dict()
# create an instance of Role from a dict
role_form_dict = role.from_dict(role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



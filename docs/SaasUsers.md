# SaasUsers


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | [**List[SaasUser]**](SaasUser.md) |  | 

## Example

```python
from saasus_sdk_python.models.saas_users import SaasUsers

# TODO update the JSON string below
json = "{}"
# create an instance of SaasUsers from a JSON string
saas_users_instance = SaasUsers.from_json(json)
# print the JSON string representation of the object
print SaasUsers.to_json()

# convert the object into a dict
saas_users_dict = saas_users_instance.to_dict()
# create an instance of SaasUsers from a dict
saas_users_form_dict = saas_users.from_dict(saas_users_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



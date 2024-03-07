# CreateTenantUserRolesParam


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_names** | **List[str]** | Role Info | 

## Example

```python
from saasus_sdk_python.src.auth.models.create_tenant_user_roles_param import CreateTenantUserRolesParam

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTenantUserRolesParam from a JSON string
create_tenant_user_roles_param_instance = CreateTenantUserRolesParam.from_json(json)
# print the JSON string representation of the object
print CreateTenantUserRolesParam.to_json()

# convert the object into a dict
create_tenant_user_roles_param_dict = create_tenant_user_roles_param_instance.to_dict()
# create an instance of CreateTenantUserRolesParam from a dict
create_tenant_user_roles_param_form_dict = create_tenant_user_roles_param.from_dict(create_tenant_user_roles_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



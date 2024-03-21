# UpdateTenantUserParam


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | **Dict[str, object]** | Attribute information (Get information set by defining user attributes in the SaaS development console)  | 

## Example

```python
from saasus_sdk_python.src.auth.models.update_tenant_user_param import UpdateTenantUserParam

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTenantUserParam from a JSON string
update_tenant_user_param_instance = UpdateTenantUserParam.from_json(json)
# print the JSON string representation of the object
print UpdateTenantUserParam.to_json()

# convert the object into a dict
update_tenant_user_param_dict = update_tenant_user_param_instance.to_dict()
# create an instance of UpdateTenantUserParam from a dict
update_tenant_user_param_form_dict = update_tenant_user_param.from_dict(update_tenant_user_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



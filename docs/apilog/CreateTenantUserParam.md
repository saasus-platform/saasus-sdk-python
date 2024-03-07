# CreateTenantUserParam


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | E-mail | 
**attributes** | **Dict[str, object]** | Attribute information (Get information set by defining user attributes in the SaaS development console)  | 

## Example

```python
from saasus_sdk_python.src.auth.models.create_tenant_user_param import CreateTenantUserParam

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTenantUserParam from a JSON string
create_tenant_user_param_instance = CreateTenantUserParam.from_json(json)
# print the JSON string representation of the object
print CreateTenantUserParam.to_json()

# convert the object into a dict
create_tenant_user_param_dict = create_tenant_user_param_instance.to_dict()
# create an instance of CreateTenantUserParam from a dict
create_tenant_user_param_form_dict = create_tenant_user_param.from_dict(create_tenant_user_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



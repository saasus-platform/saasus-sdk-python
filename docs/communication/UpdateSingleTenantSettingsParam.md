# UpdateSingleTenantSettingsParam


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | enable Single Tenant settings or not | [optional] 
**role_arn** | **str** | ARN of the role for SaaS Platform to AssumeRole | [optional] 
**cloudformation_template** | **str** | CloudFormation template file | [optional] 
**ddl_template** | **str** | ddl file to run in SaaS environment | [optional] 
**role_external_id** | **str** | External id used by SaaSus when AssumeRole to operate SaaS | [optional] 

## Example

```python
from saasus_sdk_python.src.auth.models.update_single_tenant_settings_param import UpdateSingleTenantSettingsParam

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSingleTenantSettingsParam from a JSON string
update_single_tenant_settings_param_instance = UpdateSingleTenantSettingsParam.from_json(json)
# print the JSON string representation of the object
print UpdateSingleTenantSettingsParam.to_json()

# convert the object into a dict
update_single_tenant_settings_param_dict = update_single_tenant_settings_param_instance.to_dict()
# create an instance of UpdateSingleTenantSettingsParam from a dict
update_single_tenant_settings_param_form_dict = update_single_tenant_settings_param.from_dict(update_single_tenant_settings_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



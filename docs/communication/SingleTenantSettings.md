# SingleTenantSettings


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | enable SaaS Infrastructure Management settings or not | 
**role_arn** | **str** | ARN of the role for SaaS Platform to AssumeRole | 
**cloudformation_template_url** | **str** | S3 URL where the CloudFormationTemplate to be executed in the SaaS environment is stored | 
**ddl_template_url** | **str** | S3 URL where the CloudFormationTemplate to be executed in the SaaS environment is stored | 
**role_external_id** | **str** | External id used by SaaSus when AssumeRole to operate SaaS | 

## Example

```python
from saasus_sdk_python.src.auth.models.single_tenant_settings import SingleTenantSettings

# TODO update the JSON string below
json = "{}"
# create an instance of SingleTenantSettings from a JSON string
single_tenant_settings_instance = SingleTenantSettings.from_json(json)
# print the JSON string representation of the object
print SingleTenantSettings.to_json()

# convert the object into a dict
single_tenant_settings_dict = single_tenant_settings_instance.to_dict()
# create an instance of SingleTenantSettings from a dict
single_tenant_settings_form_dict = single_tenant_settings.from_dict(single_tenant_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



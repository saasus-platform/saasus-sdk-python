# TenantIdentityProviderProps


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata_url** | **str** |  | 
**email_attribute** | **str** |  | 

## Example

```python
from saasus_sdk_python.src.auth.models.tenant_identity_provider_props import TenantIdentityProviderProps

# TODO update the JSON string below
json = "{}"
# create an instance of TenantIdentityProviderProps from a JSON string
tenant_identity_provider_props_instance = TenantIdentityProviderProps.from_json(json)
# print the JSON string representation of the object
print TenantIdentityProviderProps.to_json()

# convert the object into a dict
tenant_identity_provider_props_dict = tenant_identity_provider_props_instance.to_dict()
# create an instance of TenantIdentityProviderProps from a dict
tenant_identity_provider_props_form_dict = tenant_identity_provider_props.from_dict(tenant_identity_provider_props_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



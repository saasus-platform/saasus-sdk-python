# TenantIdentityProvidersSaml


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata_url** | **str** |  | 
**email_attribute** | **str** |  | 
**sign_in_url** | **str** |  | 

## Example

```python
from saasus_sdk_python.src.auth.models.tenant_identity_providers_saml import TenantIdentityProvidersSaml

# TODO update the JSON string below
json = "{}"
# create an instance of TenantIdentityProvidersSaml from a JSON string
tenant_identity_providers_saml_instance = TenantIdentityProvidersSaml.from_json(json)
# print the JSON string representation of the object
print TenantIdentityProvidersSaml.to_json()

# convert the object into a dict
tenant_identity_providers_saml_dict = tenant_identity_providers_saml_instance.to_dict()
# create an instance of TenantIdentityProvidersSaml from a dict
tenant_identity_providers_saml_form_dict = tenant_identity_providers_saml.from_dict(tenant_identity_providers_saml_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



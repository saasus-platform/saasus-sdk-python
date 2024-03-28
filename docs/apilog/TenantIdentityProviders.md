# TenantIdentityProviders


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**saml** | [**TenantIdentityProvidersSaml**](TenantIdentityProvidersSaml.md) |  | [optional] 

## Example

```python
from saasus_sdk_python.src.auth.models.tenant_identity_providers import TenantIdentityProviders

# TODO update the JSON string below
json = "{}"
# create an instance of TenantIdentityProviders from a JSON string
tenant_identity_providers_instance = TenantIdentityProviders.from_json(json)
# print the JSON string representation of the object
print TenantIdentityProviders.to_json()

# convert the object into a dict
tenant_identity_providers_dict = tenant_identity_providers_instance.to_dict()
# create an instance of TenantIdentityProviders from a dict
tenant_identity_providers_form_dict = tenant_identity_providers.from_dict(tenant_identity_providers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



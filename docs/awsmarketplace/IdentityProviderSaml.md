# IdentityProviderSaml


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata_url** | **str** |  | 
**email_attribute** | **str** |  | 

## Example

```python
from saasus_sdk_python.src.auth.models.identity_provider_saml import IdentityProviderSaml

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityProviderSaml from a JSON string
identity_provider_saml_instance = IdentityProviderSaml.from_json(json)
# print the JSON string representation of the object
print IdentityProviderSaml.to_json()

# convert the object into a dict
identity_provider_saml_dict = identity_provider_saml_instance.to_dict()
# create an instance of IdentityProviderSaml from a dict
identity_provider_saml_form_dict = identity_provider_saml.from_dict(identity_provider_saml_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



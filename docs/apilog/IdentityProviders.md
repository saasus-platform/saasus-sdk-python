# IdentityProviders


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**google** | [**IdentityProviderProps**](IdentityProviderProps.md) |  | 

## Example

```python
from saasus_sdk_python.src.auth.models.identity_providers import IdentityProviders

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityProviders from a JSON string
identity_providers_instance = IdentityProviders.from_json(json)
# print the JSON string representation of the object
print IdentityProviders.to_json()

# convert the object into a dict
identity_providers_dict = identity_providers_instance.to_dict()
# create an instance of IdentityProviders from a dict
identity_providers_form_dict = identity_providers.from_dict(identity_providers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



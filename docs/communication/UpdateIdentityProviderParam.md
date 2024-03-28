# UpdateIdentityProviderParam


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | [**ProviderName**](ProviderName.md) |  | 
**identity_provider_props** | [**IdentityProviderProps**](IdentityProviderProps.md) |  | [optional] 

## Example

```python
from saasus_sdk_python.src.auth.models.update_identity_provider_param import UpdateIdentityProviderParam

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateIdentityProviderParam from a JSON string
update_identity_provider_param_instance = UpdateIdentityProviderParam.from_json(json)
# print the JSON string representation of the object
print UpdateIdentityProviderParam.to_json()

# convert the object into a dict
update_identity_provider_param_dict = update_identity_provider_param_instance.to_dict()
# create an instance of UpdateIdentityProviderParam from a dict
update_identity_provider_param_form_dict = update_identity_provider_param.from_dict(update_identity_provider_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



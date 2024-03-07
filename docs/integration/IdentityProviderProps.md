# IdentityProviderProps


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_id** | **str** |  | 
**application_secret** | **str** |  | 
**approval_scope** | **str** |  | 
**is_button_hidden** | **bool** |  | [optional] 

## Example

```python
from saasus_sdk_python.src.auth.models.identity_provider_props import IdentityProviderProps

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityProviderProps from a JSON string
identity_provider_props_instance = IdentityProviderProps.from_json(json)
# print the JSON string representation of the object
print IdentityProviderProps.to_json()

# convert the object into a dict
identity_provider_props_dict = identity_provider_props_instance.to_dict()
# create an instance of IdentityProviderProps from a dict
identity_provider_props_form_dict = identity_provider_props.from_dict(identity_provider_props_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



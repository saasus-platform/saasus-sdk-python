# MfaConfiguration

MFA device authentication settings ※ This function is not yet provided, so it cannot be changed or saved. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mfa_configuration** | **str** | on: apply when all users log in optional: apply to individual users with MFA factor enabled ※ The parameter is currently optional and fixed.  | 

## Example

```python
from saasus_sdk_python.src.auth.models.mfa_configuration import MfaConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of MfaConfiguration from a JSON string
mfa_configuration_instance = MfaConfiguration.from_json(json)
# print the JSON string representation of the object
print MfaConfiguration.to_json()

# convert the object into a dict
mfa_configuration_dict = mfa_configuration_instance.to_dict()
# create an instance of MfaConfiguration from a dict
mfa_configuration_form_dict = mfa_configuration.from_dict(mfa_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



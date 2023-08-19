# MfaPreference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | MFAを有効にするか否か(enable MFA) | 
**method** | **str** | MFAの方法(enabledがtrueの場合は必須)(MFA method (required if enabled is true)) | [optional] 

## Example

```python
from saasus_sdk_python.models.mfa_preference import MfaPreference

# TODO update the JSON string below
json = "{}"
# create an instance of MfaPreference from a JSON string
mfa_preference_instance = MfaPreference.from_json(json)
# print the JSON string representation of the object
print MfaPreference.to_json()

# convert the object into a dict
mfa_preference_dict = mfa_preference_instance.to_dict()
# create an instance of MfaPreference from a dict
mfa_preference_form_dict = mfa_preference.from_dict(mfa_preference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



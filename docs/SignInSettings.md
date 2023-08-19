# SignInSettings


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password_policy** | [**PasswordPolicy**](PasswordPolicy.md) |  | 
**device_configuration** | [**DeviceConfiguration**](DeviceConfiguration.md) |  | 
**mfa_configuration** | [**MfaConfiguration**](MfaConfiguration.md) |  | 
**recaptcha_props** | [**RecaptchaProps**](RecaptchaProps.md) |  | 
**account_verification** | [**AccountVerification**](AccountVerification.md) |  | 
**self_regist** | [**SelfRegist**](SelfRegist.md) |  | 
**identity_provider_configuration** | [**IdentityProviderConfiguration**](IdentityProviderConfiguration.md) |  | 

## Example

```python
from saasus_sdk_python.models.sign_in_settings import SignInSettings

# TODO update the JSON string below
json = "{}"
# create an instance of SignInSettings from a JSON string
sign_in_settings_instance = SignInSettings.from_json(json)
# print the JSON string representation of the object
print SignInSettings.to_json()

# convert the object into a dict
sign_in_settings_dict = sign_in_settings_instance.to_dict()
# create an instance of SignInSettings from a dict
sign_in_settings_form_dict = sign_in_settings.from_dict(sign_in_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



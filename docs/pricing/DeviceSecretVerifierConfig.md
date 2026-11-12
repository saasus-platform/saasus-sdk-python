# DeviceSecretVerifierConfig

The configuration of the device secret verifier. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password_verifier** | **str** | A password verifier for a user&#39;s device. Used in SRP authentication. | [optional] 
**salt** | **str** | The salt for SRP authentication with the user&#39;s device. | [optional] 

## Example

```python
from saasus_sdk_python.src.auth.models.device_secret_verifier_config import DeviceSecretVerifierConfig

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceSecretVerifierConfig from a JSON string
device_secret_verifier_config_instance = DeviceSecretVerifierConfig.from_json(json)
# print the JSON string representation of the object
print DeviceSecretVerifierConfig.to_json()

# convert the object into a dict
device_secret_verifier_config_dict = device_secret_verifier_config_instance.to_dict()
# create an instance of DeviceSecretVerifierConfig from a dict
device_secret_verifier_config_form_dict = device_secret_verifier_config.from_dict(device_secret_verifier_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ConfirmDeviceParam

Parameters required to confirm a device. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | A valid access token. | 
**device_key** | **str** | The unique identifier of the device. | 
**device_name** | **str** | A friendly name for the device. | [optional] 
**device_secret_verifier_config** | [**DeviceSecretVerifierConfig**](DeviceSecretVerifierConfig.md) |  | [optional] 

## Example

```python
from saasus_sdk_python.src.auth.models.confirm_device_param import ConfirmDeviceParam

# TODO update the JSON string below
json = "{}"
# create an instance of ConfirmDeviceParam from a JSON string
confirm_device_param_instance = ConfirmDeviceParam.from_json(json)
# print the JSON string representation of the object
print ConfirmDeviceParam.to_json()

# convert the object into a dict
confirm_device_param_dict = confirm_device_param_instance.to_dict()
# create an instance of ConfirmDeviceParam from a dict
confirm_device_param_form_dict = confirm_device_param.from_dict(confirm_device_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ConfirmDeviceResult

Result returned after confirming a device. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_confirmation_necessary** | **bool** | When true, the user must confirm that they want to remember the device. When false, the device is immediately set as remembered.  | 

## Example

```python
from saasus_sdk_python.src.auth.models.confirm_device_result import ConfirmDeviceResult

# TODO update the JSON string below
json = "{}"
# create an instance of ConfirmDeviceResult from a JSON string
confirm_device_result_instance = ConfirmDeviceResult.from_json(json)
# print the JSON string representation of the object
print ConfirmDeviceResult.to_json()

# convert the object into a dict
confirm_device_result_dict = confirm_device_result_instance.to_dict()
# create an instance of ConfirmDeviceResult from a dict
confirm_device_result_form_dict = confirm_device_result.from_dict(confirm_device_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



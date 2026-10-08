# UpdateDeviceStatusParam

Parameters required to update a device status. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | A valid access token. | 
**device_key** | **str** | The unique identifier of the device. | 
**device_remembered_status** | [**DeviceRememberedStatus**](DeviceRememberedStatus.md) |  | 

## Example

```python
from saasus_sdk_python.src.auth.models.update_device_status_param import UpdateDeviceStatusParam

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDeviceStatusParam from a JSON string
update_device_status_param_instance = UpdateDeviceStatusParam.from_json(json)
# print the JSON string representation of the object
print UpdateDeviceStatusParam.to_json()

# convert the object into a dict
update_device_status_param_dict = update_device_status_param_instance.to_dict()
# create an instance of UpdateDeviceStatusParam from a dict
update_device_status_param_form_dict = update_device_status_param.from_dict(update_device_status_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



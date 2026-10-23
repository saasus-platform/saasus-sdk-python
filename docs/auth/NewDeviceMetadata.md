# NewDeviceMetadata

Metadata for a new device registered during authentication. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_key** | **str** | Device key identifier | [optional] 
**device_group_key** | **str** | Device group key identifier | [optional] 

## Example

```python
from saasus_sdk_python.src.auth.models.new_device_metadata import NewDeviceMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of NewDeviceMetadata from a JSON string
new_device_metadata_instance = NewDeviceMetadata.from_json(json)
# print the JSON string representation of the object
print NewDeviceMetadata.to_json()

# convert the object into a dict
new_device_metadata_dict = new_device_metadata_instance.to_dict()
# create an instance of NewDeviceMetadata from a dict
new_device_metadata_form_dict = new_device_metadata.from_dict(new_device_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# MeteringUnitCount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **int** | Timestamp | 
**count** | **int** | Count | 

## Example

```python
from saasus_sdk_python.src.pricing.models.metering_unit_count import MeteringUnitCount

# TODO update the JSON string below
json = "{}"
# create an instance of MeteringUnitCount from a JSON string
metering_unit_count_instance = MeteringUnitCount.from_json(json)
# print the JSON string representation of the object
print MeteringUnitCount.to_json()

# convert the object into a dict
metering_unit_count_dict = metering_unit_count_instance.to_dict()
# create an instance of MeteringUnitCount from a dict
metering_unit_count_form_dict = metering_unit_count.from_dict(metering_unit_count_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



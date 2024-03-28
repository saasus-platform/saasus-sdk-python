# MeteringUnits


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**units** | [**List[MeteringUnit]**](MeteringUnit.md) |  | 

## Example

```python
from saasus_sdk_python.src.pricing.models.metering_units import MeteringUnits

# TODO update the JSON string below
json = "{}"
# create an instance of MeteringUnits from a JSON string
metering_units_instance = MeteringUnits.from_json(json)
# print the JSON string representation of the object
print MeteringUnits.to_json()

# convert the object into a dict
metering_units_dict = metering_units_instance.to_dict()
# create an instance of MeteringUnits from a dict
metering_units_form_dict = metering_units.from_dict(metering_units_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# MeteringUnitProps


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unit_name** | **str** | 計測ユニット名 | 
**aggregate_usage** | [**AggregateUsage**](AggregateUsage.md) |  | [optional] 
**display_name** | **str** | 表示名 | 
**description** | **str** | 説明 | 

## Example

```python
from saasus_sdk_python.src.pricing.models.metering_unit_props import MeteringUnitProps

# TODO update the JSON string below
json = "{}"
# create an instance of MeteringUnitProps from a JSON string
metering_unit_props_instance = MeteringUnitProps.from_json(json)
# print the JSON string representation of the object
print MeteringUnitProps.to_json()

# convert the object into a dict
metering_unit_props_dict = metering_unit_props_instance.to_dict()
# create an instance of MeteringUnitProps from a dict
metering_unit_props_form_dict = metering_unit_props.from_dict(metering_unit_props_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



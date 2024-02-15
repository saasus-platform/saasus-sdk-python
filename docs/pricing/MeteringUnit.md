# MeteringUnit


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unit_name** | **str** | 計測ユニット名(metering unit name) | 
**aggregate_usage** | [**AggregateUsage**](AggregateUsage.md) |  | 
**display_name** | **str** | 表示名(display name) | 
**description** | **str** | 説明(description) | 
**id** | **str** |  | 
**used** | **bool** | メータリングユニットの使用済み設定(metering unit used settings) | 

## Example

```python
from saasus_sdk_python.src.pricing.models.metering_unit import MeteringUnit

# TODO update the JSON string below
json = "{}"
# create an instance of MeteringUnit from a JSON string
metering_unit_instance = MeteringUnit.from_json(json)
# print the JSON string representation of the object
print MeteringUnit.to_json()

# convert the object into a dict
metering_unit_dict = metering_unit_instance.to_dict()
# create an instance of MeteringUnit from a dict
metering_unit_form_dict = metering_unit.from_dict(metering_unit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



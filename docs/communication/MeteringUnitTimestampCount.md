# MeteringUnitTimestampCount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metering_unit_name** | **str** | 計測ユニット名(metering unit name) | 
**timestamp** | **int** | タイムスタンプ(timestamp) | 
**count** | **int** | 件数(count) | 

## Example

```python
from saasus_sdk_python.src.pricing.models.metering_unit_timestamp_count import MeteringUnitTimestampCount

# TODO update the JSON string below
json = "{}"
# create an instance of MeteringUnitTimestampCount from a JSON string
metering_unit_timestamp_count_instance = MeteringUnitTimestampCount.from_json(json)
# print the JSON string representation of the object
print MeteringUnitTimestampCount.to_json()

# convert the object into a dict
metering_unit_timestamp_count_dict = metering_unit_timestamp_count_instance.to_dict()
# create an instance of MeteringUnitTimestampCount from a dict
metering_unit_timestamp_count_form_dict = metering_unit_timestamp_count.from_dict(metering_unit_timestamp_count_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# MeteringUnitMonthCounts


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**counts** | [**List[MeteringUnitMonthCount]**](MeteringUnitMonthCount.md) |  | 

## Example

```python
from saasus_sdk_python.src.pricing.models.metering_unit_month_counts import MeteringUnitMonthCounts

# TODO update the JSON string below
json = "{}"
# create an instance of MeteringUnitMonthCounts from a JSON string
metering_unit_month_counts_instance = MeteringUnitMonthCounts.from_json(json)
# print the JSON string representation of the object
print MeteringUnitMonthCounts.to_json()

# convert the object into a dict
metering_unit_month_counts_dict = metering_unit_month_counts_instance.to_dict()
# create an instance of MeteringUnitMonthCounts from a dict
metering_unit_month_counts_form_dict = metering_unit_month_counts.from_dict(metering_unit_month_counts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



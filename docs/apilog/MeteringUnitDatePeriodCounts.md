# MeteringUnitDatePeriodCounts


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metering_unit_name** | **str** | 計測ユニット名(metering unit name) | 
**counts** | [**List[MeteringUnitCount]**](MeteringUnitCount.md) |  | 

## Example

```python
from saasus_sdk_python.src.pricing.models.metering_unit_date_period_counts import MeteringUnitDatePeriodCounts

# TODO update the JSON string below
json = "{}"
# create an instance of MeteringUnitDatePeriodCounts from a JSON string
metering_unit_date_period_counts_instance = MeteringUnitDatePeriodCounts.from_json(json)
# print the JSON string representation of the object
print MeteringUnitDatePeriodCounts.to_json()

# convert the object into a dict
metering_unit_date_period_counts_dict = metering_unit_date_period_counts_instance.to_dict()
# create an instance of MeteringUnitDatePeriodCounts from a dict
metering_unit_date_period_counts_form_dict = metering_unit_date_period_counts.from_dict(metering_unit_date_period_counts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



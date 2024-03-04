# MeteringUnitMonthCount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metering_unit_name** | **str** | 計測ユニット名 | 
**month** | **str** | 月 | 
**count** | **int** | 件数 | 

## Example

```python
from saasus_sdk_python.src.pricing.models.metering_unit_month_count import MeteringUnitMonthCount

# TODO update the JSON string below
json = "{}"
# create an instance of MeteringUnitMonthCount from a JSON string
metering_unit_month_count_instance = MeteringUnitMonthCount.from_json(json)
# print the JSON string representation of the object
print MeteringUnitMonthCount.to_json()

# convert the object into a dict
metering_unit_month_count_dict = metering_unit_month_count_instance.to_dict()
# create an instance of MeteringUnitMonthCount from a dict
metering_unit_month_count_form_dict = metering_unit_month_count.from_dict(metering_unit_month_count_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



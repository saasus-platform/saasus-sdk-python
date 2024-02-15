# MeteringUnitDateCount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metering_unit_name** | **str** | 計測ユニット名(metering unit name) | 
**var_date** | **str** | 日(date) | 
**count** | **int** | 件数(count) | 

## Example

```python
from saasus_sdk_python.src.pricing.models.metering_unit_date_count import MeteringUnitDateCount

# TODO update the JSON string below
json = "{}"
# create an instance of MeteringUnitDateCount from a JSON string
metering_unit_date_count_instance = MeteringUnitDateCount.from_json(json)
# print the JSON string representation of the object
print MeteringUnitDateCount.to_json()

# convert the object into a dict
metering_unit_date_count_dict = metering_unit_date_count_instance.to_dict()
# create an instance of MeteringUnitDateCount from a dict
metering_unit_date_count_form_dict = metering_unit_date_count.from_dict(metering_unit_date_count_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# MeteringUnitDateCounts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**counts** | [**List[MeteringUnitDateCount]**](MeteringUnitDateCount.md) |  | 

## Example

```python
from saasus_sdk_python.src.pricing.models.metering_unit_date_counts import MeteringUnitDateCounts

# TODO update the JSON string below
json = "{}"
# create an instance of MeteringUnitDateCounts from a JSON string
metering_unit_date_counts_instance = MeteringUnitDateCounts.from_json(json)
# print the JSON string representation of the object
print MeteringUnitDateCounts.to_json()

# convert the object into a dict
metering_unit_date_counts_dict = metering_unit_date_counts_instance.to_dict()
# create an instance of MeteringUnitDateCounts from a dict
metering_unit_date_counts_form_dict = metering_unit_date_counts.from_dict(metering_unit_date_counts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



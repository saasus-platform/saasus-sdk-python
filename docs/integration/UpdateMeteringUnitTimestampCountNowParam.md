# UpdateMeteringUnitTimestampCountNowParam


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | [**UpdateMeteringUnitTimestampCountMethod**](UpdateMeteringUnitTimestampCountMethod.md) |  | 
**count** | **int** | 件数 | 

## Example

```python
from saasus_sdk_python.src.pricing.models.update_metering_unit_timestamp_count_now_param import UpdateMeteringUnitTimestampCountNowParam

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMeteringUnitTimestampCountNowParam from a JSON string
update_metering_unit_timestamp_count_now_param_instance = UpdateMeteringUnitTimestampCountNowParam.from_json(json)
# print the JSON string representation of the object
print UpdateMeteringUnitTimestampCountNowParam.to_json()

# convert the object into a dict
update_metering_unit_timestamp_count_now_param_dict = update_metering_unit_timestamp_count_now_param_instance.to_dict()
# create an instance of UpdateMeteringUnitTimestampCountNowParam from a dict
update_metering_unit_timestamp_count_now_param_form_dict = update_metering_unit_timestamp_count_now_param.from_dict(update_metering_unit_timestamp_count_now_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



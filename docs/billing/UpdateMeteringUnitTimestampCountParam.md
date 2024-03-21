# UpdateMeteringUnitTimestampCountParam


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | [**UpdateMeteringUnitTimestampCountMethod**](UpdateMeteringUnitTimestampCountMethod.md) |  | 
**count** | **int** | Count | 

## Example

```python
from saasus_sdk_python.src.pricing.models.update_metering_unit_timestamp_count_param import UpdateMeteringUnitTimestampCountParam

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMeteringUnitTimestampCountParam from a JSON string
update_metering_unit_timestamp_count_param_instance = UpdateMeteringUnitTimestampCountParam.from_json(json)
# print the JSON string representation of the object
print UpdateMeteringUnitTimestampCountParam.to_json()

# convert the object into a dict
update_metering_unit_timestamp_count_param_dict = update_metering_unit_timestamp_count_param_instance.to_dict()
# create an instance of UpdateMeteringUnitTimestampCountParam from a dict
update_metering_unit_timestamp_count_param_form_dict = update_metering_unit_timestamp_count_param.from_dict(update_metering_unit_timestamp_count_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



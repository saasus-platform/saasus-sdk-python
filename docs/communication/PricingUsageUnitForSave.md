# PricingUsageUnitForSave


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | 名前(name) | 
**display_name** | **str** | 表示名(display name) | 
**description** | **str** | 説明(description) | 
**type** | [**UnitType**](UnitType.md) |  | 
**currency** | [**Currency**](Currency.md) |  | 
**upper_count** | **int** | 上限値(upper limit) | 
**unit_amount** | **int** | 使用量あたりの金額(amount per usage) | 
**metering_unit_name** | **str** |  | 
**aggregate_usage** | [**AggregateUsage**](AggregateUsage.md) |  | [optional] 

## Example

```python
from saasus_sdk_python.src.pricing.models.pricing_usage_unit_for_save import PricingUsageUnitForSave

# TODO update the JSON string below
json = "{}"
# create an instance of PricingUsageUnitForSave from a JSON string
pricing_usage_unit_for_save_instance = PricingUsageUnitForSave.from_json(json)
# print the JSON string representation of the object
print PricingUsageUnitForSave.to_json()

# convert the object into a dict
pricing_usage_unit_for_save_dict = pricing_usage_unit_for_save_instance.to_dict()
# create an instance of PricingUsageUnitForSave from a dict
pricing_usage_unit_for_save_form_dict = pricing_usage_unit_for_save.from_dict(pricing_usage_unit_for_save_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



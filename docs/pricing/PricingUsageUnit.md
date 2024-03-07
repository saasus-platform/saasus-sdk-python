# PricingUsageUnit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**upper_count** | **int** | Upper limit | 
**unit_amount** | **int** | Amount per usage | 
**metering_unit_name** | **str** | Metering unit name | 
**aggregate_usage** | [**AggregateUsage**](AggregateUsage.md) |  | [optional] 
**name** | **str** | Name | 
**display_name** | **str** | Display Name | 
**description** | **str** | Description | 
**type** | [**UnitType**](UnitType.md) |  | 
**currency** | [**Currency**](Currency.md) |  | 
**id** | **str** | Universally Unique Identifier | 
**metering_unit_id** | **str** | Universally Unique Identifier | 
**recurring_interval** | [**RecurringInterval**](RecurringInterval.md) |  | 
**used** | **bool** |  | 

## Example

```python
from saasus_sdk_python.src.pricing.models.pricing_usage_unit import PricingUsageUnit

# TODO update the JSON string below
json = "{}"
# create an instance of PricingUsageUnit from a JSON string
pricing_usage_unit_instance = PricingUsageUnit.from_json(json)
# print the JSON string representation of the object
print PricingUsageUnit.to_json()

# convert the object into a dict
pricing_usage_unit_dict = pricing_usage_unit_instance.to_dict()
# create an instance of PricingUsageUnit from a dict
pricing_usage_unit_form_dict = pricing_usage_unit.from_dict(pricing_usage_unit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



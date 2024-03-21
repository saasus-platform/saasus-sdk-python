# PricingUnitForSave


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**upper_count** | **int** | Upper limit | 
**metering_unit_name** | **str** | Metering unit name | 
**aggregate_usage** | [**AggregateUsage**](AggregateUsage.md) |  | [optional] 
**name** | **str** | Name | 
**display_name** | **str** | Display Name | 
**description** | **str** | Description | 
**type** | [**UnitType**](UnitType.md) |  | 
**currency** | [**Currency**](Currency.md) |  | 
**tiers** | [**List[PricingTier]**](PricingTier.md) |  | 
**unit_amount** | **int** | Price | 
**recurring_interval** | [**RecurringInterval**](RecurringInterval.md) |  | 

## Example

```python
from saasus_sdk_python.src.pricing.models.pricing_unit_for_save import PricingUnitForSave

# TODO update the JSON string below
json = "{}"
# create an instance of PricingUnitForSave from a JSON string
pricing_unit_for_save_instance = PricingUnitForSave.from_json(json)
# print the JSON string representation of the object
print PricingUnitForSave.to_json()

# convert the object into a dict
pricing_unit_for_save_dict = pricing_unit_for_save_instance.to_dict()
# create an instance of PricingUnitForSave from a dict
pricing_unit_for_save_form_dict = pricing_unit_for_save.from_dict(pricing_unit_for_save_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# PricingFixedUnitForSave


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name | 
**display_name** | **str** | Display Name | 
**description** | **str** | Description | 
**type** | [**UnitType**](UnitType.md) |  | 
**currency** | [**Currency**](Currency.md) |  | 
**unit_amount** | **int** | Price | 
**recurring_interval** | [**RecurringInterval**](RecurringInterval.md) |  | 

## Example

```python
from saasus_sdk_python.src.pricing.models.pricing_fixed_unit_for_save import PricingFixedUnitForSave

# TODO update the JSON string below
json = "{}"
# create an instance of PricingFixedUnitForSave from a JSON string
pricing_fixed_unit_for_save_instance = PricingFixedUnitForSave.from_json(json)
# print the JSON string representation of the object
print PricingFixedUnitForSave.to_json()

# convert the object into a dict
pricing_fixed_unit_for_save_dict = pricing_fixed_unit_for_save_instance.to_dict()
# create an instance of PricingFixedUnitForSave from a dict
pricing_fixed_unit_for_save_form_dict = pricing_fixed_unit_for_save.from_dict(pricing_fixed_unit_for_save_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



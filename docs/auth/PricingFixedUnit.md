# PricingFixedUnit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unit_amount** | **int** | 料金 | 
**recurring_interval** | [**RecurringInterval**](RecurringInterval.md) |  | 
**name** | **str** | 名前 | 
**display_name** | **str** | 表示名 | 
**description** | **str** | 説明 | 
**type** | [**UnitType**](UnitType.md) |  | 
**currency** | [**Currency**](Currency.md) |  | 
**id** | **str** | ユニバーサル一意識別子 | 
**used** | **bool** |  | 

## Example

```python
from saasus_sdk_python.src.pricing.models.pricing_fixed_unit import PricingFixedUnit

# TODO update the JSON string below
json = "{}"
# create an instance of PricingFixedUnit from a JSON string
pricing_fixed_unit_instance = PricingFixedUnit.from_json(json)
# print the JSON string representation of the object
print PricingFixedUnit.to_json()

# convert the object into a dict
pricing_fixed_unit_dict = pricing_fixed_unit_instance.to_dict()
# create an instance of PricingFixedUnit from a dict
pricing_fixed_unit_form_dict = pricing_fixed_unit.from_dict(pricing_fixed_unit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



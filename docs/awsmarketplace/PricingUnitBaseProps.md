# PricingUnitBaseProps


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name | 
**display_name** | **str** | Display Name | 
**description** | **str** | Description | 
**type** | [**UnitType**](UnitType.md) |  | 
**currency** | [**Currency**](Currency.md) |  | 

## Example

```python
from saasus_sdk_python.src.pricing.models.pricing_unit_base_props import PricingUnitBaseProps

# TODO update the JSON string below
json = "{}"
# create an instance of PricingUnitBaseProps from a JSON string
pricing_unit_base_props_instance = PricingUnitBaseProps.from_json(json)
# print the JSON string representation of the object
print PricingUnitBaseProps.to_json()

# convert the object into a dict
pricing_unit_base_props_dict = pricing_unit_base_props_instance.to_dict()
# create an instance of PricingUnitBaseProps from a dict
pricing_unit_base_props_form_dict = pricing_unit_base_props.from_dict(pricing_unit_base_props_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



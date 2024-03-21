# PricingUnits


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**units** | [**List[PricingUnit]**](PricingUnit.md) |  | 

## Example

```python
from saasus_sdk_python.src.pricing.models.pricing_units import PricingUnits

# TODO update the JSON string below
json = "{}"
# create an instance of PricingUnits from a JSON string
pricing_units_instance = PricingUnits.from_json(json)
# print the JSON string representation of the object
print PricingUnits.to_json()

# convert the object into a dict
pricing_units_dict = pricing_units_instance.to_dict()
# create an instance of PricingUnits from a dict
pricing_units_form_dict = pricing_units.from_dict(pricing_units_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



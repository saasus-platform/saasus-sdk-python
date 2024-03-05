# PricingMenuProps


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**units** | [**List[PricingUnit]**](PricingUnit.md) |  | 
**name** | **str** | Menu name | 
**display_name** | **str** | Menu display name | 
**description** | **str** | Menu description | 
**used** | **bool** | Menu used settings | 

## Example

```python
from saasus_sdk_python.src.pricing.models.pricing_menu_props import PricingMenuProps

# TODO update the JSON string below
json = "{}"
# create an instance of PricingMenuProps from a JSON string
pricing_menu_props_instance = PricingMenuProps.from_json(json)
# print the JSON string representation of the object
print PricingMenuProps.to_json()

# convert the object into a dict
pricing_menu_props_dict = pricing_menu_props_instance.to_dict()
# create an instance of PricingMenuProps from a dict
pricing_menu_props_form_dict = pricing_menu_props.from_dict(pricing_menu_props_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# PricingMenus


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pricing_menus** | [**List[PricingMenu]**](PricingMenu.md) |  | 

## Example

```python
from saasus_sdk_python.src.pricing.models.pricing_menus import PricingMenus

# TODO update the JSON string below
json = "{}"
# create an instance of PricingMenus from a JSON string
pricing_menus_instance = PricingMenus.from_json(json)
# print the JSON string representation of the object
print PricingMenus.to_json()

# convert the object into a dict
pricing_menus_dict = pricing_menus_instance.to_dict()
# create an instance of PricingMenus from a dict
pricing_menus_form_dict = pricing_menus.from_dict(pricing_menus_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



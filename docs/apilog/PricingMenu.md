# PricingMenu


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | メニュー名(menu name) | 
**display_name** | **str** | メニュー表示名(menu display name) | 
**description** | **str** | メニュー説明(menu description) | 
**used** | **bool** | メニューの使用済み設定(menu used settings) | 
**units** | [**List[PricingUnit]**](PricingUnit.md) |  | 
**id** | **str** |  | 

## Example

```python
from saasus_sdk_python.src.pricing.models.pricing_menu import PricingMenu

# TODO update the JSON string below
json = "{}"
# create an instance of PricingMenu from a JSON string
pricing_menu_instance = PricingMenu.from_json(json)
# print the JSON string representation of the object
print PricingMenu.to_json()

# convert the object into a dict
pricing_menu_dict = pricing_menu_instance.to_dict()
# create an instance of PricingMenu from a dict
pricing_menu_form_dict = pricing_menu.from_dict(pricing_menu_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



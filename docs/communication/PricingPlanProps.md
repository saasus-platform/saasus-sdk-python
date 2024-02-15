# PricingPlanProps


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pricing_menus** | [**List[PricingMenu]**](PricingMenu.md) |  | 
**name** | **str** | 料金プラン名(pricing plan name) | 
**display_name** | **str** | 料金プラン表示名(pricing plan display name) | 
**description** | **str** | 料金プラン説明(pricing plan description) | 
**used** | **bool** | 料金プランの使用済み設定(pricing plan used settings) | 

## Example

```python
from saasus_sdk_python.src.pricing.models.pricing_plan_props import PricingPlanProps

# TODO update the JSON string below
json = "{}"
# create an instance of PricingPlanProps from a JSON string
pricing_plan_props_instance = PricingPlanProps.from_json(json)
# print the JSON string representation of the object
print PricingPlanProps.to_json()

# convert the object into a dict
pricing_plan_props_dict = pricing_plan_props_instance.to_dict()
# create an instance of PricingPlanProps from a dict
pricing_plan_props_form_dict = pricing_plan_props.from_dict(pricing_plan_props_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


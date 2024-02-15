# PricingPlan


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | 料金プラン名(pricing plan name) | 
**display_name** | **str** | 料金プラン表示名(pricing plan display name) | 
**description** | **str** | 料金プラン説明(pricing plan description) | 
**used** | **bool** | 料金プランの使用済み設定(pricing plan used settings) | 
**pricing_menus** | [**List[PricingMenu]**](PricingMenu.md) |  | 
**id** | **str** |  | 

## Example

```python
from saasus_sdk_python.src.pricing.models.pricing_plan import PricingPlan

# TODO update the JSON string below
json = "{}"
# create an instance of PricingPlan from a JSON string
pricing_plan_instance = PricingPlan.from_json(json)
# print the JSON string representation of the object
print PricingPlan.to_json()

# convert the object into a dict
pricing_plan_dict = pricing_plan_instance.to_dict()
# create an instance of PricingPlan from a dict
pricing_plan_form_dict = pricing_plan.from_dict(pricing_plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



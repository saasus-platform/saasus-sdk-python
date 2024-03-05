# SavePricingPlanParam


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Pricing plan name | 
**display_name** | **str** | Pricing plan display name | 
**description** | **str** | Pricing plan description | 
**menu_ids** | **List[str]** | Menu ID to be added to the pricing plan | 

## Example

```python
from saasus_sdk_python.src.pricing.models.save_pricing_plan_param import SavePricingPlanParam

# TODO update the JSON string below
json = "{}"
# create an instance of SavePricingPlanParam from a JSON string
save_pricing_plan_param_instance = SavePricingPlanParam.from_json(json)
# print the JSON string representation of the object
print SavePricingPlanParam.to_json()

# convert the object into a dict
save_pricing_plan_param_dict = save_pricing_plan_param_instance.to_dict()
# create an instance of SavePricingPlanParam from a dict
save_pricing_plan_param_form_dict = save_pricing_plan_param.from_dict(save_pricing_plan_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



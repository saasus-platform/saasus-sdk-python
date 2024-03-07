# PricingPlans


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pricing_plans** | [**List[PricingPlan]**](PricingPlan.md) |  | 

## Example

```python
from saasus_sdk_python.src.pricing.models.pricing_plans import PricingPlans

# TODO update the JSON string below
json = "{}"
# create an instance of PricingPlans from a JSON string
pricing_plans_instance = PricingPlans.from_json(json)
# print the JSON string representation of the object
print PricingPlans.to_json()

# convert the object into a dict
pricing_plans_dict = pricing_plans_instance.to_dict()
# create an instance of PricingPlans from a dict
pricing_plans_form_dict = pricing_plans.from_dict(pricing_plans_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# UpdatePricingPlansUsedParam


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_ids** | **List[str]** |  | 

## Example

```python
from saasus_sdk_python.src.pricing.models.update_pricing_plans_used_param import UpdatePricingPlansUsedParam

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePricingPlansUsedParam from a JSON string
update_pricing_plans_used_param_instance = UpdatePricingPlansUsedParam.from_json(json)
# print the JSON string representation of the object
print UpdatePricingPlansUsedParam.to_json()

# convert the object into a dict
update_pricing_plans_used_param_dict = update_pricing_plans_used_param_instance.to_dict()
# create an instance of UpdatePricingPlansUsedParam from a dict
update_pricing_plans_used_param_form_dict = update_pricing_plans_used_param.from_dict(update_pricing_plans_used_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



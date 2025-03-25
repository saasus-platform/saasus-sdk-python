# PlanHistory


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_id** | **str** |  | 
**plan_applied_at** | **int** | Registration date | 
**tax_rate_id** | **str** |  | [optional] 
**proration_behavior** | [**ProrationBehavior**](ProrationBehavior.md) |  | [optional] 
**delete_usage** | **bool** | If you have a stripe linkage,  you can set whether to delete pay-as-you-go items when changing plans. When you change plan, you can remove all pay-as-you-go items included in your current subscription to stop being billed based on pay-as-you-go items. The recorded usage is cleared immediately. Since it cannot be restored, please note that plan change reservations with delete_usage set to true cannot be canceled.  | [optional] 

## Example

```python
from saasus_sdk_python.src.auth.models.plan_history import PlanHistory

# TODO update the JSON string below
json = "{}"
# create an instance of PlanHistory from a JSON string
plan_history_instance = PlanHistory.from_json(json)
# print the JSON string representation of the object
print PlanHistory.to_json()

# convert the object into a dict
plan_history_dict = plan_history_instance.to_dict()
# create an instance of PlanHistory from a dict
plan_history_form_dict = plan_history.from_dict(plan_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



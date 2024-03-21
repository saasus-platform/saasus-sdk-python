# PlanReservation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_plan_id** | **str** |  | [optional] 
**using_next_plan_from** | **int** | Next billing plan start time (When using stripe, you can create a subscription that starts at the beginning of the current month by specifying 00:00 (UTC) at the beginning of the current month. Ex. 1672531200 for January 2023.)  | [optional] 
**next_plan_tax_rate_id** | **str** |  | [optional] 
**proration_behavior** | [**ProrationBehavior**](ProrationBehavior.md) |  | [optional] 
**delete_usage** | **bool** | If you have a stripe linkage,  you can set whether to delete pay-as-you-go items when changing plans. When you change plan, you can remove all pay-as-you-go items included in your current subscription to stop being billed based on pay-as-you-go items. The recorded usage is cleared immediately. Since it cannot be restored, please note that plan change reservations with delete_usage set to true cannot be canceled.  | [optional] 

## Example

```python
from saasus_sdk_python.src.auth.models.plan_reservation import PlanReservation

# TODO update the JSON string below
json = "{}"
# create an instance of PlanReservation from a JSON string
plan_reservation_instance = PlanReservation.from_json(json)
# print the JSON string representation of the object
print PlanReservation.to_json()

# convert the object into a dict
plan_reservation_dict = plan_reservation_instance.to_dict()
# create an instance of PlanReservation from a dict
plan_reservation_form_dict = plan_reservation.from_dict(plan_reservation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



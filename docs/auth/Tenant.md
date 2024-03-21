# Tenant


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | tenant name | 
**attributes** | **Dict[str, object]** | attribute info | 
**back_office_staff_email** | **str** | administrative staff email address | 
**next_plan_id** | **str** |  | [optional] 
**using_next_plan_from** | **int** | Next billing plan start time (When using stripe, you can create a subscription that starts at the beginning of the current month by specifying 00:00 (UTC) at the beginning of the current month. Ex. 1672531200 for January 2023.)  | [optional] 
**next_plan_tax_rate_id** | **str** |  | [optional] 
**proration_behavior** | [**ProrationBehavior**](ProrationBehavior.md) |  | [optional] 
**delete_usage** | **bool** | If you have a stripe linkage,  you can set whether to delete pay-as-you-go items when changing plans. When you change plan, you can remove all pay-as-you-go items included in your current subscription to stop being billed based on pay-as-you-go items. The recorded usage is cleared immediately. Since it cannot be restored, please note that plan change reservations with delete_usage set to true cannot be canceled.  | [optional] 
**plan_histories** | [**List[PlanHistory]**](PlanHistory.md) | Plan History | 
**id** | **str** |  | 
**plan_id** | **str** |  | [optional] 
**billing_info** | [**BillingInfo**](BillingInfo.md) |  | [optional] 

## Example

```python
from saasus_sdk_python.src.auth.models.tenant import Tenant

# TODO update the JSON string below
json = "{}"
# create an instance of Tenant from a JSON string
tenant_instance = Tenant.from_json(json)
# print the JSON string representation of the object
print Tenant.to_json()

# convert the object into a dict
tenant_dict = tenant_instance.to_dict()
# create an instance of Tenant from a dict
tenant_form_dict = tenant.from_dict(tenant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



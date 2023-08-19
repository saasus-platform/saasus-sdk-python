# Tenant


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | テナント名(tenant name) | 
**attributes** | **Dict[str, object]** | 属性情報(attribute info) | 
**back_office_staff_email** | **str** | 事務管理部門スタッフメールアドレス(administrative staff email address) | 
**next_plan_id** | **str** |  | [optional] 
**using_next_plan_from** | **int** | 次回料金プラン開始日時（stripe連携時、当月月初の0時（UTC）を指定すると当月月初開始のサブスクリプションを作成できます。ex. 2023年1月の場合は、1672531200 ） (Next billing plan start time (When using stripe, you can create a subscription that starts at the beginning of the current month by specifying 00:00 (UTC) at the beginning of the current month. Ex. 1672531200 for January 2023.))  | [optional] 
**next_plan_tax_rate_id** | **str** |  | [optional] 
**plan_histories** | [**List[PlanHistory]**](PlanHistory.md) | 料金プラン履歴 | 
**id** | **str** |  | 
**plan_id** | **str** |  | [optional] 
**billing_info** | [**BillingInfo**](BillingInfo.md) |  | [optional] 

## Example

```python
from saasus_sdk_python.models.tenant import Tenant

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



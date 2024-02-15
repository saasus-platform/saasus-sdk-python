# TenantDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**plan_id** | **str** |  | [optional] 
**billing_info** | [**BillingInfo**](BillingInfo.md) |  | [optional] 
**name** | **str** | テナント名(tenant name) | 
**attributes** | **Dict[str, object]** | 属性情報(attribute info) | 
**back_office_staff_email** | **str** | 事務管理部門スタッフメールアドレス(administrative staff email address) | 
**next_plan_id** | **str** |  | [optional] 
**using_next_plan_from** | **int** | 次回料金プラン開始日時（stripe連携時、当月月初の0時（UTC）を指定すると当月月初開始のサブスクリプションを作成できます。ex. 2023年1月の場合は、1672531200 ） (Next billing plan start time (When using stripe, you can create a subscription that starts at the beginning of the current month by specifying 00:00 (UTC) at the beginning of the current month. Ex. 1672531200 for January 2023.))  | [optional] 
**next_plan_tax_rate_id** | **str** |  | [optional] 
**proration_behavior** | [**ProrationBehavior**](ProrationBehavior.md) |  | [optional] 
**delete_usage** | **bool** | stripe連携している場合で、プラン変更時に従量課金アイテムを削除するか設定できます。 プラン変更した場合に、現在のサブスクリプションに含まれる従量課金アイテムを全て削除して、従量課金アイテムに基づく請求の発生を止めることができます。 即時に記録している使用量がクリアされます。それらは復元できないため、delete_usageをtrueにしたプラン変更予約は取り消しできません。  If you have a stripe linkage,  you can set whether to delete pay-as-you-go items when changing plans. When you change plan, you can remove all pay-as-you-go items included in your current subscription to stop being billed based on pay-as-you-go items. The recorded usage is cleared immediately. Since it cannot be restored, please note that plan change reservations with delete_usage set to true cannot be canceled.  | [optional] 
**plan_histories** | [**List[PlanHistory]**](PlanHistory.md) | 料金プラン履歴 | 
**current_plan_period_start** | **int** | 現在のプランの開始日時(current plan period start) | [optional] 
**current_plan_period_end** | **int** | 現在のプランの終了日時(current plan period end) | [optional] 

## Example

```python
from saasus_sdk_python.src.auth.models.tenant_detail import TenantDetail

# TODO update the JSON string below
json = "{}"
# create an instance of TenantDetail from a JSON string
tenant_detail_instance = TenantDetail.from_json(json)
# print the JSON string representation of the object
print TenantDetail.to_json()

# convert the object into a dict
tenant_detail_dict = tenant_detail_instance.to_dict()
# create an instance of TenantDetail from a dict
tenant_detail_form_dict = tenant_detail.from_dict(tenant_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



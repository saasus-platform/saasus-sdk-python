# UserAvailableTenant


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** | テナント名(tenant name) | 
**completed_sign_up** | **bool** |  | 
**envs** | [**List[UserAvailableEnv]**](UserAvailableEnv.md) | 環境情報、役割(ロール)情報(environmental info, role info) | 
**user_attribute** | **Dict[str, object]** | ユーザー追加属性(user additional attributes) | 
**back_office_staff_email** | **str** | バックオフィス担当者のメール(back office contact email) | 
**plan_id** | **str** |  | [optional] 
**is_paid** | **bool** | テナントの支払い状況(tenant payment status)  ※ 現在はストライプ連携時のみ返却されます。Currently, it is returned only when stripe is linked.  | [optional] 

## Example

```python
from saasus_sdk_python.src.auth.models.user_available_tenant import UserAvailableTenant

# TODO update the JSON string below
json = "{}"
# create an instance of UserAvailableTenant from a JSON string
user_available_tenant_instance = UserAvailableTenant.from_json(json)
# print the JSON string representation of the object
print UserAvailableTenant.to_json()

# convert the object into a dict
user_available_tenant_dict = user_available_tenant_instance.to_dict()
# create an instance of UserAvailableTenant from a dict
user_available_tenant_form_dict = user_available_tenant.from_dict(user_available_tenant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



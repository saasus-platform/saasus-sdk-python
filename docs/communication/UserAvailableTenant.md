# UserAvailableTenant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** | Tenant Name | 
**completed_sign_up** | **bool** |  | 
**envs** | [**List[UserAvailableEnv]**](UserAvailableEnv.md) | environmental info, role info | 
**user_attribute** | **Dict[str, object]** | user additional attributes | 
**back_office_staff_email** | **str** | back office contact email | 
**plan_id** | **str** |  | [optional] 
**is_paid** | **bool** | tenant payment status ※ Currently, it is returned only when stripe is linked.  | [optional] 

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



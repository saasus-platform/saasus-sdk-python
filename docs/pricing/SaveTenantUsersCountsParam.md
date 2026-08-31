# SaveTenantUsersCountsParam


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_user_counts** | [**List[SaveTenantUserCountParam]**](SaveTenantUserCountParam.md) |  | 

## Example

```python
from saasus_sdk_python.src.auth.models.save_tenant_users_counts_param import SaveTenantUsersCountsParam

# TODO update the JSON string below
json = "{}"
# create an instance of SaveTenantUsersCountsParam from a JSON string
save_tenant_users_counts_param_instance = SaveTenantUsersCountsParam.from_json(json)
# print the JSON string representation of the object
print SaveTenantUsersCountsParam.to_json()

# convert the object into a dict
save_tenant_users_counts_param_dict = save_tenant_users_counts_param_instance.to_dict()
# create an instance of SaveTenantUsersCountsParam from a dict
save_tenant_users_counts_param_form_dict = save_tenant_users_counts_param.from_dict(save_tenant_users_counts_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# TenantUsersCounts


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_user_counts** | [**List[TenantUserCount]**](TenantUserCount.md) |  | 

## Example

```python
from saasus_sdk_python.src.auth.models.tenant_users_counts import TenantUsersCounts

# TODO update the JSON string below
json = "{}"
# create an instance of TenantUsersCounts from a JSON string
tenant_users_counts_instance = TenantUsersCounts.from_json(json)
# print the JSON string representation of the object
print TenantUsersCounts.to_json()

# convert the object into a dict
tenant_users_counts_dict = tenant_users_counts_instance.to_dict()
# create an instance of TenantUsersCounts from a dict
tenant_users_counts_form_dict = tenant_users_counts.from_dict(tenant_users_counts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# TenantUserCount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | 
**count** | **int** | Count of tenant users | 
**updated_at** | **int** | Unix timestamp (seconds) of the last update | 

## Example

```python
from saasus_sdk_python.src.auth.models.tenant_user_count import TenantUserCount

# TODO update the JSON string below
json = "{}"
# create an instance of TenantUserCount from a JSON string
tenant_user_count_instance = TenantUserCount.from_json(json)
# print the JSON string representation of the object
print TenantUserCount.to_json()

# convert the object into a dict
tenant_user_count_dict = tenant_user_count_instance.to_dict()
# create an instance of TenantUserCount from a dict
tenant_user_count_form_dict = tenant_user_count.from_dict(tenant_user_count_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



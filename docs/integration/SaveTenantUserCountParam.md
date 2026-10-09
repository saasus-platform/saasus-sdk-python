# SaveTenantUserCountParam


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | 
**count** | **int** | Count of tenant users | 

## Example

```python
from saasus_sdk_python.src.auth.models.save_tenant_user_count_param import SaveTenantUserCountParam

# TODO update the JSON string below
json = "{}"
# create an instance of SaveTenantUserCountParam from a JSON string
save_tenant_user_count_param_instance = SaveTenantUserCountParam.from_json(json)
# print the JSON string representation of the object
print SaveTenantUserCountParam.to_json()

# convert the object into a dict
save_tenant_user_count_param_dict = save_tenant_user_count_param_instance.to_dict()
# create an instance of SaveTenantUserCountParam from a dict
save_tenant_user_count_param_form_dict = save_tenant_user_count_param.from_dict(save_tenant_user_count_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



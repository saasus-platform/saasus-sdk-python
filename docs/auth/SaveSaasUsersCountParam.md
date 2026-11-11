# SaveSaasUsersCountParam


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Count of SaaS users | 

## Example

```python
from saasus_sdk_python.src.auth.models.save_saas_users_count_param import SaveSaasUsersCountParam

# TODO update the JSON string below
json = "{}"
# create an instance of SaveSaasUsersCountParam from a JSON string
save_saas_users_count_param_instance = SaveSaasUsersCountParam.from_json(json)
# print the JSON string representation of the object
print SaveSaasUsersCountParam.to_json()

# convert the object into a dict
save_saas_users_count_param_dict = save_saas_users_count_param_instance.to_dict()
# create an instance of SaveSaasUsersCountParam from a dict
save_saas_users_count_param_form_dict = save_saas_users_count_param.from_dict(save_saas_users_count_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



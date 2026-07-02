# SaasUsersCount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Count of SaaS users | 
**updated_at** | **int** | Unix timestamp (seconds) of the last update | 

## Example

```python
from saasus_sdk_python.src.auth.models.saas_users_count import SaasUsersCount

# TODO update the JSON string below
json = "{}"
# create an instance of SaasUsersCount from a JSON string
saas_users_count_instance = SaasUsersCount.from_json(json)
# print the JSON string representation of the object
print SaasUsersCount.to_json()

# convert the object into a dict
saas_users_count_dict = saas_users_count_instance.to_dict()
# create an instance of SaasUsersCount from a dict
saas_users_count_form_dict = saas_users_count.from_dict(saas_users_count_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



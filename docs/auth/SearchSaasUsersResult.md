# SearchSaasUsersResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | [**List[SaasUser]**](SaasUser.md) |  | 
**cursor** | **str** | Pagination cursor for the next page | [optional] 

## Example

```python
from saasus_sdk_python.src.auth.models.search_saas_users_result import SearchSaasUsersResult

# TODO update the JSON string below
json = "{}"
# create an instance of SearchSaasUsersResult from a JSON string
search_saas_users_result_instance = SearchSaasUsersResult.from_json(json)
# print the JSON string representation of the object
print SearchSaasUsersResult.to_json()

# convert the object into a dict
search_saas_users_result_dict = search_saas_users_result_instance.to_dict()
# create an instance of SearchSaasUsersResult from a dict
search_saas_users_result_form_dict = search_saas_users_result.from_dict(search_saas_users_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



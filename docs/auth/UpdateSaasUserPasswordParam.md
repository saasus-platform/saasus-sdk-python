# UpdateSaasUserPasswordParam


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | Password | 

## Example

```python
from saasus_sdk_python.src.auth.models.update_saas_user_password_param import UpdateSaasUserPasswordParam

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSaasUserPasswordParam from a JSON string
update_saas_user_password_param_instance = UpdateSaasUserPasswordParam.from_json(json)
# print the JSON string representation of the object
print UpdateSaasUserPasswordParam.to_json()

# convert the object into a dict
update_saas_user_password_param_dict = update_saas_user_password_param_instance.to_dict()
# create an instance of UpdateSaasUserPasswordParam from a dict
update_saas_user_password_param_form_dict = update_saas_user_password_param.from_dict(update_saas_user_password_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



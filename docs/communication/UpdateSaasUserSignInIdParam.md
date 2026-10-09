# UpdateSaasUserSignInIdParam


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sign_in_id** | **str** | Sign-in ID | 

## Example

```python
from saasus_sdk_python.src.auth.models.update_saas_user_sign_in_id_param import UpdateSaasUserSignInIdParam

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSaasUserSignInIdParam from a JSON string
update_saas_user_sign_in_id_param_instance = UpdateSaasUserSignInIdParam.from_json(json)
# print the JSON string representation of the object
print UpdateSaasUserSignInIdParam.to_json()

# convert the object into a dict
update_saas_user_sign_in_id_param_dict = update_saas_user_sign_in_id_param_instance.to_dict()
# create an instance of UpdateSaasUserSignInIdParam from a dict
update_saas_user_sign_in_id_param_form_dict = update_saas_user_sign_in_id_param.from_dict(update_saas_user_sign_in_id_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



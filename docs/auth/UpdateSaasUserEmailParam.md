# UpdateSaasUserEmailParam


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | E-mail | 

## Example

```python
from saasus_sdk_python.src.auth.models.update_saas_user_email_param import UpdateSaasUserEmailParam

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSaasUserEmailParam from a JSON string
update_saas_user_email_param_instance = UpdateSaasUserEmailParam.from_json(json)
# print the JSON string representation of the object
print UpdateSaasUserEmailParam.to_json()

# convert the object into a dict
update_saas_user_email_param_dict = update_saas_user_email_param_instance.to_dict()
# create an instance of UpdateSaasUserEmailParam from a dict
update_saas_user_email_param_form_dict = update_saas_user_email_param.from_dict(update_saas_user_email_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



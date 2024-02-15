# CreateSaasUserParam


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | メールアドレス(E-mail) | 
**password** | **str** | パスワード(Password) | 

## Example

```python
from saasus_sdk_python.src.auth.models.create_saas_user_param import CreateSaasUserParam

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSaasUserParam from a JSON string
create_saas_user_param_instance = CreateSaasUserParam.from_json(json)
# print the JSON string representation of the object
print CreateSaasUserParam.to_json()

# convert the object into a dict
create_saas_user_param_dict = create_saas_user_param_instance.to_dict()
# create an instance of CreateSaasUserParam from a dict
create_saas_user_param_form_dict = create_saas_user_param.from_dict(create_saas_user_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



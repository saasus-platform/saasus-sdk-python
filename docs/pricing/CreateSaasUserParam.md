# CreateSaasUserParam

Either email or sign_in_id must be specified, but not both. - If email is specified: Email authentication user will be created.   When password is not specified, a temporary password will be sent by email. - If sign_in_id is specified: Sign-in ID authentication user will be created.   When password is not specified, it will be auto-generated and returned in the response. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | E-mail | [optional] 
**sign_in_id** | **str** | Sign-in ID (alphanumeric and symbols -_ only, max 50 characters)  | [optional] 
**password** | **str** | Password. For email authentication, if not specified, a temporary password will be sent by email. For sign-in ID authentication, if not specified, password will be auto-generated and returned.  | [optional] 

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



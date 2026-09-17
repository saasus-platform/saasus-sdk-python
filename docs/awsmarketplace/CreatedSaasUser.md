# CreatedSaasUser


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**email** | **str** | E-mail. For sign-in ID authentication users, this field is an empty string.  | 
**sign_in_id** | **str** | Sign-in ID. For email authentication users, this field is an empty string.  | 
**attributes** | **Dict[str, object]** | Attribute information  | 
**last_login_at** | **int** | Last login date and time (unix timestamp). Null if the user has never logged in.  | [optional] 
**password** | **str** | Auto-generated password (only when sign_in_id authentication and password not specified)  | [optional] 

## Example

```python
from saasus_sdk_python.src.auth.models.created_saas_user import CreatedSaasUser

# TODO update the JSON string below
json = "{}"
# create an instance of CreatedSaasUser from a JSON string
created_saas_user_instance = CreatedSaasUser.from_json(json)
# print the JSON string representation of the object
print CreatedSaasUser.to_json()

# convert the object into a dict
created_saas_user_dict = created_saas_user_instance.to_dict()
# create an instance of CreatedSaasUser from a dict
created_saas_user_form_dict = created_saas_user.from_dict(created_saas_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



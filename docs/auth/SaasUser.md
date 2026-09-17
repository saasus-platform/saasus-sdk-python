# SaasUser


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**email** | **str** | E-mail. For sign-in ID authentication users, this field is an empty string.  | 
**sign_in_id** | **str** | Sign-in ID. For email authentication users, this field is an empty string.  | 
**attributes** | **Dict[str, object]** | Attribute information  | 
**last_login_at** | **int** | Last login date and time (unix timestamp). Null if the user has never logged in.  | [optional] 

## Example

```python
from saasus_sdk_python.src.auth.models.saas_user import SaasUser

# TODO update the JSON string below
json = "{}"
# create an instance of SaasUser from a JSON string
saas_user_instance = SaasUser.from_json(json)
# print the JSON string representation of the object
print SaasUser.to_json()

# convert the object into a dict
saas_user_dict = saas_user_instance.to_dict()
# create an instance of SaasUser from a dict
saas_user_form_dict = saas_user.from_dict(saas_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



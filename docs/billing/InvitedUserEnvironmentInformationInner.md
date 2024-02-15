# InvitedUserEnvironmentInformationInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**role_names** | **List[str]** | 役割名(role name) | 

## Example

```python
from saasus_sdk_python.src.auth.models.invited_user_environment_information_inner import InvitedUserEnvironmentInformationInner

# TODO update the JSON string below
json = "{}"
# create an instance of InvitedUserEnvironmentInformationInner from a JSON string
invited_user_environment_information_inner_instance = InvitedUserEnvironmentInformationInner.from_json(json)
# print the JSON string representation of the object
print InvitedUserEnvironmentInformationInner.to_json()

# convert the object into a dict
invited_user_environment_information_inner_dict = invited_user_environment_information_inner_instance.to_dict()
# create an instance of InvitedUserEnvironmentInformationInner from a dict
invited_user_environment_information_inner_form_dict = invited_user_environment_information_inner.from_dict(invited_user_environment_information_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



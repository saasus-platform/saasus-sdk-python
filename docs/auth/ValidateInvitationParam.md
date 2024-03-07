# ValidateInvitationParam

Access token is required for existing users, and email and password is required for new users. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | Access token of the invited user | [optional] 
**email** | **str** | Email address of the invited user | [optional] 
**password** | **str** | Password of the invited user | [optional] 

## Example

```python
from saasus_sdk_python.src.auth.models.validate_invitation_param import ValidateInvitationParam

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateInvitationParam from a JSON string
validate_invitation_param_instance = ValidateInvitationParam.from_json(json)
# print the JSON string representation of the object
print ValidateInvitationParam.to_json()

# convert the object into a dict
validate_invitation_param_dict = validate_invitation_param_instance.to_dict()
# create an instance of ValidateInvitationParam from a dict
validate_invitation_param_form_dict = validate_invitation_param.from_dict(validate_invitation_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



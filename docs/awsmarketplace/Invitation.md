# Invitation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**email** | **str** | 招待されたユーザーのメールアドレス(email address of the invited user) | 
**invitation_url** | **str** | 招待URL(invitation URL) | 
**envs** | [**List[UserAvailableEnv]**](UserAvailableEnv.md) |  | 
**expired_at** | **int** | 招待の有効期限(expiration date of the invitation) | 
**status** | [**InvitationStatus**](InvitationStatus.md) |  | 

## Example

```python
from saasus_sdk_python.src.auth.models.invitation import Invitation

# TODO update the JSON string below
json = "{}"
# create an instance of Invitation from a JSON string
invitation_instance = Invitation.from_json(json)
# print the JSON string representation of the object
print Invitation.to_json()

# convert the object into a dict
invitation_dict = invitation_instance.to_dict()
# create an instance of Invitation from a dict
invitation_form_dict = invitation.from_dict(invitation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



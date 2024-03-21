# InvitationValidity

Invitation validity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_valid** | **bool** | Whether the validation is valid or not | 

## Example

```python
from saasus_sdk_python.src.auth.models.invitation_validity import InvitationValidity

# TODO update the JSON string below
json = "{}"
# create an instance of InvitationValidity from a JSON string
invitation_validity_instance = InvitationValidity.from_json(json)
# print the JSON string representation of the object
print InvitationValidity.to_json()

# convert the object into a dict
invitation_validity_dict = invitation_validity_instance.to_dict()
# create an instance of InvitationValidity from a dict
invitation_validity_form_dict = invitation_validity.from_dict(invitation_validity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



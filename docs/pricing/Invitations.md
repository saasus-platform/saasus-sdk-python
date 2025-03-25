# Invitations


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invitations** | [**List[Invitation]**](Invitation.md) | Invitation list | 

## Example

```python
from saasus_sdk_python.src.auth.models.invitations import Invitations

# TODO update the JSON string below
json = "{}"
# create an instance of Invitations from a JSON string
invitations_instance = Invitations.from_json(json)
# print the JSON string representation of the object
print Invitations.to_json()

# convert the object into a dict
invitations_dict = invitations_instance.to_dict()
# create an instance of Invitations from a dict
invitations_form_dict = invitations.from_dict(invitations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



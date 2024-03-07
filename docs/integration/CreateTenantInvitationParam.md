# CreateTenantInvitationParam


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Email address of the user to be invited | 
**access_token** | **str** | Access token of the user who creates an invitation | 
**envs** | [**List[InvitedUserEnvironmentInformationInner]**](InvitedUserEnvironmentInformationInner.md) |  | 

## Example

```python
from saasus_sdk_python.src.auth.models.create_tenant_invitation_param import CreateTenantInvitationParam

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTenantInvitationParam from a JSON string
create_tenant_invitation_param_instance = CreateTenantInvitationParam.from_json(json)
# print the JSON string representation of the object
print CreateTenantInvitationParam.to_json()

# convert the object into a dict
create_tenant_invitation_param_dict = create_tenant_invitation_param_instance.to_dict()
# create an instance of CreateTenantInvitationParam from a dict
create_tenant_invitation_param_form_dict = create_tenant_invitation_param.from_dict(create_tenant_invitation_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



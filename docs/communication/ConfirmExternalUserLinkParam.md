# ConfirmExternalUserLinkParam


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** |  | 
**code** | **str** |  | 

## Example

```python
from saasus_sdk_python.src.auth.models.confirm_external_user_link_param import ConfirmExternalUserLinkParam

# TODO update the JSON string below
json = "{}"
# create an instance of ConfirmExternalUserLinkParam from a JSON string
confirm_external_user_link_param_instance = ConfirmExternalUserLinkParam.from_json(json)
# print the JSON string representation of the object
print ConfirmExternalUserLinkParam.to_json()

# convert the object into a dict
confirm_external_user_link_param_dict = confirm_external_user_link_param_instance.to_dict()
# create an instance of ConfirmExternalUserLinkParam from a dict
confirm_external_user_link_param_form_dict = confirm_external_user_link_param.from_dict(confirm_external_user_link_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



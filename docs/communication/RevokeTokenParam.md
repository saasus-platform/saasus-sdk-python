# RevokeTokenParam


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**refresh_token** | **str** | Refresh token to revoke | 

## Example

```python
from saasus_sdk_python.src.auth.models.revoke_token_param import RevokeTokenParam

# TODO update the JSON string below
json = "{}"
# create an instance of RevokeTokenParam from a JSON string
revoke_token_param_instance = RevokeTokenParam.from_json(json)
# print the JSON string representation of the object
print RevokeTokenParam.to_json()

# convert the object into a dict
revoke_token_param_dict = revoke_token_param_instance.to_dict()
# create an instance of RevokeTokenParam from a dict
revoke_token_param_form_dict = revoke_token_param.from_dict(revoke_token_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



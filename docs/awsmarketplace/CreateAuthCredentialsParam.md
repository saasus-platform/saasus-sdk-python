# CreateAuthCredentialsParam


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_token** | **str** | ID token | 
**access_token** | **str** | Access token | 
**refresh_token** | **str** | Refresh token | [optional] 
**code_challenge** | **str** | PKCE code challenge derived from the code verifier. It must be specified together with code_challenge_method. | [optional] 
**code_challenge_method** | **str** | Method used to derive the PKCE code challenge. It must be specified together with code_challenge. | [optional] 

## Example

```python
from saasus_sdk_python.src.auth.models.create_auth_credentials_param import CreateAuthCredentialsParam

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAuthCredentialsParam from a JSON string
create_auth_credentials_param_instance = CreateAuthCredentialsParam.from_json(json)
# print the JSON string representation of the object
print CreateAuthCredentialsParam.to_json()

# convert the object into a dict
create_auth_credentials_param_dict = create_auth_credentials_param_instance.to_dict()
# create an instance of CreateAuthCredentialsParam from a dict
create_auth_credentials_param_form_dict = create_auth_credentials_param.from_dict(create_auth_credentials_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



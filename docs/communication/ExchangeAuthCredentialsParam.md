# ExchangeAuthCredentialsParam


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_flow** | **str** | Authentication flow used for the exchange | 
**code** | **str** |  | [optional] 
**code_verifier** | **str** | PKCE code verifier associated with the temporary code | [optional] 

## Example

```python
from saasus_sdk_python.src.auth.models.exchange_auth_credentials_param import ExchangeAuthCredentialsParam

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangeAuthCredentialsParam from a JSON string
exchange_auth_credentials_param_instance = ExchangeAuthCredentialsParam.from_json(json)
# print the JSON string representation of the object
print ExchangeAuthCredentialsParam.to_json()

# convert the object into a dict
exchange_auth_credentials_param_dict = exchange_auth_credentials_param_instance.to_dict()
# create an instance of ExchangeAuthCredentialsParam from a dict
exchange_auth_credentials_param_form_dict = exchange_auth_credentials_param.from_dict(exchange_auth_credentials_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



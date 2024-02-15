# IdentityProviderConfiguration

外部IDプロバイダを利用したサインインの設定をするために必要な情報です。(This information is required to set up sign-in using an external identity provider.) 変更はできません。(It cannot be changed.) 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | ドメイン(domain) | 
**redirect_url** | **str** | リダイレクトURL(redirect URL) | 
**entity_id** | **str** | 識別子(entity ID) | 
**reply_url** | **str** | 応答URL(reply URL) | 

## Example

```python
from saasus_sdk_python.src.auth.models.identity_provider_configuration import IdentityProviderConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityProviderConfiguration from a JSON string
identity_provider_configuration_instance = IdentityProviderConfiguration.from_json(json)
# print the JSON string representation of the object
print IdentityProviderConfiguration.to_json()

# convert the object into a dict
identity_provider_configuration_dict = identity_provider_configuration_instance.to_dict()
# create an instance of IdentityProviderConfiguration from a dict
identity_provider_configuration_form_dict = identity_provider_configuration.from_dict(identity_provider_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



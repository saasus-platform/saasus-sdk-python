# UpdateTenantIdentityProviderParam

identity_provider_propsがnullの場合は、provider_typeで指定された外部IDプロバイダのサインイン情報を無効化します。  If identity_provider_props is null, the sign-in information for the external identity provider specified in provider_type is disabled. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_type** | [**ProviderType**](ProviderType.md) |  | 
**identity_provider_props** | [**TenantIdentityProviderProps**](TenantIdentityProviderProps.md) |  | [optional] 

## Example

```python
from saasus_sdk_python.src.auth.models.update_tenant_identity_provider_param import UpdateTenantIdentityProviderParam

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTenantIdentityProviderParam from a JSON string
update_tenant_identity_provider_param_instance = UpdateTenantIdentityProviderParam.from_json(json)
# print the JSON string representation of the object
print UpdateTenantIdentityProviderParam.to_json()

# convert the object into a dict
update_tenant_identity_provider_param_dict = update_tenant_identity_provider_param_instance.to_dict()
# create an instance of UpdateTenantIdentityProviderParam from a dict
update_tenant_identity_provider_param_form_dict = update_tenant_identity_provider_param.from_dict(update_tenant_identity_provider_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



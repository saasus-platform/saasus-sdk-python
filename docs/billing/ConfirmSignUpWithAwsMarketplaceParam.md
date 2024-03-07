# ConfirmSignUpWithAwsMarketplaceParam


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_name** | **str** | Tenant name | [optional] 
**access_token** | **str** | Access token | 
**registration_token** | **str** | Registration Token | 

## Example

```python
from saasus_sdk_python.src.auth.models.confirm_sign_up_with_aws_marketplace_param import ConfirmSignUpWithAwsMarketplaceParam

# TODO update the JSON string below
json = "{}"
# create an instance of ConfirmSignUpWithAwsMarketplaceParam from a JSON string
confirm_sign_up_with_aws_marketplace_param_instance = ConfirmSignUpWithAwsMarketplaceParam.from_json(json)
# print the JSON string representation of the object
print ConfirmSignUpWithAwsMarketplaceParam.to_json()

# convert the object into a dict
confirm_sign_up_with_aws_marketplace_param_dict = confirm_sign_up_with_aws_marketplace_param_instance.to_dict()
# create an instance of ConfirmSignUpWithAwsMarketplaceParam from a dict
confirm_sign_up_with_aws_marketplace_param_form_dict = confirm_sign_up_with_aws_marketplace_param.from_dict(confirm_sign_up_with_aws_marketplace_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



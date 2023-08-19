# SignUpWithAwsMarketplaceParam


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | メールアドレス(Email Address) | 
**registration_token** | **str** | Registration Token | 

## Example

```python
from saasus_sdk_python.models.sign_up_with_aws_marketplace_param import SignUpWithAwsMarketplaceParam

# TODO update the JSON string below
json = "{}"
# create an instance of SignUpWithAwsMarketplaceParam from a JSON string
sign_up_with_aws_marketplace_param_instance = SignUpWithAwsMarketplaceParam.from_json(json)
# print the JSON string representation of the object
print SignUpWithAwsMarketplaceParam.to_json()

# convert the object into a dict
sign_up_with_aws_marketplace_param_dict = sign_up_with_aws_marketplace_param_instance.to_dict()
# create an instance of SignUpWithAwsMarketplaceParam from a dict
sign_up_with_aws_marketplace_param_form_dict = sign_up_with_aws_marketplace_param.from_dict(sign_up_with_aws_marketplace_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



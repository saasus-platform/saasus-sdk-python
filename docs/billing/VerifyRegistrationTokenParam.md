# VerifyRegistrationTokenParam


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**registration_token** | **str** |  | 

## Example

```python
from saasus_sdk_python.src.awsmarketplace.models.verify_registration_token_param import VerifyRegistrationTokenParam

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyRegistrationTokenParam from a JSON string
verify_registration_token_param_instance = VerifyRegistrationTokenParam.from_json(json)
# print the JSON string representation of the object
print VerifyRegistrationTokenParam.to_json()

# convert the object into a dict
verify_registration_token_param_dict = verify_registration_token_param_instance.to_dict()
# create an instance of VerifyRegistrationTokenParam from a dict
verify_registration_token_param_form_dict = verify_registration_token_param.from_dict(verify_registration_token_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



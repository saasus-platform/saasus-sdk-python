# AccountVerification

Account authentication settings ※ This function is not yet provided, so it cannot be changed or saved. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verification_method** | **str** | code: verification code link: verification link ※ This function is not yet provided, so it cannot be changed or saved.  | 
**sending_to** | **str** | email: e-mail sms: SMS smsOrEmail: email if SMS is not possible  | 

## Example

```python
from saasus_sdk_python.src.auth.models.account_verification import AccountVerification

# TODO update the JSON string below
json = "{}"
# create an instance of AccountVerification from a JSON string
account_verification_instance = AccountVerification.from_json(json)
# print the JSON string representation of the object
print AccountVerification.to_json()

# convert the object into a dict
account_verification_dict = account_verification_instance.to_dict()
# create an instance of AccountVerification from a dict
account_verification_form_dict = account_verification.from_dict(account_verification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



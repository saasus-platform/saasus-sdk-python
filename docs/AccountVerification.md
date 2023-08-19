# AccountVerification

アカウント認証設定(account authentication settings) ※ 未提供の機能のため、変更・保存はできません(This function is not yet provided, so it cannot be changed or saved.) 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verification_method** | **str** | code: 検証コード(verification code) link: 検証リンク(verification link) ※ 未提供の機能のため、変更・保存はできません(This function is not yet provided, so it cannot be changed or saved.)  | 
**sending_to** | **str** | email: Eメール(e-mail) sms: SMS smsOrEmail: SMS不可の場合にEメール(email if SMS is not possible)  | 

## Example

```python
from saasus_sdk_python.models.account_verification import AccountVerification

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



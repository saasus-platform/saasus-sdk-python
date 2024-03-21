# PasswordPolicy

Password Policy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**minimum_length** | **int** | Minimum number of characters | 
**is_require_lowercase** | **bool** | Contains one or more lowercase characters | 
**is_require_numbers** | **bool** | Contains one or more numeric characters | 
**is_require_symbols** | **bool** | Contains one or more special characters | 
**is_require_uppercase** | **bool** | Contains one or more uppercase letters | 
**temporary_password_validity_days** | **int** | Temporary password expiration date | 

## Example

```python
from saasus_sdk_python.src.auth.models.password_policy import PasswordPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordPolicy from a JSON string
password_policy_instance = PasswordPolicy.from_json(json)
# print the JSON string representation of the object
print PasswordPolicy.to_json()

# convert the object into a dict
password_policy_dict = password_policy_instance.to_dict()
# create an instance of PasswordPolicy from a dict
password_policy_form_dict = password_policy.from_dict(password_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



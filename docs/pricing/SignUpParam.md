# SignUpParam


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | メールアドレス(Email Address) | 

## Example

```python
from saasus_sdk_python.src.auth.models.sign_up_param import SignUpParam

# TODO update the JSON string below
json = "{}"
# create an instance of SignUpParam from a JSON string
sign_up_param_instance = SignUpParam.from_json(json)
# print the JSON string representation of the object
print SignUpParam.to_json()

# convert the object into a dict
sign_up_param_dict = sign_up_param_instance.to_dict()
# create an instance of SignUpParam from a dict
sign_up_param_form_dict = sign_up_param.from_dict(sign_up_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



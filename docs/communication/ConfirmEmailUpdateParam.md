# ConfirmEmailUpdateParam


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**access_token** | **str** |  | 

## Example

```python
from saasus_sdk_python.src.auth.models.confirm_email_update_param import ConfirmEmailUpdateParam

# TODO update the JSON string below
json = "{}"
# create an instance of ConfirmEmailUpdateParam from a JSON string
confirm_email_update_param_instance = ConfirmEmailUpdateParam.from_json(json)
# print the JSON string representation of the object
print ConfirmEmailUpdateParam.to_json()

# convert the object into a dict
confirm_email_update_param_dict = confirm_email_update_param_instance.to_dict()
# create an instance of ConfirmEmailUpdateParam from a dict
confirm_email_update_param_form_dict = confirm_email_update_param.from_dict(confirm_email_update_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# UpdateSoftwareTokenParam


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | アクセストークン(access token) | 
**verification_code** | **str** | 検証コード(verification code) | 

## Example

```python
from saasus_sdk_python.models.update_software_token_param import UpdateSoftwareTokenParam

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSoftwareTokenParam from a JSON string
update_software_token_param_instance = UpdateSoftwareTokenParam.from_json(json)
# print the JSON string representation of the object
print UpdateSoftwareTokenParam.to_json()

# convert the object into a dict
update_software_token_param_dict = update_software_token_param_instance.to_dict()
# create an instance of UpdateSoftwareTokenParam from a dict
update_software_token_param_form_dict = update_software_token_param.from_dict(update_software_token_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



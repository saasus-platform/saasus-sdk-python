# UpdateBasicInfoParam


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_name** | **str** | Domain Name | 
**from_email_address** | **str** | Sender email of authentication email | 
**reply_email_address** | **str** | Reply-from email address of authentication email | [optional] 

## Example

```python
from saasus_sdk_python.src.auth.models.update_basic_info_param import UpdateBasicInfoParam

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateBasicInfoParam from a JSON string
update_basic_info_param_instance = UpdateBasicInfoParam.from_json(json)
# print the JSON string representation of the object
print UpdateBasicInfoParam.to_json()

# convert the object into a dict
update_basic_info_param_dict = update_basic_info_param_instance.to_dict()
# create an instance of UpdateBasicInfoParam from a dict
update_basic_info_param_form_dict = update_basic_info_param.from_dict(update_basic_info_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



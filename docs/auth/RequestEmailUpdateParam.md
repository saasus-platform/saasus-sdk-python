# RequestEmailUpdateParam


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Email Address | 
**access_token** | **str** |  | 

## Example

```python
from saasus_sdk_python.src.auth.models.request_email_update_param import RequestEmailUpdateParam

# TODO update the JSON string below
json = "{}"
# create an instance of RequestEmailUpdateParam from a JSON string
request_email_update_param_instance = RequestEmailUpdateParam.from_json(json)
# print the JSON string representation of the object
print RequestEmailUpdateParam.to_json()

# convert the object into a dict
request_email_update_param_dict = request_email_update_param_instance.to_dict()
# create an instance of RequestEmailUpdateParam from a dict
request_email_update_param_form_dict = request_email_update_param.from_dict(request_email_update_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



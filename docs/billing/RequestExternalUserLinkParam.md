# RequestExternalUserLinkParam


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** |  | 

## Example

```python
from saasus_sdk_python.src.auth.models.request_external_user_link_param import RequestExternalUserLinkParam

# TODO update the JSON string below
json = "{}"
# create an instance of RequestExternalUserLinkParam from a JSON string
request_external_user_link_param_instance = RequestExternalUserLinkParam.from_json(json)
# print the JSON string representation of the object
print RequestExternalUserLinkParam.to_json()

# convert the object into a dict
request_external_user_link_param_dict = request_external_user_link_param_instance.to_dict()
# create an instance of RequestExternalUserLinkParam from a dict
request_external_user_link_param_form_dict = request_external_user_link_param.from_dict(request_external_user_link_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



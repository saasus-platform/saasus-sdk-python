# SelfRegist

self sign-up permission

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** |  | 

## Example

```python
from saasus_sdk_python.src.auth.models.self_regist import SelfRegist

# TODO update the JSON string below
json = "{}"
# create an instance of SelfRegist from a JSON string
self_regist_instance = SelfRegist.from_json(json)
# print the JSON string representation of the object
print SelfRegist.to_json()

# convert the object into a dict
self_regist_dict = self_regist_instance.to_dict()
# create an instance of SelfRegist from a dict
self_regist_form_dict = self_regist.from_dict(self_regist_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



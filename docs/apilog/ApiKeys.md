# ApiKeys


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_keys** | **List[str]** | APIキー(API Key) | 

## Example

```python
from saasus_sdk_python.src.auth.models.api_keys import ApiKeys

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKeys from a JSON string
api_keys_instance = ApiKeys.from_json(json)
# print the JSON string representation of the object
print ApiKeys.to_json()

# convert the object into a dict
api_keys_dict = api_keys_instance.to_dict()
# create an instance of ApiKeys from a dict
api_keys_form_dict = api_keys.from_dict(api_keys_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



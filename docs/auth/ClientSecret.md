# ClientSecret


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_secret** | **str** | Client Secret | 

## Example

```python
from saasus_sdk_python.src.auth.models.client_secret import ClientSecret

# TODO update the JSON string below
json = "{}"
# create an instance of ClientSecret from a JSON string
client_secret_instance = ClientSecret.from_json(json)
# print the JSON string representation of the object
print ClientSecret.to_json()

# convert the object into a dict
client_secret_dict = client_secret_instance.to_dict()
# create an instance of ClientSecret from a dict
client_secret_form_dict = client_secret.from_dict(client_secret_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



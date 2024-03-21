# CreateSecretCodeParam


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | access token | 

## Example

```python
from saasus_sdk_python.src.auth.models.create_secret_code_param import CreateSecretCodeParam

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSecretCodeParam from a JSON string
create_secret_code_param_instance = CreateSecretCodeParam.from_json(json)
# print the JSON string representation of the object
print CreateSecretCodeParam.to_json()

# convert the object into a dict
create_secret_code_param_dict = create_secret_code_param_instance.to_dict()
# create an instance of CreateSecretCodeParam from a dict
create_secret_code_param_form_dict = create_secret_code_param.from_dict(create_secret_code_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



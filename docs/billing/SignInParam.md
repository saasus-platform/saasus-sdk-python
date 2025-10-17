# SignInParam

Parameters required for user sign-in The required parameters vary depending on the sign_in_flow. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sign_in_flow** | **str** | The sign-in flow to use for authentication. Currently, only USER_SRP_AUTH is supported.  | 
**sign_in_parameters** | **Dict[str, str]** | The required parameters vary depending on the sign_in_flow. USER_SRP_AUTH:   USERNAME: email address   SRP_A: SRP A value  | [optional] 

## Example

```python
from saasus_sdk_python.src.auth.models.sign_in_param import SignInParam

# TODO update the JSON string below
json = "{}"
# create an instance of SignInParam from a JSON string
sign_in_param_instance = SignInParam.from_json(json)
# print the JSON string representation of the object
print SignInParam.to_json()

# convert the object into a dict
sign_in_param_dict = sign_in_param_instance.to_dict()
# create an instance of SignInParam from a dict
sign_in_param_form_dict = sign_in_param.from_dict(sign_in_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



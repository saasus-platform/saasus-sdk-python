# SignInResult

Result returned after a sign-in attempt 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**challenge_name** | [**ChallengeName**](ChallengeName.md) |  | [optional] 
**challenge_parameters** | **Dict[str, str]** | Parameters required to complete the challenge  | [optional] 
**session** | **str** | Session identifier for the challenge. This session should be passed to the next call to RespondToSignInChallenge if another challenge is required.  | [optional] 

## Example

```python
from saasus_sdk_python.src.auth.models.sign_in_result import SignInResult

# TODO update the JSON string below
json = "{}"
# create an instance of SignInResult from a JSON string
sign_in_result_instance = SignInResult.from_json(json)
# print the JSON string representation of the object
print SignInResult.to_json()

# convert the object into a dict
sign_in_result_dict = sign_in_result_instance.to_dict()
# create an instance of SignInResult from a dict
sign_in_result_form_dict = sign_in_result.from_dict(sign_in_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



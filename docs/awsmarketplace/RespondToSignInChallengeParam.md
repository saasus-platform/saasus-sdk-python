# RespondToSignInChallengeParam

Parameters required to respond to a sign-in challenge 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**challenge_name** | [**ChallengeName**](ChallengeName.md) |  | 
**challenge_responses** | **Dict[str, str]** | Responses to the challenge. The required responses vary depending on the challenge_name.  | [optional] 
**session** | **str** | Session identifier for the challenge.  | [optional] 

## Example

```python
from saasus_sdk_python.src.auth.models.respond_to_sign_in_challenge_param import RespondToSignInChallengeParam

# TODO update the JSON string below
json = "{}"
# create an instance of RespondToSignInChallengeParam from a JSON string
respond_to_sign_in_challenge_param_instance = RespondToSignInChallengeParam.from_json(json)
# print the JSON string representation of the object
print RespondToSignInChallengeParam.to_json()

# convert the object into a dict
respond_to_sign_in_challenge_param_dict = respond_to_sign_in_challenge_param_instance.to_dict()
# create an instance of RespondToSignInChallengeParam from a dict
respond_to_sign_in_challenge_param_form_dict = respond_to_sign_in_challenge_param.from_dict(respond_to_sign_in_challenge_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



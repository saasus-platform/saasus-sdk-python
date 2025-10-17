# RespondToSignInChallengeResult

Result returned after responding to a sign-in challenge 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials** | [**Credentials**](Credentials.md) |  | [optional] 
**challenge_name** | [**ChallengeName**](ChallengeName.md) |  | [optional] 
**challenge_parameters** | **Dict[str, str]** | Parameters required for the next challenge.  | [optional] 
**session** | **str** | Session identifier for the challenge. This session should be passed to the next call to RespondToSignInChallenge if another challenge is required.  | [optional] 

## Example

```python
from saasus_sdk_python.src.auth.models.respond_to_sign_in_challenge_result import RespondToSignInChallengeResult

# TODO update the JSON string below
json = "{}"
# create an instance of RespondToSignInChallengeResult from a JSON string
respond_to_sign_in_challenge_result_instance = RespondToSignInChallengeResult.from_json(json)
# print the JSON string representation of the object
print RespondToSignInChallengeResult.to_json()

# convert the object into a dict
respond_to_sign_in_challenge_result_dict = respond_to_sign_in_challenge_result_instance.to_dict()
# create an instance of RespondToSignInChallengeResult from a dict
respond_to_sign_in_challenge_result_form_dict = respond_to_sign_in_challenge_result.from_dict(respond_to_sign_in_challenge_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



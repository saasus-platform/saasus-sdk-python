# RefreshTokenValidity

Refresh token validity period.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **int** | Refresh token validity value. The duration must be between 60 minutes and 10 years.  | 
**unit** | [**RefreshTokenValidityUnit**](RefreshTokenValidityUnit.md) |  | 

## Example

```python
from saasus_sdk_python.src.auth.models.refresh_token_validity import RefreshTokenValidity

# TODO update the JSON string below
json = "{}"
# create an instance of RefreshTokenValidity from a JSON string
refresh_token_validity_instance = RefreshTokenValidity.from_json(json)
# print the JSON string representation of the object
print RefreshTokenValidity.to_json()

# convert the object into a dict
refresh_token_validity_dict = refresh_token_validity_instance.to_dict()
# create an instance of RefreshTokenValidity from a dict
refresh_token_validity_form_dict = refresh_token_validity.from_dict(refresh_token_validity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



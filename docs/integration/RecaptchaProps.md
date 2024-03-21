# RecaptchaProps

reCAPTCHA authentication settings ※ This function is not yet provided, so it cannot be changed or saved. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**site_key** | **str** | site key | 
**secret_key** | **str** | secret key | 

## Example

```python
from saasus_sdk_python.src.auth.models.recaptcha_props import RecaptchaProps

# TODO update the JSON string below
json = "{}"
# create an instance of RecaptchaProps from a JSON string
recaptcha_props_instance = RecaptchaProps.from_json(json)
# print the JSON string representation of the object
print RecaptchaProps.to_json()

# convert the object into a dict
recaptcha_props_dict = recaptcha_props_instance.to_dict()
# create an instance of RecaptchaProps from a dict
recaptcha_props_form_dict = recaptcha_props.from_dict(recaptcha_props_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# StripeInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_registered** | **bool** |  | 

## Example

```python
from saasus_sdk_python.src.billing.models.stripe_info import StripeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of StripeInfo from a JSON string
stripe_info_instance = StripeInfo.from_json(json)
# print the JSON string representation of the object
print StripeInfo.to_json()

# convert the object into a dict
stripe_info_dict = stripe_info_instance.to_dict()
# create an instance of StripeInfo from a dict
stripe_info_form_dict = stripe_info.from_dict(stripe_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



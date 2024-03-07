# UpdateStripeInfoParam


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secret_key** | **str** | secret key | 

## Example

```python
from saasus_sdk_python.src.billing.models.update_stripe_info_param import UpdateStripeInfoParam

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateStripeInfoParam from a JSON string
update_stripe_info_param_instance = UpdateStripeInfoParam.from_json(json)
# print the JSON string representation of the object
print UpdateStripeInfoParam.to_json()

# convert the object into a dict
update_stripe_info_param_dict = update_stripe_info_param_instance.to_dict()
# create an instance of UpdateStripeInfoParam from a dict
update_stripe_info_param_form_dict = update_stripe_info_param.from_dict(update_stripe_info_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



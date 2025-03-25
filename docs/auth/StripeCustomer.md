# StripeCustomer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | stripe Customer ID | 
**subscription_schedule_id** | **str** | stripe Subscription Schedule ID | 

## Example

```python
from saasus_sdk_python.src.auth.models.stripe_customer import StripeCustomer

# TODO update the JSON string below
json = "{}"
# create an instance of StripeCustomer from a JSON string
stripe_customer_instance = StripeCustomer.from_json(json)
# print the JSON string representation of the object
print StripeCustomer.to_json()

# convert the object into a dict
stripe_customer_dict = stripe_customer_instance.to_dict()
# create an instance of StripeCustomer from a dict
stripe_customer_form_dict = stripe_customer.from_dict(stripe_customer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



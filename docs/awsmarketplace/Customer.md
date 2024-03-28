# Customer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_identifier** | **str** |  | 
**customer_aws_account_id** | **str** |  | 
**tenant_id** | **str** |  | 

## Example

```python
from saasus_sdk_python.src.awsmarketplace.models.customer import Customer

# TODO update the JSON string below
json = "{}"
# create an instance of Customer from a JSON string
customer_instance = Customer.from_json(json)
# print the JSON string representation of the object
print Customer.to_json()

# convert the object into a dict
customer_dict = customer_instance.to_dict()
# create an instance of Customer from a dict
customer_form_dict = customer.from_dict(customer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



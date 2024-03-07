# Customers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customers** | [**List[Customer]**](Customer.md) |  | 

## Example

```python
from saasus_sdk_python.src.awsmarketplace.models.customers import Customers

# TODO update the JSON string below
json = "{}"
# create an instance of Customers from a JSON string
customers_instance = Customers.from_json(json)
# print the JSON string representation of the object
print Customers.to_json()

# convert the object into a dict
customers_dict = customers_instance.to_dict()
# create an instance of Customers from a dict
customers_form_dict = customers.from_dict(customers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



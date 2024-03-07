# CreateCustomerParam


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | 
**registration_token** | **str** |  | 

## Example

```python
from saasus_sdk_python.src.awsmarketplace.models.create_customer_param import CreateCustomerParam

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCustomerParam from a JSON string
create_customer_param_instance = CreateCustomerParam.from_json(json)
# print the JSON string representation of the object
print CreateCustomerParam.to_json()

# convert the object into a dict
create_customer_param_dict = create_customer_param_instance.to_dict()
# create an instance of CreateCustomerParam from a dict
create_customer_param_form_dict = create_customer_param.from_dict(create_customer_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# BillingAddress


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**street** | **str** | Street address, apartment or suite number. | 
**city** | **str** | City, district, suburb, town, or village. | 
**state** | **str** | State name or abbreviation. | 
**country** | **str** | Country of the address using ISO 3166-1 alpha-2 code. | 
**additional_address_info** | **str** | Additional information about the address, such as a building name, floor, or department name. | [optional] 
**postal_code** | **str** | ZIP or postal code. | 

## Example

```python
from saasus_sdk_python.src.auth.models.billing_address import BillingAddress

# TODO update the JSON string below
json = "{}"
# create an instance of BillingAddress from a JSON string
billing_address_instance = BillingAddress.from_json(json)
# print the JSON string representation of the object
print BillingAddress.to_json()

# convert the object into a dict
billing_address_dict = billing_address_instance.to_dict()
# create an instance of BillingAddress from a dict
billing_address_form_dict = billing_address.from_dict(billing_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



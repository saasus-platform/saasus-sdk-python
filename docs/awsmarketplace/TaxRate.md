# TaxRate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of tax rate | 
**display_name** | **str** | Display name | 
**percentage** | **float** | Percentage | 
**inclusive** | **bool** | Inclusive or not | 
**country** | **str** | Country code of ISO 3166-1 alpha-2 | 
**description** | **str** | Description | 
**id** | **str** | Universally Unique Identifier | 

## Example

```python
from saasus_sdk_python.src.pricing.models.tax_rate import TaxRate

# TODO update the JSON string below
json = "{}"
# create an instance of TaxRate from a JSON string
tax_rate_instance = TaxRate.from_json(json)
# print the JSON string representation of the object
print TaxRate.to_json()

# convert the object into a dict
tax_rate_dict = tax_rate_instance.to_dict()
# create an instance of TaxRate from a dict
tax_rate_form_dict = tax_rate.from_dict(tax_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



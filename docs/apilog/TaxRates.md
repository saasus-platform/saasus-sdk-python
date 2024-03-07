# TaxRates


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_rates** | [**List[TaxRate]**](TaxRate.md) |  | 

## Example

```python
from saasus_sdk_python.src.pricing.models.tax_rates import TaxRates

# TODO update the JSON string below
json = "{}"
# create an instance of TaxRates from a JSON string
tax_rates_instance = TaxRates.from_json(json)
# print the JSON string representation of the object
print TaxRates.to_json()

# convert the object into a dict
tax_rates_dict = tax_rates_instance.to_dict()
# create an instance of TaxRates from a dict
tax_rates_form_dict = tax_rates.from_dict(tax_rates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



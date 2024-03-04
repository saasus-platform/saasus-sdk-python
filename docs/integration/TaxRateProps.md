# TaxRateProps


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | 税率の名前 | 
**display_name** | **str** | 表示名 | 
**percentage** | **float** | 税率 | 
**inclusive** | **bool** | 内税かどうか | 
**country** | **str** | ISO 3166-1 alpha-2 の国コード | 
**description** | **str** | 説明 | 

## Example

```python
from saasus_sdk_python.src.pricing.models.tax_rate_props import TaxRateProps

# TODO update the JSON string below
json = "{}"
# create an instance of TaxRateProps from a JSON string
tax_rate_props_instance = TaxRateProps.from_json(json)
# print the JSON string representation of the object
print TaxRateProps.to_json()

# convert the object into a dict
tax_rate_props_dict = tax_rate_props_instance.to_dict()
# create an instance of TaxRateProps from a dict
tax_rate_props_form_dict = tax_rate_props.from_dict(tax_rate_props_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



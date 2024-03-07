# UpdateTaxRateParam


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | Display name | 
**description** | **str** | Description | 

## Example

```python
from saasus_sdk_python.src.pricing.models.update_tax_rate_param import UpdateTaxRateParam

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTaxRateParam from a JSON string
update_tax_rate_param_instance = UpdateTaxRateParam.from_json(json)
# print the JSON string representation of the object
print UpdateTaxRateParam.to_json()

# convert the object into a dict
update_tax_rate_param_dict = update_tax_rate_param_instance.to_dict()
# create an instance of UpdateTaxRateParam from a dict
update_tax_rate_param_form_dict = update_tax_rate_param.from_dict(update_tax_rate_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



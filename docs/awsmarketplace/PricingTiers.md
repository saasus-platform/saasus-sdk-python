# PricingTiers


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tiers** | [**List[PricingTier]**](PricingTier.md) |  | 

## Example

```python
from saasus_sdk_python.src.pricing.models.pricing_tiers import PricingTiers

# TODO update the JSON string below
json = "{}"
# create an instance of PricingTiers from a JSON string
pricing_tiers_instance = PricingTiers.from_json(json)
# print the JSON string representation of the object
print PricingTiers.to_json()

# convert the object into a dict
pricing_tiers_dict = pricing_tiers_instance.to_dict()
# create an instance of PricingTiers from a dict
pricing_tiers_form_dict = pricing_tiers.from_dict(pricing_tiers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



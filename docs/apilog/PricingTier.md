# PricingTier


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**up_to** | **int** | 上限(upper limit) | 
**unit_amount** | **int** | 単位金額(amount per unit) | 
**flat_amount** | **int** | 固定金額(fixed Amount) | 
**inf** | **bool** | inf | 

## Example

```python
from saasus_sdk_python.src.pricing.models.pricing_tier import PricingTier

# TODO update the JSON string below
json = "{}"
# create an instance of PricingTier from a JSON string
pricing_tier_instance = PricingTier.from_json(json)
# print the JSON string representation of the object
print PricingTier.to_json()

# convert the object into a dict
pricing_tier_dict = pricing_tier_instance.to_dict()
# create an instance of PricingTier from a dict
pricing_tier_form_dict = pricing_tier.from_dict(pricing_tier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



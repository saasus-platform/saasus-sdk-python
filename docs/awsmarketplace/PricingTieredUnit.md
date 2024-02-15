# PricingTieredUnit


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**upper_count** | **int** | 上限値(upper limit) | 
**metering_unit_name** | **str** |  | 
**aggregate_usage** | [**AggregateUsage**](AggregateUsage.md) |  | [optional] 
**name** | **str** | 名前(name) | 
**display_name** | **str** | 表示名(display name) | 
**description** | **str** | 説明(description) | 
**type** | [**UnitType**](UnitType.md) |  | 
**currency** | [**Currency**](Currency.md) |  | 
**tiers** | [**List[PricingTier]**](PricingTier.md) |  | 
**id** | **str** |  | 
**metering_unit_id** | **str** |  | 
**recurring_interval** | [**RecurringInterval**](RecurringInterval.md) |  | 
**used** | **bool** |  | 

## Example

```python
from saasus_sdk_python.src.pricing.models.pricing_tiered_unit import PricingTieredUnit

# TODO update the JSON string below
json = "{}"
# create an instance of PricingTieredUnit from a JSON string
pricing_tiered_unit_instance = PricingTieredUnit.from_json(json)
# print the JSON string representation of the object
print PricingTieredUnit.to_json()

# convert the object into a dict
pricing_tiered_unit_dict = pricing_tiered_unit_instance.to_dict()
# create an instance of PricingTieredUnit from a dict
pricing_tiered_unit_form_dict = pricing_tiered_unit.from_dict(pricing_tiered_unit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


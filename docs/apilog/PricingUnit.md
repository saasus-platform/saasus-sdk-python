# PricingUnit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**UnitType**](UnitType.md) |  | 
**id** | **str** | ユニバーサル一意識別子 | 
**metering_unit_id** | **str** | ユニバーサル一意識別子 | 
**recurring_interval** | [**RecurringInterval**](RecurringInterval.md) |  | 
**used** | **bool** |  | 
**upper_count** | **int** | 上限値 | 
**metering_unit_name** | **str** | 計測ユニット名 | 
**aggregate_usage** | [**AggregateUsage**](AggregateUsage.md) |  | [optional] 
**name** | **str** | 名前 | 
**display_name** | **str** | 表示名 | 
**description** | **str** | 説明 | 
**currency** | [**Currency**](Currency.md) |  | 
**tiers** | [**List[PricingTier]**](PricingTier.md) |  | 
**unit_amount** | **int** | 料金 | 

## Example

```python
from saasus_sdk_python.src.pricing.models.pricing_unit import PricingUnit

# TODO update the JSON string below
json = "{}"
# create an instance of PricingUnit from a JSON string
pricing_unit_instance = PricingUnit.from_json(json)
# print the JSON string representation of the object
print PricingUnit.to_json()

# convert the object into a dict
pricing_unit_dict = pricing_unit_instance.to_dict()
# create an instance of PricingUnit from a dict
pricing_unit_form_dict = pricing_unit.from_dict(pricing_unit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



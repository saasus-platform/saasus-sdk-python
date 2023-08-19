# PlanHistory


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_id** | **str** |  | 
**plan_applied_at** | **int** | 登録日時 | 
**tax_rate_id** | **str** |  | [optional] 

## Example

```python
from saasus_sdk_python.models.plan_history import PlanHistory

# TODO update the JSON string below
json = "{}"
# create an instance of PlanHistory from a JSON string
plan_history_instance = PlanHistory.from_json(json)
# print the JSON string representation of the object
print PlanHistory.to_json()

# convert the object into a dict
plan_history_dict = plan_history_instance.to_dict()
# create an instance of PlanHistory from a dict
plan_history_form_dict = plan_history.from_dict(plan_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



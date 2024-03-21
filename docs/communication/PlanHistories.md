# PlanHistories


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_histories** | [**List[PlanHistory]**](PlanHistory.md) | Plan History | 

## Example

```python
from saasus_sdk_python.src.auth.models.plan_histories import PlanHistories

# TODO update the JSON string below
json = "{}"
# create an instance of PlanHistories from a JSON string
plan_histories_instance = PlanHistories.from_json(json)
# print the JSON string representation of the object
print PlanHistories.to_json()

# convert the object into a dict
plan_histories_dict = plan_histories_instance.to_dict()
# create an instance of PlanHistories from a dict
plan_histories_form_dict = plan_histories.from_dict(plan_histories_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# SavePlanParam


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_id** | **str** |  | 
**plan_name** | **str** |  | 

## Example

```python
from saasus_sdk_python.src.awsmarketplace.models.save_plan_param import SavePlanParam

# TODO update the JSON string below
json = "{}"
# create an instance of SavePlanParam from a JSON string
save_plan_param_instance = SavePlanParam.from_json(json)
# print the JSON string representation of the object
print SavePlanParam.to_json()

# convert the object into a dict
save_plan_param_dict = save_plan_param_instance.to_dict()
# create an instance of SavePlanParam from a dict
save_plan_param_form_dict = save_plan_param.from_dict(save_plan_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# SavePricingMenuParam


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Menu name | 
**display_name** | **str** | Menu display name | 
**description** | **str** | Menu description | 
**unit_ids** | **List[str]** | Unit IDs to add | 

## Example

```python
from saasus_sdk_python.src.pricing.models.save_pricing_menu_param import SavePricingMenuParam

# TODO update the JSON string below
json = "{}"
# create an instance of SavePricingMenuParam from a JSON string
save_pricing_menu_param_instance = SavePricingMenuParam.from_json(json)
# print the JSON string representation of the object
print SavePricingMenuParam.to_json()

# convert the object into a dict
save_pricing_menu_param_dict = save_pricing_menu_param_instance.to_dict()
# create an instance of SavePricingMenuParam from a dict
save_pricing_menu_param_form_dict = save_pricing_menu_param.from_dict(save_pricing_menu_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



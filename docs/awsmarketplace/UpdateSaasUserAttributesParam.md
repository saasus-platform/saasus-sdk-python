# UpdateSaasUserAttributesParam


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | **Dict[str, object]** | Attribute information  | 

## Example

```python
from saasus_sdk_python.src.auth.models.update_saas_user_attributes_param import UpdateSaasUserAttributesParam

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSaasUserAttributesParam from a JSON string
update_saas_user_attributes_param_instance = UpdateSaasUserAttributesParam.from_json(json)
# print the JSON string representation of the object
print UpdateSaasUserAttributesParam.to_json()

# convert the object into a dict
update_saas_user_attributes_param_dict = update_saas_user_attributes_param_instance.to_dict()
# create an instance of UpdateSaasUserAttributesParam from a dict
update_saas_user_attributes_param_form_dict = update_saas_user_attributes_param.from_dict(update_saas_user_attributes_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



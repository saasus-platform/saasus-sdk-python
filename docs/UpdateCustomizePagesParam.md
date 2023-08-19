# UpdateCustomizePagesParam


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sign_up_page** | [**CustomizePageProps**](CustomizePageProps.md) |  | [optional] 
**sign_in_page** | [**CustomizePageProps**](CustomizePageProps.md) |  | [optional] 
**password_reset_page** | [**CustomizePageProps**](CustomizePageProps.md) |  | [optional] 

## Example

```python
from saasus_sdk_python.models.update_customize_pages_param import UpdateCustomizePagesParam

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCustomizePagesParam from a JSON string
update_customize_pages_param_instance = UpdateCustomizePagesParam.from_json(json)
# print the JSON string representation of the object
print UpdateCustomizePagesParam.to_json()

# convert the object into a dict
update_customize_pages_param_dict = update_customize_pages_param_instance.to_dict()
# create an instance of UpdateCustomizePagesParam from a dict
update_customize_pages_param_form_dict = update_customize_pages_param.from_dict(update_customize_pages_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



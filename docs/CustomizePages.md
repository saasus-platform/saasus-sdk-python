# CustomizePages


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sign_up_page** | [**CustomizePageProps**](CustomizePageProps.md) |  | 
**sign_in_page** | [**CustomizePageProps**](CustomizePageProps.md) |  | 
**password_reset_page** | [**CustomizePageProps**](CustomizePageProps.md) |  | 

## Example

```python
from saasus_sdk_python.models.customize_pages import CustomizePages

# TODO update the JSON string below
json = "{}"
# create an instance of CustomizePages from a JSON string
customize_pages_instance = CustomizePages.from_json(json)
# print the JSON string representation of the object
print CustomizePages.to_json()

# convert the object into a dict
customize_pages_dict = customize_pages_instance.to_dict()
# create an instance of CustomizePages from a dict
customize_pages_form_dict = customize_pages.from_dict(customize_pages_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



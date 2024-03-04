# CustomizePageSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | service name | 
**terms_of_service_url** | **str** | terms of service URL | 
**privacy_policy_url** | **str** | privacy policy URL | 
**google_tag_manager_container_id** | **str** | Google Tag Manager container ID | 
**icon** | **str** | service icon | 
**favicon** | **str** | favicon | 

## Example

```python
from saasus_sdk_python.src.auth.models.customize_page_settings import CustomizePageSettings

# TODO update the JSON string below
json = "{}"
# create an instance of CustomizePageSettings from a JSON string
customize_page_settings_instance = CustomizePageSettings.from_json(json)
# print the JSON string representation of the object
print CustomizePageSettings.to_json()

# convert the object into a dict
customize_page_settings_dict = customize_page_settings_instance.to_dict()
# create an instance of CustomizePageSettings from a dict
customize_page_settings_form_dict = customize_page_settings.from_dict(customize_page_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



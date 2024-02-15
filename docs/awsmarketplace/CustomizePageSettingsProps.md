# CustomizePageSettingsProps


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | サービス名(service name) | 
**terms_of_service_url** | **str** | 利用規約URL(terms of service URL) | 
**privacy_policy_url** | **str** | プライバシーポリシーURL(privacy policy URL) | 
**google_tag_manager_container_id** | **str** | Google Tag Manager コンテナ ID(Google Tag Manager container ID) | 

## Example

```python
from saasus_sdk_python.src.auth.models.customize_page_settings_props import CustomizePageSettingsProps

# TODO update the JSON string below
json = "{}"
# create an instance of CustomizePageSettingsProps from a JSON string
customize_page_settings_props_instance = CustomizePageSettingsProps.from_json(json)
# print the JSON string representation of the object
print CustomizePageSettingsProps.to_json()

# convert the object into a dict
customize_page_settings_props_dict = customize_page_settings_props_instance.to_dict()
# create an instance of CustomizePageSettingsProps from a dict
customize_page_settings_props_form_dict = customize_page_settings_props.from_dict(customize_page_settings_props_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



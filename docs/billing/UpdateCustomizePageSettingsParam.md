# UpdateCustomizePageSettingsParam


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | サービス名(service name) | 
**terms_of_service_url** | **str** | 利用規約URL(terms of service URL) | 
**privacy_policy_url** | **str** | プライバシーポリシーURL(privacy policy URL) | 
**google_tag_manager_container_id** | **str** | Google Tag Manager コンテナ ID(Google Tag Manager container ID) | 
**icon** | **str** | サービスアイコン(service icon) | 
**favicon** | **str** | ファビコン(favicon) | 

## Example

```python
from saasus_sdk_python.src.auth.models.update_customize_page_settings_param import UpdateCustomizePageSettingsParam

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCustomizePageSettingsParam from a JSON string
update_customize_page_settings_param_instance = UpdateCustomizePageSettingsParam.from_json(json)
# print the JSON string representation of the object
print UpdateCustomizePageSettingsParam.to_json()

# convert the object into a dict
update_customize_page_settings_param_dict = update_customize_page_settings_param_instance.to_dict()
# create an instance of UpdateCustomizePageSettingsParam from a dict
update_customize_page_settings_param_form_dict = update_customize_page_settings_param.from_dict(update_customize_page_settings_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



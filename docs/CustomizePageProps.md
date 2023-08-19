# CustomizePageProps


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**html_contents** | **str** | 画面のHTMLを編集できます ※ 未提供の機能のため、変更・保存はできません  Edit page HTML ※ This function is not yet provided, so it cannot be changed or saved.  | 
**is_terms_of_service** | **bool** | 利用規約の同意チェックボックスを表示するが設定されているか(display the terms of use agreement check box) | 
**is_privacy_policy** | **bool** | プライバシーポリシーチェックボックスを表示するが設定されているか(show the privacy policy checkbox) | 

## Example

```python
from saasus_sdk_python.models.customize_page_props import CustomizePageProps

# TODO update the JSON string below
json = "{}"
# create an instance of CustomizePageProps from a JSON string
customize_page_props_instance = CustomizePageProps.from_json(json)
# print the JSON string representation of the object
print CustomizePageProps.to_json()

# convert the object into a dict
customize_page_props_dict = customize_page_props_instance.to_dict()
# create an instance of CustomizePageProps from a dict
customize_page_props_form_dict = customize_page_props.from_dict(customize_page_props_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



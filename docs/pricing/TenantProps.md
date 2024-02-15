# TenantProps


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | テナント名(tenant name) | 
**attributes** | **Dict[str, object]** | 属性情報(attribute info) | 
**back_office_staff_email** | **str** | 事務管理部門スタッフメールアドレス(administrative staff email address) | 

## Example

```python
from saasus_sdk_python.src.auth.models.tenant_props import TenantProps

# TODO update the JSON string below
json = "{}"
# create an instance of TenantProps from a JSON string
tenant_props_instance = TenantProps.from_json(json)
# print the JSON string representation of the object
print TenantProps.to_json()

# convert the object into a dict
tenant_props_dict = tenant_props_instance.to_dict()
# create an instance of TenantProps from a dict
tenant_props_form_dict = tenant_props.from_dict(tenant_props_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



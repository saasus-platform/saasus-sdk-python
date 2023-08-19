# TenantAttributes


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_attributes** | [**List[Attribute]**](Attribute.md) | テナント属性定義(Tenant Attribute Definition) | 

## Example

```python
from saasus_sdk_python.models.tenant_attributes import TenantAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of TenantAttributes from a JSON string
tenant_attributes_instance = TenantAttributes.from_json(json)
# print the JSON string representation of the object
print TenantAttributes.to_json()

# convert the object into a dict
tenant_attributes_dict = tenant_attributes_instance.to_dict()
# create an instance of TenantAttributes from a dict
tenant_attributes_form_dict = tenant_attributes.from_dict(tenant_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



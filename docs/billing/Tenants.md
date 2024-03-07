# Tenants

Tenant Info

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenants** | [**List[Tenant]**](Tenant.md) |  | 

## Example

```python
from saasus_sdk_python.src.auth.models.tenants import Tenants

# TODO update the JSON string below
json = "{}"
# create an instance of Tenants from a JSON string
tenants_instance = Tenants.from_json(json)
# print the JSON string representation of the object
print Tenants.to_json()

# convert the object into a dict
tenants_dict = tenants_instance.to_dict()
# create an instance of Tenants from a dict
tenants_form_dict = tenants.from_dict(tenants_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



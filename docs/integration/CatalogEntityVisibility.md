# CatalogEntityVisibility


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**visibility** | [**VisibilityStatus**](VisibilityStatus.md) |  | 

## Example

```python
from saasus_sdk_python.src.awsmarketplace.models.catalog_entity_visibility import CatalogEntityVisibility

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogEntityVisibility from a JSON string
catalog_entity_visibility_instance = CatalogEntityVisibility.from_json(json)
# print the JSON string representation of the object
print CatalogEntityVisibility.to_json()

# convert the object into a dict
catalog_entity_visibility_dict = catalog_entity_visibility_instance.to_dict()
# create an instance of CatalogEntityVisibility from a dict
catalog_entity_visibility_form_dict = catalog_entity_visibility.from_dict(catalog_entity_visibility_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# SaasId


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | 
**env_id** | **int** |  | 
**saas_id** | **str** | saas id | 

## Example

```python
from saasus_sdk_python.models.saas_id import SaasId

# TODO update the JSON string below
json = "{}"
# create an instance of SaasId from a JSON string
saas_id_instance = SaasId.from_json(json)
# print the JSON string representation of the object
print SaasId.to_json()

# convert the object into a dict
saas_id_dict = saas_id_instance.to_dict()
# create an instance of SaasId from a dict
saas_id_form_dict = saas_id.from_dict(saas_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# SaasUser


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**email** | **str** | E-mail | 
**attributes** | **Dict[str, object]** | Attribute information  | 

## Example

```python
from saasus_sdk_python.src.auth.models.saas_user import SaasUser

# TODO update the JSON string below
json = "{}"
# create an instance of SaasUser from a JSON string
saas_user_instance = SaasUser.from_json(json)
# print the JSON string representation of the object
print SaasUser.to_json()

# convert the object into a dict
saas_user_dict = saas_user_instance.to_dict()
# create an instance of SaasUser from a dict
saas_user_form_dict = saas_user.from_dict(saas_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



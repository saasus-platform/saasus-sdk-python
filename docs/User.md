# User


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ユーザーID(User ID) | 
**tenant_id** | **str** |  | 
**tenant_name** | **str** | テナント名(Tenant Name) | 
**email** | **str** | メールアドレス(E-mail) | 
**attributes** | **Dict[str, object]** | 属性情報（SaaS 開発コンソールでユーザー属性定義を行い設定された情報を取得します）  Attribute information (Get information set by defining user attributes in the SaaS development console)  | 
**envs** | [**List[UserAvailableEnv]**](UserAvailableEnv.md) |  | 

## Example

```python
from saasus_sdk_python.models.user import User

# TODO update the JSON string below
json = "{}"
# create an instance of User from a JSON string
user_instance = User.from_json(json)
# print the JSON string representation of the object
print User.to_json()

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of User from a dict
user_form_dict = user.from_dict(user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



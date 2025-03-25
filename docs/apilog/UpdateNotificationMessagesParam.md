# UpdateNotificationMessagesParam


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sign_up** | [**MessageTemplate**](MessageTemplate.md) |  | [optional] 
**create_user** | [**MessageTemplate**](MessageTemplate.md) |  | [optional] 
**resend_code** | [**MessageTemplate**](MessageTemplate.md) |  | [optional] 
**forgot_password** | [**MessageTemplate**](MessageTemplate.md) |  | [optional] 
**update_user_attribute** | [**MessageTemplate**](MessageTemplate.md) |  | [optional] 
**verify_user_attribute** | [**MessageTemplate**](MessageTemplate.md) |  | [optional] 
**authentication_mfa** | [**MessageTemplate**](MessageTemplate.md) |  | [optional] 
**invite_tenant_user** | [**MessageTemplate**](MessageTemplate.md) |  | [optional] 
**verify_external_user** | [**MessageTemplate**](MessageTemplate.md) |  | [optional] 

## Example

```python
from saasus_sdk_python.src.auth.models.update_notification_messages_param import UpdateNotificationMessagesParam

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateNotificationMessagesParam from a JSON string
update_notification_messages_param_instance = UpdateNotificationMessagesParam.from_json(json)
# print the JSON string representation of the object
print UpdateNotificationMessagesParam.to_json()

# convert the object into a dict
update_notification_messages_param_dict = update_notification_messages_param_instance.to_dict()
# create an instance of UpdateNotificationMessagesParam from a dict
update_notification_messages_param_form_dict = update_notification_messages_param.from_dict(update_notification_messages_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



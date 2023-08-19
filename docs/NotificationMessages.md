# NotificationMessages


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sign_up** | [**MessageTemplate**](MessageTemplate.md) |  | 
**create_user** | [**MessageTemplate**](MessageTemplate.md) |  | 
**resend_code** | [**MessageTemplate**](MessageTemplate.md) |  | 
**forgot_password** | [**MessageTemplate**](MessageTemplate.md) |  | 
**update_user_attribute** | [**MessageTemplate**](MessageTemplate.md) |  | 
**verify_user_attribute** | [**MessageTemplate**](MessageTemplate.md) |  | 
**authentication_mfa** | [**MessageTemplate**](MessageTemplate.md) |  | 

## Example

```python
from saasus_sdk_python.models.notification_messages import NotificationMessages

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationMessages from a JSON string
notification_messages_instance = NotificationMessages.from_json(json)
# print the JSON string representation of the object
print NotificationMessages.to_json()

# convert the object into a dict
notification_messages_dict = notification_messages_instance.to_dict()
# create an instance of NotificationMessages from a dict
notification_messages_form_dict = notification_messages.from_dict(notification_messages_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



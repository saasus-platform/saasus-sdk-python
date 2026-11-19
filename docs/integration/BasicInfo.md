# BasicInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_name** | **str** | Domain Name | 
**is_dns_validated** | **bool** | DNS Record Verification Results | 
**domain_setup_status** | **str** | Domain setup status. Pending means validation or configuration is in progress; action_required means user action is needed; completed means configuration has been accepted. | [optional] 
**domain_setup_reason_code** | **str** | Reason domain setup is incomplete. Omitted when no known reason is available. DNS validation may still be pending while records propagate. Failed or timed-out certificate requests require resubmitting the domain settings after correcting DNS. | [optional] 
**certificate_dns_record** | [**DnsRecord**](DnsRecord.md) |  | 
**cloud_front_dns_record** | [**DnsRecord**](DnsRecord.md) |  | 
**dkim_dns_records** | [**List[DnsRecord]**](DnsRecord.md) | DKIM DNS Records | 
**default_domain_name** | **str** | Default Domain Name | 
**from_email_address** | **str** | Sender Email for Authentication Email | 
**reply_email_address** | **str** | Reply-from email address of authentication email | 
**is_ses_sandbox_granted** | **bool** | SES sandbox release and Cognito SES configuration results | 

## Example

```python
from saasus_sdk_python.src.auth.models.basic_info import BasicInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BasicInfo from a JSON string
basic_info_instance = BasicInfo.from_json(json)
# print the JSON string representation of the object
print BasicInfo.to_json()

# convert the object into a dict
basic_info_dict = basic_info_instance.to_dict()
# create an instance of BasicInfo from a dict
basic_info_form_dict = basic_info.from_dict(basic_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# UpdateListingStatusParam


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**listing_status** | [**ListingStatus**](ListingStatus.md) |  | 

## Example

```python
from saasus_sdk_python.src.awsmarketplace.models.update_listing_status_param import UpdateListingStatusParam

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateListingStatusParam from a JSON string
update_listing_status_param_instance = UpdateListingStatusParam.from_json(json)
# print the JSON string representation of the object
print UpdateListingStatusParam.to_json()

# convert the object into a dict
update_listing_status_param_dict = update_listing_status_param_instance.to_dict()
# create an instance of UpdateListingStatusParam from a dict
update_listing_status_param_form_dict = update_listing_status_param.from_dict(update_listing_status_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



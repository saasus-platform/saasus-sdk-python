# GetListingStatusResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**listing_status** | [**ListingStatus**](ListingStatus.md) |  | 

## Example

```python
from saasus_sdk_python.src.awsmarketplace.models.get_listing_status_result import GetListingStatusResult

# TODO update the JSON string below
json = "{}"
# create an instance of GetListingStatusResult from a JSON string
get_listing_status_result_instance = GetListingStatusResult.from_json(json)
# print the JSON string representation of the object
print GetListingStatusResult.to_json()

# convert the object into a dict
get_listing_status_result_dict = get_listing_status_result_instance.to_dict()
# create an instance of GetListingStatusResult from a dict
get_listing_status_result_form_dict = get_listing_status_result.from_dict(get_listing_status_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



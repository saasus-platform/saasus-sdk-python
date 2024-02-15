# saasus_sdk_python.src.communication.FeedbackApi

All URIs are relative to *https://api.saasus.io/v1/communication*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_feedback**](FeedbackApi.md#create_feedback) | **POST** /feedbacks | 
[**create_feedback_comment**](FeedbackApi.md#create_feedback_comment) | **POST** /feedbacks/{feedback_id}/comments | 
[**create_vote_user**](FeedbackApi.md#create_vote_user) | **POST** /feedbacks/{feedback_id}/votes/users | 
[**delete_feedback**](FeedbackApi.md#delete_feedback) | **DELETE** /feedbacks/{feedback_id} | 
[**delete_feedback_comment**](FeedbackApi.md#delete_feedback_comment) | **DELETE** /feedbacks/{feedback_id}/comments/{comment_id} | 
[**delete_vote_for_feedback**](FeedbackApi.md#delete_vote_for_feedback) | **DELETE** /feedbacks/{feedback_id}/votes/users/{user_id} | 
[**get_feedback**](FeedbackApi.md#get_feedback) | **GET** /feedbacks/{feedback_id} | 
[**get_feedback_comment**](FeedbackApi.md#get_feedback_comment) | **GET** /feedbacks/{feedback_id}/comments/{comment_id} | 
[**get_feedbacks**](FeedbackApi.md#get_feedbacks) | **GET** /feedbacks | 
[**update_feedback**](FeedbackApi.md#update_feedback) | **PATCH** /feedbacks/{feedback_id} | 
[**update_feedback_comment**](FeedbackApi.md#update_feedback_comment) | **PATCH** /feedbacks/{feedback_id}/comments/{comment_id} | 
[**update_feedback_status**](FeedbackApi.md#update_feedback_status) | **PATCH** /feedbacks/{feedback_id}/status | 


# **create_feedback**
> Feedback create_feedback(create_feedback_param=create_feedback_param)



フィードバックを起票

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.communication
from saasus_sdk_python.src.communication.models.create_feedback_param import CreateFeedbackParam
from saasus_sdk_python.src.communication.models.feedback import Feedback
from saasus_sdk_python.src.communication.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.saasus.io/v1/communication
# See configuration.py for a list of all supported configuration parameters.
configuration = saasus_sdk_python.src.communication.Configuration(
    host = "https://api.saasus.io/v1/communication"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = saasus_sdk_python.src.communication.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with saasus_sdk_python.src.communication.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = saasus_sdk_python.src.communication.FeedbackApi(api_client)
    create_feedback_param = saasus_sdk_python.src.communication.CreateFeedbackParam() # CreateFeedbackParam |  (optional)

    try:
        api_response = api_instance.create_feedback(create_feedback_param=create_feedback_param)
        print("The response of FeedbackApi->create_feedback:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeedbackApi->create_feedback: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_feedback_param** | [**CreateFeedbackParam**](CreateFeedbackParam.md)|  | [optional] 

### Return type

[**Feedback**](Feedback.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_feedback_comment**
> Comment create_feedback_comment(feedback_id, create_feedback_comment_param=create_feedback_comment_param)



フィードバックへのコメント

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.communication
from saasus_sdk_python.src.communication.models.comment import Comment
from saasus_sdk_python.src.communication.models.create_feedback_comment_param import CreateFeedbackCommentParam
from saasus_sdk_python.src.communication.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.saasus.io/v1/communication
# See configuration.py for a list of all supported configuration parameters.
configuration = saasus_sdk_python.src.communication.Configuration(
    host = "https://api.saasus.io/v1/communication"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = saasus_sdk_python.src.communication.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with saasus_sdk_python.src.communication.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = saasus_sdk_python.src.communication.FeedbackApi(api_client)
    feedback_id = 'feedback_id_example' # str | 
    create_feedback_comment_param = saasus_sdk_python.src.communication.CreateFeedbackCommentParam() # CreateFeedbackCommentParam |  (optional)

    try:
        api_response = api_instance.create_feedback_comment(feedback_id, create_feedback_comment_param=create_feedback_comment_param)
        print("The response of FeedbackApi->create_feedback_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeedbackApi->create_feedback_comment: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feedback_id** | **str**|  | 
 **create_feedback_comment_param** | [**CreateFeedbackCommentParam**](CreateFeedbackCommentParam.md)|  | [optional] 

### Return type

[**Comment**](Comment.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_vote_user**
> Votes create_vote_user(feedback_id, create_vote_user_param=create_vote_user_param)



フィードバックへの投票

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.communication
from saasus_sdk_python.src.communication.models.create_vote_user_param import CreateVoteUserParam
from saasus_sdk_python.src.communication.models.votes import Votes
from saasus_sdk_python.src.communication.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.saasus.io/v1/communication
# See configuration.py for a list of all supported configuration parameters.
configuration = saasus_sdk_python.src.communication.Configuration(
    host = "https://api.saasus.io/v1/communication"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = saasus_sdk_python.src.communication.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with saasus_sdk_python.src.communication.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = saasus_sdk_python.src.communication.FeedbackApi(api_client)
    feedback_id = 'feedback_id_example' # str | 
    create_vote_user_param = saasus_sdk_python.src.communication.CreateVoteUserParam() # CreateVoteUserParam |  (optional)

    try:
        api_response = api_instance.create_vote_user(feedback_id, create_vote_user_param=create_vote_user_param)
        print("The response of FeedbackApi->create_vote_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeedbackApi->create_vote_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feedback_id** | **str**|  | 
 **create_vote_user_param** | [**CreateVoteUserParam**](CreateVoteUserParam.md)|  | [optional] 

### Return type

[**Votes**](Votes.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_feedback**
> delete_feedback(feedback_id)



フィードバックの削除

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.communication
from saasus_sdk_python.src.communication.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.saasus.io/v1/communication
# See configuration.py for a list of all supported configuration parameters.
configuration = saasus_sdk_python.src.communication.Configuration(
    host = "https://api.saasus.io/v1/communication"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = saasus_sdk_python.src.communication.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with saasus_sdk_python.src.communication.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = saasus_sdk_python.src.communication.FeedbackApi(api_client)
    feedback_id = 'feedback_id_example' # str | 

    try:
        api_instance.delete_feedback(feedback_id)
    except Exception as e:
        print("Exception when calling FeedbackApi->delete_feedback: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feedback_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_feedback_comment**
> delete_feedback_comment(feedback_id, comment_id)



フィードバックへのコメント削除

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.communication
from saasus_sdk_python.src.communication.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.saasus.io/v1/communication
# See configuration.py for a list of all supported configuration parameters.
configuration = saasus_sdk_python.src.communication.Configuration(
    host = "https://api.saasus.io/v1/communication"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = saasus_sdk_python.src.communication.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with saasus_sdk_python.src.communication.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = saasus_sdk_python.src.communication.FeedbackApi(api_client)
    feedback_id = 'feedback_id_example' # str | 
    comment_id = 'comment_id_example' # str | 

    try:
        api_instance.delete_feedback_comment(feedback_id, comment_id)
    except Exception as e:
        print("Exception when calling FeedbackApi->delete_feedback_comment: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feedback_id** | **str**|  | 
 **comment_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_vote_for_feedback**
> delete_vote_for_feedback(feedback_id, user_id)



フィードバックへの投票の取消

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.communication
from saasus_sdk_python.src.communication.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.saasus.io/v1/communication
# See configuration.py for a list of all supported configuration parameters.
configuration = saasus_sdk_python.src.communication.Configuration(
    host = "https://api.saasus.io/v1/communication"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = saasus_sdk_python.src.communication.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with saasus_sdk_python.src.communication.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = saasus_sdk_python.src.communication.FeedbackApi(api_client)
    feedback_id = 'feedback_id_example' # str | 
    user_id = 'user_id_example' # str | 

    try:
        api_instance.delete_vote_for_feedback(feedback_id, user_id)
    except Exception as e:
        print("Exception when calling FeedbackApi->delete_vote_for_feedback: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feedback_id** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_feedback**
> Feedback get_feedback(feedback_id)



フィードバックの取得

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.communication
from saasus_sdk_python.src.communication.models.feedback import Feedback
from saasus_sdk_python.src.communication.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.saasus.io/v1/communication
# See configuration.py for a list of all supported configuration parameters.
configuration = saasus_sdk_python.src.communication.Configuration(
    host = "https://api.saasus.io/v1/communication"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = saasus_sdk_python.src.communication.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with saasus_sdk_python.src.communication.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = saasus_sdk_python.src.communication.FeedbackApi(api_client)
    feedback_id = 'feedback_id_example' # str | 

    try:
        api_response = api_instance.get_feedback(feedback_id)
        print("The response of FeedbackApi->get_feedback:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeedbackApi->get_feedback: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feedback_id** | **str**|  | 

### Return type

[**Feedback**](Feedback.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_feedback_comment**
> Comment get_feedback_comment(feedback_id, comment_id)



フィードバックへのコメント取得

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.communication
from saasus_sdk_python.src.communication.models.comment import Comment
from saasus_sdk_python.src.communication.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.saasus.io/v1/communication
# See configuration.py for a list of all supported configuration parameters.
configuration = saasus_sdk_python.src.communication.Configuration(
    host = "https://api.saasus.io/v1/communication"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = saasus_sdk_python.src.communication.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with saasus_sdk_python.src.communication.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = saasus_sdk_python.src.communication.FeedbackApi(api_client)
    feedback_id = 'feedback_id_example' # str | 
    comment_id = 'comment_id_example' # str | 

    try:
        api_response = api_instance.get_feedback_comment(feedback_id, comment_id)
        print("The response of FeedbackApi->get_feedback_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeedbackApi->get_feedback_comment: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feedback_id** | **str**|  | 
 **comment_id** | **str**|  | 

### Return type

[**Comment**](Comment.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_feedbacks**
> Feedbacks get_feedbacks()



フィードバックの一覧を取得

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.communication
from saasus_sdk_python.src.communication.models.feedbacks import Feedbacks
from saasus_sdk_python.src.communication.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.saasus.io/v1/communication
# See configuration.py for a list of all supported configuration parameters.
configuration = saasus_sdk_python.src.communication.Configuration(
    host = "https://api.saasus.io/v1/communication"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = saasus_sdk_python.src.communication.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with saasus_sdk_python.src.communication.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = saasus_sdk_python.src.communication.FeedbackApi(api_client)

    try:
        api_response = api_instance.get_feedbacks()
        print("The response of FeedbackApi->get_feedbacks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeedbackApi->get_feedbacks: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**Feedbacks**](Feedbacks.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_feedback**
> update_feedback(feedback_id, update_feedback_param=update_feedback_param)



フィードバックの編集

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.communication
from saasus_sdk_python.src.communication.models.update_feedback_param import UpdateFeedbackParam
from saasus_sdk_python.src.communication.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.saasus.io/v1/communication
# See configuration.py for a list of all supported configuration parameters.
configuration = saasus_sdk_python.src.communication.Configuration(
    host = "https://api.saasus.io/v1/communication"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = saasus_sdk_python.src.communication.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with saasus_sdk_python.src.communication.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = saasus_sdk_python.src.communication.FeedbackApi(api_client)
    feedback_id = 'feedback_id_example' # str | 
    update_feedback_param = saasus_sdk_python.src.communication.UpdateFeedbackParam() # UpdateFeedbackParam |  (optional)

    try:
        api_instance.update_feedback(feedback_id, update_feedback_param=update_feedback_param)
    except Exception as e:
        print("Exception when calling FeedbackApi->update_feedback: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feedback_id** | **str**|  | 
 **update_feedback_param** | [**UpdateFeedbackParam**](UpdateFeedbackParam.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_feedback_comment**
> update_feedback_comment(feedback_id, comment_id, update_feedback_comment_param=update_feedback_comment_param)



フィードバックへのコメント編集

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.communication
from saasus_sdk_python.src.communication.models.update_feedback_comment_param import UpdateFeedbackCommentParam
from saasus_sdk_python.src.communication.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.saasus.io/v1/communication
# See configuration.py for a list of all supported configuration parameters.
configuration = saasus_sdk_python.src.communication.Configuration(
    host = "https://api.saasus.io/v1/communication"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = saasus_sdk_python.src.communication.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with saasus_sdk_python.src.communication.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = saasus_sdk_python.src.communication.FeedbackApi(api_client)
    feedback_id = 'feedback_id_example' # str | 
    comment_id = 'comment_id_example' # str | 
    update_feedback_comment_param = saasus_sdk_python.src.communication.UpdateFeedbackCommentParam() # UpdateFeedbackCommentParam |  (optional)

    try:
        api_instance.update_feedback_comment(feedback_id, comment_id, update_feedback_comment_param=update_feedback_comment_param)
    except Exception as e:
        print("Exception when calling FeedbackApi->update_feedback_comment: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feedback_id** | **str**|  | 
 **comment_id** | **str**|  | 
 **update_feedback_comment_param** | [**UpdateFeedbackCommentParam**](UpdateFeedbackCommentParam.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_feedback_status**
> update_feedback_status(feedback_id, update_feedback_status_param=update_feedback_status_param)



フィードバックのステータス更新

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import saasus_sdk_python.src.communication
from saasus_sdk_python.src.communication.models.update_feedback_status_param import UpdateFeedbackStatusParam
from saasus_sdk_python.src.communication.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.saasus.io/v1/communication
# See configuration.py for a list of all supported configuration parameters.
configuration = saasus_sdk_python.src.communication.Configuration(
    host = "https://api.saasus.io/v1/communication"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = saasus_sdk_python.src.communication.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with saasus_sdk_python.src.communication.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = saasus_sdk_python.src.communication.FeedbackApi(api_client)
    feedback_id = 'feedback_id_example' # str | 
    update_feedback_status_param = saasus_sdk_python.src.communication.UpdateFeedbackStatusParam() # UpdateFeedbackStatusParam |  (optional)

    try:
        api_instance.update_feedback_status(feedback_id, update_feedback_status_param=update_feedback_status_param)
    except Exception as e:
        print("Exception when calling FeedbackApi->update_feedback_status: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feedback_id** | **str**|  | 
 **update_feedback_status_param** | [**UpdateFeedbackStatusParam**](UpdateFeedbackStatusParam.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

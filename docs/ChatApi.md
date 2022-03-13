# ecoserver.ChatApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**chat_get_chat**](ChatApi.md#chat_get_chat) | **GET** /api/v1/chat | Returns all non-private player chat messages sent within the given time range.
[**chat_get_chat_by_tag**](ChatApi.md#chat_get_chat_by_tag) | **GET** /api/v1/chat/tag | Returns all non-private player chat messages sent to the given tag within the given time range.
[**chat_get_chat_messages_sent_by**](ChatApi.md#chat_get_chat_messages_sent_by) | **GET** /api/v1/chat/{username} | Returns all non-private chat messages sent by the given user within the given time range.
[**chat_get_next**](ChatApi.md#chat_get_next) | **POST** /api/v1/chat/next | Gets the. &lt;code&gt;numNextMessages&lt;/code&gt; chat messages sent after the given message on the same tag.
[**chat_get_previous**](ChatApi.md#chat_get_previous) | **POST** /api/v1/chat/previous | Gets the. &lt;code&gt;numPreviousMessages&lt;/code&gt; chat messages sent before the given message on the same tag.
[**chat_send_chat**](ChatApi.md#chat_send_chat) | **GET** /api/v1/chat/sendChat | Sends chat message like username.


# **chat_get_chat**
> chat_get_chat(authtoken, authtokentype, start_day=start_day, end_day=end_day)

Returns all non-private player chat messages sent within the given time range.

### Example
```python
from __future__ import print_function
import time
import ecoserver
from ecoserver.rest import ApiException
from pprint import pprint

# Configure API key authorization: authtoken
configuration = ecoserver.Configuration()
configuration.api_key['authtoken'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authtoken'] = 'Bearer'
# Configure API key authorization: authtokentype
configuration = ecoserver.Configuration()
configuration.api_key['authtokentype'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authtokentype'] = 'Bearer'

# create an instance of the API class
api_instance = ecoserver.ChatApi(ecoserver.ApiClient(configuration))
authtoken = 'authtoken_example' # str | Eco user authentication token.
authtokentype = 'authtokentype_example' # str | Eco user authentication token type.
start_day = 0 # float | The lower bound on the time range. Default is 0. (optional) (default to 0)
end_day = -1 # float | The upper bound on the time range. Default is now. (optional) (default to -1)

try:
    # Returns all non-private player chat messages sent within the given time range.
    api_instance.chat_get_chat(authtoken, authtokentype, start_day=start_day, end_day=end_day)
except ApiException as e:
    print("Exception when calling ChatApi->chat_get_chat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authtoken** | **str**| Eco user authentication token. | 
 **authtokentype** | **str**| Eco user authentication token type. | 
 **start_day** | **float**| The lower bound on the time range. Default is 0. | [optional] [default to 0]
 **end_day** | **float**| The upper bound on the time range. Default is now. | [optional] [default to -1]

### Return type

void (empty response body)

### Authorization

[authtoken](../README.md#authtoken), [authtokentype](../README.md#authtokentype)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chat_get_chat_by_tag**
> chat_get_chat_by_tag(authtoken, authtokentype, tag=tag, start_day=start_day, end_day=end_day)

Returns all non-private player chat messages sent to the given tag within the given time range.

### Example
```python
from __future__ import print_function
import time
import ecoserver
from ecoserver.rest import ApiException
from pprint import pprint

# Configure API key authorization: authtoken
configuration = ecoserver.Configuration()
configuration.api_key['authtoken'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authtoken'] = 'Bearer'
# Configure API key authorization: authtokentype
configuration = ecoserver.Configuration()
configuration.api_key['authtokentype'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authtokentype'] = 'Bearer'

# create an instance of the API class
api_instance = ecoserver.ChatApi(ecoserver.ApiClient(configuration))
authtoken = 'authtoken_example' # str | Eco user authentication token.
authtokentype = 'authtokentype_example' # str | Eco user authentication token type.
tag = 'tag_example' # str | The tag name in question. (optional)
start_day = 0 # float | The lower bound on the time range. Default is 0. (optional) (default to 0)
end_day = -1 # float | The upper bound on the time range. Default is now. (optional) (default to -1)

try:
    # Returns all non-private player chat messages sent to the given tag within the given time range.
    api_instance.chat_get_chat_by_tag(authtoken, authtokentype, tag=tag, start_day=start_day, end_day=end_day)
except ApiException as e:
    print("Exception when calling ChatApi->chat_get_chat_by_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authtoken** | **str**| Eco user authentication token. | 
 **authtokentype** | **str**| Eco user authentication token type. | 
 **tag** | **str**| The tag name in question. | [optional] 
 **start_day** | **float**| The lower bound on the time range. Default is 0. | [optional] [default to 0]
 **end_day** | **float**| The upper bound on the time range. Default is now. | [optional] [default to -1]

### Return type

void (empty response body)

### Authorization

[authtoken](../README.md#authtoken), [authtokentype](../README.md#authtokentype)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chat_get_chat_messages_sent_by**
> chat_get_chat_messages_sent_by(username, authtoken, authtokentype, start_day=start_day, end_day=end_day)

Returns all non-private chat messages sent by the given user within the given time range.

### Example
```python
from __future__ import print_function
import time
import ecoserver
from ecoserver.rest import ApiException
from pprint import pprint

# Configure API key authorization: authtoken
configuration = ecoserver.Configuration()
configuration.api_key['authtoken'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authtoken'] = 'Bearer'
# Configure API key authorization: authtokentype
configuration = ecoserver.Configuration()
configuration.api_key['authtokentype'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authtokentype'] = 'Bearer'

# create an instance of the API class
api_instance = ecoserver.ChatApi(ecoserver.ApiClient(configuration))
username = 'username_example' # str | The user in question.
authtoken = 'authtoken_example' # str | Eco user authentication token.
authtokentype = 'authtokentype_example' # str | Eco user authentication token type.
start_day = 0 # float | The lower bound on the time range. Default is 0. (optional) (default to 0)
end_day = -1 # float | The upper bound on the time range. Default is now. (optional) (default to -1)

try:
    # Returns all non-private chat messages sent by the given user within the given time range.
    api_instance.chat_get_chat_messages_sent_by(username, authtoken, authtokentype, start_day=start_day, end_day=end_day)
except ApiException as e:
    print("Exception when calling ChatApi->chat_get_chat_messages_sent_by: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The user in question. | 
 **authtoken** | **str**| Eco user authentication token. | 
 **authtokentype** | **str**| Eco user authentication token type. | 
 **start_day** | **float**| The lower bound on the time range. Default is 0. | [optional] [default to 0]
 **end_day** | **float**| The upper bound on the time range. Default is now. | [optional] [default to -1]

### Return type

void (empty response body)

### Authorization

[authtoken](../README.md#authtoken), [authtokentype](../README.md#authtokentype)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chat_get_next**
> chat_get_next(authtoken, authtokentype, num_next_messages=num_next_messages, body=body)

Gets the. <code>numNextMessages</code> chat messages sent after the given message on the same tag.

### Example
```python
from __future__ import print_function
import time
import ecoserver
from ecoserver.rest import ApiException
from pprint import pprint

# Configure API key authorization: authtoken
configuration = ecoserver.Configuration()
configuration.api_key['authtoken'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authtoken'] = 'Bearer'
# Configure API key authorization: authtokentype
configuration = ecoserver.Configuration()
configuration.api_key['authtokentype'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authtokentype'] = 'Bearer'

# create an instance of the API class
api_instance = ecoserver.ChatApi(ecoserver.ApiClient(configuration))
authtoken = 'authtoken_example' # str | Eco user authentication token.
authtokentype = 'authtokentype_example' # str | Eco user authentication token type.
num_next_messages = 56 # int | The number of following messages to return. (optional)
body = ecoserver.EcoWebServerDataTransferObjectsChatMessageDTO() # EcoWebServerDataTransferObjectsChatMessageDTO | The message in question. (optional)

try:
    # Gets the. <code>numNextMessages</code> chat messages sent after the given message on the same tag.
    api_instance.chat_get_next(authtoken, authtokentype, num_next_messages=num_next_messages, body=body)
except ApiException as e:
    print("Exception when calling ChatApi->chat_get_next: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authtoken** | **str**| Eco user authentication token. | 
 **authtokentype** | **str**| Eco user authentication token type. | 
 **num_next_messages** | **int**| The number of following messages to return. | [optional] 
 **body** | [**EcoWebServerDataTransferObjectsChatMessageDTO**](EcoWebServerDataTransferObjectsChatMessageDTO.md)| The message in question. | [optional] 

### Return type

void (empty response body)

### Authorization

[authtoken](../README.md#authtoken), [authtokentype](../README.md#authtokentype)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chat_get_previous**
> chat_get_previous(authtoken, authtokentype, num_previous_messages=num_previous_messages, body=body)

Gets the. <code>numPreviousMessages</code> chat messages sent before the given message on the same tag.

### Example
```python
from __future__ import print_function
import time
import ecoserver
from ecoserver.rest import ApiException
from pprint import pprint

# Configure API key authorization: authtoken
configuration = ecoserver.Configuration()
configuration.api_key['authtoken'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authtoken'] = 'Bearer'
# Configure API key authorization: authtokentype
configuration = ecoserver.Configuration()
configuration.api_key['authtokentype'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authtokentype'] = 'Bearer'

# create an instance of the API class
api_instance = ecoserver.ChatApi(ecoserver.ApiClient(configuration))
authtoken = 'authtoken_example' # str | Eco user authentication token.
authtokentype = 'authtokentype_example' # str | Eco user authentication token type.
num_previous_messages = 56 # int | The number of preceding messages to return. (optional)
body = ecoserver.EcoWebServerDataTransferObjectsChatMessageDTO() # EcoWebServerDataTransferObjectsChatMessageDTO | The message in question. (optional)

try:
    # Gets the. <code>numPreviousMessages</code> chat messages sent before the given message on the same tag.
    api_instance.chat_get_previous(authtoken, authtokentype, num_previous_messages=num_previous_messages, body=body)
except ApiException as e:
    print("Exception when calling ChatApi->chat_get_previous: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authtoken** | **str**| Eco user authentication token. | 
 **authtokentype** | **str**| Eco user authentication token type. | 
 **num_previous_messages** | **int**| The number of preceding messages to return. | [optional] 
 **body** | [**EcoWebServerDataTransferObjectsChatMessageDTO**](EcoWebServerDataTransferObjectsChatMessageDTO.md)| The message in question. | [optional] 

### Return type

void (empty response body)

### Authorization

[authtoken](../README.md#authtoken), [authtokentype](../README.md#authtokentype)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chat_send_chat**
> chat_send_chat(authtoken, authtokentype, username=username, message=message)

Sends chat message like username.

> This endpoint can only be invoked when AllowDebugCalls is enabled on the server.

### Example
```python
from __future__ import print_function
import time
import ecoserver
from ecoserver.rest import ApiException
from pprint import pprint

# Configure API key authorization: authtoken
configuration = ecoserver.Configuration()
configuration.api_key['authtoken'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authtoken'] = 'Bearer'
# Configure API key authorization: authtokentype
configuration = ecoserver.Configuration()
configuration.api_key['authtokentype'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authtokentype'] = 'Bearer'

# create an instance of the API class
api_instance = ecoserver.ChatApi(ecoserver.ApiClient(configuration))
authtoken = 'authtoken_example' # str | Eco user authentication token.
authtokentype = 'authtokentype_example' # str | Eco user authentication token type.
username = 'username_example' # str | User who wants to send message. (optional)
message = 'message_example' # str | The message to send. (optional)

try:
    # Sends chat message like username.
    api_instance.chat_send_chat(authtoken, authtokentype, username=username, message=message)
except ApiException as e:
    print("Exception when calling ChatApi->chat_send_chat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authtoken** | **str**| Eco user authentication token. | 
 **authtokentype** | **str**| Eco user authentication token type. | 
 **username** | **str**| User who wants to send message. | [optional] 
 **message** | **str**| The message to send. | [optional] 

### Return type

void (empty response body)

### Authorization

[authtoken](../README.md#authtoken), [authtokentype](../README.md#authtokentype)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


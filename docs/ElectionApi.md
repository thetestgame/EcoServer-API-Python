# ecoserver.ElectionApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**election_add_comment**](ElectionApi.md#election_add_comment) | **POST** /api/v1/elections/addcomment | Adds a comment to the currently running election, if any.
[**election_finish_election**](ElectionApi.md#election_finish_election) | **POST** /api/v1/elections/finishelection | 
[**election_force_election_end**](ElectionApi.md#election_force_election_end) | **POST** /api/v1/elections/forceelectionend | Forces the currently running election to end now, and for the current election winner to become the leader. Can only be called by an admin or dev.
[**election_generate_test_data**](ElectionApi.md#election_generate_test_data) | **POST** /api/v1/elections/generatetestdata | Create a bunch of test elections.
[**election_get_comments**](ElectionApi.md#election_get_comments) | **GET** /api/v1/elections/listcomments | List comments on the election.
[**election_get_elected_title_by_id**](ElectionApi.md#election_get_elected_title_by_id) | **GET** /api/v1/elections/titles/{id} | Returns the elected title with the given id.
[**election_get_election_by_id**](ElectionApi.md#election_get_election_by_id) | **GET** /api/v1/elections/{id} | Returns the election with the given id.
[**election_list_elected_titles**](ElectionApi.md#election_list_elected_titles) | **GET** /api/v1/elections/titles | Returns all elected titles and their occupants matching the given state (active by default).
[**election_list_elections**](ElectionApi.md#election_list_elections) | **GET** /api/v1/elections | Returns all elections that are either active or inactive.
[**election_vote**](ElectionApi.md#election_vote) | **POST** /api/v1/elections/vote | Places a vote on behalf of the given player.  Can only be called if an election is currently running.
[**election_votes**](ElectionApi.md#election_votes) | **GET** /api/v1/elections/votes | Returns a list of votes that were made on the indicated election.


# **election_add_comment**
> election_add_comment(authtoken, authtokentype, election_id=election_id, body=body)

Adds a comment to the currently running election, if any.

> This endpoint can only be invoked by a ??.

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
api_instance = ecoserver.ElectionApi(ecoserver.ApiClient(configuration))
authtoken = 'authtoken_example' # str | Eco user authentication token.
authtokentype = 'authtokentype_example' # str | Eco user authentication token type.
election_id = 56 # int | ID of the election. (optional)
body = ecoserver.EcoWebServerDataTransferObjectsElectionCommentDTO() # EcoWebServerDataTransferObjectsElectionCommentDTO | The comment to be added to the election. (optional)

try:
    # Adds a comment to the currently running election, if any.
    api_instance.election_add_comment(authtoken, authtokentype, election_id=election_id, body=body)
except ApiException as e:
    print("Exception when calling ElectionApi->election_add_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authtoken** | **str**| Eco user authentication token. | 
 **authtokentype** | **str**| Eco user authentication token type. | 
 **election_id** | **int**| ID of the election. | [optional] 
 **body** | [**EcoWebServerDataTransferObjectsElectionCommentDTO**](EcoWebServerDataTransferObjectsElectionCommentDTO.md)| The comment to be added to the election. | [optional] 

### Return type

void (empty response body)

### Authorization

[authtoken](../README.md#authtoken), [authtokentype](../README.md#authtokentype)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **election_finish_election**
> election_finish_election(authtoken, authtokentype)



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
api_instance = ecoserver.ElectionApi(ecoserver.ApiClient(configuration))
authtoken = 'authtoken_example' # str | Eco user authentication token.
authtokentype = 'authtokentype_example' # str | Eco user authentication token type.

try:
    api_instance.election_finish_election(authtoken, authtokentype)
except ApiException as e:
    print("Exception when calling ElectionApi->election_finish_election: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authtoken** | **str**| Eco user authentication token. | 
 **authtokentype** | **str**| Eco user authentication token type. | 

### Return type

void (empty response body)

### Authorization

[authtoken](../README.md#authtoken), [authtokentype](../README.md#authtokentype)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **election_force_election_end**
> election_force_election_end(authtoken, authtokentype, election_id=election_id)

Forces the currently running election to end now, and for the current election winner to become the leader. Can only be called by an admin or dev.

> This endpoint can only be invoked by a Admin user.

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
api_instance = ecoserver.ElectionApi(ecoserver.ApiClient(configuration))
authtoken = 'authtoken_example' # str | Eco user authentication token.
authtokentype = 'authtokentype_example' # str | Eco user authentication token type.
election_id = 56 # int | ID of the election. (optional)

try:
    # Forces the currently running election to end now, and for the current election winner to become the leader. Can only be called by an admin or dev.
    api_instance.election_force_election_end(authtoken, authtokentype, election_id=election_id)
except ApiException as e:
    print("Exception when calling ElectionApi->election_force_election_end: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authtoken** | **str**| Eco user authentication token. | 
 **authtokentype** | **str**| Eco user authentication token type. | 
 **election_id** | **int**| ID of the election. | [optional] 

### Return type

void (empty response body)

### Authorization

[authtoken](../README.md#authtoken), [authtokentype](../README.md#authtokentype)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **election_generate_test_data**
> election_generate_test_data(authtoken, authtokentype)

Create a bunch of test elections.

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
api_instance = ecoserver.ElectionApi(ecoserver.ApiClient(configuration))
authtoken = 'authtoken_example' # str | Eco user authentication token.
authtokentype = 'authtokentype_example' # str | Eco user authentication token type.

try:
    # Create a bunch of test elections.
    api_instance.election_generate_test_data(authtoken, authtokentype)
except ApiException as e:
    print("Exception when calling ElectionApi->election_generate_test_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authtoken** | **str**| Eco user authentication token. | 
 **authtokentype** | **str**| Eco user authentication token type. | 

### Return type

void (empty response body)

### Authorization

[authtoken](../README.md#authtoken), [authtokentype](../README.md#authtokentype)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **election_get_comments**
> list[EcoWebServerDataTransferObjectsElectionCommentDTO] election_get_comments(authtoken, authtokentype, election_id=election_id)

List comments on the election.

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
api_instance = ecoserver.ElectionApi(ecoserver.ApiClient(configuration))
authtoken = 'authtoken_example' # str | Eco user authentication token.
authtokentype = 'authtokentype_example' # str | Eco user authentication token type.
election_id = 56 # int | ID of the election. (optional)

try:
    # List comments on the election.
    api_response = api_instance.election_get_comments(authtoken, authtokentype, election_id=election_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ElectionApi->election_get_comments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authtoken** | **str**| Eco user authentication token. | 
 **authtokentype** | **str**| Eco user authentication token type. | 
 **election_id** | **int**| ID of the election. | [optional] 

### Return type

[**list[EcoWebServerDataTransferObjectsElectionCommentDTO]**](EcoWebServerDataTransferObjectsElectionCommentDTO.md)

### Authorization

[authtoken](../README.md#authtoken), [authtokentype](../README.md#authtokentype)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **election_get_elected_title_by_id**
> election_get_elected_title_by_id(id, authtoken, authtokentype)

Returns the elected title with the given id.

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
api_instance = ecoserver.ElectionApi(ecoserver.ApiClient(configuration))
id = 56 # int | 
authtoken = 'authtoken_example' # str | Eco user authentication token.
authtokentype = 'authtokentype_example' # str | Eco user authentication token type.

try:
    # Returns the elected title with the given id.
    api_instance.election_get_elected_title_by_id(id, authtoken, authtokentype)
except ApiException as e:
    print("Exception when calling ElectionApi->election_get_elected_title_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **authtoken** | **str**| Eco user authentication token. | 
 **authtokentype** | **str**| Eco user authentication token type. | 

### Return type

void (empty response body)

### Authorization

[authtoken](../README.md#authtoken), [authtokentype](../README.md#authtokentype)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **election_get_election_by_id**
> election_get_election_by_id(id, authtoken, authtokentype)

Returns the election with the given id.

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
api_instance = ecoserver.ElectionApi(ecoserver.ApiClient(configuration))
id = 56 # int | 
authtoken = 'authtoken_example' # str | Eco user authentication token.
authtokentype = 'authtokentype_example' # str | Eco user authentication token type.

try:
    # Returns the election with the given id.
    api_instance.election_get_election_by_id(id, authtoken, authtokentype)
except ApiException as e:
    print("Exception when calling ElectionApi->election_get_election_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **authtoken** | **str**| Eco user authentication token. | 
 **authtokentype** | **str**| Eco user authentication token type. | 

### Return type

void (empty response body)

### Authorization

[authtoken](../README.md#authtoken), [authtokentype](../README.md#authtokentype)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **election_list_elected_titles**
> list[EcoWebServerDataTransferObjectsElectedTitleDTO] election_list_elected_titles(authtoken, authtokentype, state=state)

Returns all elected titles and their occupants matching the given state (active by default).

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
api_instance = ecoserver.ElectionApi(ecoserver.ApiClient(configuration))
authtoken = 'authtoken_example' # str | Eco user authentication token.
authtokentype = 'authtokentype_example' # str | Eco user authentication token type.
state = NULL # object |  (optional)

try:
    # Returns all elected titles and their occupants matching the given state (active by default).
    api_response = api_instance.election_list_elected_titles(authtoken, authtokentype, state=state)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ElectionApi->election_list_elected_titles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authtoken** | **str**| Eco user authentication token. | 
 **authtokentype** | **str**| Eco user authentication token type. | 
 **state** | [**object**](.md)|  | [optional] 

### Return type

[**list[EcoWebServerDataTransferObjectsElectedTitleDTO]**](EcoWebServerDataTransferObjectsElectedTitleDTO.md)

### Authorization

[authtoken](../README.md#authtoken), [authtokentype](../README.md#authtokentype)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **election_list_elections**
> list[EcoWebServerDataTransferObjectsElectionDTO] election_list_elections(authtoken, authtokentype, return_active=return_active)

Returns all elections that are either active or inactive.

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
api_instance = ecoserver.ElectionApi(ecoserver.ApiClient(configuration))
authtoken = 'authtoken_example' # str | Eco user authentication token.
authtokentype = 'authtokentype_example' # str | Eco user authentication token type.
return_active = true # bool |  (optional) (default to true)

try:
    # Returns all elections that are either active or inactive.
    api_response = api_instance.election_list_elections(authtoken, authtokentype, return_active=return_active)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ElectionApi->election_list_elections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authtoken** | **str**| Eco user authentication token. | 
 **authtokentype** | **str**| Eco user authentication token type. | 
 **return_active** | **bool**|  | [optional] [default to true]

### Return type

[**list[EcoWebServerDataTransferObjectsElectionDTO]**](EcoWebServerDataTransferObjectsElectionDTO.md)

### Authorization

[authtoken](../README.md#authtoken), [authtokentype](../README.md#authtokentype)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **election_vote**
> election_vote(authtoken, authtokentype, force_vote=force_vote, body=body)

Places a vote on behalf of the given player.  Can only be called if an election is currently running.

> This endpoint can only be invoked by a ??.

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
api_instance = ecoserver.ElectionApi(ecoserver.ApiClient(configuration))
authtoken = 'authtoken_example' # str | Eco user authentication token.
authtokentype = 'authtokentype_example' # str | Eco user authentication token type.
force_vote = true # bool | Force vote ignoring election process. (optional)
body = ecoserver.EcoWebServerDataTransferObjectsRunoffVoteDTO() # EcoWebServerDataTransferObjectsRunoffVoteDTO | The player's vote.  Must contain a ranked list of all candidates for the current election. (optional)

try:
    # Places a vote on behalf of the given player.  Can only be called if an election is currently running.
    api_instance.election_vote(authtoken, authtokentype, force_vote=force_vote, body=body)
except ApiException as e:
    print("Exception when calling ElectionApi->election_vote: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authtoken** | **str**| Eco user authentication token. | 
 **authtokentype** | **str**| Eco user authentication token type. | 
 **force_vote** | **bool**| Force vote ignoring election process. | [optional] 
 **body** | [**EcoWebServerDataTransferObjectsRunoffVoteDTO**](EcoWebServerDataTransferObjectsRunoffVoteDTO.md)| The player&#39;s vote.  Must contain a ranked list of all candidates for the current election. | [optional] 

### Return type

void (empty response body)

### Authorization

[authtoken](../README.md#authtoken), [authtokentype](../README.md#authtokentype)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **election_votes**
> list[EcoWebServerDataTransferObjectsRunoffVoteDTO] election_votes(authtoken, authtokentype, id=id)

Returns a list of votes that were made on the indicated election.

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
api_instance = ecoserver.ElectionApi(ecoserver.ApiClient(configuration))
authtoken = 'authtoken_example' # str | Eco user authentication token.
authtokentype = 'authtokentype_example' # str | Eco user authentication token type.
id = 56 # int |  (optional)

try:
    # Returns a list of votes that were made on the indicated election.
    api_response = api_instance.election_votes(authtoken, authtokentype, id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ElectionApi->election_votes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authtoken** | **str**| Eco user authentication token. | 
 **authtokentype** | **str**| Eco user authentication token type. | 
 **id** | **int**|  | [optional] 

### Return type

[**list[EcoWebServerDataTransferObjectsRunoffVoteDTO]**](EcoWebServerDataTransferObjectsRunoffVoteDTO.md)

### Authorization

[authtoken](../README.md#authtoken), [authtokentype](../README.md#authtokentype)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


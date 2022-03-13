# ecoserver.LogApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**log_get_all_logs**](LogApi.md#log_get_all_logs) | **GET** /api/v1/logs | Retrieves a list of all log files on the server.
[**log_get_category_logs**](LogApi.md#log_get_category_logs) | **GET** /api/v1/logs/{category} | Retrieves a list of all log files in the requested category subfolder if it exists.
[**log_get_log_file**](LogApi.md#log_get_log_file) | **GET** /api/v1/logs/get | Streams a log file over HTTP/HTTPS to a client.


# **log_get_all_logs**
> list[str] log_get_all_logs(authtoken, authtokentype)

Retrieves a list of all log files on the server.

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
api_instance = ecoserver.LogApi(ecoserver.ApiClient(configuration))
authtoken = 'authtoken_example' # str | Eco user authentication token.
authtokentype = 'authtokentype_example' # str | Eco user authentication token type.

try:
    # Retrieves a list of all log files on the server.
    api_response = api_instance.log_get_all_logs(authtoken, authtokentype)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LogApi->log_get_all_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authtoken** | **str**| Eco user authentication token. | 
 **authtokentype** | **str**| Eco user authentication token type. | 

### Return type

**list[str]**

### Authorization

[authtoken](../README.md#authtoken), [authtokentype](../README.md#authtokentype)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **log_get_category_logs**
> list[str] log_get_category_logs(category, authtoken, authtokentype)

Retrieves a list of all log files in the requested category subfolder if it exists.

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
api_instance = ecoserver.LogApi(ecoserver.ApiClient(configuration))
category = 'category_example' # str | Category log subfolder to search.
authtoken = 'authtoken_example' # str | Eco user authentication token.
authtokentype = 'authtokentype_example' # str | Eco user authentication token type.

try:
    # Retrieves a list of all log files in the requested category subfolder if it exists.
    api_response = api_instance.log_get_category_logs(category, authtoken, authtokentype)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LogApi->log_get_category_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | **str**| Category log subfolder to search. | 
 **authtoken** | **str**| Eco user authentication token. | 
 **authtokentype** | **str**| Eco user authentication token type. | 

### Return type

**list[str]**

### Authorization

[authtoken](../README.md#authtoken), [authtokentype](../README.md#authtokentype)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **log_get_log_file**
> log_get_log_file(authtoken, authtokentype, filepath=filepath)

Streams a log file over HTTP/HTTPS to a client.

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
api_instance = ecoserver.LogApi(ecoserver.ApiClient(configuration))
authtoken = 'authtoken_example' # str | Eco user authentication token.
authtokentype = 'authtokentype_example' # str | Eco user authentication token type.
filepath = 'filepath_example' # str | Filepath of the log file to stream. (optional)

try:
    # Streams a log file over HTTP/HTTPS to a client.
    api_instance.log_get_log_file(authtoken, authtokentype, filepath=filepath)
except ApiException as e:
    print("Exception when calling LogApi->log_get_log_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authtoken** | **str**| Eco user authentication token. | 
 **authtokentype** | **str**| Eco user authentication token type. | 
 **filepath** | **str**| Filepath of the log file to stream. | [optional] 

### Return type

void (empty response body)

### Authorization

[authtoken](../README.md#authtoken), [authtokentype](../README.md#authtokentype)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# ecoserver.ProfilingResultsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**profiling_results_download**](ProfilingResultsApi.md#profiling_results_download) | **GET** /api/v1/profiling-results/{filename} | 
[**profiling_results_list**](ProfilingResultsApi.md#profiling_results_list) | **GET** /api/v1/profiling-results | Returns the list of generated profiling results.


# **profiling_results_download**
> profiling_results_download(filename, authtoken, authtokentype)



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
api_instance = ecoserver.ProfilingResultsApi(ecoserver.ApiClient(configuration))
filename = 'filename_example' # str | 
authtoken = 'authtoken_example' # str | Eco user authentication token.
authtokentype = 'authtokentype_example' # str | Eco user authentication token type.

try:
    api_instance.profiling_results_download(filename, authtoken, authtokentype)
except ApiException as e:
    print("Exception when calling ProfilingResultsApi->profiling_results_download: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filename** | **str**|  | 
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

# **profiling_results_list**
> list[EcoWebServerDataTransferObjectsProfilingResultDTO] profiling_results_list(authtoken, authtokentype)

Returns the list of generated profiling results.

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
api_instance = ecoserver.ProfilingResultsApi(ecoserver.ApiClient(configuration))
authtoken = 'authtoken_example' # str | Eco user authentication token.
authtokentype = 'authtokentype_example' # str | Eco user authentication token type.

try:
    # Returns the list of generated profiling results.
    api_response = api_instance.profiling_results_list(authtoken, authtokentype)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfilingResultsApi->profiling_results_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authtoken** | **str**| Eco user authentication token. | 
 **authtokentype** | **str**| Eco user authentication token type. | 

### Return type

[**list[EcoWebServerDataTransferObjectsProfilingResultDTO]**](EcoWebServerDataTransferObjectsProfilingResultDTO.md)

### Authorization

[authtoken](../README.md#authtoken), [authtokentype](../README.md#authtokentype)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


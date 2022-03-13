# ecoserver.StatsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**stats_generate_test_data**](StatsApi.md#stats_generate_test_data) | **GET** /datasets/generatetestdata | Generates fake stat data for testing.
[**stats_get**](StatsApi.md#stats_get) | **GET** /datasets/get | /// Returns Eco.WebServer.Web.Controllers.StatsController.MaximumSamples data points between dayStart and dayEnd of the selected data.             If there are more than Eco.WebServer.Web.Controllers.StatsController.MaximumSamples samples, it will be averaged out to contain exactly Eco.WebServer.Web.Controllers.StatsController.MaximumSamples.///.
[**stats_get_flat_list**](StatsApi.md#stats_get_flat_list) | **GET** /datasets/flatlist | /// Returns all stat infos that contain data, formatted as a list, where each key is a list of strings. ///.
[**stats_get_list**](StatsApi.md#stats_get_list) | **GET** /datasets/getlist | Returns a \&quot;package\&quot; of multiple statistics in the order of their request.
[**stats_get_time_range**](StatsApi.md#stats_get_time_range) | **GET** /datasets/timerange | /// Returns the timerange of the simulation, in days///.
[**stats_get_tree_list**](StatsApi.md#stats_get_tree_list) | **GET** /datasets/treelist | Returns all dataset keys, formatted as a tree. ///.
[**stats_graphs**](StatsApi.md#stats_graphs) | **GET** /datasets/graphs | Returns the list of premade graphs to be displayed on the front page.


# **stats_generate_test_data**
> stats_generate_test_data(authtoken, authtokentype, days=days, users=users, generate_climate_data=generate_climate_data, pollution_multiplier=pollution_multiplier)

Generates fake stat data for testing.

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
api_instance = ecoserver.StatsApi(ecoserver.ApiClient(configuration))
authtoken = 'authtoken_example' # str | Eco user authentication token.
authtokentype = 'authtokentype_example' # str | Eco user authentication token type.
days = 3.4 # float | The number of days to simulate. (optional)
users = 56 # int | The number of users to simulate. (optional)
generate_climate_data = false # bool | Whether to generate climate data. Default is false. (optional) (default to false)
pollution_multiplier = 1 # float | How much pollution to generate. Default is 1. (optional) (default to 1)

try:
    # Generates fake stat data for testing.
    api_instance.stats_generate_test_data(authtoken, authtokentype, days=days, users=users, generate_climate_data=generate_climate_data, pollution_multiplier=pollution_multiplier)
except ApiException as e:
    print("Exception when calling StatsApi->stats_generate_test_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authtoken** | **str**| Eco user authentication token. | 
 **authtokentype** | **str**| Eco user authentication token type. | 
 **days** | **float**| The number of days to simulate. | [optional] 
 **users** | **int**| The number of users to simulate. | [optional] 
 **generate_climate_data** | **bool**| Whether to generate climate data. Default is false. | [optional] [default to false]
 **pollution_multiplier** | **float**| How much pollution to generate. Default is 1. | [optional] [default to 1]

### Return type

void (empty response body)

### Authorization

[authtoken](../README.md#authtoken), [authtokentype](../README.md#authtokentype)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stats_get**
> EcoWebServerWebControllersStatReturn stats_get(authtoken, authtokentype, dataset=dataset, day_start=day_start, day_end=day_end)

/// Returns Eco.WebServer.Web.Controllers.StatsController.MaximumSamples data points between dayStart and dayEnd of the selected data.             If there are more than Eco.WebServer.Web.Controllers.StatsController.MaximumSamples samples, it will be averaged out to contain exactly Eco.WebServer.Web.Controllers.StatsController.MaximumSamples.///.

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
api_instance = ecoserver.StatsApi(ecoserver.ApiClient(configuration))
authtoken = 'authtoken_example' # str | Eco user authentication token.
authtokentype = 'authtokentype_example' # str | Eco user authentication token type.
dataset = 'dataset_example' # str | dataset to take the data from. (optional)
day_start = 0 # float | Day from which on data is returned. Default is 0. (optional) (default to 0)
day_end = -1 # float | Day until which data is returned. Default is now. (optional) (default to -1)

try:
    # /// Returns Eco.WebServer.Web.Controllers.StatsController.MaximumSamples data points between dayStart and dayEnd of the selected data.             If there are more than Eco.WebServer.Web.Controllers.StatsController.MaximumSamples samples, it will be averaged out to contain exactly Eco.WebServer.Web.Controllers.StatsController.MaximumSamples.///.
    api_response = api_instance.stats_get(authtoken, authtokentype, dataset=dataset, day_start=day_start, day_end=day_end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->stats_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authtoken** | **str**| Eco user authentication token. | 
 **authtokentype** | **str**| Eco user authentication token type. | 
 **dataset** | **str**| dataset to take the data from. | [optional] 
 **day_start** | **float**| Day from which on data is returned. Default is 0. | [optional] [default to 0]
 **day_end** | **float**| Day until which data is returned. Default is now. | [optional] [default to -1]

### Return type

[**EcoWebServerWebControllersStatReturn**](EcoWebServerWebControllersStatReturn.md)

### Authorization

[authtoken](../README.md#authtoken), [authtokentype](../README.md#authtokentype)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stats_get_flat_list**
> list[EcoStatsStatInfo] stats_get_flat_list(authtoken, authtokentype)

/// Returns all stat infos that contain data, formatted as a list, where each key is a list of strings. ///.

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
api_instance = ecoserver.StatsApi(ecoserver.ApiClient(configuration))
authtoken = 'authtoken_example' # str | Eco user authentication token.
authtokentype = 'authtokentype_example' # str | Eco user authentication token type.

try:
    # /// Returns all stat infos that contain data, formatted as a list, where each key is a list of strings. ///.
    api_response = api_instance.stats_get_flat_list(authtoken, authtokentype)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->stats_get_flat_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authtoken** | **str**| Eco user authentication token. | 
 **authtokentype** | **str**| Eco user authentication token type. | 

### Return type

[**list[EcoStatsStatInfo]**](EcoStatsStatInfo.md)

### Authorization

[authtoken](../README.md#authtoken), [authtokentype](../README.md#authtokentype)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stats_get_list**
> list[EcoWebServerWebControllersStatReturn] stats_get_list(authtoken, authtokentype, requested_sets=requested_sets, day_start=day_start, day_end=day_end)

Returns a \"package\" of multiple statistics in the order of their request.

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
api_instance = ecoserver.StatsApi(ecoserver.ApiClient(configuration))
authtoken = 'authtoken_example' # str | Eco user authentication token.
authtokentype = 'authtokentype_example' # str | Eco user authentication token type.
requested_sets = ['requested_sets_example'] # list[str] | A list of statistics that should be returned. (optional)
day_start = 0 # float | Day from which the data should be taken from. Default is 0. (optional) (default to 0)
day_end = -1 # float | Day until which data is returned. Default is now. (optional) (default to -1)

try:
    # Returns a \"package\" of multiple statistics in the order of their request.
    api_response = api_instance.stats_get_list(authtoken, authtokentype, requested_sets=requested_sets, day_start=day_start, day_end=day_end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->stats_get_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authtoken** | **str**| Eco user authentication token. | 
 **authtokentype** | **str**| Eco user authentication token type. | 
 **requested_sets** | [**list[str]**](str.md)| A list of statistics that should be returned. | [optional] 
 **day_start** | **float**| Day from which the data should be taken from. Default is 0. | [optional] [default to 0]
 **day_end** | **float**| Day until which data is returned. Default is now. | [optional] [default to -1]

### Return type

[**list[EcoWebServerWebControllersStatReturn]**](EcoWebServerWebControllersStatReturn.md)

### Authorization

[authtoken](../README.md#authtoken), [authtokentype](../README.md#authtokentype)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stats_get_time_range**
> list[float] stats_get_time_range(authtoken, authtokentype)

/// Returns the timerange of the simulation, in days///.

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
api_instance = ecoserver.StatsApi(ecoserver.ApiClient(configuration))
authtoken = 'authtoken_example' # str | Eco user authentication token.
authtokentype = 'authtokentype_example' # str | Eco user authentication token type.

try:
    # /// Returns the timerange of the simulation, in days///.
    api_response = api_instance.stats_get_time_range(authtoken, authtokentype)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->stats_get_time_range: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authtoken** | **str**| Eco user authentication token. | 
 **authtokentype** | **str**| Eco user authentication token type. | 

### Return type

**list[float]**

### Authorization

[authtoken](../README.md#authtoken), [authtokentype](../README.md#authtokentype)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stats_get_tree_list**
> EcoStatsStatCategory stats_get_tree_list(authtoken, authtokentype)

Returns all dataset keys, formatted as a tree. ///.

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
api_instance = ecoserver.StatsApi(ecoserver.ApiClient(configuration))
authtoken = 'authtoken_example' # str | Eco user authentication token.
authtokentype = 'authtokentype_example' # str | Eco user authentication token type.

try:
    # Returns all dataset keys, formatted as a tree. ///.
    api_response = api_instance.stats_get_tree_list(authtoken, authtokentype)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->stats_get_tree_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authtoken** | **str**| Eco user authentication token. | 
 **authtokentype** | **str**| Eco user authentication token type. | 

### Return type

[**EcoStatsStatCategory**](EcoStatsStatCategory.md)

### Authorization

[authtoken](../README.md#authtoken), [authtokentype](../README.md#authtokentype)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stats_graphs**
> list[EcoStatsNamedGraph] stats_graphs(authtoken, authtokentype)

Returns the list of premade graphs to be displayed on the front page.

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
api_instance = ecoserver.StatsApi(ecoserver.ApiClient(configuration))
authtoken = 'authtoken_example' # str | Eco user authentication token.
authtokentype = 'authtokentype_example' # str | Eco user authentication token type.

try:
    # Returns the list of premade graphs to be displayed on the front page.
    api_response = api_instance.stats_graphs(authtoken, authtokentype)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->stats_graphs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authtoken** | **str**| Eco user authentication token. | 
 **authtokentype** | **str**| Eco user authentication token type. | 

### Return type

[**list[EcoStatsNamedGraph]**](EcoStatsNamedGraph.md)

### Authorization

[authtoken](../README.md#authtoken), [authtokentype](../README.md#authtokentype)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


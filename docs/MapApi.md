# ecoserver.MapApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**map_entities**](MapApi.md#map_entities) | **GET** /api/v1/map/entities | Allows access to all entities currently available in the simulation.
[**map_entity_types**](MapApi.md#map_entity_types) | **GET** /api/v1/map/entitytypes | Allows access to all species currently available in the simulation.
[**map_get_dimension**](MapApi.md#map_get_dimension) | **GET** /api/v1/map/dimension | Returns the dimension of the world, in blocks.
[**map_get_property**](MapApi.md#map_get_property) | **GET** /api/v1/map/property | 
[**map_layer_list**](MapApi.md#map_layer_list) | **GET** /api/v1/map/layerList | List Layer Names.
[**map_make_map_json**](MapApi.md#map_make_map_json) | **GET** /api/v1/map/map.json | One request to get all required web map data.
[**map_map_stats**](MapApi.md#map_map_stats) | **GET** /api/v1/map/mapstats | 
[**map_water_level**](MapApi.md#map_water_level) | **GET** /api/v1/map/waterLevel | Get water height.


# **map_entities**
> list[EcoWebServerDataTransferObjectsEntityDTO] map_entities(authtoken, authtokentype, entity_types=entity_types, states=states)

Allows access to all entities currently available in the simulation.

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
api_instance = ecoserver.MapApi(ecoserver.ApiClient(configuration))
authtoken = 'authtoken_example' # str | Eco user authentication token.
authtokentype = 'authtokentype_example' # str | Eco user authentication token type.
entity_types = ['entity_types_example'] # list[str] | A list of user type names that will be used to filter the response. (optional)
states = ['states_example'] # list[str] | A list of Animal states that will be used to filter the response. (optional)

try:
    # Allows access to all entities currently available in the simulation.
    api_response = api_instance.map_entities(authtoken, authtokentype, entity_types=entity_types, states=states)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MapApi->map_entities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authtoken** | **str**| Eco user authentication token. | 
 **authtokentype** | **str**| Eco user authentication token type. | 
 **entity_types** | [**list[str]**](str.md)| A list of user type names that will be used to filter the response. | [optional] 
 **states** | [**list[str]**](str.md)| A list of Animal states that will be used to filter the response. | [optional] 

### Return type

[**list[EcoWebServerDataTransferObjectsEntityDTO]**](EcoWebServerDataTransferObjectsEntityDTO.md)

### Authorization

[authtoken](../README.md#authtoken), [authtokentype](../README.md#authtokentype)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_entity_types**
> list[str] map_entity_types(authtoken, authtokentype)

Allows access to all species currently available in the simulation.

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
api_instance = ecoserver.MapApi(ecoserver.ApiClient(configuration))
authtoken = 'authtoken_example' # str | Eco user authentication token.
authtokentype = 'authtokentype_example' # str | Eco user authentication token type.

try:
    # Allows access to all species currently available in the simulation.
    api_response = api_instance.map_entity_types(authtoken, authtokentype)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MapApi->map_entity_types: %s\n" % e)
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

# **map_get_dimension**
> EcoSharedMathVector3i map_get_dimension(authtoken, authtokentype)

Returns the dimension of the world, in blocks.

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
api_instance = ecoserver.MapApi(ecoserver.ApiClient(configuration))
authtoken = 'authtoken_example' # str | Eco user authentication token.
authtokentype = 'authtokentype_example' # str | Eco user authentication token type.

try:
    # Returns the dimension of the world, in blocks.
    api_response = api_instance.map_get_dimension(authtoken, authtokentype)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MapApi->map_get_dimension: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authtoken** | **str**| Eco user authentication token. | 
 **authtokentype** | **str**| Eco user authentication token type. | 

### Return type

[**EcoSharedMathVector3i**](EcoSharedMathVector3i.md)

### Authorization

[authtoken](../README.md#authtoken), [authtokentype](../README.md#authtokentype)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_get_property**
> map_get_property(authtoken, authtokentype)



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
api_instance = ecoserver.MapApi(ecoserver.ApiClient(configuration))
authtoken = 'authtoken_example' # str | Eco user authentication token.
authtokentype = 'authtokentype_example' # str | Eco user authentication token type.

try:
    api_instance.map_get_property(authtoken, authtokentype)
except ApiException as e:
    print("Exception when calling MapApi->map_get_property: %s\n" % e)
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

# **map_layer_list**
> list[str] map_layer_list(authtoken, authtokentype)

List Layer Names.

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
api_instance = ecoserver.MapApi(ecoserver.ApiClient(configuration))
authtoken = 'authtoken_example' # str | Eco user authentication token.
authtokentype = 'authtokentype_example' # str | Eco user authentication token type.

try:
    # List Layer Names.
    api_response = api_instance.map_layer_list(authtoken, authtokentype)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MapApi->map_layer_list: %s\n" % e)
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

# **map_make_map_json**
> map_make_map_json(authtoken, authtokentype)

One request to get all required web map data.

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
api_instance = ecoserver.MapApi(ecoserver.ApiClient(configuration))
authtoken = 'authtoken_example' # str | Eco user authentication token.
authtokentype = 'authtokentype_example' # str | Eco user authentication token type.

try:
    # One request to get all required web map data.
    api_instance.map_make_map_json(authtoken, authtokentype)
except ApiException as e:
    print("Exception when calling MapApi->map_make_map_json: %s\n" % e)
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

# **map_map_stats**
> EcoWebServerDataTransferObjectsMapStats map_map_stats(authtoken, authtokentype)



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
api_instance = ecoserver.MapApi(ecoserver.ApiClient(configuration))
authtoken = 'authtoken_example' # str | Eco user authentication token.
authtokentype = 'authtokentype_example' # str | Eco user authentication token type.

try:
    api_response = api_instance.map_map_stats(authtoken, authtokentype)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MapApi->map_map_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authtoken** | **str**| Eco user authentication token. | 
 **authtokentype** | **str**| Eco user authentication token type. | 

### Return type

[**EcoWebServerDataTransferObjectsMapStats**](EcoWebServerDataTransferObjectsMapStats.md)

### Authorization

[authtoken](../README.md#authtoken), [authtokentype](../README.md#authtokentype)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_water_level**
> float map_water_level(authtoken, authtokentype)

Get water height.

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
api_instance = ecoserver.MapApi(ecoserver.ApiClient(configuration))
authtoken = 'authtoken_example' # str | Eco user authentication token.
authtokentype = 'authtokentype_example' # str | Eco user authentication token type.

try:
    # Get water height.
    api_response = api_instance.map_water_level(authtoken, authtokentype)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MapApi->map_water_level: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authtoken** | **str**| Eco user authentication token. | 
 **authtokentype** | **str**| Eco user authentication token type. | 

### Return type

**float**

### Authorization

[authtoken](../README.md#authtoken), [authtokentype](../README.md#authtokentype)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


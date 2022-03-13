# ecoserver.WorldLayerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**world_layer_area_description**](WorldLayerApi.md#world_layer_area_description) | **GET** /api/v1/worldlayers/relationships/areadescription | Describes the area selected with a string.
[**world_layer_list_layers**](WorldLayerApi.md#world_layer_list_layers) | **GET** /api/v1/worldlayers/layers | Enumerates every world layer in the simulation.
[**world_layer_list_relevant_layers**](WorldLayerApi.md#world_layer_list_relevant_layers) | **GET** /api/v1/worldlayers/layers/{focusLayer} | Enumerates the layers that should be displayed when the user is focused on a particular layer and world area.
[**world_layer_list_relevant_relationships**](WorldLayerApi.md#world_layer_list_relevant_relationships) | **GET** /api/v1/worldlayers/relationships/{focusLayer} | Enumerates the layer relationships that should be displayed when the user is focused on a particular layer and world area.


# **world_layer_area_description**
> str world_layer_area_description(authtoken, authtokentype, min_x=min_x, min_y=min_y, max_x=max_x, max_y=max_y)

Describes the area selected with a string.

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
api_instance = ecoserver.WorldLayerApi(ecoserver.ApiClient(configuration))
authtoken = 'authtoken_example' # str | Eco user authentication token.
authtokentype = 'authtokentype_example' # str | Eco user authentication token type.
min_x = -1 # float | The least x boundary of the viewed area, in world coordinates.  Should not be wrapped. (optional) (default to -1)
min_y = -1 # float | The least y boundary of the viewed area, in world coordinates.  Should not be wrapped. (optional) (default to -1)
max_x = -1 # float | The greatest x boundary of the viewed area, in world coordinates.  Should not be wrapped. (optional) (default to -1)
max_y = -1 # float | The greatest y boundary of the viewed area, in world coordinates.  Should not be wrapped. (optional) (default to -1)

try:
    # Describes the area selected with a string.
    api_response = api_instance.world_layer_area_description(authtoken, authtokentype, min_x=min_x, min_y=min_y, max_x=max_x, max_y=max_y)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorldLayerApi->world_layer_area_description: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authtoken** | **str**| Eco user authentication token. | 
 **authtokentype** | **str**| Eco user authentication token type. | 
 **min_x** | **float**| The least x boundary of the viewed area, in world coordinates.  Should not be wrapped. | [optional] [default to -1]
 **min_y** | **float**| The least y boundary of the viewed area, in world coordinates.  Should not be wrapped. | [optional] [default to -1]
 **max_x** | **float**| The greatest x boundary of the viewed area, in world coordinates.  Should not be wrapped. | [optional] [default to -1]
 **max_y** | **float**| The greatest y boundary of the viewed area, in world coordinates.  Should not be wrapped. | [optional] [default to -1]

### Return type

**str**

### Authorization

[authtoken](../README.md#authtoken), [authtokentype](../README.md#authtokentype)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **world_layer_list_layers**
> list[EcoWebServerDataTransferObjectsWorldLayersWorldLayerGroupDTO] world_layer_list_layers(authtoken, authtokentype)

Enumerates every world layer in the simulation.

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
api_instance = ecoserver.WorldLayerApi(ecoserver.ApiClient(configuration))
authtoken = 'authtoken_example' # str | Eco user authentication token.
authtokentype = 'authtokentype_example' # str | Eco user authentication token type.

try:
    # Enumerates every world layer in the simulation.
    api_response = api_instance.world_layer_list_layers(authtoken, authtokentype)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorldLayerApi->world_layer_list_layers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authtoken** | **str**| Eco user authentication token. | 
 **authtokentype** | **str**| Eco user authentication token type. | 

### Return type

[**list[EcoWebServerDataTransferObjectsWorldLayersWorldLayerGroupDTO]**](EcoWebServerDataTransferObjectsWorldLayersWorldLayerGroupDTO.md)

### Authorization

[authtoken](../README.md#authtoken), [authtokentype](../README.md#authtokentype)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **world_layer_list_relevant_layers**
> list[EcoWebServerDataTransferObjectsWorldLayersWorldLayerDTO] world_layer_list_relevant_layers(focus_layer, authtoken, authtokentype, min_x=min_x, min_y=min_y, max_x=max_x, max_y=max_y)

Enumerates the layers that should be displayed when the user is focused on a particular layer and world area.

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
api_instance = ecoserver.WorldLayerApi(ecoserver.ApiClient(configuration))
focus_layer = 'focus_layer_example' # str | Name of the layer we're querying.
authtoken = 'authtoken_example' # str | Eco user authentication token.
authtokentype = 'authtokentype_example' # str | Eco user authentication token type.
min_x = -1 # float | The least x boundary of the viewed area, in world coordinates.  Should not be wrapped. (optional) (default to -1)
min_y = -1 # float | The least y boundary of the viewed area, in world coordinates.  Should not be wrapped. (optional) (default to -1)
max_x = -1 # float | The greatest x boundary of the viewed area, in world coordinates.  Should not be wrapped. (optional) (default to -1)
max_y = -1 # float | The greatest y boundary of the viewed area, in world coordinates.  Should not be wrapped. (optional) (default to -1)

try:
    # Enumerates the layers that should be displayed when the user is focused on a particular layer and world area.
    api_response = api_instance.world_layer_list_relevant_layers(focus_layer, authtoken, authtokentype, min_x=min_x, min_y=min_y, max_x=max_x, max_y=max_y)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorldLayerApi->world_layer_list_relevant_layers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **focus_layer** | **str**| Name of the layer we&#39;re querying. | 
 **authtoken** | **str**| Eco user authentication token. | 
 **authtokentype** | **str**| Eco user authentication token type. | 
 **min_x** | **float**| The least x boundary of the viewed area, in world coordinates.  Should not be wrapped. | [optional] [default to -1]
 **min_y** | **float**| The least y boundary of the viewed area, in world coordinates.  Should not be wrapped. | [optional] [default to -1]
 **max_x** | **float**| The greatest x boundary of the viewed area, in world coordinates.  Should not be wrapped. | [optional] [default to -1]
 **max_y** | **float**| The greatest y boundary of the viewed area, in world coordinates.  Should not be wrapped. | [optional] [default to -1]

### Return type

[**list[EcoWebServerDataTransferObjectsWorldLayersWorldLayerDTO]**](EcoWebServerDataTransferObjectsWorldLayersWorldLayerDTO.md)

### Authorization

[authtoken](../README.md#authtoken), [authtokentype](../README.md#authtokentype)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **world_layer_list_relevant_relationships**
> list[EcoWebServerDataTransferObjectsWorldLayersLayerRelationshipDTO] world_layer_list_relevant_relationships(focus_layer, authtoken, authtokentype, min_x=min_x, min_y=min_y, max_x=max_x, max_y=max_y)

Enumerates the layer relationships that should be displayed when the user is focused on a particular layer and world area.

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
api_instance = ecoserver.WorldLayerApi(ecoserver.ApiClient(configuration))
focus_layer = 'focus_layer_example' # str | The name of the focused layer.
authtoken = 'authtoken_example' # str | Eco user authentication token.
authtokentype = 'authtokentype_example' # str | Eco user authentication token type.
min_x = -1 # float | The least x boundary of the viewed area, in world coordinates.  Should not be wrapped. (optional) (default to -1)
min_y = -1 # float | The least y boundary of the viewed area, in world coordinates.  Should not be wrapped. (optional) (default to -1)
max_x = -1 # float | The greatest x boundary of the viewed area, in world coordinates.  Should not be wrapped. (optional) (default to -1)
max_y = -1 # float | The greatest y boundary of the viewed area, in world coordinates.  Should not be wrapped. (optional) (default to -1)

try:
    # Enumerates the layer relationships that should be displayed when the user is focused on a particular layer and world area.
    api_response = api_instance.world_layer_list_relevant_relationships(focus_layer, authtoken, authtokentype, min_x=min_x, min_y=min_y, max_x=max_x, max_y=max_y)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorldLayerApi->world_layer_list_relevant_relationships: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **focus_layer** | **str**| The name of the focused layer. | 
 **authtoken** | **str**| Eco user authentication token. | 
 **authtokentype** | **str**| Eco user authentication token type. | 
 **min_x** | **float**| The least x boundary of the viewed area, in world coordinates.  Should not be wrapped. | [optional] [default to -1]
 **min_y** | **float**| The least y boundary of the viewed area, in world coordinates.  Should not be wrapped. | [optional] [default to -1]
 **max_x** | **float**| The greatest x boundary of the viewed area, in world coordinates.  Should not be wrapped. | [optional] [default to -1]
 **max_y** | **float**| The greatest y boundary of the viewed area, in world coordinates.  Should not be wrapped. | [optional] [default to -1]

### Return type

[**list[EcoWebServerDataTransferObjectsWorldLayersLayerRelationshipDTO]**](EcoWebServerDataTransferObjectsWorldLayersLayerRelationshipDTO.md)

### Authorization

[authtoken](../README.md#authtoken), [authtokentype](../README.md#authtokentype)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


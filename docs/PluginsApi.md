# ecoserver.PluginsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**plugins_get_plugin_config**](PluginsApi.md#plugins_get_plugin_config) | **GET** /api/v1/plugins/{name} | 
[**plugins_get_plugins**](PluginsApi.md#plugins_get_plugins) | **GET** /api/v1/plugins | Gets the list and status of all running plugins on the server.
[**plugins_post_plugin_config**](PluginsApi.md#plugins_post_plugin_config) | **POST** /api/v1/plugins/{name} | Sets the configuration options for the given plugin.


# **plugins_get_plugin_config**
> plugins_get_plugin_config(name, authtoken, authtokentype)



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
api_instance = ecoserver.PluginsApi(ecoserver.ApiClient(configuration))
name = 'name_example' # str | 
authtoken = 'authtoken_example' # str | Eco user authentication token.
authtokentype = 'authtokentype_example' # str | Eco user authentication token type.

try:
    api_instance.plugins_get_plugin_config(name, authtoken, authtokentype)
except ApiException as e:
    print("Exception when calling PluginsApi->plugins_get_plugin_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
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

# **plugins_get_plugins**
> list[EcoWebServerDataTransferObjectsPluginInfo] plugins_get_plugins()

Gets the list and status of all running plugins on the server.

### Example
```python
from __future__ import print_function
import time
import ecoserver
from ecoserver.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ecoserver.PluginsApi()

try:
    # Gets the list and status of all running plugins on the server.
    api_response = api_instance.plugins_get_plugins()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PluginsApi->plugins_get_plugins: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[EcoWebServerDataTransferObjectsPluginInfo]**](EcoWebServerDataTransferObjectsPluginInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **plugins_post_plugin_config**
> plugins_post_plugin_config(name, authtoken, authtokentype, body=body)

Sets the configuration options for the given plugin.

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
api_instance = ecoserver.PluginsApi(ecoserver.ApiClient(configuration))
name = 'name_example' # str | The name of the plugin.
authtoken = 'authtoken_example' # str | Eco user authentication token.
authtokentype = 'authtokentype_example' # str | Eco user authentication token type.
body = NULL # object | New plugin config. (optional)

try:
    # Sets the configuration options for the given plugin.
    api_instance.plugins_post_plugin_config(name, authtoken, authtokentype, body=body)
except ApiException as e:
    print("Exception when calling PluginsApi->plugins_post_plugin_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the plugin. | 
 **authtoken** | **str**| Eco user authentication token. | 
 **authtokentype** | **str**| Eco user authentication token type. | 
 **body** | **object**| New plugin config. | [optional] 

### Return type

void (empty response body)

### Authorization

[authtoken](../README.md#authtoken), [authtokentype](../README.md#authtokentype)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


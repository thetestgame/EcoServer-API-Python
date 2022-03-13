# ecoserver.AdminApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_get_get_access**](AdminApi.md#admin_get_get_access) | **GET** /api/v1/admin/get/access | 
[**admin_get_get_server_name**](AdminApi.md#admin_get_get_server_name) | **GET** /api/v1/admin/get/servername | 
[**admin_post_game_export**](AdminApi.md#admin_post_game_export) | **POST** /api/v1/admin/game/export | 
[**admin_post_set_access**](AdminApi.md#admin_post_set_access) | **POST** /api/v1/admin/set/access | Sets how accessible this server is.
[**admin_post_set_server_name**](AdminApi.md#admin_post_set_server_name) | **POST** /api/v1/admin/set/servername | 


# **admin_get_get_access**
> str admin_get_get_access(authtoken, authtokentype)



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
api_instance = ecoserver.AdminApi(ecoserver.ApiClient(configuration))
authtoken = 'authtoken_example' # str | Eco user authentication token.
authtokentype = 'authtokentype_example' # str | Eco user authentication token type.

try:
    api_response = api_instance.admin_get_get_access(authtoken, authtokentype)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->admin_get_get_access: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authtoken** | **str**| Eco user authentication token. | 
 **authtokentype** | **str**| Eco user authentication token type. | 

### Return type

**str**

### Authorization

[authtoken](../README.md#authtoken), [authtokentype](../README.md#authtokentype)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_get_get_server_name**
> str admin_get_get_server_name()



### Example
```python
from __future__ import print_function
import time
import ecoserver
from ecoserver.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ecoserver.AdminApi()

try:
    api_response = api_instance.admin_get_get_server_name()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->admin_get_get_server_name: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_post_game_export**
> EcoWebServerWebModelsAdminReturnModel admin_post_game_export(authtoken, authtokentype, body=body)



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
api_instance = ecoserver.AdminApi(ecoserver.ApiClient(configuration))
authtoken = 'authtoken_example' # str | Eco user authentication token.
authtokentype = 'authtokentype_example' # str | Eco user authentication token type.
body = ecoserver.EcoWebServerWebModelsExportGameModel() # EcoWebServerWebModelsExportGameModel |  (optional)

try:
    api_response = api_instance.admin_post_game_export(authtoken, authtokentype, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->admin_post_game_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authtoken** | **str**| Eco user authentication token. | 
 **authtokentype** | **str**| Eco user authentication token type. | 
 **body** | [**EcoWebServerWebModelsExportGameModel**](EcoWebServerWebModelsExportGameModel.md)|  | [optional] 

### Return type

[**EcoWebServerWebModelsAdminReturnModel**](EcoWebServerWebModelsAdminReturnModel.md)

### Authorization

[authtoken](../README.md#authtoken), [authtokentype](../README.md#authtokentype)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_post_set_access**
> admin_post_set_access(authtoken, authtokentype, value=value, password=password)

Sets how accessible this server is.

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
api_instance = ecoserver.AdminApi(ecoserver.ApiClient(configuration))
authtoken = 'authtoken_example' # str | Eco user authentication token.
authtokentype = 'authtokentype_example' # str | Eco user authentication token type.
value = 'value_example' # str | Can be 'public' (listed in server browser, no password), 'private' (listed in server browser, with password) or 'hidden' (unlisted, without password). (optional)
password = 'password_example' # str | If setting private, must set a password. If not set to private, this is unused. (optional)

try:
    # Sets how accessible this server is.
    api_instance.admin_post_set_access(authtoken, authtokentype, value=value, password=password)
except ApiException as e:
    print("Exception when calling AdminApi->admin_post_set_access: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authtoken** | **str**| Eco user authentication token. | 
 **authtokentype** | **str**| Eco user authentication token type. | 
 **value** | **str**| Can be &#39;public&#39; (listed in server browser, no password), &#39;private&#39; (listed in server browser, with password) or &#39;hidden&#39; (unlisted, without password). | [optional] 
 **password** | **str**| If setting private, must set a password. If not set to private, this is unused. | [optional] 

### Return type

void (empty response body)

### Authorization

[authtoken](../README.md#authtoken), [authtokentype](../README.md#authtokentype)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_post_set_server_name**
> admin_post_set_server_name(authtoken, authtokentype, name=name)



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
api_instance = ecoserver.AdminApi(ecoserver.ApiClient(configuration))
authtoken = 'authtoken_example' # str | Eco user authentication token.
authtokentype = 'authtokentype_example' # str | Eco user authentication token type.
name = 'name_example' # str |  (optional)

try:
    api_instance.admin_post_set_server_name(authtoken, authtokentype, name=name)
except ApiException as e:
    print("Exception when calling AdminApi->admin_post_set_server_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authtoken** | **str**| Eco user authentication token. | 
 **authtokentype** | **str**| Eco user authentication token type. | 
 **name** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[authtoken](../README.md#authtoken), [authtokentype](../README.md#authtokentype)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


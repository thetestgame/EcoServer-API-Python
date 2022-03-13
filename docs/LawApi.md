# ecoserver.LawApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**law_generate_test_data**](LawApi.md#law_generate_test_data) | **POST** /api/v1/laws/generatetestdata | Genereate test laws.
[**law_get_district_map**](LawApi.md#law_get_district_map) | **GET** /api/v1/laws/districtmap/{name} | 
[**law_get_law**](LawApi.md#law_get_law) | **GET** /api/v1/laws/{id} | Returns the law with the specified id.
[**law_list**](LawApi.md#law_list) | **GET** /api/v1/laws/byStates/{states} | Returns all laws currently present in the game in the specified states, active by default.
[**law_list_all**](LawApi.md#law_list_all) | **GET** /api/v1/laws | Returns all laws currently present in the game


# **law_generate_test_data**
> law_generate_test_data(authtoken, authtokentype)

Genereate test laws.

> This endpoint can only be invoked by a DevTier user.

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
api_instance = ecoserver.LawApi(ecoserver.ApiClient(configuration))
authtoken = 'authtoken_example' # str | Eco user authentication token.
authtokentype = 'authtokentype_example' # str | Eco user authentication token type.

try:
    # Genereate test laws.
    api_instance.law_generate_test_data(authtoken, authtokentype)
except ApiException as e:
    print("Exception when calling LawApi->law_generate_test_data: %s\n" % e)
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

# **law_get_district_map**
> EcoWebServerDataTransferObjectsDistrictMapDTO law_get_district_map(name, authtoken, authtokentype)



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
api_instance = ecoserver.LawApi(ecoserver.ApiClient(configuration))
name = 'name_example' # str | 
authtoken = 'authtoken_example' # str | Eco user authentication token.
authtokentype = 'authtokentype_example' # str | Eco user authentication token type.

try:
    api_response = api_instance.law_get_district_map(name, authtoken, authtokentype)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LawApi->law_get_district_map: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **authtoken** | **str**| Eco user authentication token. | 
 **authtokentype** | **str**| Eco user authentication token type. | 

### Return type

[**EcoWebServerDataTransferObjectsDistrictMapDTO**](EcoWebServerDataTransferObjectsDistrictMapDTO.md)

### Authorization

[authtoken](../README.md#authtoken), [authtokentype](../README.md#authtokentype)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **law_get_law**
> EcoWebServerDataTransferObjectsLawDTO law_get_law(id, authtoken, authtokentype)

Returns the law with the specified id.

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
api_instance = ecoserver.LawApi(ecoserver.ApiClient(configuration))
id = 56 # int | 
authtoken = 'authtoken_example' # str | Eco user authentication token.
authtokentype = 'authtokentype_example' # str | Eco user authentication token type.

try:
    # Returns the law with the specified id.
    api_response = api_instance.law_get_law(id, authtoken, authtokentype)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LawApi->law_get_law: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **authtoken** | **str**| Eco user authentication token. | 
 **authtokentype** | **str**| Eco user authentication token type. | 

### Return type

[**EcoWebServerDataTransferObjectsLawDTO**](EcoWebServerDataTransferObjectsLawDTO.md)

### Authorization

[authtoken](../README.md#authtoken), [authtokentype](../README.md#authtokentype)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **law_list**
> list[EcoWebServerDataTransferObjectsLawDTO] law_list(states, authtoken, authtokentype)

Returns all laws currently present in the game in the specified states, active by default.

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
api_instance = ecoserver.LawApi(ecoserver.ApiClient(configuration))
states = 'states_example' # str | 
authtoken = 'authtoken_example' # str | Eco user authentication token.
authtokentype = 'authtokentype_example' # str | Eco user authentication token type.

try:
    # Returns all laws currently present in the game in the specified states, active by default.
    api_response = api_instance.law_list(states, authtoken, authtokentype)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LawApi->law_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **states** | **str**|  | 
 **authtoken** | **str**| Eco user authentication token. | 
 **authtokentype** | **str**| Eco user authentication token type. | 

### Return type

[**list[EcoWebServerDataTransferObjectsLawDTO]**](EcoWebServerDataTransferObjectsLawDTO.md)

### Authorization

[authtoken](../README.md#authtoken), [authtokentype](../README.md#authtokentype)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **law_list_all**
> list[EcoWebServerDataTransferObjectsLawDTO] law_list_all(authtoken, authtokentype)

Returns all laws currently present in the game

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
api_instance = ecoserver.LawApi(ecoserver.ApiClient(configuration))
authtoken = 'authtoken_example' # str | Eco user authentication token.
authtokentype = 'authtokentype_example' # str | Eco user authentication token type.

try:
    # Returns all laws currently present in the game
    api_response = api_instance.law_list_all(authtoken, authtokentype)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LawApi->law_list_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authtoken** | **str**| Eco user authentication token. | 
 **authtokentype** | **str**| Eco user authentication token type. | 

### Return type

[**list[EcoWebServerDataTransferObjectsLawDTO]**](EcoWebServerDataTransferObjectsLawDTO.md)

### Authorization

[authtoken](../README.md#authtoken), [authtokentype](../README.md#authtokentype)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


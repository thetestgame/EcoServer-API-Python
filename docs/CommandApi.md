# ecoserver.CommandApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**command_exec_command**](CommandApi.md#command_exec_command) | **POST** /api/v1/command/exec | Executes a chat command on the server.


# **command_exec_command**
> EcoWebServerDataTransferObjectsCommandResultDTO command_exec_command(authtoken, authtokentype, body=body)

Executes a chat command on the server.

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
api_instance = ecoserver.CommandApi(ecoserver.ApiClient(configuration))
authtoken = 'authtoken_example' # str | Eco user authentication token.
authtokentype = 'authtokentype_example' # str | Eco user authentication token type.
body = ecoserver.EcoWebServerDataTransferObjectsExecuteCommandDTO() # EcoWebServerDataTransferObjectsExecuteCommandDTO |  (optional)

try:
    # Executes a chat command on the server.
    api_response = api_instance.command_exec_command(authtoken, authtokentype, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommandApi->command_exec_command: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authtoken** | **str**| Eco user authentication token. | 
 **authtokentype** | **str**| Eco user authentication token type. | 
 **body** | [**EcoWebServerDataTransferObjectsExecuteCommandDTO**](EcoWebServerDataTransferObjectsExecuteCommandDTO.md)|  | [optional] 

### Return type

[**EcoWebServerDataTransferObjectsCommandResultDTO**](EcoWebServerDataTransferObjectsCommandResultDTO.md)

### Authorization

[authtoken](../README.md#authtoken), [authtokentype](../README.md#authtokentype)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


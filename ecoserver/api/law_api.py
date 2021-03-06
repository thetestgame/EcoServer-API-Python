# coding: utf-8

"""
    Eco Game API

    First API draft for Eco. Heavy work in progress and subject to changes.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from ecoserver.api_client import ApiClient


class LawApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def law_generate_test_data(self, authtoken, authtokentype, **kwargs):  # noqa: E501
        """Genereate test laws.  # noqa: E501

        > This endpoint can only be invoked by a DevTier user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.law_generate_test_data(authtoken, authtokentype, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authtoken: Eco user authentication token. (required)
        :param str authtokentype: Eco user authentication token type. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.law_generate_test_data_with_http_info(authtoken, authtokentype, **kwargs)  # noqa: E501
        else:
            (data) = self.law_generate_test_data_with_http_info(authtoken, authtokentype, **kwargs)  # noqa: E501
            return data

    def law_generate_test_data_with_http_info(self, authtoken, authtokentype, **kwargs):  # noqa: E501
        """Genereate test laws.  # noqa: E501

        > This endpoint can only be invoked by a DevTier user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.law_generate_test_data_with_http_info(authtoken, authtokentype, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authtoken: Eco user authentication token. (required)
        :param str authtokentype: Eco user authentication token type. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authtoken', 'authtokentype']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method law_generate_test_data" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authtoken' is set
        if self.api_client.client_side_validation and ('authtoken' not in params or
                                                       params['authtoken'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `authtoken` when calling `law_generate_test_data`")  # noqa: E501
        # verify the required parameter 'authtokentype' is set
        if self.api_client.client_side_validation and ('authtokentype' not in params or
                                                       params['authtokentype'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `authtokentype` when calling `law_generate_test_data`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'authtoken' in params:
            query_params.append(('authtoken', params['authtoken']))  # noqa: E501
        if 'authtokentype' in params:
            query_params.append(('authtokentype', params['authtokentype']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['authtoken', 'authtokentype']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/laws/generatetestdata', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def law_get_district_map(self, name, authtoken, authtokentype, **kwargs):  # noqa: E501
        """law_get_district_map  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.law_get_district_map(name, authtoken, authtokentype, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: (required)
        :param str authtoken: Eco user authentication token. (required)
        :param str authtokentype: Eco user authentication token type. (required)
        :return: EcoWebServerDataTransferObjectsDistrictMapDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.law_get_district_map_with_http_info(name, authtoken, authtokentype, **kwargs)  # noqa: E501
        else:
            (data) = self.law_get_district_map_with_http_info(name, authtoken, authtokentype, **kwargs)  # noqa: E501
            return data

    def law_get_district_map_with_http_info(self, name, authtoken, authtokentype, **kwargs):  # noqa: E501
        """law_get_district_map  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.law_get_district_map_with_http_info(name, authtoken, authtokentype, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: (required)
        :param str authtoken: Eco user authentication token. (required)
        :param str authtokentype: Eco user authentication token type. (required)
        :return: EcoWebServerDataTransferObjectsDistrictMapDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'authtoken', 'authtokentype']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method law_get_district_map" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if self.api_client.client_side_validation and ('name' not in params or
                                                       params['name'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `name` when calling `law_get_district_map`")  # noqa: E501
        # verify the required parameter 'authtoken' is set
        if self.api_client.client_side_validation and ('authtoken' not in params or
                                                       params['authtoken'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `authtoken` when calling `law_get_district_map`")  # noqa: E501
        # verify the required parameter 'authtokentype' is set
        if self.api_client.client_side_validation and ('authtokentype' not in params or
                                                       params['authtokentype'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `authtokentype` when calling `law_get_district_map`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501

        query_params = []
        if 'authtoken' in params:
            query_params.append(('authtoken', params['authtoken']))  # noqa: E501
        if 'authtokentype' in params:
            query_params.append(('authtokentype', params['authtokentype']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['authtoken', 'authtokentype']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/laws/districtmap/{name}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EcoWebServerDataTransferObjectsDistrictMapDTO',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def law_get_law(self, id, authtoken, authtokentype, **kwargs):  # noqa: E501
        """Returns the law with the specified id.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.law_get_law(id, authtoken, authtokentype, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: (required)
        :param str authtoken: Eco user authentication token. (required)
        :param str authtokentype: Eco user authentication token type. (required)
        :return: EcoWebServerDataTransferObjectsLawDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.law_get_law_with_http_info(id, authtoken, authtokentype, **kwargs)  # noqa: E501
        else:
            (data) = self.law_get_law_with_http_info(id, authtoken, authtokentype, **kwargs)  # noqa: E501
            return data

    def law_get_law_with_http_info(self, id, authtoken, authtokentype, **kwargs):  # noqa: E501
        """Returns the law with the specified id.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.law_get_law_with_http_info(id, authtoken, authtokentype, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: (required)
        :param str authtoken: Eco user authentication token. (required)
        :param str authtokentype: Eco user authentication token type. (required)
        :return: EcoWebServerDataTransferObjectsLawDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'authtoken', 'authtokentype']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method law_get_law" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `law_get_law`")  # noqa: E501
        # verify the required parameter 'authtoken' is set
        if self.api_client.client_side_validation and ('authtoken' not in params or
                                                       params['authtoken'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `authtoken` when calling `law_get_law`")  # noqa: E501
        # verify the required parameter 'authtokentype' is set
        if self.api_client.client_side_validation and ('authtokentype' not in params or
                                                       params['authtokentype'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `authtokentype` when calling `law_get_law`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'authtoken' in params:
            query_params.append(('authtoken', params['authtoken']))  # noqa: E501
        if 'authtokentype' in params:
            query_params.append(('authtokentype', params['authtokentype']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['authtoken', 'authtokentype']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/laws/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EcoWebServerDataTransferObjectsLawDTO',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def law_list(self, states, authtoken, authtokentype, **kwargs):  # noqa: E501
        """Returns all laws currently present in the game in the specified states, active by default.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.law_list(states, authtoken, authtokentype, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str states: (required)
        :param str authtoken: Eco user authentication token. (required)
        :param str authtokentype: Eco user authentication token type. (required)
        :return: list[EcoWebServerDataTransferObjectsLawDTO]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.law_list_with_http_info(states, authtoken, authtokentype, **kwargs)  # noqa: E501
        else:
            (data) = self.law_list_with_http_info(states, authtoken, authtokentype, **kwargs)  # noqa: E501
            return data

    def law_list_with_http_info(self, states, authtoken, authtokentype, **kwargs):  # noqa: E501
        """Returns all laws currently present in the game in the specified states, active by default.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.law_list_with_http_info(states, authtoken, authtokentype, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str states: (required)
        :param str authtoken: Eco user authentication token. (required)
        :param str authtokentype: Eco user authentication token type. (required)
        :return: list[EcoWebServerDataTransferObjectsLawDTO]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['states', 'authtoken', 'authtokentype']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method law_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'states' is set
        if self.api_client.client_side_validation and ('states' not in params or
                                                       params['states'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `states` when calling `law_list`")  # noqa: E501
        # verify the required parameter 'authtoken' is set
        if self.api_client.client_side_validation and ('authtoken' not in params or
                                                       params['authtoken'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `authtoken` when calling `law_list`")  # noqa: E501
        # verify the required parameter 'authtokentype' is set
        if self.api_client.client_side_validation and ('authtokentype' not in params or
                                                       params['authtokentype'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `authtokentype` when calling `law_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'states' in params:
            path_params['states'] = params['states']  # noqa: E501

        query_params = []
        if 'authtoken' in params:
            query_params.append(('authtoken', params['authtoken']))  # noqa: E501
        if 'authtokentype' in params:
            query_params.append(('authtokentype', params['authtokentype']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['authtoken', 'authtokentype']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/laws/byStates/{states}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[EcoWebServerDataTransferObjectsLawDTO]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def law_list_all(self, authtoken, authtokentype, **kwargs):  # noqa: E501
        """Returns all laws currently present in the game  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.law_list_all(authtoken, authtokentype, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authtoken: Eco user authentication token. (required)
        :param str authtokentype: Eco user authentication token type. (required)
        :return: list[EcoWebServerDataTransferObjectsLawDTO]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.law_list_all_with_http_info(authtoken, authtokentype, **kwargs)  # noqa: E501
        else:
            (data) = self.law_list_all_with_http_info(authtoken, authtokentype, **kwargs)  # noqa: E501
            return data

    def law_list_all_with_http_info(self, authtoken, authtokentype, **kwargs):  # noqa: E501
        """Returns all laws currently present in the game  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.law_list_all_with_http_info(authtoken, authtokentype, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authtoken: Eco user authentication token. (required)
        :param str authtokentype: Eco user authentication token type. (required)
        :return: list[EcoWebServerDataTransferObjectsLawDTO]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authtoken', 'authtokentype']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method law_list_all" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authtoken' is set
        if self.api_client.client_side_validation and ('authtoken' not in params or
                                                       params['authtoken'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `authtoken` when calling `law_list_all`")  # noqa: E501
        # verify the required parameter 'authtokentype' is set
        if self.api_client.client_side_validation and ('authtokentype' not in params or
                                                       params['authtokentype'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `authtokentype` when calling `law_list_all`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'authtoken' in params:
            query_params.append(('authtoken', params['authtoken']))  # noqa: E501
        if 'authtokentype' in params:
            query_params.append(('authtokentype', params['authtokentype']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['authtoken', 'authtokentype']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/laws', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[EcoWebServerDataTransferObjectsLawDTO]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

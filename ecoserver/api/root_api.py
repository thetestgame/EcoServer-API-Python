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


class RootApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def root_front_page(self, authtoken, authtokentype, **kwargs):  # noqa: E501
        """root_front_page  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.root_front_page(authtoken, authtokentype, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authtoken: Eco user authentication token. (required)
        :param str authtokentype: Eco user authentication token type. (required)
        :return: EcoWebServerDataTransferObjectsFrontPage
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.root_front_page_with_http_info(authtoken, authtokentype, **kwargs)  # noqa: E501
        else:
            (data) = self.root_front_page_with_http_info(authtoken, authtokentype, **kwargs)  # noqa: E501
            return data

    def root_front_page_with_http_info(self, authtoken, authtokentype, **kwargs):  # noqa: E501
        """root_front_page  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.root_front_page_with_http_info(authtoken, authtokentype, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authtoken: Eco user authentication token. (required)
        :param str authtokentype: Eco user authentication token type. (required)
        :return: EcoWebServerDataTransferObjectsFrontPage
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
                    " to method root_front_page" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authtoken' is set
        if self.api_client.client_side_validation and ('authtoken' not in params or
                                                       params['authtoken'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `authtoken` when calling `root_front_page`")  # noqa: E501
        # verify the required parameter 'authtokentype' is set
        if self.api_client.client_side_validation and ('authtokentype' not in params or
                                                       params['authtokentype'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `authtokentype` when calling `root_front_page`")  # noqa: E501

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
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['authtoken', 'authtokentype']  # noqa: E501

        return self.api_client.call_api(
            '/frontpage', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EcoWebServerDataTransferObjectsFrontPage',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def root_get_admins(self, authtoken, authtokentype, **kwargs):  # noqa: E501
        """Returns the server's configured administrative users.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.root_get_admins(authtoken, authtokentype, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authtoken: Eco user authentication token. (required)
        :param str authtokentype: Eco user authentication token type. (required)
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.root_get_admins_with_http_info(authtoken, authtokentype, **kwargs)  # noqa: E501
        else:
            (data) = self.root_get_admins_with_http_info(authtoken, authtokentype, **kwargs)  # noqa: E501
            return data

    def root_get_admins_with_http_info(self, authtoken, authtokentype, **kwargs):  # noqa: E501
        """Returns the server's configured administrative users.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.root_get_admins_with_http_info(authtoken, authtokentype, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authtoken: Eco user authentication token. (required)
        :param str authtokentype: Eco user authentication token type. (required)
        :return: list[str]
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
                    " to method root_get_admins" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authtoken' is set
        if self.api_client.client_side_validation and ('authtoken' not in params or
                                                       params['authtoken'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `authtoken` when calling `root_get_admins`")  # noqa: E501
        # verify the required parameter 'authtokentype' is set
        if self.api_client.client_side_validation and ('authtokentype' not in params or
                                                       params['authtokentype'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `authtokentype` when calling `root_get_admins`")  # noqa: E501

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
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['authtoken', 'authtokentype']  # noqa: E501

        return self.api_client.call_api(
            '/admins', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[str]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def root_get_info(self, authtoken, authtokentype, **kwargs):  # noqa: E501
        """root_get_info  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.root_get_info(authtoken, authtokentype, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authtoken: Eco user authentication token. (required)
        :param str authtokentype: Eco user authentication token type. (required)
        :return: EcoSharedNetworkingServerInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.root_get_info_with_http_info(authtoken, authtokentype, **kwargs)  # noqa: E501
        else:
            (data) = self.root_get_info_with_http_info(authtoken, authtokentype, **kwargs)  # noqa: E501
            return data

    def root_get_info_with_http_info(self, authtoken, authtokentype, **kwargs):  # noqa: E501
        """root_get_info  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.root_get_info_with_http_info(authtoken, authtokentype, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authtoken: Eco user authentication token. (required)
        :param str authtokentype: Eco user authentication token type. (required)
        :return: EcoSharedNetworkingServerInfo
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
                    " to method root_get_info" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authtoken' is set
        if self.api_client.client_side_validation and ('authtoken' not in params or
                                                       params['authtoken'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `authtoken` when calling `root_get_info`")  # noqa: E501
        # verify the required parameter 'authtokentype' is set
        if self.api_client.client_side_validation and ('authtokentype' not in params or
                                                       params['authtokentype'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `authtokentype` when calling `root_get_info`")  # noqa: E501

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
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['authtoken', 'authtokentype']  # noqa: E501

        return self.api_client.call_api(
            '/info', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EcoSharedNetworkingServerInfo',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def root_is_admin(self, authtoken, authtokentype, **kwargs):  # noqa: E501
        """Return if the user is an admin and authentication is required.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.root_is_admin(authtoken, authtokentype, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authtoken: Eco user authentication token. (required)
        :param str authtokentype: Eco user authentication token type. (required)
        :return: bool
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.root_is_admin_with_http_info(authtoken, authtokentype, **kwargs)  # noqa: E501
        else:
            (data) = self.root_is_admin_with_http_info(authtoken, authtokentype, **kwargs)  # noqa: E501
            return data

    def root_is_admin_with_http_info(self, authtoken, authtokentype, **kwargs):  # noqa: E501
        """Return if the user is an admin and authentication is required.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.root_is_admin_with_http_info(authtoken, authtokentype, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authtoken: Eco user authentication token. (required)
        :param str authtokentype: Eco user authentication token type. (required)
        :return: bool
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
                    " to method root_is_admin" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authtoken' is set
        if self.api_client.client_side_validation and ('authtoken' not in params or
                                                       params['authtoken'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `authtoken` when calling `root_is_admin`")  # noqa: E501
        # verify the required parameter 'authtokentype' is set
        if self.api_client.client_side_validation and ('authtokentype' not in params or
                                                       params['authtokentype'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `authtokentype` when calling `root_is_admin`")  # noqa: E501

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
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['authtoken', 'authtokentype']  # noqa: E501

        return self.api_client.call_api(
            '/isadmin', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='bool',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
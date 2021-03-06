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


class LogApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def log_get_all_logs(self, authtoken, authtokentype, **kwargs):  # noqa: E501
        """Retrieves a list of all log files on the server.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.log_get_all_logs(authtoken, authtokentype, async_req=True)
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
            return self.log_get_all_logs_with_http_info(authtoken, authtokentype, **kwargs)  # noqa: E501
        else:
            (data) = self.log_get_all_logs_with_http_info(authtoken, authtokentype, **kwargs)  # noqa: E501
            return data

    def log_get_all_logs_with_http_info(self, authtoken, authtokentype, **kwargs):  # noqa: E501
        """Retrieves a list of all log files on the server.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.log_get_all_logs_with_http_info(authtoken, authtokentype, async_req=True)
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
                    " to method log_get_all_logs" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authtoken' is set
        if self.api_client.client_side_validation and ('authtoken' not in params or
                                                       params['authtoken'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `authtoken` when calling `log_get_all_logs`")  # noqa: E501
        # verify the required parameter 'authtokentype' is set
        if self.api_client.client_side_validation and ('authtokentype' not in params or
                                                       params['authtokentype'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `authtokentype` when calling `log_get_all_logs`")  # noqa: E501

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
            '/api/v1/logs', 'GET',
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

    def log_get_category_logs(self, category, authtoken, authtokentype, **kwargs):  # noqa: E501
        """Retrieves a list of all log files in the requested category subfolder if it exists.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.log_get_category_logs(category, authtoken, authtokentype, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str category: Category log subfolder to search. (required)
        :param str authtoken: Eco user authentication token. (required)
        :param str authtokentype: Eco user authentication token type. (required)
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.log_get_category_logs_with_http_info(category, authtoken, authtokentype, **kwargs)  # noqa: E501
        else:
            (data) = self.log_get_category_logs_with_http_info(category, authtoken, authtokentype, **kwargs)  # noqa: E501
            return data

    def log_get_category_logs_with_http_info(self, category, authtoken, authtokentype, **kwargs):  # noqa: E501
        """Retrieves a list of all log files in the requested category subfolder if it exists.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.log_get_category_logs_with_http_info(category, authtoken, authtokentype, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str category: Category log subfolder to search. (required)
        :param str authtoken: Eco user authentication token. (required)
        :param str authtokentype: Eco user authentication token type. (required)
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['category', 'authtoken', 'authtokentype']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method log_get_category_logs" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'category' is set
        if self.api_client.client_side_validation and ('category' not in params or
                                                       params['category'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `category` when calling `log_get_category_logs`")  # noqa: E501
        # verify the required parameter 'authtoken' is set
        if self.api_client.client_side_validation and ('authtoken' not in params or
                                                       params['authtoken'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `authtoken` when calling `log_get_category_logs`")  # noqa: E501
        # verify the required parameter 'authtokentype' is set
        if self.api_client.client_side_validation and ('authtokentype' not in params or
                                                       params['authtokentype'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `authtokentype` when calling `log_get_category_logs`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'category' in params:
            path_params['category'] = params['category']  # noqa: E501

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
            '/api/v1/logs/{category}', 'GET',
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

    def log_get_log_file(self, authtoken, authtokentype, **kwargs):  # noqa: E501
        """Streams a log file over HTTP/HTTPS to a client.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.log_get_log_file(authtoken, authtokentype, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authtoken: Eco user authentication token. (required)
        :param str authtokentype: Eco user authentication token type. (required)
        :param str filepath: Filepath of the log file to stream.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.log_get_log_file_with_http_info(authtoken, authtokentype, **kwargs)  # noqa: E501
        else:
            (data) = self.log_get_log_file_with_http_info(authtoken, authtokentype, **kwargs)  # noqa: E501
            return data

    def log_get_log_file_with_http_info(self, authtoken, authtokentype, **kwargs):  # noqa: E501
        """Streams a log file over HTTP/HTTPS to a client.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.log_get_log_file_with_http_info(authtoken, authtokentype, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authtoken: Eco user authentication token. (required)
        :param str authtokentype: Eco user authentication token type. (required)
        :param str filepath: Filepath of the log file to stream.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authtoken', 'authtokentype', 'filepath']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method log_get_log_file" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authtoken' is set
        if self.api_client.client_side_validation and ('authtoken' not in params or
                                                       params['authtoken'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `authtoken` when calling `log_get_log_file`")  # noqa: E501
        # verify the required parameter 'authtokentype' is set
        if self.api_client.client_side_validation and ('authtokentype' not in params or
                                                       params['authtokentype'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `authtokentype` when calling `log_get_log_file`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'filepath' in params:
            query_params.append(('filepath', params['filepath']))  # noqa: E501
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
            '/api/v1/logs/get', 'GET',
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

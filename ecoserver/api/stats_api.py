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


class StatsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def stats_generate_test_data(self, authtoken, authtokentype, **kwargs):  # noqa: E501
        """Generates fake stat data for testing.  # noqa: E501

        > This endpoint can only be invoked when AllowDebugCalls is enabled on the server.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.stats_generate_test_data(authtoken, authtokentype, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authtoken: Eco user authentication token. (required)
        :param str authtokentype: Eco user authentication token type. (required)
        :param float days: The number of days to simulate.
        :param int users: The number of users to simulate.
        :param bool generate_climate_data: Whether to generate climate data. Default is false.
        :param float pollution_multiplier: How much pollution to generate. Default is 1.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.stats_generate_test_data_with_http_info(authtoken, authtokentype, **kwargs)  # noqa: E501
        else:
            (data) = self.stats_generate_test_data_with_http_info(authtoken, authtokentype, **kwargs)  # noqa: E501
            return data

    def stats_generate_test_data_with_http_info(self, authtoken, authtokentype, **kwargs):  # noqa: E501
        """Generates fake stat data for testing.  # noqa: E501

        > This endpoint can only be invoked when AllowDebugCalls is enabled on the server.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.stats_generate_test_data_with_http_info(authtoken, authtokentype, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authtoken: Eco user authentication token. (required)
        :param str authtokentype: Eco user authentication token type. (required)
        :param float days: The number of days to simulate.
        :param int users: The number of users to simulate.
        :param bool generate_climate_data: Whether to generate climate data. Default is false.
        :param float pollution_multiplier: How much pollution to generate. Default is 1.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authtoken', 'authtokentype', 'days', 'users', 'generate_climate_data', 'pollution_multiplier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method stats_generate_test_data" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authtoken' is set
        if self.api_client.client_side_validation and ('authtoken' not in params or
                                                       params['authtoken'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `authtoken` when calling `stats_generate_test_data`")  # noqa: E501
        # verify the required parameter 'authtokentype' is set
        if self.api_client.client_side_validation and ('authtokentype' not in params or
                                                       params['authtokentype'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `authtokentype` when calling `stats_generate_test_data`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'days' in params:
            query_params.append(('days', params['days']))  # noqa: E501
        if 'users' in params:
            query_params.append(('users', params['users']))  # noqa: E501
        if 'generate_climate_data' in params:
            query_params.append(('generateClimateData', params['generate_climate_data']))  # noqa: E501
        if 'pollution_multiplier' in params:
            query_params.append(('pollutionMultiplier', params['pollution_multiplier']))  # noqa: E501
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
            '/datasets/generatetestdata', 'GET',
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

    def stats_get(self, authtoken, authtokentype, **kwargs):  # noqa: E501
        """/// Returns Eco.WebServer.Web.Controllers.StatsController.MaximumSamples data points between dayStart and dayEnd of the selected data.             If there are more than Eco.WebServer.Web.Controllers.StatsController.MaximumSamples samples, it will be averaged out to contain exactly Eco.WebServer.Web.Controllers.StatsController.MaximumSamples.///.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.stats_get(authtoken, authtokentype, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authtoken: Eco user authentication token. (required)
        :param str authtokentype: Eco user authentication token type. (required)
        :param str dataset: dataset to take the data from.
        :param float day_start: Day from which on data is returned. Default is 0.
        :param float day_end: Day until which data is returned. Default is now.
        :return: EcoWebServerWebControllersStatReturn
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.stats_get_with_http_info(authtoken, authtokentype, **kwargs)  # noqa: E501
        else:
            (data) = self.stats_get_with_http_info(authtoken, authtokentype, **kwargs)  # noqa: E501
            return data

    def stats_get_with_http_info(self, authtoken, authtokentype, **kwargs):  # noqa: E501
        """/// Returns Eco.WebServer.Web.Controllers.StatsController.MaximumSamples data points between dayStart and dayEnd of the selected data.             If there are more than Eco.WebServer.Web.Controllers.StatsController.MaximumSamples samples, it will be averaged out to contain exactly Eco.WebServer.Web.Controllers.StatsController.MaximumSamples.///.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.stats_get_with_http_info(authtoken, authtokentype, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authtoken: Eco user authentication token. (required)
        :param str authtokentype: Eco user authentication token type. (required)
        :param str dataset: dataset to take the data from.
        :param float day_start: Day from which on data is returned. Default is 0.
        :param float day_end: Day until which data is returned. Default is now.
        :return: EcoWebServerWebControllersStatReturn
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authtoken', 'authtokentype', 'dataset', 'day_start', 'day_end']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method stats_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authtoken' is set
        if self.api_client.client_side_validation and ('authtoken' not in params or
                                                       params['authtoken'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `authtoken` when calling `stats_get`")  # noqa: E501
        # verify the required parameter 'authtokentype' is set
        if self.api_client.client_side_validation and ('authtokentype' not in params or
                                                       params['authtokentype'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `authtokentype` when calling `stats_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'dataset' in params:
            query_params.append(('dataset', params['dataset']))  # noqa: E501
        if 'day_start' in params:
            query_params.append(('dayStart', params['day_start']))  # noqa: E501
        if 'day_end' in params:
            query_params.append(('dayEnd', params['day_end']))  # noqa: E501
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
            '/datasets/get', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EcoWebServerWebControllersStatReturn',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def stats_get_flat_list(self, authtoken, authtokentype, **kwargs):  # noqa: E501
        """/// Returns all stat infos that contain data, formatted as a list, where each key is a list of strings. ///.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.stats_get_flat_list(authtoken, authtokentype, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authtoken: Eco user authentication token. (required)
        :param str authtokentype: Eco user authentication token type. (required)
        :return: list[EcoStatsStatInfo]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.stats_get_flat_list_with_http_info(authtoken, authtokentype, **kwargs)  # noqa: E501
        else:
            (data) = self.stats_get_flat_list_with_http_info(authtoken, authtokentype, **kwargs)  # noqa: E501
            return data

    def stats_get_flat_list_with_http_info(self, authtoken, authtokentype, **kwargs):  # noqa: E501
        """/// Returns all stat infos that contain data, formatted as a list, where each key is a list of strings. ///.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.stats_get_flat_list_with_http_info(authtoken, authtokentype, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authtoken: Eco user authentication token. (required)
        :param str authtokentype: Eco user authentication token type. (required)
        :return: list[EcoStatsStatInfo]
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
                    " to method stats_get_flat_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authtoken' is set
        if self.api_client.client_side_validation and ('authtoken' not in params or
                                                       params['authtoken'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `authtoken` when calling `stats_get_flat_list`")  # noqa: E501
        # verify the required parameter 'authtokentype' is set
        if self.api_client.client_side_validation and ('authtokentype' not in params or
                                                       params['authtokentype'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `authtokentype` when calling `stats_get_flat_list`")  # noqa: E501

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
            '/datasets/flatlist', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[EcoStatsStatInfo]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def stats_get_list(self, authtoken, authtokentype, **kwargs):  # noqa: E501
        """Returns a \"package\" of multiple statistics in the order of their request.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.stats_get_list(authtoken, authtokentype, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authtoken: Eco user authentication token. (required)
        :param str authtokentype: Eco user authentication token type. (required)
        :param list[str] requested_sets: A list of statistics that should be returned.
        :param float day_start: Day from which the data should be taken from. Default is 0.
        :param float day_end: Day until which data is returned. Default is now.
        :return: list[EcoWebServerWebControllersStatReturn]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.stats_get_list_with_http_info(authtoken, authtokentype, **kwargs)  # noqa: E501
        else:
            (data) = self.stats_get_list_with_http_info(authtoken, authtokentype, **kwargs)  # noqa: E501
            return data

    def stats_get_list_with_http_info(self, authtoken, authtokentype, **kwargs):  # noqa: E501
        """Returns a \"package\" of multiple statistics in the order of their request.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.stats_get_list_with_http_info(authtoken, authtokentype, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authtoken: Eco user authentication token. (required)
        :param str authtokentype: Eco user authentication token type. (required)
        :param list[str] requested_sets: A list of statistics that should be returned.
        :param float day_start: Day from which the data should be taken from. Default is 0.
        :param float day_end: Day until which data is returned. Default is now.
        :return: list[EcoWebServerWebControllersStatReturn]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authtoken', 'authtokentype', 'requested_sets', 'day_start', 'day_end']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method stats_get_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authtoken' is set
        if self.api_client.client_side_validation and ('authtoken' not in params or
                                                       params['authtoken'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `authtoken` when calling `stats_get_list`")  # noqa: E501
        # verify the required parameter 'authtokentype' is set
        if self.api_client.client_side_validation and ('authtokentype' not in params or
                                                       params['authtokentype'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `authtokentype` when calling `stats_get_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'requested_sets' in params:
            query_params.append(('requestedSets', params['requested_sets']))  # noqa: E501
            collection_formats['requestedSets'] = 'csv'  # noqa: E501
        if 'day_start' in params:
            query_params.append(('dayStart', params['day_start']))  # noqa: E501
        if 'day_end' in params:
            query_params.append(('dayEnd', params['day_end']))  # noqa: E501
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
            '/datasets/getlist', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[EcoWebServerWebControllersStatReturn]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def stats_get_time_range(self, authtoken, authtokentype, **kwargs):  # noqa: E501
        """/// Returns the timerange of the simulation, in days///.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.stats_get_time_range(authtoken, authtokentype, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authtoken: Eco user authentication token. (required)
        :param str authtokentype: Eco user authentication token type. (required)
        :return: list[float]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.stats_get_time_range_with_http_info(authtoken, authtokentype, **kwargs)  # noqa: E501
        else:
            (data) = self.stats_get_time_range_with_http_info(authtoken, authtokentype, **kwargs)  # noqa: E501
            return data

    def stats_get_time_range_with_http_info(self, authtoken, authtokentype, **kwargs):  # noqa: E501
        """/// Returns the timerange of the simulation, in days///.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.stats_get_time_range_with_http_info(authtoken, authtokentype, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authtoken: Eco user authentication token. (required)
        :param str authtokentype: Eco user authentication token type. (required)
        :return: list[float]
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
                    " to method stats_get_time_range" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authtoken' is set
        if self.api_client.client_side_validation and ('authtoken' not in params or
                                                       params['authtoken'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `authtoken` when calling `stats_get_time_range`")  # noqa: E501
        # verify the required parameter 'authtokentype' is set
        if self.api_client.client_side_validation and ('authtokentype' not in params or
                                                       params['authtokentype'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `authtokentype` when calling `stats_get_time_range`")  # noqa: E501

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
            '/datasets/timerange', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[float]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def stats_get_tree_list(self, authtoken, authtokentype, **kwargs):  # noqa: E501
        """Returns all dataset keys, formatted as a tree. ///.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.stats_get_tree_list(authtoken, authtokentype, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authtoken: Eco user authentication token. (required)
        :param str authtokentype: Eco user authentication token type. (required)
        :return: EcoStatsStatCategory
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.stats_get_tree_list_with_http_info(authtoken, authtokentype, **kwargs)  # noqa: E501
        else:
            (data) = self.stats_get_tree_list_with_http_info(authtoken, authtokentype, **kwargs)  # noqa: E501
            return data

    def stats_get_tree_list_with_http_info(self, authtoken, authtokentype, **kwargs):  # noqa: E501
        """Returns all dataset keys, formatted as a tree. ///.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.stats_get_tree_list_with_http_info(authtoken, authtokentype, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authtoken: Eco user authentication token. (required)
        :param str authtokentype: Eco user authentication token type. (required)
        :return: EcoStatsStatCategory
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
                    " to method stats_get_tree_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authtoken' is set
        if self.api_client.client_side_validation and ('authtoken' not in params or
                                                       params['authtoken'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `authtoken` when calling `stats_get_tree_list`")  # noqa: E501
        # verify the required parameter 'authtokentype' is set
        if self.api_client.client_side_validation and ('authtokentype' not in params or
                                                       params['authtokentype'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `authtokentype` when calling `stats_get_tree_list`")  # noqa: E501

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
            '/datasets/treelist', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EcoStatsStatCategory',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def stats_graphs(self, authtoken, authtokentype, **kwargs):  # noqa: E501
        """Returns the list of premade graphs to be displayed on the front page.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.stats_graphs(authtoken, authtokentype, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authtoken: Eco user authentication token. (required)
        :param str authtokentype: Eco user authentication token type. (required)
        :return: list[EcoStatsNamedGraph]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.stats_graphs_with_http_info(authtoken, authtokentype, **kwargs)  # noqa: E501
        else:
            (data) = self.stats_graphs_with_http_info(authtoken, authtokentype, **kwargs)  # noqa: E501
            return data

    def stats_graphs_with_http_info(self, authtoken, authtokentype, **kwargs):  # noqa: E501
        """Returns the list of premade graphs to be displayed on the front page.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.stats_graphs_with_http_info(authtoken, authtokentype, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authtoken: Eco user authentication token. (required)
        :param str authtokentype: Eco user authentication token type. (required)
        :return: list[EcoStatsNamedGraph]
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
                    " to method stats_graphs" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authtoken' is set
        if self.api_client.client_side_validation and ('authtoken' not in params or
                                                       params['authtoken'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `authtoken` when calling `stats_graphs`")  # noqa: E501
        # verify the required parameter 'authtokentype' is set
        if self.api_client.client_side_validation and ('authtokentype' not in params or
                                                       params['authtokentype'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `authtokentype` when calling `stats_graphs`")  # noqa: E501

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
            '/datasets/graphs', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[EcoStatsNamedGraph]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

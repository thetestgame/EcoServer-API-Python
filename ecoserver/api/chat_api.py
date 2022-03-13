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


class ChatApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def chat_get_chat(self, authtoken, authtokentype, **kwargs):  # noqa: E501
        """Returns all non-private player chat messages sent within the given time range.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.chat_get_chat(authtoken, authtokentype, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authtoken: Eco user authentication token. (required)
        :param str authtokentype: Eco user authentication token type. (required)
        :param float start_day: The lower bound on the time range. Default is 0.
        :param float end_day: The upper bound on the time range. Default is now.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.chat_get_chat_with_http_info(authtoken, authtokentype, **kwargs)  # noqa: E501
        else:
            (data) = self.chat_get_chat_with_http_info(authtoken, authtokentype, **kwargs)  # noqa: E501
            return data

    def chat_get_chat_with_http_info(self, authtoken, authtokentype, **kwargs):  # noqa: E501
        """Returns all non-private player chat messages sent within the given time range.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.chat_get_chat_with_http_info(authtoken, authtokentype, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authtoken: Eco user authentication token. (required)
        :param str authtokentype: Eco user authentication token type. (required)
        :param float start_day: The lower bound on the time range. Default is 0.
        :param float end_day: The upper bound on the time range. Default is now.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authtoken', 'authtokentype', 'start_day', 'end_day']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method chat_get_chat" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authtoken' is set
        if self.api_client.client_side_validation and ('authtoken' not in params or
                                                       params['authtoken'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `authtoken` when calling `chat_get_chat`")  # noqa: E501
        # verify the required parameter 'authtokentype' is set
        if self.api_client.client_side_validation and ('authtokentype' not in params or
                                                       params['authtokentype'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `authtokentype` when calling `chat_get_chat`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_day' in params:
            query_params.append(('startDay', params['start_day']))  # noqa: E501
        if 'end_day' in params:
            query_params.append(('endDay', params['end_day']))  # noqa: E501
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
            '/api/v1/chat', 'GET',
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

    def chat_get_chat_by_tag(self, authtoken, authtokentype, **kwargs):  # noqa: E501
        """Returns all non-private player chat messages sent to the given tag within the given time range.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.chat_get_chat_by_tag(authtoken, authtokentype, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authtoken: Eco user authentication token. (required)
        :param str authtokentype: Eco user authentication token type. (required)
        :param str tag: The tag name in question.
        :param float start_day: The lower bound on the time range. Default is 0.
        :param float end_day: The upper bound on the time range. Default is now.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.chat_get_chat_by_tag_with_http_info(authtoken, authtokentype, **kwargs)  # noqa: E501
        else:
            (data) = self.chat_get_chat_by_tag_with_http_info(authtoken, authtokentype, **kwargs)  # noqa: E501
            return data

    def chat_get_chat_by_tag_with_http_info(self, authtoken, authtokentype, **kwargs):  # noqa: E501
        """Returns all non-private player chat messages sent to the given tag within the given time range.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.chat_get_chat_by_tag_with_http_info(authtoken, authtokentype, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authtoken: Eco user authentication token. (required)
        :param str authtokentype: Eco user authentication token type. (required)
        :param str tag: The tag name in question.
        :param float start_day: The lower bound on the time range. Default is 0.
        :param float end_day: The upper bound on the time range. Default is now.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authtoken', 'authtokentype', 'tag', 'start_day', 'end_day']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method chat_get_chat_by_tag" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authtoken' is set
        if self.api_client.client_side_validation and ('authtoken' not in params or
                                                       params['authtoken'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `authtoken` when calling `chat_get_chat_by_tag`")  # noqa: E501
        # verify the required parameter 'authtokentype' is set
        if self.api_client.client_side_validation and ('authtokentype' not in params or
                                                       params['authtokentype'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `authtokentype` when calling `chat_get_chat_by_tag`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'tag' in params:
            query_params.append(('tag', params['tag']))  # noqa: E501
        if 'start_day' in params:
            query_params.append(('startDay', params['start_day']))  # noqa: E501
        if 'end_day' in params:
            query_params.append(('endDay', params['end_day']))  # noqa: E501
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
            '/api/v1/chat/tag', 'GET',
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

    def chat_get_chat_messages_sent_by(self, username, authtoken, authtokentype, **kwargs):  # noqa: E501
        """Returns all non-private chat messages sent by the given user within the given time range.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.chat_get_chat_messages_sent_by(username, authtoken, authtokentype, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str username: The user in question. (required)
        :param str authtoken: Eco user authentication token. (required)
        :param str authtokentype: Eco user authentication token type. (required)
        :param float start_day: The lower bound on the time range. Default is 0.
        :param float end_day: The upper bound on the time range. Default is now.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.chat_get_chat_messages_sent_by_with_http_info(username, authtoken, authtokentype, **kwargs)  # noqa: E501
        else:
            (data) = self.chat_get_chat_messages_sent_by_with_http_info(username, authtoken, authtokentype, **kwargs)  # noqa: E501
            return data

    def chat_get_chat_messages_sent_by_with_http_info(self, username, authtoken, authtokentype, **kwargs):  # noqa: E501
        """Returns all non-private chat messages sent by the given user within the given time range.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.chat_get_chat_messages_sent_by_with_http_info(username, authtoken, authtokentype, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str username: The user in question. (required)
        :param str authtoken: Eco user authentication token. (required)
        :param str authtokentype: Eco user authentication token type. (required)
        :param float start_day: The lower bound on the time range. Default is 0.
        :param float end_day: The upper bound on the time range. Default is now.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['username', 'authtoken', 'authtokentype', 'start_day', 'end_day']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method chat_get_chat_messages_sent_by" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'username' is set
        if self.api_client.client_side_validation and ('username' not in params or
                                                       params['username'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `username` when calling `chat_get_chat_messages_sent_by`")  # noqa: E501
        # verify the required parameter 'authtoken' is set
        if self.api_client.client_side_validation and ('authtoken' not in params or
                                                       params['authtoken'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `authtoken` when calling `chat_get_chat_messages_sent_by`")  # noqa: E501
        # verify the required parameter 'authtokentype' is set
        if self.api_client.client_side_validation and ('authtokentype' not in params or
                                                       params['authtokentype'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `authtokentype` when calling `chat_get_chat_messages_sent_by`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'username' in params:
            path_params['username'] = params['username']  # noqa: E501

        query_params = []
        if 'start_day' in params:
            query_params.append(('startDay', params['start_day']))  # noqa: E501
        if 'end_day' in params:
            query_params.append(('endDay', params['end_day']))  # noqa: E501
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
            '/api/v1/chat/{username}', 'GET',
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

    def chat_get_next(self, authtoken, authtokentype, **kwargs):  # noqa: E501
        """Gets the. <code>numNextMessages</code> chat messages sent after the given message on the same tag.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.chat_get_next(authtoken, authtokentype, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authtoken: Eco user authentication token. (required)
        :param str authtokentype: Eco user authentication token type. (required)
        :param int num_next_messages: The number of following messages to return.
        :param EcoWebServerDataTransferObjectsChatMessageDTO body: The message in question.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.chat_get_next_with_http_info(authtoken, authtokentype, **kwargs)  # noqa: E501
        else:
            (data) = self.chat_get_next_with_http_info(authtoken, authtokentype, **kwargs)  # noqa: E501
            return data

    def chat_get_next_with_http_info(self, authtoken, authtokentype, **kwargs):  # noqa: E501
        """Gets the. <code>numNextMessages</code> chat messages sent after the given message on the same tag.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.chat_get_next_with_http_info(authtoken, authtokentype, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authtoken: Eco user authentication token. (required)
        :param str authtokentype: Eco user authentication token type. (required)
        :param int num_next_messages: The number of following messages to return.
        :param EcoWebServerDataTransferObjectsChatMessageDTO body: The message in question.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authtoken', 'authtokentype', 'num_next_messages', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method chat_get_next" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authtoken' is set
        if self.api_client.client_side_validation and ('authtoken' not in params or
                                                       params['authtoken'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `authtoken` when calling `chat_get_next`")  # noqa: E501
        # verify the required parameter 'authtokentype' is set
        if self.api_client.client_side_validation and ('authtokentype' not in params or
                                                       params['authtokentype'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `authtokentype` when calling `chat_get_next`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'num_next_messages' in params:
            query_params.append(('numNextMessages', params['num_next_messages']))  # noqa: E501
        if 'authtoken' in params:
            query_params.append(('authtoken', params['authtoken']))  # noqa: E501
        if 'authtokentype' in params:
            query_params.append(('authtokentype', params['authtokentype']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['authtoken', 'authtokentype']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/chat/next', 'POST',
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

    def chat_get_previous(self, authtoken, authtokentype, **kwargs):  # noqa: E501
        """Gets the. <code>numPreviousMessages</code> chat messages sent before the given message on the same tag.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.chat_get_previous(authtoken, authtokentype, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authtoken: Eco user authentication token. (required)
        :param str authtokentype: Eco user authentication token type. (required)
        :param int num_previous_messages: The number of preceding messages to return.
        :param EcoWebServerDataTransferObjectsChatMessageDTO body: The message in question.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.chat_get_previous_with_http_info(authtoken, authtokentype, **kwargs)  # noqa: E501
        else:
            (data) = self.chat_get_previous_with_http_info(authtoken, authtokentype, **kwargs)  # noqa: E501
            return data

    def chat_get_previous_with_http_info(self, authtoken, authtokentype, **kwargs):  # noqa: E501
        """Gets the. <code>numPreviousMessages</code> chat messages sent before the given message on the same tag.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.chat_get_previous_with_http_info(authtoken, authtokentype, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authtoken: Eco user authentication token. (required)
        :param str authtokentype: Eco user authentication token type. (required)
        :param int num_previous_messages: The number of preceding messages to return.
        :param EcoWebServerDataTransferObjectsChatMessageDTO body: The message in question.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authtoken', 'authtokentype', 'num_previous_messages', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method chat_get_previous" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authtoken' is set
        if self.api_client.client_side_validation and ('authtoken' not in params or
                                                       params['authtoken'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `authtoken` when calling `chat_get_previous`")  # noqa: E501
        # verify the required parameter 'authtokentype' is set
        if self.api_client.client_side_validation and ('authtokentype' not in params or
                                                       params['authtokentype'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `authtokentype` when calling `chat_get_previous`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'num_previous_messages' in params:
            query_params.append(('numPreviousMessages', params['num_previous_messages']))  # noqa: E501
        if 'authtoken' in params:
            query_params.append(('authtoken', params['authtoken']))  # noqa: E501
        if 'authtokentype' in params:
            query_params.append(('authtokentype', params['authtokentype']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['authtoken', 'authtokentype']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/chat/previous', 'POST',
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

    def chat_send_chat(self, authtoken, authtokentype, **kwargs):  # noqa: E501
        """Sends chat message like username.  # noqa: E501

        > This endpoint can only be invoked when AllowDebugCalls is enabled on the server.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.chat_send_chat(authtoken, authtokentype, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authtoken: Eco user authentication token. (required)
        :param str authtokentype: Eco user authentication token type. (required)
        :param str username: User who wants to send message.
        :param str message: The message to send.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.chat_send_chat_with_http_info(authtoken, authtokentype, **kwargs)  # noqa: E501
        else:
            (data) = self.chat_send_chat_with_http_info(authtoken, authtokentype, **kwargs)  # noqa: E501
            return data

    def chat_send_chat_with_http_info(self, authtoken, authtokentype, **kwargs):  # noqa: E501
        """Sends chat message like username.  # noqa: E501

        > This endpoint can only be invoked when AllowDebugCalls is enabled on the server.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.chat_send_chat_with_http_info(authtoken, authtokentype, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authtoken: Eco user authentication token. (required)
        :param str authtokentype: Eco user authentication token type. (required)
        :param str username: User who wants to send message.
        :param str message: The message to send.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authtoken', 'authtokentype', 'username', 'message']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method chat_send_chat" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authtoken' is set
        if self.api_client.client_side_validation and ('authtoken' not in params or
                                                       params['authtoken'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `authtoken` when calling `chat_send_chat`")  # noqa: E501
        # verify the required parameter 'authtokentype' is set
        if self.api_client.client_side_validation and ('authtokentype' not in params or
                                                       params['authtokentype'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `authtokentype` when calling `chat_send_chat`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'username' in params:
            query_params.append(('username', params['username']))  # noqa: E501
        if 'message' in params:
            query_params.append(('message', params['message']))  # noqa: E501
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
            '/api/v1/chat/sendChat', 'GET',
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
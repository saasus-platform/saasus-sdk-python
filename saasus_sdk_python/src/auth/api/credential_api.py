# coding: utf-8

"""
    SaaSus Auth API Schema

    Schema

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError
from typing_extensions import Annotated

from pydantic import Field, StrictStr

from typing import Optional

from saasus_sdk_python.src.auth.models.authorization_temp_code import AuthorizationTempCode
from saasus_sdk_python.src.auth.models.credentials import Credentials

from saasus_sdk_python.src.auth.api_client import ApiClient
from saasus_sdk_python.src.auth.api_response import ApiResponse
from saasus_sdk_python.src.auth.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class CredentialApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def create_auth_credentials(self, body : Optional[Credentials] = None, **kwargs) -> AuthorizationTempCode:  # noqa: E501
        """Save Authentication/Authorization Information  # noqa: E501

        Temporarily save the parameter for the ID token, access token, and refresh token and return a temporary code for obtaining. Temporary codes are valid for 10 seconds from issuance.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_auth_credentials(body, async_req=True)
        >>> result = thread.get()

        :param body:
        :type body: Credentials
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: AuthorizationTempCode
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the create_auth_credentials_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.create_auth_credentials_with_http_info(body, **kwargs)  # noqa: E501

    @validate_arguments
    def create_auth_credentials_with_http_info(self, body : Optional[Credentials] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Save Authentication/Authorization Information  # noqa: E501

        Temporarily save the parameter for the ID token, access token, and refresh token and return a temporary code for obtaining. Temporary codes are valid for 10 seconds from issuance.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_auth_credentials_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param body:
        :type body: Credentials
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(AuthorizationTempCode, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'body'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_auth_credentials" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['body'] is not None:
            _body_params = _params['body']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['Bearer']  # noqa: E501

        _response_types_map = {
            '201': "AuthorizationTempCode",
            '400': "Error",
            '401': "Error",
            '500': "Error",
        }

        return self.api_client.call_api(
            '/credentials', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_auth_credentials(self, code : Annotated[Optional[StrictStr], Field(description="Temp Code")] = None, auth_flow : Annotated[Optional[StrictStr], Field(description="Authentication Flow tempCodeAuth: Getting authentication information using a temporary code refreshTokenAuth: Getting authentication information using a refresh token If not specified, it will be tempCodeAuth ")] = None, refresh_token : Annotated[Optional[StrictStr], Field(description="Refresh Token")] = None, **kwargs) -> Credentials:  # noqa: E501
        """Get Authentication/Authorization Information  # noqa: E501

        Get ID token, access token, and refresh token using a temporary code or a refresh token.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_auth_credentials(code, auth_flow, refresh_token, async_req=True)
        >>> result = thread.get()

        :param code: Temp Code
        :type code: str
        :param auth_flow: Authentication Flow tempCodeAuth: Getting authentication information using a temporary code refreshTokenAuth: Getting authentication information using a refresh token If not specified, it will be tempCodeAuth 
        :type auth_flow: str
        :param refresh_token: Refresh Token
        :type refresh_token: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Credentials
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_auth_credentials_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_auth_credentials_with_http_info(code, auth_flow, refresh_token, **kwargs)  # noqa: E501

    @validate_arguments
    def get_auth_credentials_with_http_info(self, code : Annotated[Optional[StrictStr], Field(description="Temp Code")] = None, auth_flow : Annotated[Optional[StrictStr], Field(description="Authentication Flow tempCodeAuth: Getting authentication information using a temporary code refreshTokenAuth: Getting authentication information using a refresh token If not specified, it will be tempCodeAuth ")] = None, refresh_token : Annotated[Optional[StrictStr], Field(description="Refresh Token")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Get Authentication/Authorization Information  # noqa: E501

        Get ID token, access token, and refresh token using a temporary code or a refresh token.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_auth_credentials_with_http_info(code, auth_flow, refresh_token, async_req=True)
        >>> result = thread.get()

        :param code: Temp Code
        :type code: str
        :param auth_flow: Authentication Flow tempCodeAuth: Getting authentication information using a temporary code refreshTokenAuth: Getting authentication information using a refresh token If not specified, it will be tempCodeAuth 
        :type auth_flow: str
        :param refresh_token: Refresh Token
        :type refresh_token: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(Credentials, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'code',
            'auth_flow',
            'refresh_token'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_auth_credentials" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('code') is not None:  # noqa: E501
            _query_params.append(('code', _params['code']))

        if _params.get('auth_flow') is not None:  # noqa: E501
            _query_params.append(('auth-flow', _params['auth_flow']))

        if _params.get('refresh_token') is not None:  # noqa: E501
            _query_params.append(('refresh-token', _params['refresh_token']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['Bearer']  # noqa: E501

        _response_types_map = {
            '200': "Credentials",
            '404': "Error",
            '500': "Error",
        }

        return self.api_client.call_api(
            '/credentials', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

from __future__ import annotations

from typing import Tuple, Optional, Union, Any

from openapi_client.exceptions import UnauthorizedException, ServiceException
from saasus_sdk_python import UserInfoApi
from saasus_sdk_python.client.client import AuthClient

from fastapi import HTTPException,Request
from flask import request, jsonify
from django.http import JsonResponse
from functools import wraps


class AuthenticationError(Exception):
    pass


class ErrorResponse:
    def __init__(self, data: str | None, message: str, type: str):
        self.data = data
        self.message = message
        self.type = type

    def __str__(self):
        return f"data = {self.data}, message = {self.message}, type = {self.type}"


class Authenticate:
    def __init__(self):
        self.client = AuthClient()

    def authenticate(self, id_token: str) -> Tuple[Optional[dict], Optional[Union[AuthenticationError, ErrorResponse]]]:
        if not id_token:
            return None, AuthenticationError("Invalid Authorization header")

        try:
            response = self.user_info(id_token)
            return response, None

        # 401に対応するエラー処理
        except UnauthorizedException as e:
            error_body = e.body
            return None, ErrorResponse(error_body["data"], error_body["message"], error_body["type"])

        # 500に対応するエラー処理
        except ServiceException as e:
            error_body = e.body
            return None, ErrorResponse(error_body["data"], error_body["message"], error_body["type"])

        # 上記以外の200以外のエラー処理
        except Exception as e:
            return None, ErrorResponse("N/A", str(e), "UnexpectedError")

    def user_info(self, id_token: str) -> dict[str, Any]:
        endpoint = f"/auth/userinfo?token={id_token}"
        return self.client.api_request(UserInfoApi, "get_user_info", "GET", endpoint, token=id_token)

    # FastAPI middleware
    def fastapi_auth(self, request: Request) -> Union[dict, HTTPException]:
        auth_header = request.headers.get("Authorization", "")
        token = auth_header.replace("Bearer ", "") if "Bearer " in auth_header else ""
        user_info, error = self.authenticate(token)
        if error:
            raise HTTPException(status_code=401, detail=str(error))
        return user_info

    # Flask middleware
    def flask_auth(self, f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            token = request.headers.get('Authorization', '')
            user_info, error = self.authenticate(token)
            if error:
                return jsonify(error=str(error)), 401
            return f(user_info, *args, **kwargs)

        return decorated_function

    # Django middleware
    def django_auth(self, view_func):
        def _wrapped_view(request, *args, **kwargs):
            token = request.headers.get('Authorization', '')
            user_info, error = self.authenticate(token)
            if error:
                return JsonResponse({'error': str(error)}, status=401)
            return view_func(request, user_info, *args, **kwargs)

        return _wrapped_view

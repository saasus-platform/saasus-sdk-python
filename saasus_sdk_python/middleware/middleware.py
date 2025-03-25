from __future__ import annotations
import os

from openapi_client.exceptions import UnauthorizedException, ServiceException
from saasus_sdk_python.src.auth import UserInfoApi, UserInfo
from saasus_sdk_python.client.client import Client
from saasus_sdk_python.src.auth import ApiClient


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
        self.client = Client()
        self.base_url = os.getenv("SAASUS_BASE_URL", "https://api.saasus.io/v1")

    def authenticate(self, id_token: str, referer: str | None = None, x_saasus_referer: str | None = None) -> tuple[None, AuthenticationError] | tuple[UserInfo, None] | tuple[None, ErrorResponse]:  # noqa: E501
        if not id_token:
            return None, AuthenticationError("Invalid Authorization header")

        self.client.referer = referer
        self.client.x_saasus_referer = x_saasus_referer
        try:
            response = self.user_info(id_token)
            return response, None

        except (UnauthorizedException, ServiceException) as e:
            return None, self._create_error_response(e.body)
        except Exception as e:
            return None, ErrorResponse("N/A", str(e), "UnexpectedError")

    def user_info(self, id_token: str) -> UserInfo:
        api_client = ApiClient()
        endpoint = f"/auth/userinfo?token={id_token}"
        headers = self.client.generate_signature("GET", f"{self.client.base_url}{endpoint}")
        headers = self.client.set_referer_header(headers)
        api_client.configuration.default_headers = headers
        # 環境変数でAPIサーバーを切り替える
        api_client.configuration.host = f"{self.base_url}/auth"

        user_info = UserInfoApi(api_client=api_client).get_user_info(_headers=headers, token=id_token)
        return user_info

    @staticmethod
    def _create_error_response(body: dict) -> ErrorResponse:
        return ErrorResponse(body.get("data"), body.get("message"), body.get("type"))

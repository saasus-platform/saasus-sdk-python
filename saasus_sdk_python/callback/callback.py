import json
import os
from typing import Union

from saasus_sdk_python.client.client import Client
from saasus_sdk_python.middleware.middleware import ErrorResponse
from saasus_sdk_python.src.auth import CredentialApi, Credentials, ApiClient
from saasus_sdk_python.src.auth.exceptions import BadRequestException, UnauthorizedException, ServiceException


class Callback:
    def __init__(self):
        self.client = Client()
        self.base_url = os.getenv("SAASUS_BASE_URL", "https://api.saasus.io/v1")

    def get_auth_credentials(self, code: str, auth_type: str = "tempCodeAuth") -> Credentials:
        api_client = ApiClient()
        endpoint = f"/auth/credentials?code={code}&auth-flow={auth_type}"
        headers = self.client.generate_signature(method="GET", url=f"{self.client.base_url}{endpoint}", body=None,
                                                 headers={})
        api_client.configuration.default_headers = headers
        # 環境変数でAPIサーバーを切り替える
        api_client.configuration.host = f"{self.base_url}/auth"
        credentials = CredentialApi(api_client=api_client).get_auth_credentials(
            _headers=api_client.configuration.default_headers, code=code, auth_flow=auth_type)
        return credentials

    # refresh_tokenを使って認証するメソッド
    def get_refresh_token_auth_credentials(self, refresh_token: str, auth_type: str = "refreshTokenAuth") -> Credentials:
        api_client = ApiClient()
        # クエリパラメータの順番を入れ替えると署名生成でエラーになるので注意
        endpoint = f"/auth/credentials?auth-flow={auth_type}&refresh-token={refresh_token}"
        headers = self.client.generate_signature(method="GET", url=f"{self.client.base_url}{endpoint}", body=None,
                                                 headers={})
        api_client.configuration.default_headers = headers
        # 環境変数でAPIサーバーを切り替える
        api_client.configuration.host = f"{self.base_url}/auth"
        credentials = CredentialApi(api_client=api_client).get_auth_credentials(
            _headers=api_client.configuration.default_headers, refresh_token=refresh_token, auth_flow=auth_type)
        return credentials

    # fixme callback_route_functionという名前を変更する
    def callback_route_function(self, code: str):
        try:
            response = self.get_auth_credentials(code)
            return response
        except (BadRequestException, UnauthorizedException, ServiceException) as e:
            return self.handle_exception(e)

    @staticmethod
    def handle_exception(e: Exception) -> Union[None, ErrorResponse]:
        # 400, 401, 500のエラーをハンドリングする
        if isinstance(e, (BadRequestException, UnauthorizedException, ServiceException)):
            error_body = json.loads(e.body)
            return ErrorResponse(error_body["data"], error_body["message"], error_body["type"])
        # それ以外の場合のエラー
        else:
            return ErrorResponse(data="N/A", message=str(e), type="UnexpectedError")

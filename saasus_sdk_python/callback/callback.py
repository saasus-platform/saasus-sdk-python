import json
from typing import Any

from fastapi import HTTPException, Request

from saasus_sdk_python.client.client import AuthClient
from saasus_sdk_python.middleware.middleware import ErrorResponse
from saasus_sdk_python.api.credential_api import CredentialApi
from saasus_sdk_python.exceptions import BadRequestException, UnauthorizedException, ServiceException


class Callback:

    def __init__(self):
        self.client = AuthClient()

    def get_auth_credentials(self, code: str, auth_type: str = "tempCodeAuth") -> Any:
        endpoint = f"/auth/credentials?code={code}&auth-flow={auth_type}"
        return self.client.api_request(CredentialApi, "get_auth_credentials", "GET", endpoint, code=code,
                                       auth_flow=auth_type)

    async def callback_route_function(self, request: Request):
        code = request.query_params.get("code")
        if not code:
            raise HTTPException(status_code=400, detail="code is not provided by query parameter")

        try:
            response = self.get_auth_credentials(code)
            return response

        # 400に対応するエラー処理
        except BadRequestException as e:
            error_body = json.loads(e.body)
            return None, ErrorResponse(error_body["data"], error_body["message"], error_body["type"])

        # 401に対応するエラー処理
        except UnauthorizedException as e:
            error_body = json.loads(e.body)
            return None, ErrorResponse(data=None, message=error_body["message"], type=error_body["type"])

        # 500に対応するエラー処理
        except ServiceException as e:
            error_body = json.loads(e.body)
            return None, ErrorResponse(data=error_body["data"], message=error_body["message"], type=error_body["type"])

        # 上記以外の200以外のエラー処理
        except Exception as e:
            return None, ErrorResponse(data="N/A", message=str(e), type="UnexpectedError")


callback_instance = Callback()

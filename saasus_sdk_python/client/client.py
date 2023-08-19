from __future__ import annotations

import hashlib
import hmac
import os
import time
from typing import Any, Callable, Type
from urllib.parse import urlparse

from dotenv import load_dotenv
from saasus_sdk_python import ApiClient, AuthInfoApi, Configuration, BasicInfoApi, UserInfoApi, CredentialApi

load_dotenv()


class AuthClient:
    def __init__(self, time_provider: Callable[[], str] = lambda: time.strftime("%Y%m%d%H%M", time.gmtime())) -> None:
        self.api_key = os.getenv("SAASUS_API_KEY", "")
        self.secret_key = os.getenv("SAASUS_SECRET_KEY", "")
        self.saas_id = os.getenv("SAASUS_SAAS_ID", "")
        self.base_url = os.getenv("SAASUS_BASE_URL", "https://api.saasus.io/v1")
        self.auth_mode = os.getenv("SAASUS_AUTH_MODE", "API")
        self.code = os.getenv("CODE", "")
        self.time_provider = time_provider
        self.api_client = self.configure_api_client()

    def configure_api_client(self) -> ApiClient:
        config = Configuration()
        config.default_headers = {}
        return ApiClient(configuration=config)

    # 認証用の署名を生成する
    def generate_signature(self, method: str, url: str, body: str | None = None) -> str:
        literal = "SAASUSSIGV1"
        # テストを行う際に時間を外部から注入できるようにするためにこのような実装にしているがデフォルトでは現在時刻がUTCで入る
        timestamp = self.time_provider()
        parsed_url = urlparse(url)
        host_and_path = parsed_url.netloc + parsed_url.path
        if parsed_url.query:
            host_and_path += "?" + parsed_url.query
        msg = timestamp + self.api_key + method.upper() + host_and_path + (body if body is not None else "")
        signature_hmac = hmac.new(self.secret_key.encode(), msg=msg.encode(), digestmod=hashlib.sha256)
        return "{} Sig={}, SaaSID={}, APIKey={}".format(literal, signature_hmac.hexdigest(), self.saas_id, self.api_key)

    def api_request(self, api_class: Type[Any], api_method_name: str, method: str, endpoint: str, **kwargs) -> Any:
        """
        :param api_class: APIのクラス (BasicInfoApi, AuthInfoApiなど)
        :param api_method_name: APIのメソッド名 ('get_basic_info', 'get_auth_info'など)
        :param method: HTTPメソッド ('GET', 'POST'など)
        :param endpoint: エンドポイントのパス ('/basic_info, auth_info'など)
        :param kwargs: その他の引数
        :return: APIのレスポンス
        """
        api_client = self.get_api_client_with_signature(method, endpoint)
        api_instance = api_class(api_client)
        api_func = getattr(api_instance, api_method_name)
        return api_func(_headers=api_client.configuration.default_headers, **kwargs)

    def get_api_client_with_signature(self, method: str, path: str):
        try:
            config = Configuration()
            signature = self.generate_signature(method, self.base_url + path)
            config.default_headers = {"Authorization": signature}
            return ApiClient(configuration=config)
        except Exception as e:
            print(f"Error in get_api_client_with_signature: {e}")
            return None


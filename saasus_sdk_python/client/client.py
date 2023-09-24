from __future__ import annotations
import hashlib
import hmac
import os
import time
from typing import Any
from urllib.parse import urlparse, urlencode
from dotenv import load_dotenv
from saasus_sdk_python import ApiClient

load_dotenv()


def serialize_object(obj: Any) -> str | None:
    if hasattr(obj, 'to_json'):
        return obj.to_json()
    else:
        print("This object does not have to_json method")
        return None


class AuthClient:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.referer = None
            cls._instance.api_key = os.getenv("SAASUS_API_KEY", "")
            cls._instance.secret_key = os.getenv("SAASUS_SECRET_KEY", "")
            cls._instance.saas_id = os.getenv("SAASUS_SAAS_ID", "")
            cls._instance.base_url = os.getenv("SAASUS_BASE_URL", "https://api.saasus.io/v1")
            cls._instance.time_provider = lambda: time.strftime("%Y%m%d%H%M", time.gmtime())
        return cls._instance

    # 認証用の署名を生成する
    def generate_signature(self, method: str, url: str, body: str | None = None, headers: dict | None = None) -> dict:
        literal = "SAASUSSIGV1"
        timestamp = self.time_provider()
        parsed_url = urlparse(url)
        host_and_path = parsed_url.netloc + parsed_url.path
        if parsed_url.query:
            host_and_path += "?" + parsed_url.query
        # POSTなどリクエストボディが空でない場合はJSON文字列に変換する
        body = serialize_object(body) if body is not None else ""
        msg = timestamp + self.api_key + method.upper() + host_and_path + body
        signature_hmac = hmac.new(self.secret_key.encode(), msg=msg.encode(), digestmod=hashlib.sha256)
        headers = headers or {}
        headers["Authorization"] = f"{literal} Sig={signature_hmac.hexdigest()}, SaaSID={self.saas_id}, APIKey={self.api_key}"
        return headers

    def set_referer_header(self, header_params: dict) -> dict:
        if self.referer:
            header_params["Referer"] = self.referer
        return header_params


class SignedApiClient(ApiClient):

    def __init__(self, *args, **kwargs):
        self.auth_client = AuthClient()
        super().__init__(*args, **kwargs)

    def call_api(self, resource_path, method,
                 path_params=None, query_params=None, header_params=None,
                 body=None, post_params=None, files=None,
                 response_types_map=None, auth_settings=None,
                 async_req=None, _return_http_data_only=None,
                 collection_formats=None, _preload_content=True,
                 _request_timeout=None, _host=None, _request_auth=None):

        if path_params:
            resource_path = resource_path.format(**path_params)
        if query_params:
            query_string = urlencode(query_params)
            resource_path += f"?{query_string}"

        # リクエストを行う直前に署名を生成する
        signature_headers = self.auth_client.generate_signature(
            method, self.configuration.host + resource_path, body
        )

        # header_paramsを署名つきのヘッダで更新する。
        if header_params is None:
            header_params = {}
        header_params.update(signature_headers)

        return super().call_api(
            resource_path, method,
            path_params, query_params, header_params,
            body, post_params, files,
            response_types_map, auth_settings,
            async_req, _return_http_data_only,
            collection_formats, _preload_content,
            _request_timeout, _host, _request_auth
        )

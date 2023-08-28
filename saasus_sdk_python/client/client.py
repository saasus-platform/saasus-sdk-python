from __future__ import annotations

import hashlib
import hmac
import os
import time
import logging
from typing import Any, Callable
from urllib.parse import urlparse, urlencode

from dotenv import load_dotenv
from saasus_sdk_python import ApiClient

load_dotenv()


class AuthClient:
    def __init__(self, time_provider: Callable[[], str] = lambda: time.strftime("%Y%m%d%H%M", time.gmtime())) -> None:
        self.api_key = os.getenv("SAASUS_API_KEY", "")
        self.secret_key = os.getenv("SAASUS_SECRET_KEY", "")
        self.saas_id = os.getenv("SAASUS_SAAS_ID", "")
        self.base_url = os.getenv("SAASUS_BASE_URL", "https://api.saasus.io/v1")
        self.time_provider = time_provider

    # 認証用の署名を生成する
    def generate_signature(self, method: str, url: str, body: str | None, headers: dict | None = None, timestamp: str | None = None) -> dict | None:
        logging.info(f"Generating signature with method={method}, url={url}, body={body}, headers={headers}, timestamp={timestamp}")
        literal = "SAASUSSIGV1"
        # テストを行う際に時間を外部から注入できるようにするためにこのような実装にしているがデフォルトでは現在時刻がUTCで入る
        timestamp = timestamp if timestamp else self.time_provider()
        parsed_url = urlparse(url)
        host_and_path = parsed_url.netloc + parsed_url.path
        if parsed_url.query:
            host_and_path += "?" + parsed_url.query
        msg = timestamp + self.api_key + method.upper() + host_and_path + (body if body is not None else "")
        signature_hmac = hmac.new(self.secret_key.encode(), msg=msg.encode(), digestmod=hashlib.sha256)

        authorization = "{} Sig={}, SaaSID={}, APIKey={}".format(literal, signature_hmac.hexdigest(), self.saas_id,
                                                                 self.api_key)
        headers["Authorization"] = authorization
        return headers


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
            method, self.configuration.host + resource_path, body, {}
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


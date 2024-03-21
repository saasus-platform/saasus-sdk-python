import os
from saasus_sdk_python.client.client import Client
from urllib.parse import urlencode
from saasus_sdk_python.src.billing.api_client import ApiClient


class SignedBillingApiClient(ApiClient):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = Client()
        self.configuration.default_headers = {}
        self.base_url = os.getenv("SAASUS_BASE_URL", "https://api.saasus.io/v1")

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

        self.configuration.host = f"{self.base_url}/billing"

        # 署名ヘッダを生成してリクエストヘッダに追加する
        signature_headers = self.client.generate_signature(
            method, self.configuration.host + resource_path, body
        )

        # header_paramsを署名つきのヘッダで更新する。
        if header_params is None:
            header_params = {}
        header_params.update(signature_headers)

        # APIクライアントのcall_apiメソッドを呼び出して、署名付きのリクエストを行う
        return super().call_api(
            resource_path, method,
            path_params, query_params, header_params,
            body, post_params, files,
            response_types_map, auth_settings,
            async_req, _return_http_data_only,
            collection_formats, _preload_content,
            _request_timeout, _host, _request_auth
        )

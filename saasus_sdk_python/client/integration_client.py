import os
from saasus_sdk_python.client.client import Client
from saasus_sdk_python.src.integration.api_client import ApiClient
from saasus_sdk_python.src.integration import rest

class SignedIntegrationApiClient(ApiClient):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = Client()
        self.configuration.default_headers = {}
        self.base_url = os.getenv("SAASUS_BASE_URL", "https://api.saasus.io/v1")
        self.configuration.host = f"{self.base_url}/integration"

    def call_api(
        self,
        method,
        url,
        header_params=None,
        body=None,
        post_params=None,
        _request_timeout=None
    ) -> rest.RESTResponse:

        # 署名ヘッダを生成してリクエストヘッダに追加する
        signature_headers = self.client.generate_signature(
            method, url, body
        )

        # header_paramsを署名つきのヘッダで更新する。
        if header_params is None:
            header_params = {}
        header_params.update(signature_headers)

        # APIクライアントのcall_apiメソッドを呼び出して、署名付きのリクエストを行う
        return super().call_api(
            method=method,
            url=url,
            header_params=header_params,
            body=body,
            post_params=post_params,
            _request_timeout=_request_timeout
        )

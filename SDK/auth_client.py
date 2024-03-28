import hashlib
import hmac
import os
import time
from typing import Any
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv

load_dotenv()


class AuthClient:
    def __init__(self) -> None:
        self.api_key = os.getenv("SAASUS_API_KEY", "")
        self.secret_key = os.getenv("SAASUS_SECRET_KEY", "")
        self.saas_id = os.getenv("SAASUS_SAAS_ID", "")
        self.base_url = os.getenv("SAASUS_BASE_URL", "http://localhost:8080/v1")

    # 認証用の署名を生成する
    def _generate_signature(self, method: str, url: str, body: str | None = None) -> str:
        literal = "SAASUSSIGV1"
        now = time.strftime("%Y%m%d%H%M", time.gmtime())
        parsed_url = urlparse(url)
        host_and_path = parsed_url.netloc + parsed_url.path
        msg = now + self.api_key + method.upper() + host_and_path + (body if body is not None else "")
        signature_hmac = hmac.new(self.secret_key.encode(), msg=msg.encode(), digestmod=hashlib.sha256)
        return "{} Sig={}, SaaSID={}, APIKey={}".format(literal, signature_hmac.hexdigest(), self.saas_id, self.api_key)

    # basic-info APIにGETリクエストを送信する
    def basic_info(self) -> dict[str, Any]:
        url = f"{self.base_url}/auth/basic-info"
        method = "GET"
        signature = self._generate_signature(method, url)
        headers = {
            "Authorization": signature,
        }
        response = requests.get(url, headers=headers)
        return response.json()

from __future__ import annotations
import hashlib
import hmac
import os
import time
from typing import Any
from urllib.parse import urlparse, urlencode
from dotenv import load_dotenv

load_dotenv()


def serialize_object(obj: Any) -> str | None:
    if hasattr(obj, 'to_json'):
        return obj.to_json()
    else:
        print("This object does not have to_json method")
        return None


class Client:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.referer = None
            cls._instance.x_saasus_referer = None
            cls._instance.api_key = os.getenv("SAASUS_API_KEY", "")
            cls._instance.secret_key = os.getenv("SAASUS_SECRET_KEY", "")
            cls._instance.saas_id = os.getenv("SAASUS_SAAS_ID", "")
            cls._instance.time_provider = lambda: time.strftime("%Y%m%d%H%M", time.gmtime())
            cls._instance.base_url = os.getenv("SAASUS_BASE_URL", "https://api.saasus.io/v1")
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
        headers[
            "Authorization"] = f"{literal} Sig={signature_hmac.hexdigest()}, SaaSID={self.saas_id}, APIKey={self.api_key}"
        return headers

    def set_referer_header(self, header_params: dict) -> dict:
        if self.referer:
            header_params["Referer"] = self.referer
        if self.x_saasus_referer:
            header_params["X-SaaSus-Referer"] = self.x_saasus_referer
        return header_params

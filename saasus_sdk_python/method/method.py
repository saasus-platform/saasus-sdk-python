from __future__ import annotations

from typing import Any

from saasus_sdk_python.client.client import AuthClient
from saasus_sdk_python import TenantUserApi


class Method:
    def __init__(self):
        self.client = AuthClient()

    def get_tenant_user(self, user_id: str, tenant_id: str) -> dict[str, Any]:
        endpoint = f"/auth/tenants/{tenant_id}/users/{user_id}"
        return self.client.api_request(TenantUserApi, "get_tenant_user", "GET", endpoint, tenant_id=tenant_id,
                                       user_id=user_id)

    def get_tenant_users(self, tenant_id: str) -> dict[str, Any]:
        endpoint = f"/auth/tenants/{tenant_id}/users"
        return self.client.api_request(TenantUserApi, "get_tenant_users", "GET", endpoint, tenant_id=tenant_id)

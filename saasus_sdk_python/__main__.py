from fastapi import FastAPI, Request, Depends, HTTPException, Header
from starlette.middleware.cors import CORSMiddleware

from saasus_sdk_python import TenantUserApi
from saasus_sdk_python.callback.callback import callback_instance
from saasus_sdk_python.middleware.middleware import Authenticate
from saasus_sdk_python.method.method import Method
from saasus_sdk_python.client.client import AuthClient

from dotenv import load_dotenv

load_dotenv()
app = FastAPI()
auth = Authenticate()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/credential")
async def get_credentials(request: Request):
    return await callback_instance.callback_route_function(request)


@app.get("/userinfo")
def get_user_info(user_info: dict = Depends(auth.fastapi_auth)):
    return user_info


@app.get("/users")
def get_tenant_user_info(auth_user: dict = Depends(auth.fastapi_auth)):  # fastapi_authは前回の例で用いた認証関数です
    user_id = auth_user.id
    if not auth_user.tenants:
        raise HTTPException(status_code=400, detail="No tenants found for the user")

    tenant_id = auth_user.tenants[0].id
    print(f"Tenant ID: {tenant_id}")

    try:
        tenant_user_info = TenantUserApi(AuthClient().api_client).get_tenant_user(tenant_id=tenant_id, user_id=user_id)
        return tenant_user_info.users
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def get_tenant_user_info(auth_user: dict = Depends(auth.fastapi_auth)):  # fastapi_authは前回の例で用いた認証関数です
    user_id = auth_user.id
    print(f"User ID: {user_id}")
    if not auth_user.tenants:
        raise HTTPException(status_code=400, detail="No tenants found for the user")

    tenant_id = auth_user.tenants[0].id
    print(f"Tenant ID: {tenant_id}")

    try:
        tenant_user_info = Method().get_tenant_users(tenant_id=tenant_id)
        return tenant_user_info.users
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=80)

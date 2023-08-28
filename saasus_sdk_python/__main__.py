from fastapi import FastAPI, Request, Depends, HTTPException, Header
from starlette.middleware.cors import CORSMiddleware

from saasus_sdk_python import TenantUserApi, BasicInfoApi
from saasus_sdk_python.callback.callback import callback_instance
from saasus_sdk_python.middleware.middleware import Authenticate
from saasus_sdk_python.client.client import AuthClient, SignedApiClient

from dotenv import load_dotenv

load_dotenv()
app = FastAPI()
auth = Authenticate()
authclient = AuthClient()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ApiClientを継承したSignedApiClientを使う
api_client = SignedApiClient()


@app.get("/credential")
async def get_credentials(request: Request):
    return await callback_instance.callback_route_function(request)


@app.get("/userinfo")
def get_user_info(user_info: dict = Depends(auth.fastapi_auth)):
    return user_info


@app.get("/users")
def get_tenant_users(auth_user: dict = Depends(auth.fastapi_auth)):  # fastapi_authは前回の例で用いた認証関数です
    if not auth_user.tenants:
        raise HTTPException(status_code=400, detail="No tenants found for the user")

    tenant_id = auth_user.tenants[0].id

    try:
        tenant_user_info = TenantUserApi(api_client=api_client).get_tenant_users(tenant_id=tenant_id,
                                                                                 _headers=api_client.configuration.default_headers)

        return tenant_user_info.users
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/basicinfo")
def get_basic_info():
    basic_info = BasicInfoApi(api_client=api_client).get_basic_info(_headers=api_client.configuration.default_headers)
    return basic_info


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=80)

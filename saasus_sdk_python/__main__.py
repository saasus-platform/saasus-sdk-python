import uvicorn
from typing import Union
from fastapi import FastAPI, Request, Depends, HTTPException
from starlette.middleware.cors import CORSMiddleware

from saasus_sdk_python.src.auth import TenantUserApi, BasicInfoApi
from saasus_sdk_python.src.pricing import PricingUnitsApi
from saasus_sdk_python.src.billing import StripeApi
from saasus_sdk_python.src.awsmarketplace import AwsMarketplaceApi
from saasus_sdk_python.src.integration import EventBridgeApi
from saasus_sdk_python.src.apilog import ApiLogApi
from saasus_sdk_python.src.communication import FeedbackApi
from saasus_sdk_python.callback.callback import Callback
from saasus_sdk_python.middleware.middleware import Authenticate
from saasus_sdk_python.client.auth_client import SignedAuthApiClient
from saasus_sdk_python.client.pricing_client import SignedPricingApiClient
from saasus_sdk_python.client.billing_client import SignedBillingApiClient
from saasus_sdk_python.client.awsmarketplace_client import SignedAwsmarketplaceApiClient
from saasus_sdk_python.client.integration_client import SignedIntegrationApiClient
from saasus_sdk_python.client.apilog_client import SignedApilogApiClient
from saasus_sdk_python.client.communication_client import SignedCommunicationApiClient

from dotenv import load_dotenv

load_dotenv()
app = FastAPI()
auth = Authenticate()
callback = Callback()
# ApiClientを継承したSignedApiClientを使う
auth_api_client = SignedAuthApiClient()
pricing_api_client = SignedPricingApiClient()
billing_api_client = SignedBillingApiClient()
awsmarketplace_api_client = SignedAwsmarketplaceApiClient()
integration_api_client = SignedIntegrationApiClient()
apilog_api_client = SignedApilogApiClient()
communication_api_client = SignedCommunicationApiClient()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# FastAPI用の認証メソッド
def fastapi_auth(request: Request) -> Union[dict, HTTPException]:
    auth_header = request.headers.get("Authorization", "")
    token = auth_header.replace("Bearer ", "") if "Bearer " in auth_header else ""
    referer = request.headers.get("Referer", "")
    user_info, error = auth.authenticate(id_token=token, referer=referer)
    if error:
        raise HTTPException(status_code=401, detail=str(error))
    return user_info


# 一時コードを取得する
def get_temp_code(request: Request):
    code = request.query_params.get("code")
    if not code:
        raise HTTPException(status_code=400, detail="code is not provided by query parameter")
    return code


# refresh tokenを取得する
def get_refresh_token(request: Request):
    refresh_token = request.query_params.get("refreshtoken")
    if not refresh_token:
        raise HTTPException(status_code=400, detail="refresh_token is not provided by query parameter")
    return refresh_token


@app.get("/credentials")
def get_credentials(request: Request):
    return callback.callback_route_function(get_temp_code(request))


@app.get("/userinfo")
def get_user_info(user_info: dict = Depends(fastapi_auth)):
    return user_info


@app.get("/users")
def get_tenant_users(auth_user: dict = Depends(fastapi_auth)):
    if not auth_user.tenants:
        raise HTTPException(status_code=400, detail="No tenants found for the user")

    tenant_id = auth_user.tenants[0].id

    try:
        tenant_user_info = TenantUserApi(api_client=auth_api_client).get_tenant_users(tenant_id=tenant_id,
                                                                                      _headers=auth_api_client.configuration.default_headers)
        return tenant_user_info.users

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/refresh")
def get_refresh(request: Request):
    return callback.get_refresh_token_auth_credentials(get_refresh_token(request))


@app.get("/basic-info")
def get_basic_info():
    basic_info = BasicInfoApi(api_client=auth_api_client).get_basic_info(
        _headers=auth_api_client.configuration.default_headers)
    return basic_info


@app.get("/units")
def get_pricing_units():
    pricing_units = PricingUnitsApi(api_client=pricing_api_client).get_pricing_units(
        _headers=pricing_api_client.configuration.default_headers)
    return pricing_units


@app.get("/stripe/info")
def get_stripe_info():
    stripe_info = StripeApi(api_client=billing_api_client).get_stripe_info(
        _headers=billing_api_client.configuration.default_headers)
    return stripe_info


@app.get("/settings")
def get_settings():
    settings = AwsMarketplaceApi(api_client=awsmarketplace_api_client).get_settings(
        _headers=awsmarketplace_api_client.configuration.default_headers)
    return settings


@app.get("/eventbridge/info")
def event_bridge_info():
    # TODO うまく動いていないのでなおす
    event_bridge_settings = EventBridgeApi(api_client=integration_api_client).get_event_bridge_settings(
        _headers=integration_api_client.configuration.default_headers)
    return event_bridge_settings


@app.get("/logs")
def get_apilogs():
    logs = ApiLogApi(api_client=apilog_api_client).get_logs(
        _headers=apilog_api_client.configuration.default_headers)
    return logs


@app.get("/feedbacks")
def get_feedbacks():
    feedbacks = FeedbackApi(api_client=communication_api_client).get_feedbacks(
        _headers=communication_api_client.configuration.default_headers)
    return feedbacks


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)

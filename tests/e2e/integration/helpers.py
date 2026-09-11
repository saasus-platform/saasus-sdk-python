"""Integration (EventBridge) E2E test helper functions.

JavaScriptのintegration/helpers.tsを参考にしたペイロードビルダー群。
"""

import json
import os
import uuid

from saasus_sdk_python.src.integration.models.aws_region import AwsRegion
from saasus_sdk_python.src.integration.models.create_event_bridge_event_param import (
    CreateEventBridgeEventParam,
)
from saasus_sdk_python.src.integration.models.event_bridge_settings import EventBridgeSettings
from saasus_sdk_python.src.integration.models.event_message import EventMessage

DEFAULT_ACCOUNT_ID = "267185063265"
DEFAULT_REGION = "ap-northeast-1"


def get_test_aws_account_id() -> str:
    value = os.getenv("TEST_AWS_ACCOUNT_ID")
    return value if value else DEFAULT_ACCOUNT_ID


def get_test_aws_region() -> AwsRegion:
    value = os.getenv("TEST_AWS_REGION") or DEFAULT_REGION
    return AwsRegion(value)


def generate_test_event_message() -> EventMessage:
    return EventMessage(
        event_type="api_call",
        event_detail_type="create_user",
        message=json.dumps({"id": uuid.uuid4().hex, "name": "integration-e2e"}),
    )


def create_event_bridge_settings_param() -> EventBridgeSettings:
    return EventBridgeSettings(
        aws_account_id=get_test_aws_account_id(),
        aws_region=get_test_aws_region(),
    )


def create_event_bridge_event_param() -> CreateEventBridgeEventParam:
    return CreateEventBridgeEventParam(event_messages=[generate_test_event_message()])

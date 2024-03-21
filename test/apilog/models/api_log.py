# coding: utf-8

"""
    SaaSus ApiLog API Schema

    SaaSus ApiLog API Schema

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json



from pydantic import BaseModel, Field, StrictInt, StrictStr

class ApiLog(BaseModel):
    """
    ApiLog
    """
    trace_id: StrictStr = Field(..., description="Trace ID")
    api_log_id: StrictStr = Field(...)
    created_at: StrictInt = Field(..., description="Epoch second of API log registration timestamp")
    created_date: StrictStr = Field(..., description="API log registration date")
    ttl: StrictInt = Field(..., description="Epoch second of planned API log deletion")
    request_method: StrictStr = Field(..., description="Request method")
    saas_id: StrictStr = Field(...)
    api_key: StrictStr = Field(..., description="API Key")
    response_status: StrictStr = Field(..., description="Response status")
    request_uri: StrictStr = Field(..., description="Request URI")
    remote_address: StrictStr = Field(..., description="Client IP Address")
    referer: StrictStr = Field(..., description="The referrer of the request")
    request_body: StrictStr = Field(..., description="The body of the request")
    response_body: StrictStr = Field(..., description="The body of the response")
    __properties = ["trace_id", "api_log_id", "created_at", "created_date", "ttl", "request_method", "saas_id", "api_key", "response_status", "request_uri", "remote_address", "referer", "request_body", "response_body"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ApiLog:
        """Create an instance of ApiLog from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiLog:
        """Create an instance of ApiLog from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiLog.parse_obj(obj)

        _obj = ApiLog.parse_obj({
            "trace_id": obj.get("trace_id"),
            "api_log_id": obj.get("api_log_id"),
            "created_at": obj.get("created_at"),
            "created_date": obj.get("created_date"),
            "ttl": obj.get("ttl"),
            "request_method": obj.get("request_method"),
            "saas_id": obj.get("saas_id"),
            "api_key": obj.get("api_key"),
            "response_status": obj.get("response_status"),
            "request_uri": obj.get("request_uri"),
            "remote_address": obj.get("remote_address"),
            "referer": obj.get("referer"),
            "request_body": obj.get("request_body"),
            "response_body": obj.get("response_body")
        })
        return _obj



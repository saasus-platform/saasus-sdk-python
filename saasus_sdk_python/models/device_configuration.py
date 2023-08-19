# coding: utf-8

"""
    SaaSus Auth API Schema

    スキーマ

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json



from pydantic import BaseModel, Field, StrictStr, validator

class DeviceConfiguration(BaseModel):
    """
    信頼済みデバイスの記憶の設定(settings for remembering trusted devices) 
    """
    device_remembering: StrictStr = Field(..., description="always: 常に記憶する(always remember) userOptIn: ユーザーオプトイン(user opt-in) no: (don't save) ")
    __properties = ["device_remembering"]

    @validator('device_remembering')
    def device_remembering_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('always', 'userOptIn', 'no'):
            raise ValueError("must be one of enum values ('always', 'userOptIn', 'no')")
        return value

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
    def from_json(cls, json_str: str) -> DeviceConfiguration:
        """Create an instance of DeviceConfiguration from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DeviceConfiguration:
        """Create an instance of DeviceConfiguration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DeviceConfiguration.parse_obj(obj)

        _obj = DeviceConfiguration.parse_obj({
            "device_remembering": obj.get("device_remembering")
        })
        return _obj



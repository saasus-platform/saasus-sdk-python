# coding: utf-8

"""
    SaaSus Auth API Schema

    Schema

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import field_validator, ConfigDict, BaseModel, Field, StrictBool, StrictStr

class MfaPreference(BaseModel):
    """
    MfaPreference
    """
    enabled: StrictBool = Field(..., description="enable MFA")
    method: Optional[StrictStr] = Field(None, description="MFA method (required if enabled is true)")
    __properties = ["enabled", "method"]

    @field_validator('method')
    @classmethod
    def method_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('softwareToken'):
            raise ValueError("must be one of enum values ('softwareToken')")
        return value
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> MfaPreference:
        """Create an instance of MfaPreference from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MfaPreference:
        """Create an instance of MfaPreference from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MfaPreference.parse_obj(obj)

        _obj = MfaPreference.parse_obj({
            "enabled": obj.get("enabled"),
            "method": obj.get("method")
        })
        return _obj



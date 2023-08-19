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



from pydantic import BaseModel, Field, StrictStr

class IdentityProviderProps(BaseModel):
    """
    IdentityProviderProps
    """
    application_id: StrictStr = Field(...)
    application_secret: StrictStr = Field(...)
    approval_scope: StrictStr = Field(...)
    __properties = ["application_id", "application_secret", "approval_scope"]

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
    def from_json(cls, json_str: str) -> IdentityProviderProps:
        """Create an instance of IdentityProviderProps from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> IdentityProviderProps:
        """Create an instance of IdentityProviderProps from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return IdentityProviderProps.parse_obj(obj)

        _obj = IdentityProviderProps.parse_obj({
            "application_id": obj.get("application_id"),
            "application_secret": obj.get("application_secret"),
            "approval_scope": obj.get("approval_scope")
        })
        return _obj



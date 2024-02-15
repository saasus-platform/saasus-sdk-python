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



from pydantic import BaseModel, Field
from saasus_sdk_python.src.auth.models.identity_provider_props import IdentityProviderProps

class IdentityProviders(BaseModel):
    """
    IdentityProviders
    """
    google: IdentityProviderProps = Field(...)
    __properties = ["google"]

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
    def from_json(cls, json_str: str) -> IdentityProviders:
        """Create an instance of IdentityProviders from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of google
        if self.google:
            _dict['google'] = self.google.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> IdentityProviders:
        """Create an instance of IdentityProviders from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return IdentityProviders.parse_obj(obj)

        _obj = IdentityProviders.parse_obj({
            "google": IdentityProviderProps.from_dict(obj.get("google")) if obj.get("google") is not None else None
        })
        return _obj


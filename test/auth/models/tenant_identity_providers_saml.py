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

class TenantIdentityProvidersSaml(BaseModel):
    """
    TenantIdentityProvidersSaml
    """
    metadata_url: StrictStr = Field(...)
    email_attribute: StrictStr = Field(...)
    sign_in_url: StrictStr = Field(...)
    __properties = ["metadata_url", "email_attribute", "sign_in_url"]

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
    def from_json(cls, json_str: str) -> TenantIdentityProvidersSaml:
        """Create an instance of TenantIdentityProvidersSaml from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TenantIdentityProvidersSaml:
        """Create an instance of TenantIdentityProvidersSaml from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TenantIdentityProvidersSaml.parse_obj(obj)

        _obj = TenantIdentityProvidersSaml.parse_obj({
            "metadata_url": obj.get("metadata_url"),
            "email_attribute": obj.get("email_attribute"),
            "sign_in_url": obj.get("sign_in_url")
        })
        return _obj



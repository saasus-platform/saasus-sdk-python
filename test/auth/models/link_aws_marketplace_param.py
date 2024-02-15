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

class LinkAwsMarketplaceParam(BaseModel):
    """
    LinkAwsMarketplaceParam
    """
    tenant_id: StrictStr = Field(..., description="テナントID(tenant ID)")
    access_token: StrictStr = Field(..., description="アクセストークン(access token)")
    registration_token: StrictStr = Field(..., description="Registration Token")
    __properties = ["tenant_id", "access_token", "registration_token"]

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
    def from_json(cls, json_str: str) -> LinkAwsMarketplaceParam:
        """Create an instance of LinkAwsMarketplaceParam from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LinkAwsMarketplaceParam:
        """Create an instance of LinkAwsMarketplaceParam from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LinkAwsMarketplaceParam.parse_obj(obj)

        _obj = LinkAwsMarketplaceParam.parse_obj({
            "tenant_id": obj.get("tenant_id"),
            "access_token": obj.get("access_token"),
            "registration_token": obj.get("registration_token")
        })
        return _obj



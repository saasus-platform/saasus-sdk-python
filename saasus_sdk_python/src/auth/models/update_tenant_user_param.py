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


from typing import Any, Dict
from pydantic import ConfigDict, BaseModel, Field

class UpdateTenantUserParam(BaseModel):
    """
    UpdateTenantUserParam
    """
    attributes: Dict[str, Any] = Field(..., description="Attribute information (Get information set by defining user attributes in the SaaS development console) ")
    __properties = ["attributes"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> UpdateTenantUserParam:
        """Create an instance of UpdateTenantUserParam from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UpdateTenantUserParam:
        """Create an instance of UpdateTenantUserParam from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UpdateTenantUserParam.parse_obj(obj)

        _obj = UpdateTenantUserParam.parse_obj({
            "attributes": obj.get("attributes")
        })
        return _obj



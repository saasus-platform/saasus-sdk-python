# coding: utf-8

"""
    SaaSus Pricing API Schema

    SaaSus Pricing API Schema

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List
from pydantic import ConfigDict, BaseModel, Field, StrictStr
from typing_extensions import Annotated

class UpdatePricingPlansUsedParam(BaseModel):
    """
    UpdatePricingPlansUsedParam
    """
    plan_ids: Annotated[List[StrictStr], Field()] = Field(...)
    __properties = ["plan_ids"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> UpdatePricingPlansUsedParam:
        """Create an instance of UpdatePricingPlansUsedParam from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UpdatePricingPlansUsedParam:
        """Create an instance of UpdatePricingPlansUsedParam from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UpdatePricingPlansUsedParam.parse_obj(obj)

        _obj = UpdatePricingPlansUsedParam.parse_obj({
            "plan_ids": obj.get("plan_ids")
        })
        return _obj



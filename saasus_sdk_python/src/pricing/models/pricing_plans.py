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
from pydantic import BaseModel, Field, conlist
from saasus_sdk_python.src.pricing.models.pricing_plan import PricingPlan

class PricingPlans(BaseModel):
    """
    PricingPlans
    """
    pricing_plans: conlist(PricingPlan) = Field(...)
    __properties = ["pricing_plans"]

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
    def from_json(cls, json_str: str) -> PricingPlans:
        """Create an instance of PricingPlans from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in pricing_plans (list)
        _items = []
        if self.pricing_plans:
            for _item in self.pricing_plans:
                if _item:
                    _items.append(_item.to_dict())
            _dict['pricing_plans'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PricingPlans:
        """Create an instance of PricingPlans from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PricingPlans.parse_obj(obj)

        _obj = PricingPlans.parse_obj({
            "pricing_plans": [PricingPlan.from_dict(_item) for _item in obj.get("pricing_plans")] if obj.get("pricing_plans") is not None else None
        })
        return _obj


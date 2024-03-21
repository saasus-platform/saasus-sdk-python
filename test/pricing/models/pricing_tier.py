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



from pydantic import BaseModel, Field, StrictBool, StrictInt

class PricingTier(BaseModel):
    """
    PricingTier
    """
    up_to: StrictInt = Field(..., description="Upper limit")
    unit_amount: StrictInt = Field(..., description="Amount per unit")
    flat_amount: StrictInt = Field(..., description="Fixed amount")
    inf: StrictBool = Field(..., description="Indefinite")
    __properties = ["up_to", "unit_amount", "flat_amount", "inf"]

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
    def from_json(cls, json_str: str) -> PricingTier:
        """Create an instance of PricingTier from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PricingTier:
        """Create an instance of PricingTier from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PricingTier.parse_obj(obj)

        _obj = PricingTier.parse_obj({
            "up_to": obj.get("up_to"),
            "unit_amount": obj.get("unit_amount"),
            "flat_amount": obj.get("flat_amount"),
            "inf": obj.get("inf")
        })
        return _obj



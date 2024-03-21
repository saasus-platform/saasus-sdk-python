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
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist
from saasus_sdk_python.src.pricing.models.pricing_unit import PricingUnit

class PricingMenu(BaseModel):
    """
    PricingMenu
    """
    name: StrictStr = Field(..., description="Menu name")
    display_name: StrictStr = Field(..., description="Menu display name")
    description: StrictStr = Field(..., description="Menu description")
    used: StrictBool = Field(..., description="Menu used settings")
    units: conlist(PricingUnit) = Field(...)
    id: StrictStr = Field(..., description="Universally Unique Identifier")
    __properties = ["name", "display_name", "description", "used", "units", "id"]

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
    def from_json(cls, json_str: str) -> PricingMenu:
        """Create an instance of PricingMenu from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in units (list)
        _items = []
        if self.units:
            for _item in self.units:
                if _item:
                    _items.append(_item.to_dict())
            _dict['units'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PricingMenu:
        """Create an instance of PricingMenu from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PricingMenu.parse_obj(obj)

        _obj = PricingMenu.parse_obj({
            "name": obj.get("name"),
            "display_name": obj.get("display_name"),
            "description": obj.get("description"),
            "used": obj.get("used"),
            "units": [PricingUnit.from_dict(_item) for _item in obj.get("units")] if obj.get("units") is not None else None,
            "id": obj.get("id")
        })
        return _obj



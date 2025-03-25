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
from pydantic import ConfigDict, BaseModel, Field, StrictBool, StrictStr
from saasus_sdk_python.src.pricing.models.pricing_menu import PricingMenu
from typing_extensions import Annotated

class PricingPlan(BaseModel):
    """
    PricingPlan
    """
    name: StrictStr = Field(..., description="Pricing plan name")
    display_name: StrictStr = Field(..., description="Pricing plan display name")
    description: StrictStr = Field(..., description="Pricing plan description")
    used: StrictBool = Field(..., description="Pricing plan used settings")
    pricing_menus: Annotated[List[PricingMenu], Field()] = Field(...)
    id: StrictStr = Field(..., description="Universally Unique Identifier")
    __properties = ["name", "display_name", "description", "used", "pricing_menus", "id"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> PricingPlan:
        """Create an instance of PricingPlan from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in pricing_menus (list)
        _items = []
        if self.pricing_menus:
            for _item in self.pricing_menus:
                if _item:
                    _items.append(_item.to_dict())
            _dict['pricing_menus'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PricingPlan:
        """Create an instance of PricingPlan from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PricingPlan.parse_obj(obj)

        _obj = PricingPlan.parse_obj({
            "name": obj.get("name"),
            "display_name": obj.get("display_name"),
            "description": obj.get("description"),
            "used": obj.get("used"),
            "pricing_menus": [PricingMenu.from_dict(_item) for _item in obj.get("pricing_menus")] if obj.get("pricing_menus") is not None else None,
            "id": obj.get("id")
        })
        return _obj



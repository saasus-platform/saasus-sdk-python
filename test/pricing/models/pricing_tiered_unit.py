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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist
from saasus_sdk_python.src.pricing.models.aggregate_usage import AggregateUsage
from saasus_sdk_python.src.pricing.models.currency import Currency
from saasus_sdk_python.src.pricing.models.pricing_tier import PricingTier
from saasus_sdk_python.src.pricing.models.recurring_interval import RecurringInterval
from saasus_sdk_python.src.pricing.models.unit_type import UnitType

class PricingTieredUnit(BaseModel):
    """
    PricingTieredUnit
    """
    upper_count: StrictInt = Field(..., description="上限値(upper limit)")
    metering_unit_name: StrictStr = Field(...)
    aggregate_usage: Optional[AggregateUsage] = None
    name: StrictStr = Field(..., description="名前(name)")
    display_name: StrictStr = Field(..., description="表示名(display name)")
    description: StrictStr = Field(..., description="説明(description)")
    type: UnitType = Field(...)
    currency: Currency = Field(...)
    tiers: conlist(PricingTier) = Field(...)
    id: StrictStr = Field(...)
    metering_unit_id: StrictStr = Field(...)
    recurring_interval: RecurringInterval = Field(...)
    used: StrictBool = Field(...)
    __properties = ["upper_count", "metering_unit_name", "aggregate_usage", "name", "display_name", "description", "type", "currency", "tiers", "id", "metering_unit_id", "recurring_interval", "used"]

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
    def from_json(cls, json_str: str) -> PricingTieredUnit:
        """Create an instance of PricingTieredUnit from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in tiers (list)
        _items = []
        if self.tiers:
            for _item in self.tiers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['tiers'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PricingTieredUnit:
        """Create an instance of PricingTieredUnit from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PricingTieredUnit.parse_obj(obj)

        _obj = PricingTieredUnit.parse_obj({
            "upper_count": obj.get("upper_count"),
            "metering_unit_name": obj.get("metering_unit_name"),
            "aggregate_usage": obj.get("aggregate_usage"),
            "name": obj.get("name"),
            "display_name": obj.get("display_name"),
            "description": obj.get("description"),
            "type": obj.get("type"),
            "currency": obj.get("currency"),
            "tiers": [PricingTier.from_dict(_item) for _item in obj.get("tiers")] if obj.get("tiers") is not None else None,
            "id": obj.get("id"),
            "metering_unit_id": obj.get("metering_unit_id"),
            "recurring_interval": obj.get("recurring_interval"),
            "used": obj.get("used")
        })
        return _obj



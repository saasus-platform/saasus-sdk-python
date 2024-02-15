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
from pydantic import BaseModel, Field, StrictStr, conlist
from saasus_sdk_python.src.pricing.models.metering_unit_count import MeteringUnitCount

class MeteringUnitDatePeriodCounts(BaseModel):
    """
    MeteringUnitDatePeriodCounts
    """
    metering_unit_name: StrictStr = Field(..., description="計測ユニット名(metering unit name)")
    counts: conlist(MeteringUnitCount) = Field(...)
    __properties = ["metering_unit_name", "counts"]

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
    def from_json(cls, json_str: str) -> MeteringUnitDatePeriodCounts:
        """Create an instance of MeteringUnitDatePeriodCounts from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in counts (list)
        _items = []
        if self.counts:
            for _item in self.counts:
                if _item:
                    _items.append(_item.to_dict())
            _dict['counts'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MeteringUnitDatePeriodCounts:
        """Create an instance of MeteringUnitDatePeriodCounts from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MeteringUnitDatePeriodCounts.parse_obj(obj)

        _obj = MeteringUnitDatePeriodCounts.parse_obj({
            "metering_unit_name": obj.get("metering_unit_name"),
            "counts": [MeteringUnitCount.from_dict(_item) for _item in obj.get("counts")] if obj.get("counts") is not None else None
        })
        return _obj



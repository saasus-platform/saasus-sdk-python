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
from pydantic import ConfigDict, BaseModel, Field
from saasus_sdk_python.src.pricing.models.metering_unit_date_count import MeteringUnitDateCount
from typing_extensions import Annotated

class MeteringUnitDateCounts(BaseModel):
    """
    MeteringUnitDateCounts
    """
    counts: Annotated[List[MeteringUnitDateCount], Field()] = Field(...)
    __properties = ["counts"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> MeteringUnitDateCounts:
        """Create an instance of MeteringUnitDateCounts from a JSON string"""
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
    def from_dict(cls, obj: dict) -> MeteringUnitDateCounts:
        """Create an instance of MeteringUnitDateCounts from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MeteringUnitDateCounts.parse_obj(obj)

        _obj = MeteringUnitDateCounts.parse_obj({
            "counts": [MeteringUnitDateCount.from_dict(_item) for _item in obj.get("counts")] if obj.get("counts") is not None else None
        })
        return _obj



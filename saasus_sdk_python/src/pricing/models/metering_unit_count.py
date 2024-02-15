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



from pydantic import BaseModel, Field, StrictInt

class MeteringUnitCount(BaseModel):
    """
    MeteringUnitCount
    """
    timestamp: StrictInt = Field(..., description="日時(timestamp)")
    count: StrictInt = Field(..., description="件数(count)")
    __properties = ["timestamp", "count"]

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
    def from_json(cls, json_str: str) -> MeteringUnitCount:
        """Create an instance of MeteringUnitCount from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MeteringUnitCount:
        """Create an instance of MeteringUnitCount from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MeteringUnitCount.parse_obj(obj)

        _obj = MeteringUnitCount.parse_obj({
            "timestamp": obj.get("timestamp"),
            "count": obj.get("count")
        })
        return _obj


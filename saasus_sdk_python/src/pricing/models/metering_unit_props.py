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



from pydantic import BaseModel, Field, StrictStr
from saasus_sdk_python.src.pricing.models.aggregate_usage import AggregateUsage

class MeteringUnitProps(BaseModel):
    """
    MeteringUnitProps
    """
    unit_name: StrictStr = Field(..., description="計測ユニット名(metering unit name)")
    aggregate_usage: AggregateUsage = Field(...)
    display_name: StrictStr = Field(..., description="表示名(display name)")
    description: StrictStr = Field(..., description="説明(description)")
    __properties = ["unit_name", "aggregate_usage", "display_name", "description"]

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
    def from_json(cls, json_str: str) -> MeteringUnitProps:
        """Create an instance of MeteringUnitProps from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MeteringUnitProps:
        """Create an instance of MeteringUnitProps from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MeteringUnitProps.parse_obj(obj)

        _obj = MeteringUnitProps.parse_obj({
            "unit_name": obj.get("unit_name"),
            "aggregate_usage": obj.get("aggregate_usage"),
            "display_name": obj.get("display_name"),
            "description": obj.get("description")
        })
        return _obj



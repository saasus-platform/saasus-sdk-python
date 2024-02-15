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
from saasus_sdk_python.src.pricing.models.update_metering_unit_timestamp_count_method import UpdateMeteringUnitTimestampCountMethod

class UpdateMeteringUnitTimestampCountParam(BaseModel):
    """
    UpdateMeteringUnitTimestampCountParam
    """
    method: UpdateMeteringUnitTimestampCountMethod = Field(...)
    count: StrictInt = Field(..., description="件数(count)")
    __properties = ["method", "count"]

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
    def from_json(cls, json_str: str) -> UpdateMeteringUnitTimestampCountParam:
        """Create an instance of UpdateMeteringUnitTimestampCountParam from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UpdateMeteringUnitTimestampCountParam:
        """Create an instance of UpdateMeteringUnitTimestampCountParam from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UpdateMeteringUnitTimestampCountParam.parse_obj(obj)

        _obj = UpdateMeteringUnitTimestampCountParam.parse_obj({
            "method": obj.get("method"),
            "count": obj.get("count")
        })
        return _obj



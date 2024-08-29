# coding: utf-8

"""
    SaaSus Auth API Schema

    Schema

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json



from pydantic import ConfigDict, BaseModel, Field, StrictBool

class SelfRegist(BaseModel):
    """
    self sign-up permission
    """
    enable: StrictBool = Field(...)
    __properties = ["enable"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> SelfRegist:
        """Create an instance of SelfRegist from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SelfRegist:
        """Create an instance of SelfRegist from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SelfRegist.parse_obj(obj)

        _obj = SelfRegist.parse_obj({
            "enable": obj.get("enable")
        })
        return _obj



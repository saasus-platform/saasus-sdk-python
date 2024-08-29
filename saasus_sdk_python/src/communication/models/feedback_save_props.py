# coding: utf-8

"""
    SaaSus Communication API Schema

    SaaSus Communication API Schema

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json



from pydantic import ConfigDict, BaseModel, Field, StrictStr

class FeedbackSaveProps(BaseModel):
    """
    FeedbackSaveProps
    """
    feedback_title: StrictStr = Field(...)
    feedback_description: StrictStr = Field(...)
    __properties = ["feedback_title", "feedback_description"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> FeedbackSaveProps:
        """Create an instance of FeedbackSaveProps from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FeedbackSaveProps:
        """Create an instance of FeedbackSaveProps from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FeedbackSaveProps.parse_obj(obj)

        _obj = FeedbackSaveProps.parse_obj({
            "feedback_title": obj.get("feedback_title"),
            "feedback_description": obj.get("feedback_description")
        })
        return _obj



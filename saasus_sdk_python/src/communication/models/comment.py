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



from pydantic import BaseModel, Field, StrictInt, StrictStr

class Comment(BaseModel):
    """
    Comment
    """
    id: StrictStr = Field(...)
    user_id: StrictStr = Field(...)
    created_at: StrictInt = Field(...)
    body: StrictStr = Field(...)
    __properties = ["id", "user_id", "created_at", "body"]

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
    def from_json(cls, json_str: str) -> Comment:
        """Create an instance of Comment from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Comment:
        """Create an instance of Comment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Comment.parse_obj(obj)

        _obj = Comment.parse_obj({
            "id": obj.get("id"),
            "user_id": obj.get("user_id"),
            "created_at": obj.get("created_at"),
            "body": obj.get("body")
        })
        return _obj


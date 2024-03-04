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


from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel, StrictInt, StrictStr
from saasus_sdk_python.src.communication.models.comment import Comment
from saasus_sdk_python.src.communication.models.user import User
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Feedback(BaseModel):
    """
    Feedback
    """ # noqa: E501
    feedback_title: StrictStr
    feedback_description: StrictStr
    comments: List[Comment]
    count: StrictInt
    users: List[User]
    id: StrictStr
    user_id: StrictStr
    created_at: StrictInt
    status: StrictInt
    __properties: ClassVar[List[str]] = ["feedback_title", "feedback_description", "comments", "count", "users", "id", "user_id", "created_at", "status"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Feedback from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in comments (list)
        _items = []
        if self.comments:
            for _item in self.comments:
                if _item:
                    _items.append(_item.to_dict())
            _dict['comments'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in users (list)
        _items = []
        if self.users:
            for _item in self.users:
                if _item:
                    _items.append(_item.to_dict())
            _dict['users'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Feedback from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "feedback_title": obj.get("feedback_title"),
            "feedback_description": obj.get("feedback_description"),
            "comments": [Comment.from_dict(_item) for _item in obj.get("comments")] if obj.get("comments") is not None else None,
            "count": obj.get("count"),
            "users": [User.from_dict(_item) for _item in obj.get("users")] if obj.get("users") is not None else None,
            "id": obj.get("id"),
            "user_id": obj.get("user_id"),
            "created_at": obj.get("created_at"),
            "status": obj.get("status")
        })
        return _obj



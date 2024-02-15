# coding: utf-8

"""
    SaaSus Auth API Schema

    スキーマ

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist
from saasus_sdk_python.src.auth.models.invitation_status import InvitationStatus
from saasus_sdk_python.src.auth.models.user_available_env import UserAvailableEnv

class Invitation(BaseModel):
    """
    Invitation
    """
    id: StrictStr = Field(...)
    email: StrictStr = Field(..., description="招待されたユーザーのメールアドレス(email address of the invited user)")
    invitation_url: StrictStr = Field(..., description="招待URL(invitation URL)")
    envs: conlist(UserAvailableEnv) = Field(...)
    expired_at: StrictInt = Field(..., description="招待の有効期限(expiration date of the invitation)")
    status: InvitationStatus = Field(...)
    __properties = ["id", "email", "invitation_url", "envs", "expired_at", "status"]

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
    def from_json(cls, json_str: str) -> Invitation:
        """Create an instance of Invitation from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in envs (list)
        _items = []
        if self.envs:
            for _item in self.envs:
                if _item:
                    _items.append(_item.to_dict())
            _dict['envs'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Invitation:
        """Create an instance of Invitation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Invitation.parse_obj(obj)

        _obj = Invitation.parse_obj({
            "id": obj.get("id"),
            "email": obj.get("email"),
            "invitation_url": obj.get("invitation_url"),
            "envs": [UserAvailableEnv.from_dict(_item) for _item in obj.get("envs")] if obj.get("envs") is not None else None,
            "expired_at": obj.get("expired_at"),
            "status": obj.get("status")
        })
        return _obj


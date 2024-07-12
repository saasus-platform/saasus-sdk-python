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


from typing import Any, Dict, List, Optional
from pydantic import ConfigDict, BaseModel, Field, StrictBool, StrictStr
from saasus_sdk_python.src.auth.models.user_available_env import UserAvailableEnv
from typing_extensions import Annotated

class UserAvailableTenant(BaseModel):
    """
    UserAvailableTenant
    """
    id: StrictStr = Field(...)
    name: StrictStr = Field(..., description="Tenant Name")
    completed_sign_up: StrictBool = Field(...)
    envs: Annotated[List[UserAvailableEnv], Field()] = Field(..., description="environmental info, role info")
    user_attribute: Dict[str, Any] = Field(..., description="user additional attributes")
    back_office_staff_email: StrictStr = Field(..., description="back office contact email")
    plan_id: Optional[StrictStr] = None
    is_paid: Optional[StrictBool] = Field(None, description="tenant payment status ※ Currently, it is returned only when stripe is linked. ")
    __properties = ["id", "name", "completed_sign_up", "envs", "user_attribute", "back_office_staff_email", "plan_id", "is_paid"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> UserAvailableTenant:
        """Create an instance of UserAvailableTenant from a JSON string"""
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
    def from_dict(cls, obj: dict) -> UserAvailableTenant:
        """Create an instance of UserAvailableTenant from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UserAvailableTenant.parse_obj(obj)

        _obj = UserAvailableTenant.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "completed_sign_up": obj.get("completed_sign_up"),
            "envs": [UserAvailableEnv.from_dict(_item) for _item in obj.get("envs")] if obj.get("envs") is not None else None,
            "user_attribute": obj.get("user_attribute"),
            "back_office_staff_email": obj.get("back_office_staff_email"),
            "plan_id": obj.get("plan_id"),
            "is_paid": obj.get("is_paid")
        })
        return _obj



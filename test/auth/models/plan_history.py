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


from typing import Optional
from pydantic import ConfigDict, BaseModel, Field, StrictBool, StrictInt, StrictStr
from saasus_sdk_python.src.auth.models.proration_behavior import ProrationBehavior

class PlanHistory(BaseModel):
    """
    PlanHistory
    """
    plan_id: StrictStr = Field(...)
    plan_applied_at: StrictInt = Field(..., description="Registration date")
    tax_rate_id: Optional[StrictStr] = None
    proration_behavior: Optional[ProrationBehavior] = None
    delete_usage: Optional[StrictBool] = Field(None, description="If you have a stripe linkage,  you can set whether to delete pay-as-you-go items when changing plans. When you change plan, you can remove all pay-as-you-go items included in your current subscription to stop being billed based on pay-as-you-go items. The recorded usage is cleared immediately. Since it cannot be restored, please note that plan change reservations with delete_usage set to true cannot be canceled. ")
    __properties = ["plan_id", "plan_applied_at", "tax_rate_id", "proration_behavior", "delete_usage"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> PlanHistory:
        """Create an instance of PlanHistory from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PlanHistory:
        """Create an instance of PlanHistory from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PlanHistory.parse_obj(obj)

        _obj = PlanHistory.parse_obj({
            "plan_id": obj.get("plan_id"),
            "plan_applied_at": obj.get("plan_applied_at"),
            "tax_rate_id": obj.get("tax_rate_id"),
            "proration_behavior": obj.get("proration_behavior"),
            "delete_usage": obj.get("delete_usage")
        })
        return _obj



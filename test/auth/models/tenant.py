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
from pydantic import ConfigDict, BaseModel, Field, StrictBool, StrictInt, StrictStr
from saasus_sdk_python.src.auth.models.billing_info import BillingInfo
from saasus_sdk_python.src.auth.models.plan_history import PlanHistory
from saasus_sdk_python.src.auth.models.proration_behavior import ProrationBehavior
from typing_extensions import Annotated

class Tenant(BaseModel):
    """
    Tenant
    """
    name: StrictStr = Field(..., description="tenant name")
    attributes: Dict[str, Any] = Field(..., description="attribute info")
    back_office_staff_email: StrictStr = Field(..., description="administrative staff email address")
    next_plan_id: Optional[StrictStr] = None
    using_next_plan_from: Optional[StrictInt] = Field(None, description="Next billing plan start time (When using stripe, you can create a subscription that starts at the beginning of the current month by specifying 00:00 (UTC) at the beginning of the current month. Ex. 1672531200 for January 2023.) ")
    next_plan_tax_rate_id: Optional[StrictStr] = None
    proration_behavior: Optional[ProrationBehavior] = None
    delete_usage: Optional[StrictBool] = Field(None, description="If you have a stripe linkage,  you can set whether to delete pay-as-you-go items when changing plans. When you change plan, you can remove all pay-as-you-go items included in your current subscription to stop being billed based on pay-as-you-go items. The recorded usage is cleared immediately. Since it cannot be restored, please note that plan change reservations with delete_usage set to true cannot be canceled. ")
    plan_histories: Annotated[List[PlanHistory], Field()] = Field(..., description="Plan History")
    id: StrictStr = Field(...)
    plan_id: Optional[StrictStr] = None
    billing_info: Optional[BillingInfo] = None
    __properties = ["name", "attributes", "back_office_staff_email", "next_plan_id", "using_next_plan_from", "next_plan_tax_rate_id", "proration_behavior", "delete_usage", "plan_histories", "id", "plan_id", "billing_info"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Tenant:
        """Create an instance of Tenant from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in plan_histories (list)
        _items = []
        if self.plan_histories:
            for _item in self.plan_histories:
                if _item:
                    _items.append(_item.to_dict())
            _dict['plan_histories'] = _items
        # override the default output from pydantic by calling `to_dict()` of billing_info
        if self.billing_info:
            _dict['billing_info'] = self.billing_info.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Tenant:
        """Create an instance of Tenant from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Tenant.parse_obj(obj)

        _obj = Tenant.parse_obj({
            "name": obj.get("name"),
            "attributes": obj.get("attributes"),
            "back_office_staff_email": obj.get("back_office_staff_email"),
            "next_plan_id": obj.get("next_plan_id"),
            "using_next_plan_from": obj.get("using_next_plan_from"),
            "next_plan_tax_rate_id": obj.get("next_plan_tax_rate_id"),
            "proration_behavior": obj.get("proration_behavior"),
            "delete_usage": obj.get("delete_usage"),
            "plan_histories": [PlanHistory.from_dict(_item) for _item in obj.get("plan_histories")] if obj.get("plan_histories") is not None else None,
            "id": obj.get("id"),
            "plan_id": obj.get("plan_id"),
            "billing_info": BillingInfo.from_dict(obj.get("billing_info")) if obj.get("billing_info") is not None else None
        })
        return _obj



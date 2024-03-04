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


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from pydantic import Field
from saasus_sdk_python.src.auth.models.billing_info import BillingInfo
from saasus_sdk_python.src.auth.models.plan_history import PlanHistory
from saasus_sdk_python.src.auth.models.proration_behavior import ProrationBehavior
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class TenantDetail(BaseModel):
    """
    TenantDetail
    """ # noqa: E501
    id: StrictStr
    plan_id: Optional[StrictStr] = None
    billing_info: Optional[BillingInfo] = None
    name: StrictStr = Field(description="tenant name")
    attributes: Dict[str, Any] = Field(description="attribute info")
    back_office_staff_email: StrictStr = Field(description="administrative staff email address")
    next_plan_id: Optional[StrictStr] = None
    using_next_plan_from: Optional[StrictInt] = Field(default=None, description="Next billing plan start time (When using stripe, you can create a subscription that starts at the beginning of the current month by specifying 00:00 (UTC) at the beginning of the current month. Ex. 1672531200 for January 2023.) ")
    next_plan_tax_rate_id: Optional[StrictStr] = None
    proration_behavior: Optional[ProrationBehavior] = None
    delete_usage: Optional[StrictBool] = Field(default=None, description="If you have a stripe linkage,  you can set whether to delete pay-as-you-go items when changing plans. When you change plan, you can remove all pay-as-you-go items included in your current subscription to stop being billed based on pay-as-you-go items. The recorded usage is cleared immediately. Since it cannot be restored, please note that plan change reservations with delete_usage set to true cannot be canceled. ")
    plan_histories: List[PlanHistory] = Field(description="Plan History")
    current_plan_period_start: Optional[StrictInt] = Field(default=None, description="current plan period start")
    current_plan_period_end: Optional[StrictInt] = Field(default=None, description="current plan period end")
    __properties: ClassVar[List[str]] = ["id", "plan_id", "billing_info", "name", "attributes", "back_office_staff_email", "next_plan_id", "using_next_plan_from", "next_plan_tax_rate_id", "proration_behavior", "delete_usage", "plan_histories", "current_plan_period_start", "current_plan_period_end"]

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
        """Create an instance of TenantDetail from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of billing_info
        if self.billing_info:
            _dict['billing_info'] = self.billing_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in plan_histories (list)
        _items = []
        if self.plan_histories:
            for _item in self.plan_histories:
                if _item:
                    _items.append(_item.to_dict())
            _dict['plan_histories'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of TenantDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "plan_id": obj.get("plan_id"),
            "billing_info": BillingInfo.from_dict(obj.get("billing_info")) if obj.get("billing_info") is not None else None,
            "name": obj.get("name"),
            "attributes": obj.get("attributes"),
            "back_office_staff_email": obj.get("back_office_staff_email"),
            "next_plan_id": obj.get("next_plan_id"),
            "using_next_plan_from": obj.get("using_next_plan_from"),
            "next_plan_tax_rate_id": obj.get("next_plan_tax_rate_id"),
            "proration_behavior": obj.get("proration_behavior"),
            "delete_usage": obj.get("delete_usage"),
            "plan_histories": [PlanHistory.from_dict(_item) for _item in obj.get("plan_histories")] if obj.get("plan_histories") is not None else None,
            "current_plan_period_start": obj.get("current_plan_period_start"),
            "current_plan_period_end": obj.get("current_plan_period_end")
        })
        return _obj



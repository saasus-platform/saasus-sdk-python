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


from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel, StrictInt, StrictStr
from pydantic import Field
from saasus_sdk_python.src.pricing.models.currency import Currency
from saasus_sdk_python.src.pricing.models.recurring_interval import RecurringInterval
from saasus_sdk_python.src.pricing.models.unit_type import UnitType
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class PricingFixedUnitForSave(BaseModel):
    """
    PricingFixedUnitForSave
    """ # noqa: E501
    name: StrictStr = Field(description="名前")
    display_name: StrictStr = Field(description="表示名")
    description: StrictStr = Field(description="説明")
    type: UnitType
    currency: Currency
    unit_amount: StrictInt = Field(description="料金")
    recurring_interval: RecurringInterval
    __properties: ClassVar[List[str]] = ["name", "display_name", "description", "type", "currency", "unit_amount", "recurring_interval"]

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
        """Create an instance of PricingFixedUnitForSave from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of PricingFixedUnitForSave from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "display_name": obj.get("display_name"),
            "description": obj.get("description"),
            "type": obj.get("type"),
            "currency": obj.get("currency"),
            "unit_amount": obj.get("unit_amount"),
            "recurring_interval": obj.get("recurring_interval")
        })
        return _obj



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


from typing import List
from pydantic import ConfigDict, BaseModel, Field
from saasus_sdk_python.src.pricing.models.tax_rate import TaxRate
from typing_extensions import Annotated

class TaxRates(BaseModel):
    """
    TaxRates
    """
    tax_rates: Annotated[List[TaxRate], Field()] = Field(...)
    __properties = ["tax_rates"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> TaxRates:
        """Create an instance of TaxRates from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in tax_rates (list)
        _items = []
        if self.tax_rates:
            for _item in self.tax_rates:
                if _item:
                    _items.append(_item.to_dict())
            _dict['tax_rates'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TaxRates:
        """Create an instance of TaxRates from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TaxRates.parse_obj(obj)

        _obj = TaxRates.parse_obj({
            "tax_rates": [TaxRate.from_dict(_item) for _item in obj.get("tax_rates")] if obj.get("tax_rates") is not None else None
        })
        return _obj



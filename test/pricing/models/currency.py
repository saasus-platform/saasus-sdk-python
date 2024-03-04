# coding: utf-8

"""
    SaaSus Pricing API Schema

    SaaSus Pricing API Schema

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
import re  # noqa: F401
from enum import Enum



try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class Currency(str, Enum):
    """
    計測単位の通貨
    """

    """
    allowed enum values
    """
    JPY = 'JPY'
    USD = 'USD'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Currency from a JSON string"""
        return cls(json.loads(json_str))



# coding: utf-8

"""
    SaaSus Pricing API Schema

    SaaSus Pricing API Schema

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class Currency(str, Enum):
    """
    Unit of currency
    """

    """
    allowed enum values
    """
    JPY = 'JPY'
    USD = 'USD'

    @classmethod
    def from_json(cls, json_str: str) -> Currency:
        """Create an instance of Currency from a JSON string"""
        return Currency(json.loads(json_str))



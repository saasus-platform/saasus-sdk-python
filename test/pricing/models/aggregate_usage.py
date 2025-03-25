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





class AggregateUsage(str, Enum):
    """
    Aggregate usage sum: Total usage during the period max: Maximum usage during the period 
    """

    """
    allowed enum values
    """
    SUM = 'sum'
    MAX = 'max'

    @classmethod
    def from_json(cls, json_str: str) -> AggregateUsage:
        """Create an instance of AggregateUsage from a JSON string"""
        return AggregateUsage(json.loads(json_str))



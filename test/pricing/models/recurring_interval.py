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





class RecurringInterval(str, Enum):
    """
    繰り返し期間(cycle) month: 月単位(monthly) year: 年単位(yearly) 
    """

    """
    allowed enum values
    """
    MONTH = 'month'
    YEAR = 'year'

    @classmethod
    def from_json(cls, json_str: str) -> RecurringInterval:
        """Create an instance of RecurringInterval from a JSON string"""
        return RecurringInterval(json.loads(json_str))



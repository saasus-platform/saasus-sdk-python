# coding: utf-8

"""
    SaaSus Auth API Schema

    Schema

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class ProviderType(str, Enum):
    """
    ProviderType
    """

    """
    allowed enum values
    """
    SAML = 'SAML'

    @classmethod
    def from_json(cls, json_str: str) -> ProviderType:
        """Create an instance of ProviderType from a JSON string"""
        return ProviderType(json.loads(json_str))



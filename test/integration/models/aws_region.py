# coding: utf-8

"""
    SaaSus Eventbridge API Schema

    SaaSus Eventbridge API Schema

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class AwsRegion(str, Enum):
    """
    中国の寧夏、北京を除く全てのAWSリージョンが選択可能です。  All AWS regions except Ningxia and Beijing in China can be selected. 
    """

    """
    allowed enum values
    """
    US_MINUS_EAST_MINUS_1 = 'us-east-1'
    US_MINUS_EAST_MINUS_2 = 'us-east-2'
    US_MINUS_WEST_MINUS_1 = 'us-west-1'
    US_MINUS_WEST_MINUS_2 = 'us-west-2'
    AF_MINUS_SOUTH_MINUS_1 = 'af-south-1'
    AP_MINUS_EAST_MINUS_1 = 'ap-east-1'
    AP_MINUS_SOUTH_MINUS_1 = 'ap-south-1'
    AP_MINUS_NORTHEAST_MINUS_1 = 'ap-northeast-1'
    AP_MINUS_NORTHEAST_MINUS_2 = 'ap-northeast-2'
    AP_MINUS_NORTHEAST_MINUS_3 = 'ap-northeast-3'
    AP_MINUS_SOUTHEAST_MINUS_1 = 'ap-southeast-1'
    AP_MINUS_SOUTHEAST_MINUS_2 = 'ap-southeast-2'
    AP_MINUS_SOUTHEAST_MINUS_3 = 'ap-southeast-3'
    CA_MINUS_CENTRAL_MINUS_1 = 'ca-central-1'
    EU_MINUS_CENTRAL_MINUS_1 = 'eu-central-1'
    EU_MINUS_NORTH_MINUS_1 = 'eu-north-1'
    EU_MINUS_SOUTH_MINUS_1 = 'eu-south-1'
    EU_MINUS_WEST_MINUS_1 = 'eu-west-1'
    EU_MINUS_WEST_MINUS_2 = 'eu-west-2'
    EU_MINUS_WEST_MINUS_3 = 'eu-west-3'
    ME_MINUS_SOUTH_MINUS_1 = 'me-south-1'
    SA_MINUS_EAST_MINUS_1 = 'sa-east-1'

    @classmethod
    def from_json(cls, json_str: str) -> AwsRegion:
        """Create an instance of AwsRegion from a JSON string"""
        return AwsRegion(json.loads(json_str))


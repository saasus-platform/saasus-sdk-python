# coding: utf-8

"""
    SaaSus Auth API Schema

    スキーマ

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class ProrationBehavior(str, Enum):
    """
    stripe連携している場合で、プラン変更時の比例配分の挙動を設定できます。 プラン変更した場合に、請求金額を日割り計算し次回請求書に反映させるか、日割り計算した請求を即時に発行する、日割り計算をしないを設定できます。  If you have a strine linkage, you can set the behavior of the proportional allocation when changing plans. When a plan is changed, you can set whether to prorate the billing amount and reflect it on the next invoice, to issue a prorated invoice immediately, or not to prorate at all. 
    """

    """
    allowed enum values
    """
    CREATE_PRORATIONS = 'create_prorations'
    NONE = 'none'
    ALWAYS_INVOICE = 'always_invoice'

    @classmethod
    def from_json(cls, json_str: str) -> ProrationBehavior:
        """Create an instance of ProrationBehavior from a JSON string"""
        return ProrationBehavior(json.loads(json_str))


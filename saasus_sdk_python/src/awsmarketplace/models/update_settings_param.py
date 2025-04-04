# coding: utf-8

"""
    SaaSus AWS Marketplace API Schema

    SaaSus AWS Marketplace API Schema

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import ConfigDict, BaseModel, StrictStr

class UpdateSettingsParam(BaseModel):
    """
    UpdateSettingsParam
    """
    product_code: Optional[StrictStr] = None
    role_arn: Optional[StrictStr] = None
    role_external_id: Optional[StrictStr] = None
    sns_topic_arn: Optional[StrictStr] = None
    cas_bucket_name: Optional[StrictStr] = None
    cas_sns_topic_arn: Optional[StrictStr] = None
    seller_sns_topic_arn: Optional[StrictStr] = None
    sqs_arn: Optional[StrictStr] = None
    __properties = ["product_code", "role_arn", "role_external_id", "sns_topic_arn", "cas_bucket_name", "cas_sns_topic_arn", "seller_sns_topic_arn", "sqs_arn"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> UpdateSettingsParam:
        """Create an instance of UpdateSettingsParam from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UpdateSettingsParam:
        """Create an instance of UpdateSettingsParam from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UpdateSettingsParam.parse_obj(obj)

        _obj = UpdateSettingsParam.parse_obj({
            "product_code": obj.get("product_code"),
            "role_arn": obj.get("role_arn"),
            "role_external_id": obj.get("role_external_id"),
            "sns_topic_arn": obj.get("sns_topic_arn"),
            "cas_bucket_name": obj.get("cas_bucket_name"),
            "cas_sns_topic_arn": obj.get("cas_sns_topic_arn"),
            "seller_sns_topic_arn": obj.get("seller_sns_topic_arn"),
            "sqs_arn": obj.get("sqs_arn")
        })
        return _obj



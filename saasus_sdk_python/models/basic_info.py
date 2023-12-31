# coding: utf-8

"""
    SaaSus Auth API Schema

    スキーマ

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist
from saasus_sdk_python.models.dns_record import DnsRecord

class BasicInfo(BaseModel):
    """
    BasicInfo
    """
    domain_name: StrictStr = Field(..., description="ドメイン名(Domain Name)")
    is_dns_validated: StrictBool = Field(..., description="DNSレコードの検証結果(DNS Record Verification Results)")
    certificate_dns_record: DnsRecord = Field(...)
    cloud_front_dns_record: DnsRecord = Field(...)
    dkim_dns_records: conlist(DnsRecord) = Field(..., description="DKIM DNS レコード(DKIM DNS Records)")
    default_domain_name: StrictStr = Field(..., description="デフォルトドメイン名(Default Domain Name)")
    from_email_address: StrictStr = Field(..., description="認証メールの送信元メールアドレス(Sender Email for Authentication Email)")
    reply_email_address: StrictStr = Field(..., description="認証メールの返信元メールアドレス(Reply-from email address of authentication email)")
    is_ses_sandbox_granted: StrictBool = Field(..., description="SESのサンドボックス解除及びCognitoのSES設定結果(SES sandbox release and Cognito SES configuration results)")
    __properties = ["domain_name", "is_dns_validated", "certificate_dns_record", "cloud_front_dns_record", "dkim_dns_records", "default_domain_name", "from_email_address", "reply_email_address", "is_ses_sandbox_granted"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> BasicInfo:
        """Create an instance of BasicInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of certificate_dns_record
        if self.certificate_dns_record:
            _dict['certificate_dns_record'] = self.certificate_dns_record.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cloud_front_dns_record
        if self.cloud_front_dns_record:
            _dict['cloud_front_dns_record'] = self.cloud_front_dns_record.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in dkim_dns_records (list)
        _items = []
        if self.dkim_dns_records:
            for _item in self.dkim_dns_records:
                if _item:
                    _items.append(_item.to_dict())
            _dict['dkim_dns_records'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BasicInfo:
        """Create an instance of BasicInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BasicInfo.parse_obj(obj)

        _obj = BasicInfo.parse_obj({
            "domain_name": obj.get("domain_name"),
            "is_dns_validated": obj.get("is_dns_validated"),
            "certificate_dns_record": DnsRecord.from_dict(obj.get("certificate_dns_record")) if obj.get("certificate_dns_record") is not None else None,
            "cloud_front_dns_record": DnsRecord.from_dict(obj.get("cloud_front_dns_record")) if obj.get("cloud_front_dns_record") is not None else None,
            "dkim_dns_records": [DnsRecord.from_dict(_item) for _item in obj.get("dkim_dns_records")] if obj.get("dkim_dns_records") is not None else None,
            "default_domain_name": obj.get("default_domain_name"),
            "from_email_address": obj.get("from_email_address"),
            "reply_email_address": obj.get("reply_email_address"),
            "is_ses_sandbox_granted": obj.get("is_ses_sandbox_granted")
        })
        return _obj



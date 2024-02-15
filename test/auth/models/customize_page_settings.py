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



from pydantic import BaseModel, Field, StrictStr

class CustomizePageSettings(BaseModel):
    """
    CustomizePageSettings
    """
    title: StrictStr = Field(..., description="サービス名(service name)")
    terms_of_service_url: StrictStr = Field(..., description="利用規約URL(terms of service URL)")
    privacy_policy_url: StrictStr = Field(..., description="プライバシーポリシーURL(privacy policy URL)")
    google_tag_manager_container_id: StrictStr = Field(..., description="Google Tag Manager コンテナ ID(Google Tag Manager container ID)")
    icon: StrictStr = Field(..., description="サービスアイコン(service icon)")
    favicon: StrictStr = Field(..., description="ファビコン(favicon)")
    __properties = ["title", "terms_of_service_url", "privacy_policy_url", "google_tag_manager_container_id", "icon", "favicon"]

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
    def from_json(cls, json_str: str) -> CustomizePageSettings:
        """Create an instance of CustomizePageSettings from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CustomizePageSettings:
        """Create an instance of CustomizePageSettings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CustomizePageSettings.parse_obj(obj)

        _obj = CustomizePageSettings.parse_obj({
            "title": obj.get("title"),
            "terms_of_service_url": obj.get("terms_of_service_url"),
            "privacy_policy_url": obj.get("privacy_policy_url"),
            "google_tag_manager_container_id": obj.get("google_tag_manager_container_id"),
            "icon": obj.get("icon"),
            "favicon": obj.get("favicon")
        })
        return _obj



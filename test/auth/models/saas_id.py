# coding: utf-8

"""
    SaaSus Auth API Schema

    Schema

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json



from pydantic import ConfigDict, BaseModel, Field, StrictInt, StrictStr

class SaasId(BaseModel):
    """
    SaasId
    """
    tenant_id: StrictStr = Field(...)
    env_id: StrictInt = Field(...)
    saas_id: StrictStr = Field(..., description="SaaS ID")
    __properties = ["tenant_id", "env_id", "saas_id"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> SaasId:
        """Create an instance of SaasId from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SaasId:
        """Create an instance of SaasId from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SaasId.parse_obj(obj)

        _obj = SaasId.parse_obj({
            "tenant_id": obj.get("tenant_id"),
            "env_id": obj.get("env_id"),
            "saas_id": obj.get("saas_id")
        })
        return _obj



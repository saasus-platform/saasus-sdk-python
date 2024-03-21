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



from pydantic import BaseModel, Field, StrictStr, validator

class MfaConfiguration(BaseModel):
    """
    MFA device authentication settings ※ This function is not yet provided, so it cannot be changed or saved. 
    """
    mfa_configuration: StrictStr = Field(..., description="on: apply when all users log in optional: apply to individual users with MFA factor enabled ※ The parameter is currently optional and fixed. ")
    __properties = ["mfa_configuration"]

    @validator('mfa_configuration')
    def mfa_configuration_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('on', 'optional'):
            raise ValueError("must be one of enum values ('on', 'optional')")
        return value

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
    def from_json(cls, json_str: str) -> MfaConfiguration:
        """Create an instance of MfaConfiguration from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MfaConfiguration:
        """Create an instance of MfaConfiguration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MfaConfiguration.parse_obj(obj)

        _obj = MfaConfiguration.parse_obj({
            "mfa_configuration": obj.get("mfa_configuration")
        })
        return _obj



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



from pydantic import BaseModel, Field
from saasus_sdk_python.src.auth.models.account_verification import AccountVerification
from saasus_sdk_python.src.auth.models.device_configuration import DeviceConfiguration
from saasus_sdk_python.src.auth.models.identity_provider_configuration import IdentityProviderConfiguration
from saasus_sdk_python.src.auth.models.mfa_configuration import MfaConfiguration
from saasus_sdk_python.src.auth.models.password_policy import PasswordPolicy
from saasus_sdk_python.src.auth.models.recaptcha_props import RecaptchaProps
from saasus_sdk_python.src.auth.models.self_regist import SelfRegist

class SignInSettings(BaseModel):
    """
    SignInSettings
    """
    password_policy: PasswordPolicy = Field(...)
    device_configuration: DeviceConfiguration = Field(...)
    mfa_configuration: MfaConfiguration = Field(...)
    recaptcha_props: RecaptchaProps = Field(...)
    account_verification: AccountVerification = Field(...)
    self_regist: SelfRegist = Field(...)
    identity_provider_configuration: IdentityProviderConfiguration = Field(...)
    __properties = ["password_policy", "device_configuration", "mfa_configuration", "recaptcha_props", "account_verification", "self_regist", "identity_provider_configuration"]

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
    def from_json(cls, json_str: str) -> SignInSettings:
        """Create an instance of SignInSettings from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of password_policy
        if self.password_policy:
            _dict['password_policy'] = self.password_policy.to_dict()
        # override the default output from pydantic by calling `to_dict()` of device_configuration
        if self.device_configuration:
            _dict['device_configuration'] = self.device_configuration.to_dict()
        # override the default output from pydantic by calling `to_dict()` of mfa_configuration
        if self.mfa_configuration:
            _dict['mfa_configuration'] = self.mfa_configuration.to_dict()
        # override the default output from pydantic by calling `to_dict()` of recaptcha_props
        if self.recaptcha_props:
            _dict['recaptcha_props'] = self.recaptcha_props.to_dict()
        # override the default output from pydantic by calling `to_dict()` of account_verification
        if self.account_verification:
            _dict['account_verification'] = self.account_verification.to_dict()
        # override the default output from pydantic by calling `to_dict()` of self_regist
        if self.self_regist:
            _dict['self_regist'] = self.self_regist.to_dict()
        # override the default output from pydantic by calling `to_dict()` of identity_provider_configuration
        if self.identity_provider_configuration:
            _dict['identity_provider_configuration'] = self.identity_provider_configuration.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SignInSettings:
        """Create an instance of SignInSettings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SignInSettings.parse_obj(obj)

        _obj = SignInSettings.parse_obj({
            "password_policy": PasswordPolicy.from_dict(obj.get("password_policy")) if obj.get("password_policy") is not None else None,
            "device_configuration": DeviceConfiguration.from_dict(obj.get("device_configuration")) if obj.get("device_configuration") is not None else None,
            "mfa_configuration": MfaConfiguration.from_dict(obj.get("mfa_configuration")) if obj.get("mfa_configuration") is not None else None,
            "recaptcha_props": RecaptchaProps.from_dict(obj.get("recaptcha_props")) if obj.get("recaptcha_props") is not None else None,
            "account_verification": AccountVerification.from_dict(obj.get("account_verification")) if obj.get("account_verification") is not None else None,
            "self_regist": SelfRegist.from_dict(obj.get("self_regist")) if obj.get("self_regist") is not None else None,
            "identity_provider_configuration": IdentityProviderConfiguration.from_dict(obj.get("identity_provider_configuration")) if obj.get("identity_provider_configuration") is not None else None
        })
        return _obj


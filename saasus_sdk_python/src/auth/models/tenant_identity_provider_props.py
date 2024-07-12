# coding: utf-8

"""
    SaaSus Auth API Schema

    Schema

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401

from typing import Literal, Any, List, Optional
from pydantic import field_validator, ConfigDict, BaseModel, StrictStr, ValidationError
from saasus_sdk_python.src.auth.models.identity_provider_saml import IdentityProviderSaml
from typing import Union, Any, List, TYPE_CHECKING
from pydantic import StrictStr

TENANTIDENTITYPROVIDERPROPS_ONE_OF_SCHEMAS = ["IdentityProviderSaml"]

class TenantIdentityProviderProps(BaseModel):
    """
    TenantIdentityProviderProps
    """
    # data type: IdentityProviderSaml
    oneof_schema_1_validator: Optional[IdentityProviderSaml] = None
    if TYPE_CHECKING:
        actual_instance: Union[IdentityProviderSaml]
    else:
        actual_instance: Any = None
    one_of_schemas: Literal[TENANTIDENTITYPROVIDERPROPS_ONE_OF_SCHEMAS] = TENANTIDENTITYPROVIDERPROPS_ONE_OF_SCHEMAS
    model_config = ConfigDict(validate_assignment=True)

    def __init__(self, *args, **kwargs):
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    @classmethod
    def actual_instance_must_validate_oneof(cls, v):
        instance = TenantIdentityProviderProps.construct()
        error_messages = []
        match = 0
        # validate data type: IdentityProviderSaml
        if not isinstance(v, IdentityProviderSaml):
            error_messages.append(f"Error! Input type `{type(v)}` is not `IdentityProviderSaml`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in TenantIdentityProviderProps with oneOf schemas: IdentityProviderSaml. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in TenantIdentityProviderProps with oneOf schemas: IdentityProviderSaml. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> TenantIdentityProviderProps:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> TenantIdentityProviderProps:
        """Returns the object represented by the json string"""
        instance = TenantIdentityProviderProps.construct()
        error_messages = []
        match = 0

        # deserialize data into IdentityProviderSaml
        try:
            instance.actual_instance = IdentityProviderSaml.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into TenantIdentityProviderProps with oneOf schemas: IdentityProviderSaml. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into TenantIdentityProviderProps with oneOf schemas: IdentityProviderSaml. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> dict:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        to_dict = getattr(self.actual_instance, "to_dict", None)
        if callable(to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.dict())



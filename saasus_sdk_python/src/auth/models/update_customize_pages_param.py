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


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel
from saasus_sdk_python.src.auth.models.customize_page_props import CustomizePageProps
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class UpdateCustomizePagesParam(BaseModel):
    """
    UpdateCustomizePagesParam
    """ # noqa: E501
    sign_up_page: Optional[CustomizePageProps] = None
    sign_in_page: Optional[CustomizePageProps] = None
    password_reset_page: Optional[CustomizePageProps] = None
    __properties: ClassVar[List[str]] = ["sign_up_page", "sign_in_page", "password_reset_page"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of UpdateCustomizePagesParam from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of sign_up_page
        if self.sign_up_page:
            _dict['sign_up_page'] = self.sign_up_page.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sign_in_page
        if self.sign_in_page:
            _dict['sign_in_page'] = self.sign_in_page.to_dict()
        # override the default output from pydantic by calling `to_dict()` of password_reset_page
        if self.password_reset_page:
            _dict['password_reset_page'] = self.password_reset_page.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of UpdateCustomizePagesParam from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "sign_up_page": CustomizePageProps.from_dict(obj.get("sign_up_page")) if obj.get("sign_up_page") is not None else None,
            "sign_in_page": CustomizePageProps.from_dict(obj.get("sign_in_page")) if obj.get("sign_in_page") is not None else None,
            "password_reset_page": CustomizePageProps.from_dict(obj.get("password_reset_page")) if obj.get("password_reset_page") is not None else None
        })
        return _obj



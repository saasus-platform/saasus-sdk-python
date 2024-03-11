# coding: utf-8

"""
    SaaSus Pricing API Schema

    SaaSus Pricing API Schema

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401

from typing import Any, List, Optional
from pydantic import BaseModel, Field, StrictStr, ValidationError, field_validator
from saasus_sdk_python.src.pricing.models.pricing_fixed_unit_for_save import PricingFixedUnitForSave
from saasus_sdk_python.src.pricing.models.pricing_tiered_unit_for_save import PricingTieredUnitForSave
from saasus_sdk_python.src.pricing.models.pricing_tiered_usage_unit_for_save import PricingTieredUsageUnitForSave
from saasus_sdk_python.src.pricing.models.pricing_usage_unit_for_save import PricingUsageUnitForSave
from typing import Union, Any, List, TYPE_CHECKING, Optional, Dict
from typing_extensions import Literal
from pydantic import StrictStr, Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

PRICINGUNITFORSAVE_ONE_OF_SCHEMAS = ["PricingFixedUnitForSave", "PricingTieredUnitForSave", "PricingTieredUsageUnitForSave", "PricingUsageUnitForSave"]

class PricingUnitForSave(BaseModel):
    """
    PricingUnitForSave
    """
    # data type: PricingTieredUsageUnitForSave
    oneof_schema_1_validator: Optional[PricingTieredUsageUnitForSave] = None
    # data type: PricingTieredUnitForSave
    oneof_schema_2_validator: Optional[PricingTieredUnitForSave] = None
    # data type: PricingUsageUnitForSave
    oneof_schema_3_validator: Optional[PricingUsageUnitForSave] = None
    # data type: PricingFixedUnitForSave
    oneof_schema_4_validator: Optional[PricingFixedUnitForSave] = None
    actual_instance: Optional[Union[PricingFixedUnitForSave, PricingTieredUnitForSave, PricingTieredUsageUnitForSave, PricingUsageUnitForSave]] = None
    one_of_schemas: List[str] = Literal["PricingFixedUnitForSave", "PricingTieredUnitForSave", "PricingTieredUsageUnitForSave", "PricingUsageUnitForSave"]

    model_config = {
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    discriminator_value_class_map: Dict[str, str] = {
    }

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = PricingUnitForSave.model_construct()
        error_messages = []
        match = 0
        # validate data type: PricingTieredUsageUnitForSave
        if not isinstance(v, PricingTieredUsageUnitForSave):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PricingTieredUsageUnitForSave`")
        else:
            match += 1
        # validate data type: PricingTieredUnitForSave
        if not isinstance(v, PricingTieredUnitForSave):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PricingTieredUnitForSave`")
        else:
            match += 1
        # validate data type: PricingUsageUnitForSave
        if not isinstance(v, PricingUsageUnitForSave):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PricingUsageUnitForSave`")
        else:
            match += 1
        # validate data type: PricingFixedUnitForSave
        if not isinstance(v, PricingFixedUnitForSave):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PricingFixedUnitForSave`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in PricingUnitForSave with oneOf schemas: PricingFixedUnitForSave, PricingTieredUnitForSave, PricingTieredUsageUnitForSave, PricingUsageUnitForSave. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in PricingUnitForSave with oneOf schemas: PricingFixedUnitForSave, PricingTieredUnitForSave, PricingTieredUsageUnitForSave, PricingUsageUnitForSave. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # use oneOf discriminator to lookup the data type
        _data_type = json.loads(json_str).get("type")
        if not _data_type:
            raise ValueError("Failed to lookup data type from the field `type` in the input.")

        # check if data type is `PricingFixedUnitForSave`
        if _data_type == "fixed":
            instance.actual_instance = PricingFixedUnitForSave.from_json(json_str)
            return instance

        # check if data type is `PricingTieredUnitForSave`
        if _data_type == "tiered":
            instance.actual_instance = PricingTieredUnitForSave.from_json(json_str)
            return instance

        # check if data type is `PricingTieredUsageUnitForSave`
        if _data_type == "tiered_usage":
            instance.actual_instance = PricingTieredUsageUnitForSave.from_json(json_str)
            return instance

        # check if data type is `PricingUsageUnitForSave`
        if _data_type == "usage":
            instance.actual_instance = PricingUsageUnitForSave.from_json(json_str)
            return instance

        # check if data type is `PricingFixedUnitForSave`
        if _data_type == "PricingFixedUnitForSave":
            instance.actual_instance = PricingFixedUnitForSave.from_json(json_str)
            return instance

        # check if data type is `PricingTieredUnitForSave`
        if _data_type == "PricingTieredUnitForSave":
            instance.actual_instance = PricingTieredUnitForSave.from_json(json_str)
            return instance

        # check if data type is `PricingTieredUsageUnitForSave`
        if _data_type == "PricingTieredUsageUnitForSave":
            instance.actual_instance = PricingTieredUsageUnitForSave.from_json(json_str)
            return instance

        # check if data type is `PricingUsageUnitForSave`
        if _data_type == "PricingUsageUnitForSave":
            instance.actual_instance = PricingUsageUnitForSave.from_json(json_str)
            return instance

        # deserialize data into PricingTieredUsageUnitForSave
        try:
            instance.actual_instance = PricingTieredUsageUnitForSave.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into PricingTieredUnitForSave
        try:
            instance.actual_instance = PricingTieredUnitForSave.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into PricingUsageUnitForSave
        try:
            instance.actual_instance = PricingUsageUnitForSave.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into PricingFixedUnitForSave
        try:
            instance.actual_instance = PricingFixedUnitForSave.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into PricingUnitForSave with oneOf schemas: PricingFixedUnitForSave, PricingTieredUnitForSave, PricingTieredUsageUnitForSave, PricingUsageUnitForSave. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into PricingUnitForSave with oneOf schemas: PricingFixedUnitForSave, PricingTieredUnitForSave, PricingTieredUsageUnitForSave, PricingUsageUnitForSave. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Dict:
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
        return pprint.pformat(self.model_dump())



# coding: utf-8

"""
    SaaSus Auth API Schema

    スキーマ

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

import openapi_client
from openapi_client.models.tenant_attributes import TenantAttributes  # noqa: E501
from openapi_client.rest import ApiException

class TestTenantAttributes(unittest.TestCase):
    """TenantAttributes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TenantAttributes
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TenantAttributes`
        """
        model = openapi_client.models.tenant_attributes.TenantAttributes()  # noqa: E501
        if include_optional :
            return TenantAttributes(
                tenant_attributes = [
                    openapi_client.models.attribute.Attribute(
                        attribute_name = 'birthday', 
                        display_name = '誕生日', 
                        attribute_type = 'string', )
                    ]
            )
        else :
            return TenantAttributes(
                tenant_attributes = [
                    openapi_client.models.attribute.Attribute(
                        attribute_name = 'birthday', 
                        display_name = '誕生日', 
                        attribute_type = 'string', )
                    ],
        )
        """

    def testTenantAttributes(self):
        """Test TenantAttributes"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

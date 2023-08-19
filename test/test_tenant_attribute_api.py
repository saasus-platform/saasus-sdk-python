# coding: utf-8

"""
    SaaSus Auth API Schema

    スキーマ

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

import openapi_client
from openapi_client.api.tenant_attribute_api import TenantAttributeApi  # noqa: E501
from openapi_client.rest import ApiException


class TestTenantAttributeApi(unittest.TestCase):
    """TenantAttributeApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.tenant_attribute_api.TenantAttributeApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_tenant_attribute(self):
        """Test case for create_tenant_attribute

        テナント属性の作成(Create Tenant Attribute)  # noqa: E501
        """
        pass

    def test_delete_tenant_attribute(self):
        """Test case for delete_tenant_attribute

        テナント属性の削除(Delete Tenant Attribute)  # noqa: E501
        """
        pass

    def test_get_tenant_attributes(self):
        """Test case for get_tenant_attributes

        テナント属性の一覧を取得(Get Tenant Attributes)  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

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
from openapi_client.models.saas_id import SaasId  # noqa: E501
from openapi_client.rest import ApiException

class TestSaasId(unittest.TestCase):
    """SaasId unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SaasId
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SaasId`
        """
        model = openapi_client.models.saas_id.SaasId()  # noqa: E501
        if include_optional :
            return SaasId(
                tenant_id = '69e732d6-8ecc-45c4-c2eb-8438f7ffe775', 
                env_id = 1, 
                saas_id = 'ede66c43-9b9d-4222-93ed-5f11c96e08e2'
            )
        else :
            return SaasId(
                tenant_id = '69e732d6-8ecc-45c4-c2eb-8438f7ffe775',
                env_id = 1,
                saas_id = 'ede66c43-9b9d-4222-93ed-5f11c96e08e2',
        )
        """

    def testSaasId(self):
        """Test SaasId"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

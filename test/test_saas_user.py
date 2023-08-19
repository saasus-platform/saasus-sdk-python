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
from openapi_client.models.saas_user import SaasUser  # noqa: E501
from openapi_client.rest import ApiException

class TestSaasUser(unittest.TestCase):
    """SaasUser unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SaasUser
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SaasUser`
        """
        model = openapi_client.models.saas_user.SaasUser()  # noqa: E501
        if include_optional :
            return SaasUser(
                id = '69e732d6-8ecc-45c4-c2eb-8438f7ffe775', 
                email = 'hoge@example.com'
            )
        else :
            return SaasUser(
                id = '69e732d6-8ecc-45c4-c2eb-8438f7ffe775',
                email = 'hoge@example.com',
        )
        """

    def testSaasUser(self):
        """Test SaasUser"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

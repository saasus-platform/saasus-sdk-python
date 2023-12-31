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
from openapi_client.models.mfa_preference import MfaPreference  # noqa: E501
from openapi_client.rest import ApiException

class TestMfaPreference(unittest.TestCase):
    """MfaPreference unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MfaPreference
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MfaPreference`
        """
        model = openapi_client.models.mfa_preference.MfaPreference()  # noqa: E501
        if include_optional :
            return MfaPreference(
                enabled = True, 
                method = 'softwareToken'
            )
        else :
            return MfaPreference(
                enabled = True,
        )
        """

    def testMfaPreference(self):
        """Test MfaPreference"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

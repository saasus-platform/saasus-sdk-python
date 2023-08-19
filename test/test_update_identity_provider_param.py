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
from openapi_client.models.update_identity_provider_param import UpdateIdentityProviderParam  # noqa: E501
from openapi_client.rest import ApiException

class TestUpdateIdentityProviderParam(unittest.TestCase):
    """UpdateIdentityProviderParam unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UpdateIdentityProviderParam
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateIdentityProviderParam`
        """
        model = openapi_client.models.update_identity_provider_param.UpdateIdentityProviderParam()  # noqa: E501
        if include_optional :
            return UpdateIdentityProviderParam(
                provider = 'Google', 
                identity_provider_props = openapi_client.models.identity_provider_props.IdentityProviderProps(
                    application_id = '1234567890123456', 
                    application_secret = '123456789b00def123456a12345678d1', 
                    approval_scope = 'profile email openid', )
            )
        else :
            return UpdateIdentityProviderParam(
                provider = 'Google',
        )
        """

    def testUpdateIdentityProviderParam(self):
        """Test UpdateIdentityProviderParam"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

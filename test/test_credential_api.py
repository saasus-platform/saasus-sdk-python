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
from openapi_client.api.credential_api import CredentialApi  # noqa: E501
from openapi_client.rest import ApiException


class TestCredentialApi(unittest.TestCase):
    """CredentialApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.credential_api.CredentialApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_auth_credentials(self):
        """Test case for create_auth_credentials

        認証・認可情報の保存(Save Authentication/Authorization Information)  # noqa: E501
        """
        pass

    def test_get_auth_credentials(self):
        """Test case for get_auth_credentials

        認証・認可情報の取得(Get Authentication/Authorization Information)  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

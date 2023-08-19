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
from openapi_client.api.env_api import EnvApi  # noqa: E501
from openapi_client.rest import ApiException


class TestEnvApi(unittest.TestCase):
    """EnvApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.env_api.EnvApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_env(self):
        """Test case for create_env

        環境情報を作成(Create Env Info)  # noqa: E501
        """
        pass

    def test_delete_env(self):
        """Test case for delete_env

        環境情報を削除(Delete Env Info)  # noqa: E501
        """
        pass

    def test_get_env(self):
        """Test case for get_env

        環境情報を取得(Get Env Details)  # noqa: E501
        """
        pass

    def test_get_envs(self):
        """Test case for get_envs

        環境情報一覧を取得(Get Env Info)  # noqa: E501
        """
        pass

    def test_update_env(self):
        """Test case for update_env

        環境情報を更新(Update Env Info)  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

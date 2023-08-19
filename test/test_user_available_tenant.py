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
from openapi_client.models.user_available_tenant import UserAvailableTenant  # noqa: E501
from openapi_client.rest import ApiException

class TestUserAvailableTenant(unittest.TestCase):
    """UserAvailableTenant unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UserAvailableTenant
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserAvailableTenant`
        """
        model = openapi_client.models.user_available_tenant.UserAvailableTenant()  # noqa: E501
        if include_optional :
            return UserAvailableTenant(
                id = '69e732d6-8ecc-45c4-c2eb-8438f7ffe775', 
                name = 'Anti-Pattern Inc.', 
                completed_sign_up = True, 
                envs = [
                    openapi_client.models.user_available_env.UserAvailableEnv(
                        id = 1, 
                        name = 'SaaSus dev', 
                        roles = [
                            openapi_client.models.役割(ロール)(role).役割(ロール)(Role)(
                                role_name = 'admin', 
                                display_name = '管理者', )
                            ], )
                    ], 
                user_attribute = {"address":"東京都","employee_number":100}, 
                back_office_staff_email = 'hoge@example.com', 
                plan_id = '69e732d6-8ecc-45c4-c2eb-8438f7ffe775', 
                is_paid = True
            )
        else :
            return UserAvailableTenant(
                id = '69e732d6-8ecc-45c4-c2eb-8438f7ffe775',
                name = 'Anti-Pattern Inc.',
                completed_sign_up = True,
                envs = [
                    openapi_client.models.user_available_env.UserAvailableEnv(
                        id = 1, 
                        name = 'SaaSus dev', 
                        roles = [
                            openapi_client.models.役割(ロール)(role).役割(ロール)(Role)(
                                role_name = 'admin', 
                                display_name = '管理者', )
                            ], )
                    ],
                user_attribute = {"address":"東京都","employee_number":100},
                back_office_staff_email = 'hoge@example.com',
        )
        """

    def testUserAvailableTenant(self):
        """Test UserAvailableTenant"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

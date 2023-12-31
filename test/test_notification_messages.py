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
from openapi_client.models.notification_messages import NotificationMessages  # noqa: E501
from openapi_client.rest import ApiException

class TestNotificationMessages(unittest.TestCase):
    """NotificationMessages unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test NotificationMessages
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NotificationMessages`
        """
        model = openapi_client.models.notification_messages.NotificationMessages()  # noqa: E501
        if include_optional :
            return NotificationMessages(
                sign_up = openapi_client.models.message_template.MessageTemplate(
                    subject = 'Verify your new account', 
                    message = 'The verification code to your new account is {####}', ), 
                create_user = openapi_client.models.message_template.MessageTemplate(
                    subject = 'Verify your new account', 
                    message = 'The verification code to your new account is {####}', ), 
                resend_code = openapi_client.models.message_template.MessageTemplate(
                    subject = 'Verify your new account', 
                    message = 'The verification code to your new account is {####}', ), 
                forgot_password = openapi_client.models.message_template.MessageTemplate(
                    subject = 'Verify your new account', 
                    message = 'The verification code to your new account is {####}', ), 
                update_user_attribute = openapi_client.models.message_template.MessageTemplate(
                    subject = 'Verify your new account', 
                    message = 'The verification code to your new account is {####}', ), 
                verify_user_attribute = openapi_client.models.message_template.MessageTemplate(
                    subject = 'Verify your new account', 
                    message = 'The verification code to your new account is {####}', ), 
                authentication_mfa = openapi_client.models.message_template.MessageTemplate(
                    subject = 'Verify your new account', 
                    message = 'The verification code to your new account is {####}', )
            )
        else :
            return NotificationMessages(
                sign_up = openapi_client.models.message_template.MessageTemplate(
                    subject = 'Verify your new account', 
                    message = 'The verification code to your new account is {####}', ),
                create_user = openapi_client.models.message_template.MessageTemplate(
                    subject = 'Verify your new account', 
                    message = 'The verification code to your new account is {####}', ),
                resend_code = openapi_client.models.message_template.MessageTemplate(
                    subject = 'Verify your new account', 
                    message = 'The verification code to your new account is {####}', ),
                forgot_password = openapi_client.models.message_template.MessageTemplate(
                    subject = 'Verify your new account', 
                    message = 'The verification code to your new account is {####}', ),
                update_user_attribute = openapi_client.models.message_template.MessageTemplate(
                    subject = 'Verify your new account', 
                    message = 'The verification code to your new account is {####}', ),
                verify_user_attribute = openapi_client.models.message_template.MessageTemplate(
                    subject = 'Verify your new account', 
                    message = 'The verification code to your new account is {####}', ),
                authentication_mfa = openapi_client.models.message_template.MessageTemplate(
                    subject = 'Verify your new account', 
                    message = 'The verification code to your new account is {####}', ),
        )
        """

    def testNotificationMessages(self):
        """Test NotificationMessages"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

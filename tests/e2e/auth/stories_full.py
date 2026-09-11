"""
Auth module SaaS User Attributes Management stories

SaaSユーザー属性管理のストーリーを定義します（通常版と_with_http_info版）。
"""

import os
import random
from typing import List
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from testlib.models import Story, Step
from tests.e2e.auth.helpers import (
    unique_email,
    unique_string,
    build_create_saas_user_params,
    build_create_user_attribute_params,
    get_default_password,
    get_or_create_test_plan_id,
    get_cognito_tokens_safe,
    is_stripe_configured,
    setup_stripe_integration,
    get_stripe_secret_key
)
from saasus_sdk_python.src.billing.models.update_stripe_info_param import UpdateStripeInfoParam


def get_saas_user_attributes_story() -> Story:
    """SaaSユーザー属性管理のストーリー（通常版）"""
    from saasus_sdk_python.src.auth.models.update_saas_user_attributes_param import UpdateSaasUserAttributesParam
    
    return Story(
        name="saas_user_attributes_management",
        description="SaaSユーザーの追加属性を管理するメソッドをテストします。",
        module="auth",
        steps=[
            Step(
                method_name="create_saas_user",
                params=lambda vars: {
                    "create_saas_user_param": build_create_saas_user_params(unique_email("saas-user"), get_default_password())
                },
                description="CreateSaasUser",
                store_as="created_user"
            ),
            Step(
                method_name="create_saas_user_attribute",
                params=lambda vars: {
                    "body": build_create_user_attribute_params(unique_string("custom-field"), f"Custom Field {unique_string('field')}")
                },
                description="CreateSaasUserAttribute",
                store_as="created_attribute"
            ),
            Step(
                method_name="update_saas_user_attributes",
                params=lambda vars: {
                    "user_id": getattr(vars.get("created_user"), "id", "mock-user-id"),
                    "update_saas_user_attributes_param": UpdateSaasUserAttributesParam(
                        attributes={getattr(vars.get("created_attribute"), "attribute_name", "mock-attr"): "test value"}
                    )
                },
                description="UpdateSaasUserAttributes"
            ),
            Step(
                method_name="delete_saas_user",
                params=lambda vars: {"user_id": getattr(vars.get("created_user"), "id", "mock-user-id")},
                description="DeleteSaasUser"
            ),
        ],
        tags=["auth", "attributes", "crud"]
    )


def get_saas_user_attributes_with_http_info_story() -> Story:
    """SaaSユーザー属性管理のストーリー（_with_http_infoバージョン）"""
    from saasus_sdk_python.src.auth.models.update_saas_user_attributes_param import UpdateSaasUserAttributesParam
    
    return Story(
        name="saas_user_attributes_management_with_http_info",
        description="SaaSユーザーの追加属性を管理するメソッドをテストします。_with_http_infoバージョンを使用してHTTPレスポンス詳細を取得します。",
        module="auth",
        steps=[
            Step(
                method_name="create_saas_user_with_http_info",
                params=lambda vars: {
                    "create_saas_user_param": build_create_saas_user_params(unique_email("saas-user-http"), get_default_password())
                },
                description="CreateSaasUserWithHttpInfo",
                store_as="created_user"
            ),
            Step(
                method_name="create_saas_user_attribute_with_http_info",
                params=lambda vars: {
                    "body": build_create_user_attribute_params(unique_string("http-field"), f"HTTP Field {unique_string('field')}")
                },
                description="CreateSaasUserAttributeWithHttpInfo",
                store_as="created_attribute"
            ),
            Step(
                method_name="update_saas_user_attributes_with_http_info",
                params=lambda vars: {
                    "user_id": getattr(vars.get("created_user"), "id", "mock-user-id"),
                    "update_saas_user_attributes_param": UpdateSaasUserAttributesParam(
                        attributes={getattr(vars.get("created_attribute"), "attribute_name", "mock-attr"): "http test value"}
                    )
                },
                description="UpdateSaasUserAttributesWithHttpInfo"
            ),
            Step(
                method_name="delete_saas_user_with_http_info",
                params=lambda vars: {"user_id": getattr(vars.get("created_user"), "id", "mock-user-id")},
                description="DeleteSaasUserWithHttpInfo"
            ),
        ],
        tags=["auth", "attributes", "with-http-info"]
    )


def get_external_user_link_and_email_update_story() -> Story:
    """外部ユーザーリンクとメール更新のストーリー"""
    return Story(
        name="external_user_link_and_email_update",
        description="外部ユーザーアカウントのリンクとメールアドレス更新確認機能をテストします。",
        module="auth",
        steps=[
            Step(
                method_name="create_saas_user",
                params=lambda vars: {
                    "create_saas_user_param": build_create_saas_user_params(unique_email("external-link"), get_default_password())
                },
                description="CreateSaasUser for external link test",
                store_as="created_user"
            ),
            Step(
                method_name="request_external_user_link",
                params=lambda vars: {},
                description="RequestExternalUserLink",
                skip=True,
                skip_reason="Requires Cognito authentication"
            ),
            Step(
                method_name="confirm_external_user_link",
                params=lambda vars: {},
                description="ConfirmExternalUserLink",
                skip=True,
                skip_reason="Requires Cognito authentication"
            ),
            Step(
                method_name="request_email_update",
                params=lambda vars: {},
                description="RequestEmailUpdate",
                skip=True,
                skip_reason="Requires Cognito authentication"
            ),
            Step(
                method_name="confirm_email_update",
                params=lambda vars: {},
                description="ConfirmEmailUpdate",
                skip=True,
                skip_reason="Requires Cognito authentication"
            ),
            Step(
                method_name="delete_saas_user",
                params=lambda vars: {"user_id": getattr(vars.get("created_user"), "id", "mock-user-id")},
                description="DeleteSaasUser after external link test"
            ),
        ],
        tags=["auth", "external-link", "email-update"]
    )


def get_external_user_link_and_email_update_with_http_info_story() -> Story:
    """外部ユーザーリンクとメール更新のストーリー（_with_http_infoバージョン）"""
    return Story(
        name="external_user_link_and_email_update_with_http_info",
        description="外部ユーザーアカウントのリンクとメールアドレス更新確認機能をテストします。_with_http_infoバージョン。",
        module="auth",
        steps=[
            Step(
                method_name="create_saas_user_with_http_info",
                params=lambda vars: {
                    "create_saas_user_param": build_create_saas_user_params(unique_email("external-link-http"), get_default_password())
                },
                description="CreateSaasUserWithHttpInfo for external link test",
                store_as="created_user"
            ),
            Step(
                method_name="request_external_user_link_with_http_info",
                params=lambda vars: {},
                description="RequestExternalUserLinkWithHttpInfo",
                skip=True,
                skip_reason="Requires Cognito authentication"
            ),
            Step(
                method_name="confirm_external_user_link_with_http_info",
                params=lambda vars: {},
                description="ConfirmExternalUserLinkWithHttpInfo",
                skip=True,
                skip_reason="Requires Cognito authentication"
            ),
            Step(
                method_name="request_email_update_with_http_info",
                params=lambda vars: {},
                description="RequestEmailUpdateWithHttpInfo",
                skip=True,
                skip_reason="Requires Cognito authentication"
            ),
            Step(
                method_name="confirm_email_update_with_http_info",
                params=lambda vars: {},
                description="ConfirmEmailUpdateWithHttpInfo",
                skip=True,
                skip_reason="Requires Cognito authentication"
            ),
            Step(
                method_name="delete_saas_user_with_http_info",
                params=lambda vars: {"user_id": getattr(vars.get("created_user"), "id", "mock-user-id")},
                description="DeleteSaasUserWithHttpInfo after external link test"
            ),
        ],
        tags=["auth", "external-link", "email-update", "with-http-info"]
    )


def get_missing_methods_coverage_story() -> Story:
    """未実装メソッドカバレッジのストーリー"""
    from saasus_sdk_python.src.auth.models.billing_info import BillingInfo
    from saasus_sdk_python.src.auth.models.billing_address import BillingAddress
    from saasus_sdk_python.src.auth.models.invoice_language import InvoiceLanguage
    from saasus_sdk_python.src.auth.models.plan_reservation import PlanReservation
    
    # Stripe設定を確認
    stripe_configured = is_stripe_configured()
    if stripe_configured:
        setup_stripe_integration()
    
    return Story(
        name="missing_methods_coverage",
        description="未実装の3メソッド（GetUserInfoByEmail, UpdateTenantPlan, UpdateTenantBillingInfo）をテストします。",
        module="auth",
        steps=[
            Step(
                method_name="create_saas_user",
                params=lambda vars: {
                    "create_saas_user_param": build_create_saas_user_params(unique_email("saas-user"), get_default_password())
                },
                description="CreateSaasUser for missing methods test",
                store_as="created_user"
            ),
            Step(
                method_name="create_tenant",
                params=lambda vars: {
                    "body": {
                        "name": unique_string("tenant"),
                        "attributes": {},
                        "back_office_staff_email": unique_email("tenant-staff")
                    }
                },
                description="CreateTenant for missing methods test",
                store_as="created_tenant"
            ),
            Step(
                method_name="get_user_info_by_email",
                params=lambda vars: {
                    "email": getattr(vars.get("created_user"), "email", "mock@example.com")
                },
                description="GetUserInfoByEmail"
            ),
            Step(
                method_name="update_tenant_plan",
                params=lambda vars: {
                    "tenant_id": getattr(vars.get("created_tenant"), "id", "mock-tenant-id"),
                    "body": PlanReservation(next_plan_id=get_or_create_test_plan_id())
                },
                description="UpdateTenantPlan",
                skip=not stripe_configured,
                skip_reason="Requires Stripe integration (STRIPE_SECRET_KEY)"
            ),
            Step(
                method_name="update_tenant_billing_info",
                params=lambda vars: {
                    "tenant_id": getattr(vars.get("created_tenant"), "id", "mock-tenant-id"),
                    "body": BillingInfo(
                        name="Test Company",
                        invoice_language=InvoiceLanguage.JA_MINUS_JP,
                        address=BillingAddress(
                            city="Chiyoda",
                            country="JP",
                            postal_code="100-0001",
                            state="Tokyo",
                            street="1-1-1 Test Building"
                        )
                    )
                },
                description="UpdateTenantBillingInfo",
                skip=not stripe_configured,
                skip_reason="Requires Stripe integration (STRIPE_SECRET_KEY)"
            ),
            Step(
                method_name="delete_tenant",
                params=lambda vars: {"tenant_id": getattr(vars.get("created_tenant"), "id", "mock-tenant-id")},
                description="DeleteTenant after missing methods test"
            ),
            Step(
                method_name="delete_saas_user",
                params=lambda vars: {"user_id": getattr(vars.get("created_user"), "id", "mock-user-id")},
                description="DeleteSaasUser after missing methods test"
            ),
        ],
        tags=["auth", "missing-methods", "crud"]
    )


def get_missing_methods_coverage_with_http_info_story() -> Story:
    """未実装メソッドカバレッジのストーリー（_with_http_infoバージョン）"""
    from saasus_sdk_python.src.auth.models.billing_info import BillingInfo
    from saasus_sdk_python.src.auth.models.billing_address import BillingAddress
    from saasus_sdk_python.src.auth.models.invoice_language import InvoiceLanguage
    from saasus_sdk_python.src.auth.models.plan_reservation import PlanReservation
    
    # Stripe設定を確認
    stripe_configured = is_stripe_configured()
    if stripe_configured:
        setup_stripe_integration()
    
    return Story(
        name="missing_methods_coverage_with_http_info",
        description="未実装の3メソッド（GetUserInfoByEmail, UpdateTenantPlan, UpdateTenantBillingInfo）をテストします。_with_http_infoバージョン。",
        module="auth",
        steps=[
            Step(
                method_name="create_saas_user_with_http_info",
                params=lambda vars: {
                    "create_saas_user_param": build_create_saas_user_params(unique_email("saas-user-http"), get_default_password())
                },
                description="CreateSaasUserWithHttpInfo for missing methods test",
                store_as="created_user"
            ),
            Step(
                method_name="create_tenant_with_http_info",
                params=lambda vars: {
                    "body": {
                        "name": unique_string("tenant-http"),
                        "attributes": {},
                        "back_office_staff_email": unique_email("tenant-staff-http")
                    }
                },
                description="CreateTenantWithHttpInfo for missing methods test",
                store_as="created_tenant"
            ),
            Step(
                method_name="get_user_info_by_email_with_http_info",
                params=lambda vars: {
                    "email": getattr(vars.get("created_user"), "email", "mock@example.com")
                },
                description="GetUserInfoByEmailWithHttpInfo"
            ),
            Step(
                method_name="update_tenant_plan_with_http_info",
                params=lambda vars: {
                    "tenant_id": getattr(vars.get("created_tenant"), "id", "mock-tenant-id"),
                    "body": PlanReservation(next_plan_id=get_or_create_test_plan_id())
                },
                description="UpdateTenantPlanWithHttpInfo",
                skip=not stripe_configured,
                skip_reason="Requires Stripe integration (STRIPE_SECRET_KEY)"
            ),
            Step(
                method_name="update_tenant_billing_info_with_http_info",
                params=lambda vars: {
                    "tenant_id": getattr(vars.get("created_tenant"), "id", "mock-tenant-id"),
                    "body": BillingInfo(
                        name="Test Company HTTP",
                        invoice_language=InvoiceLanguage.JA_MINUS_JP,
                        address=BillingAddress(
                            city="Chiyoda",
                            country="JP",
                            postal_code="100-0001",
                            state="Tokyo",
                            street="1-1-1 Test Building"
                        )
                    )
                },
                description="UpdateTenantBillingInfoWithHttpInfo",
                skip=not stripe_configured,
                skip_reason="Requires Stripe integration (STRIPE_SECRET_KEY)"
            ),
            Step(
                method_name="delete_tenant_with_http_info",
                params=lambda vars: {"tenant_id": getattr(vars.get("created_tenant"), "id", "mock-tenant-id")},
                description="DeleteTenantWithHttpInfo after missing methods test"
            ),
            Step(
                method_name="delete_saas_user_with_http_info",
                params=lambda vars: {"user_id": getattr(vars.get("created_user"), "id", "mock-user-id")},
                description="DeleteSaasUserWithHttpInfo after missing methods test"
            ),
        ],
        tags=["auth", "missing-methods", "with-http-info"]
    )


def get_sign_up_and_provider_management_story() -> Story:
    """サインアップとプロバイダー管理のストーリー"""
    from saasus_sdk_python.src.auth.models.update_sign_in_settings_param import UpdateSignInSettingsParam
    from saasus_sdk_python.src.auth.models.self_regist import SelfRegist
    from saasus_sdk_python.src.auth.models.sign_up_param import SignUpParam
    from saasus_sdk_python.src.auth.models.resend_sign_up_confirmation_email_param import ResendSignUpConfirmationEmailParam
    from saasus_sdk_python.src.auth.models.tenant_props import TenantProps
    
    signup_email = unique_email("signup")
    
    return Story(
        name="sign_up_and_provider_management",
        description="サインアップ、AWS Marketplace連携、プロバイダー管理機能をテストします。",
        module="auth",
        steps=[
            # Enable self registration
            Step(
                method_name="update_sign_in_settings",
                params=lambda vars: {
                    "update_sign_in_settings_param": UpdateSignInSettingsParam(
                        self_regist=SelfRegist(enable=True)
                    )
                },
                description="UpdateSignInSettings (Enable Self Regist)"
            ),
            Step(
                method_name="get_sign_in_settings",
                params=lambda vars: {},
                description="GetSignInSettings (Verify Self Regist)",
                store_as="sign_in_settings"
            ),
            # SignUp
            Step(
                method_name="sign_up",
                params=lambda vars: {
                    "sign_up_param": SignUpParam(email=signup_email)
                },
                description="SignUp",
                store_as="signup_user"
            ),
            # ResendSignUpConfirmationEmail
            Step(
                method_name="resend_sign_up_confirmation_email",
                params=lambda vars: {
                    "resend_sign_up_confirmation_email_param": ResendSignUpConfirmationEmailParam(
                        email=getattr(vars.get("signup_user"), "email", signup_email)
                    )
                },
                description="ResendSignUpConfirmationEmail"
            ),
            # Delete signup user
            Step(
                method_name="delete_saas_user",
                params=lambda vars: {"user_id": getattr(vars.get("signup_user"), "id", "mock-user-id")},
                description="Delete signup user"
            ),
            # AWS Marketplace (skipped - requires valid token)
            Step(
                method_name="confirm_sign_up_with_aws_marketplace",
                params=lambda vars: {},
                description="ConfirmSignUpWithAwsMarketplace",
                skip=True,
                skip_reason="Requires valid AWS Marketplace registration token"
            ),
            # Create tenant for AWS Marketplace link test
            Step(
                method_name="create_tenant",
                params=lambda vars: {
                    "body": TenantProps(
                        name="signup-test-tenant",
                        attributes={},
                        back_office_staff_email="test-backoffice@example.com"
                    )
                },
                description="CreateTenant for AWS Marketplace link",
                store_as="created_tenant"
            ),
            Step(
                method_name="link_aws_marketplace",
                params=lambda vars: {},
                description="LinkAwsMarketplace",
                skip=True,
                skip_reason="Requires valid AWS Marketplace registration token"
            ),
            # Provider unlink test
            Step(
                method_name="create_saas_user",
                params=lambda vars: {
                    "create_saas_user_param": build_create_saas_user_params(
                        unique_email("provider-unlink"), get_default_password()
                    )
                },
                description="CreateSaasUser for provider unlink",
                store_as="provider_user"
            ),
            Step(
                method_name="unlink_provider",
                params=lambda vars: {
                    "provider_name": "Google",
                    "user_id": getattr(vars.get("provider_user"), "id", "mock-user-id")
                },
                description="UnlinkProvider",
                skip=True,
                skip_reason="Requires real social provider linking before unlink can succeed"
            ),
            # Cleanup
            Step(
                method_name="delete_saas_user",
                params=lambda vars: {"user_id": getattr(vars.get("provider_user"), "id", "mock-user-id")},
                description="DeleteSaasUser after provider test"
            ),
            Step(
                method_name="delete_tenant",
                params=lambda vars: {"tenant_id": getattr(vars.get("created_tenant"), "id", "mock-tenant-id")},
                description="DeleteTenant after AWS Marketplace test"
            ),
        ],
        tags=["auth", "signup", "provider"]
    )


def get_sign_up_and_provider_management_with_http_info_story() -> Story:
    """サインアップとプロバイダー管理のストーリー（_with_http_info版）"""
    from saasus_sdk_python.src.auth.models.update_sign_in_settings_param import UpdateSignInSettingsParam
    from saasus_sdk_python.src.auth.models.self_regist import SelfRegist
    from saasus_sdk_python.src.auth.models.sign_up_param import SignUpParam
    from saasus_sdk_python.src.auth.models.resend_sign_up_confirmation_email_param import ResendSignUpConfirmationEmailParam
    from saasus_sdk_python.src.auth.models.tenant_props import TenantProps
    
    signup_email = unique_email("signup")
    
    return Story(
        name="sign_up_and_provider_management_with_http_info",
        description="サインアップ、AWS Marketplace連携、プロバイダー管理機能をテストします（_with_http_info版）。",
        module="auth",
        steps=[
            Step(
                method_name="update_sign_in_settings_with_http_info",
                params=lambda vars: {
                    "update_sign_in_settings_param": UpdateSignInSettingsParam(
                        self_regist=SelfRegist(enable=True)
                    )
                },
                description="UpdateSignInSettingsWithHttpInfo (Enable Self Regist)"
            ),
            Step(
                method_name="get_sign_in_settings_with_http_info",
                params=lambda vars: {},
                description="GetSignInSettingsWithHttpInfo (Verify Self Regist)",
                store_as="sign_in_settings"
            ),
            Step(
                method_name="sign_up_with_http_info",
                params=lambda vars: {
                    "sign_up_param": SignUpParam(email=signup_email)
                },
                description="SignUpWithHttpInfo",
                store_as="signup_user"
            ),
            Step(
                method_name="resend_sign_up_confirmation_email_with_http_info",
                params=lambda vars: {
                    "resend_sign_up_confirmation_email_param": ResendSignUpConfirmationEmailParam(
                        email=getattr(vars.get("signup_user"), "email", signup_email)
                    )
                },
                description="ResendSignUpConfirmationEmailWithHttpInfo"
            ),
            Step(
                method_name="delete_saas_user_with_http_info",
                params=lambda vars: {"user_id": getattr(vars.get("signup_user"), "id", "mock-user-id")},
                description="Delete signup user with http info"
            ),
            Step(
                method_name="confirm_sign_up_with_aws_marketplace_with_http_info",
                params=lambda vars: {},
                description="ConfirmSignUpWithAwsMarketplaceWithHttpInfo",
                skip=True,
                skip_reason="Requires valid AWS Marketplace registration token"
            ),
            Step(
                method_name="create_tenant_with_http_info",
                params=lambda vars: {
                    "body": TenantProps(
                        name="signup-test-tenant",
                        attributes={},
                        back_office_staff_email="test-backoffice@example.com"
                    )
                },
                description="CreateTenantWithHttpInfo for AWS Marketplace link",
                store_as="created_tenant"
            ),
            Step(
                method_name="link_aws_marketplace_with_http_info",
                params=lambda vars: {},
                description="LinkAwsMarketplaceWithHttpInfo",
                skip=True,
                skip_reason="Requires valid AWS Marketplace registration token"
            ),
            Step(
                method_name="create_saas_user_with_http_info",
                params=lambda vars: {
                    "create_saas_user_param": build_create_saas_user_params(
                        unique_email("provider-unlink"), get_default_password()
                    )
                },
                description="CreateSaasUserWithHttpInfo for provider unlink",
                store_as="provider_user"
            ),
            Step(
                method_name="unlink_provider_with_http_info",
                params=lambda vars: {
                    "provider_name": "Google",
                    "user_id": getattr(vars.get("provider_user"), "id", "mock-user-id")
                },
                description="UnlinkProviderWithHttpInfo",
                skip=True,
                skip_reason="Requires real social provider linking before unlink can succeed"
            ),
            Step(
                method_name="delete_saas_user_with_http_info",
                params=lambda vars: {"user_id": getattr(vars.get("provider_user"), "id", "mock-user-id")},
                description="DeleteSaasUserWithHttpInfo after provider test"
            ),
            Step(
                method_name="delete_tenant_with_http_info",
                params=lambda vars: {"tenant_id": getattr(vars.get("created_tenant"), "id", "mock-tenant-id")},
                description="DeleteTenantWithHttpInfo after AWS Marketplace test"
            ),
        ],
        tags=["auth", "signup", "provider", "with-http-info"]
    )


def get_all_auth_stories() -> List[Story]:
    """全Auth APIストーリーを取得"""
    return [
        get_saas_user_attributes_story(),
        get_saas_user_attributes_with_http_info_story(),
        get_external_user_link_and_email_update_story(),
        get_external_user_link_and_email_update_with_http_info_story(),
        get_missing_methods_coverage_story(),
        get_missing_methods_coverage_with_http_info_story(),
        get_sign_up_and_provider_management_story(),
        get_sign_up_and_provider_management_with_http_info_story(),
        get_postman_collection_story(),
        get_postman_collection_with_http_info_story(),
    ]


def get_postman_collection_story() -> Story:
    """Postman Collectionに基づいた包括的なストーリー（通常版）
    
    カバーするAPI:
    - basic-info: GetBasicInfo, UpdateBasicInfo, FindNotificationMessages, UpdateNotificationMessages,
                  GetCustomizePages, UpdateCustomizePages, GetCustomizePageSettings, UpdateCustomizePageSettings
    - auth-info: GetAuthInfo, UpdateAuthInfo, GetIdentityProviders, UpdateIdentityProvider
    - user-info: GetUserInfo (Cognito IDトークン必要)
    - saas-users: GetSaasUsers, CreateSaasUser, GetSaasUser, UpdateSaasUserPassword, UpdateSaasUserEmail,
                  GetUserMfaPreference, CreateSecretCode, UpdateSoftwareToken, UpdateUserMfaPreference, DeleteSaasUser
    - user-attributes: GetUserAttributes, CreateUserAttribute, DeleteUserAttribute
    - roles: GetRoles, CreateRole, DeleteRole
    - envs: GetEnvs, CreateEnv, GetEnv, UpdateEnv, DeleteEnv
    - tenant-attributes: GetTenantAttributes, CreateTenantAttribute, DeleteTenantAttribute
    - tenants: GetTenants, CreateTenant, GetTenant, UpdateTenant, DeleteTenant,
               GetTenantIdentityProviders, UpdateTenantIdentityProvider
    - tenant-users: GetAllTenantUsers, GetAllTenantUser, CreateTenantUser, GetTenantUser, GetTenantUsers,
                    UpdateTenantUser, DeleteTenantUser
    - tenant-user-roles: CreateTenantUserRoles, DeleteTenantUserRole
    - invitation: CreateTenantInvitation, GetTenantInvitations, GetTenantInvitation, GetInvitationValidity, DeleteTenantInvitation
    - single-tenant: GetSingleTenantSettings, UpdateSingleTenantSettings, GetCloudFormationLaunchStackLinkForSingleTenant
    - auth-credentials: CreateAuthCredentials, GetAuthCredentials
    - sign-in-settings: GetSignInSettings, UpdateSignInSettings
    - aws-marketplace: SignUpWithAwsMarketplace
    """
    from saasus_sdk_python.src.auth.models.role import Role
    from saasus_sdk_python.src.auth.models.attribute import Attribute
    from saasus_sdk_python.src.auth.models.attribute_type import AttributeType
    from saasus_sdk_python.src.auth.models.tenant_props import TenantProps
    from saasus_sdk_python.src.auth.models.create_tenant_user_param import CreateTenantUserParam
    from saasus_sdk_python.src.auth.models.update_tenant_user_param import UpdateTenantUserParam
    from saasus_sdk_python.src.auth.models.create_tenant_invitation_param import CreateTenantInvitationParam
    from saasus_sdk_python.src.auth.models.invited_user_environment_information_inner import InvitedUserEnvironmentInformationInner
    from saasus_sdk_python.src.auth.models.update_basic_info_param import UpdateBasicInfoParam
    from saasus_sdk_python.src.auth.models.update_notification_messages_param import UpdateNotificationMessagesParam
    from saasus_sdk_python.src.auth.models.message_template import MessageTemplate
    from saasus_sdk_python.src.auth.models.update_customize_pages_param import UpdateCustomizePagesParam
    from saasus_sdk_python.src.auth.models.customize_page_props import CustomizePageProps
    from saasus_sdk_python.src.auth.models.update_customize_page_settings_param import UpdateCustomizePageSettingsParam
    from saasus_sdk_python.src.auth.models.update_identity_provider_param import UpdateIdentityProviderParam
    from saasus_sdk_python.src.auth.models.identity_provider_props import IdentityProviderProps
    from saasus_sdk_python.src.auth.models.update_env_param import UpdateEnvParam
    from saasus_sdk_python.src.auth.models.env import Env
    from saasus_sdk_python.src.auth.models.update_saas_user_password_param import UpdateSaasUserPasswordParam
    from saasus_sdk_python.src.auth.models.update_saas_user_email_param import UpdateSaasUserEmailParam
    from saasus_sdk_python.src.auth.models.update_software_token_param import UpdateSoftwareTokenParam
    from saasus_sdk_python.src.auth.models.update_single_tenant_settings_param import UpdateSingleTenantSettingsParam
    from saasus_sdk_python.src.auth.models.create_secret_code_param import CreateSecretCodeParam
    from saasus_sdk_python.src.auth.models.mfa_preference import MfaPreference
    from saasus_sdk_python.src.auth.models.tenant_identity_provider_props import TenantIdentityProviderProps
    from saasus_sdk_python.src.auth.models.sign_up_with_aws_marketplace_param import SignUpWithAwsMarketplaceParam
    from saasus_sdk_python.src.auth.models.auth_info import AuthInfo
    from saasus_sdk_python.src.auth.models.plan_reservation import PlanReservation
    from saasus_sdk_python.src.auth.models.billing_info import BillingInfo
    from saasus_sdk_python.src.auth.models.update_sign_in_settings_param import UpdateSignInSettingsParam
    from saasus_sdk_python.src.auth.models.device_configuration import DeviceConfiguration
    from saasus_sdk_python.src.auth.models.billing_address import BillingAddress
    from saasus_sdk_python.src.auth.models.invoice_language import InvoiceLanguage
    from saasus_sdk_python.src.auth.models.mfa_configuration import MfaConfiguration
    from saasus_sdk_python.src.auth.models.account_verification import AccountVerification
    from saasus_sdk_python.src.auth.models.self_regist import SelfRegist
    from saasus_sdk_python.src.auth.models.create_tenant_user_roles_param import CreateTenantUserRolesParam
    
    role_name = unique_string("role")
    attr_name = unique_string("attr")
    user_attr_name = unique_string("uattr")
    env_name = unique_string("env")
    
    # Cognitoトークンを取得
    cognito_tokens = get_cognito_tokens_safe()
    cognito_configured = cognito_tokens is not None
    
    # Stripe設定を確認
    stripe_configured = is_stripe_configured()
    if stripe_configured:
        setup_stripe_integration()
    
    return Story(
        name="postman_collection_story",
        description="Postman Collectionに基づいた包括的なAuth APIテスト",
        module="auth",
        steps=[
            # === basic-info ===
            Step(
                method_name="get_basic_info",
                params=lambda vars: {},
                description="GetBasicInfo",
                store_as="basic_info"
            ),
            Step(
                method_name="update_basic_info",
                params=lambda vars: {
                    "update_basic_info_param": UpdateBasicInfoParam(
                        domain_name=getattr(vars.get("basic_info"), "domain_name", "example"),
                        from_email_address=getattr(vars.get("basic_info"), "from_email_address", "noreply@example.com"),
                        reply_email_address=getattr(vars.get("basic_info"), "reply_email_address", "support@example.com")
                    )
                },
                description="UpdateBasicInfo"
            ),
            Step(
                method_name="find_notification_messages",
                params=lambda vars: {},
                description="FindNotificationMessages",
                store_as="notification_messages"
            ),
            Step(
                method_name="update_notification_messages",
                params=lambda vars: {
                    "update_notification_messages_param": UpdateNotificationMessagesParam(
                        authentication_mfa=MessageTemplate(
                            subject="Verify your new account",
                            message="The verification code to your new account is {####}"
                        ),
                        create_user=MessageTemplate(
                            subject="Verify your new account",
                            message="The verification code to your new account is {####}"
                        )
                    )
                },
                description="UpdateNotificationMessages"
            ),
            Step(
                method_name="get_customize_pages",
                params=lambda vars: {},
                description="GetCustomizePages",
                store_as="customize_pages"
            ),
            Step(
                method_name="update_customize_pages",
                params=lambda vars: {
                    "update_customize_pages_param": UpdateCustomizePagesParam(
                        sign_up_page=CustomizePageProps(
                            html_contents="<html><div>Sign Up Page</div></html>",
                            is_privacy_policy=False,
                            is_terms_of_service=False
                        ),
                        sign_in_page=CustomizePageProps(
                            html_contents="<html><div>Sign In Page</div></html>",
                            is_privacy_policy=False,
                            is_terms_of_service=False
                        )
                    )
                },
                description="UpdateCustomizePages"
            ),
            Step(
                method_name="get_customize_page_settings",
                params=lambda vars: {},
                description="GetCustomizePageSettings",
                store_as="customize_page_settings"
            ),
            Step(
                method_name="update_customize_page_settings",
                params=lambda vars: {
                    "update_customize_page_settings_param": UpdateCustomizePageSettingsParam(
                        title="Test Title",
                        terms_of_service_url="https://example.com/tos",
                        privacy_policy_url="https://example.com/privacy",
                        google_tag_manager_container_id="",
                        icon="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNkYPhfDwAChwGA60e6kgAAAABJRU5ErkJggg==",
                        favicon="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNkYPhfDwAChwGA60e6kgAAAABJRU5ErkJggg=="
                    )
                },
                description="UpdateCustomizePageSettings"
            ),
            # === auth-info ===
            Step(
                method_name="get_auth_info",
                params=lambda vars: {},
                description="GetAuthInfo",
                store_as="auth_info"
            ),
            Step(
                method_name="update_auth_info",
                params=lambda vars: {
                    "body": AuthInfo(
                        callback_url=getattr(vars.get("auth_info"), "callback_url", "https://example.com/callback")
                    )
                },
                description="UpdateAuthInfo"
            ),
            Step(
                method_name="get_identity_providers",
                params=lambda vars: {},
                description="GetIdentityProviders",
                store_as="identity_providers"
            ),
            Step(
                method_name="update_identity_provider",
                params=lambda vars: {
                    "update_identity_provider_param": UpdateIdentityProviderParam(
                        provider="Google",
                        identity_provider_props=IdentityProviderProps(
                            application_id="test-app-id",
                            application_secret="test-app-secret",
                            approval_scope="profile email openid"
                        )
                    )
                },
                description="UpdateIdentityProvider"
            ),
            # === sign-in-settings ===
            Step(
                method_name="get_sign_in_settings",
                params=lambda vars: {},
                description="GetSignInSettings",
                store_as="sign_in_settings"
            ),
            Step(
                method_name="update_sign_in_settings",
                params=lambda vars: {
                    "update_sign_in_settings_param": UpdateSignInSettingsParam(
                        device_configuration=DeviceConfiguration(device_remembering="userOptIn"),
                        mfa_configuration=MfaConfiguration(mfa_configuration="optional"),
                        account_verification=AccountVerification(verification_method="code", sending_to="email"),
                        self_regist=SelfRegist(enable=True)
                    )
                },
                description="UpdateSignInSettings"
            ),
            # === user-info ===
            Step(
                method_name="get_user_info",
                params=lambda vars: {
                    "token": cognito_tokens["id_token"] if cognito_tokens else "dummy-token"
                },
                description="GetUserInfo",
                store_as="cognito_user_info",
                allow_failure=True
            ),
            # === saas-users ===
            Step(
                method_name="get_saas_users",
                params=lambda vars: {},
                description="GetSaasUsers"
            ),
            Step(
                method_name="create_saas_user",
                params=lambda vars: {
                    "create_saas_user_param": build_create_saas_user_params(unique_email("mfa-test"), get_default_password())
                },
                description="CreateSaasUser for MFA test",
                store_as="mfa_test_user"
            ),
            Step(
                method_name="get_saas_user",
                params=lambda vars: {
                    "user_id": getattr(vars.get("mfa_test_user"), "id", "mock-user-id")
                },
                description="GetSaasUser"
            ),
            Step(
                method_name="update_saas_user_password",
                params=lambda vars: {
                    "user_id": getattr(vars.get("mfa_test_user"), "id", "mock-user-id"),
                    "update_saas_user_password_param": UpdateSaasUserPasswordParam(password=get_default_password())
                },
                description="UpdateSaasUserPassword"
            ),
            Step(
                method_name="update_saas_user_email",
                params=lambda vars: {
                    "user_id": getattr(vars.get("mfa_test_user"), "id", "mock-user-id"),
                    "update_saas_user_email_param": UpdateSaasUserEmailParam(email=unique_email("mfa-test-updated"))
                },
                description="UpdateSaasUserEmail"
            ),
            Step(
                method_name="get_user_mfa_preference",
                params=lambda vars: {
                    "user_id": getattr(vars.get("mfa_test_user"), "id", "mock-user-id")
                },
                description="GetUserMfaPreference"
            ),
            Step(
                method_name="create_secret_code",
                params=lambda vars: {
                    "user_id": getattr(vars.get("mfa_test_user"), "id", "mock-user-id"),
                    "create_secret_code_param": CreateSecretCodeParam(access_token="dummy-token")
                },
                description="CreateSecretCode",
                skip=True,
                skip_reason="Requires valid Cognito access token"
            ),
            Step(
                method_name="update_software_token",
                params=lambda vars: {
                    "user_id": getattr(vars.get("mfa_test_user"), "id", "mock-user-id"),
                    "update_software_token_param": UpdateSoftwareTokenParam(
                        access_token="dummy-token",
                        verification_code="123456"
                    )
                },
                description="UpdateSoftwareToken",
                skip=True,
                skip_reason="Requires valid Cognito access token and verification code"
            ),
            Step(
                method_name="update_user_mfa_preference",
                params=lambda vars: {
                    "user_id": getattr(vars.get("mfa_test_user"), "id", "mock-user-id"),
                    "body": MfaPreference(enabled=False)
                },
                description="UpdateUserMfaPreference"
            ),
            Step(
                method_name="delete_saas_user",
                params=lambda vars: {
                    "user_id": getattr(vars.get("mfa_test_user"), "id", "mock-user-id")
                },
                description="DeleteSaasUser for MFA test"
            ),
            # === user-attributes ===
            Step(
                method_name="get_user_attributes",
                params=lambda vars: {},
                description="GetUserAttributes"
            ),
            Step(
                method_name="create_user_attribute",
                params=lambda vars: {
                    "body": Attribute(attribute_name=user_attr_name, display_name=f"User Attr {user_attr_name}", attribute_type=AttributeType.STRING)
                },
                description="CreateUserAttribute",
                store_as="created_user_attr"
            ),
            # === roles ===
            Step(
                method_name="get_roles",
                params=lambda vars: {},
                description="GetRoles (before create)"
            ),
            Step(
                method_name="create_role",
                params=lambda vars: {
                    "body": Role(role_name=role_name, display_name=f"Test Role {role_name}")
                },
                description="CreateRole",
                store_as="created_role"
            ),
            Step(
                method_name="get_roles",
                params=lambda vars: {},
                description="GetRoles (after create)"
            ),
            # === envs ===
            Step(
                method_name="get_envs",
                params=lambda vars: {},
                description="GetEnvs",
                store_as="envs_list"
            ),
            Step(
                method_name="create_env",
                params=lambda vars: {
                    "body": Env(id=random.randint(100000, 999999), name=env_name, display_name=f"Test Env {env_name}")
                },
                description="CreateEnv",
                store_as="created_env"
            ),
            Step(
                method_name="get_env",
                params=lambda vars: {
                    "env_id": getattr(vars.get("created_env"), "id", 1)
                },
                description="GetEnv"
            ),
            Step(
                method_name="update_env",
                params=lambda vars: {
                    "env_id": getattr(vars.get("created_env"), "id", 1),
                    "update_env_param": UpdateEnvParam(
                        name=env_name,
                        display_name=f"Updated Env {env_name}"
                    )
                },
                description="UpdateEnv"
            ),
            # === tenant-attributes ===
            Step(
                method_name="get_tenant_attributes",
                params=lambda vars: {},
                description="GetTenantAttributes (before create)"
            ),
            Step(
                method_name="create_tenant_attribute",
                params=lambda vars: {
                    "body": Attribute(attribute_name=attr_name, display_name=f"Tenant Attr {attr_name}", attribute_type=AttributeType.STRING)
                },
                description="CreateTenantAttribute",
                store_as="created_tenant_attr"
            ),
            Step(
                method_name="get_tenant_attributes",
                params=lambda vars: {},
                description="GetTenantAttributes (after create)"
            ),
            # === tenants ===
            Step(
                method_name="get_tenants",
                params=lambda vars: {},
                description="GetTenants (before create)"
            ),
            Step(
                method_name="create_tenant",
                params=lambda vars: {
                    "body": TenantProps(
                        name=unique_string("tenant"),
                        attributes={},
                        back_office_staff_email=unique_email("tenant-staff")
                    )
                },
                description="CreateTenant",
                store_as="created_tenant"
            ),
            Step(
                method_name="get_tenant",
                params=lambda vars: {
                    "tenant_id": getattr(vars.get("created_tenant"), "id", "mock-tenant-id")
                },
                description="GetTenant"
            ),
            Step(
                method_name="update_tenant",
                params=lambda vars: {
                    "tenant_id": getattr(vars.get("created_tenant"), "id", "mock-tenant-id"),
                    "body": TenantProps(
                        name=unique_string("tenant-updated"),
                        attributes={getattr(vars.get("created_tenant_attr"), "attribute_name", attr_name): "test-value"},
                        back_office_staff_email=unique_email("tenant-staff-updated")
                    )
                },
                description="UpdateTenant"
            ),
            # === tenant-plan & billing (Stripe連携) ===
            Step(
                method_name="update_tenant_plan",
                params=lambda vars: {
                    "tenant_id": getattr(vars.get("created_tenant"), "id", "mock-tenant-id"),
                    "body": PlanReservation(next_plan_id=get_or_create_test_plan_id())
                },
                description="UpdateTenantPlan",
                skip=not stripe_configured,
                skip_reason="Requires Stripe integration (STRIPE_SECRET_KEY)"
            ),
            Step(
                method_name="update_tenant_billing_info",
                params=lambda vars: {
                    "tenant_id": getattr(vars.get("created_tenant"), "id", "mock-tenant-id"),
                    "body": BillingInfo(
                        name="テスト用文字列",
                        invoice_language=InvoiceLanguage.JA_MINUS_JP,
                        address=BillingAddress(
                            city="test_city",
                            country="JP",
                            postal_code="123-4567",
                            state="test_state",
                            street="test_street",
                            additional_address_info="test_additional_info"
                        )
                    )
                },
                description="UpdateTenantBillingInfo",
                skip=not stripe_configured,
                skip_reason="Requires Stripe integration (STRIPE_SECRET_KEY)"
            ),
            Step(
                method_name="create_tenant_and_pricing",
                params=lambda vars: {},
                description="CreateTenantAndPricing",
                skip=not stripe_configured,
                skip_reason="Requires Stripe integration (STRIPE_SECRET_KEY)"
            ),
            Step(
                method_name="get_stripe_customer",
                params=lambda vars: {
                    "tenant_id": getattr(vars.get("created_tenant"), "id", "mock-tenant-id")
                },
                description="GetStripeCustomer",
                skip=not stripe_configured,
                skip_reason="Requires Stripe integration (STRIPE_SECRET_KEY)"
            ),
            Step(
                method_name="delete_stripe_tenant_and_pricing",
                params=lambda vars: {},
                description="DeleteStripeTenantAndPricing",
                skip=not stripe_configured,
                skip_reason="Requires Stripe integration (STRIPE_SECRET_KEY)"
            ),
            Step(
                method_name="reset_plan",
                params=lambda vars: {},
                description="ResetPlan",
                skip=not stripe_configured,
                skip_reason="Requires Stripe integration (STRIPE_SECRET_KEY)"
            ),
            Step(
                method_name="get_tenant_identity_providers",
                params=lambda vars: {
                    "tenant_id": getattr(vars.get("created_tenant"), "id", "mock-tenant-id")
                },
                description="GetTenantIdentityProviders"
            ),
            Step(
                method_name="update_tenant_identity_provider",
                params=lambda vars: {
                    "tenant_id": getattr(vars.get("created_tenant"), "id", "mock-tenant-id"),
                    "update_tenant_identity_provider_param": TenantIdentityProviderProps()
                },
                description="UpdateTenantIdentityProvider",
                skip=True,
                skip_reason="Requires valid identity provider configuration"
            ),
            # === all-tenant-users ===
            Step(
                method_name="get_all_tenant_users",
                params=lambda vars: {},
                description="GetAllTenantUsers"
            ),
            # === invitation (Cognitoアクセストークン必要) ===
            # CognitoユーザーをテナントユーザーとしてCognitoユーザーをテナントに追加（招待者はテナントに所属している必要がある）
            # 注: CognitoユーザーはSaaSユーザーとして事前に登録されている必要がある
            Step(
                method_name="create_tenant_user",
                params=lambda vars: {
                    "tenant_id": getattr(vars.get("created_tenant"), "id", "mock-tenant-id"),
                    "create_tenant_user_param": CreateTenantUserParam(
                        email=getattr(vars.get("cognito_user_info"), "email", "mock@example.com"),
                        attributes={}
                    )
                },
                description="CreateTenantUser for Cognito inviter",
                store_as="cognito_tenant_user",
                skip=not cognito_configured,
                skip_reason="Requires Cognito configuration (E2E_COGNITO_*)"
            ),
            Step(
                method_name="create_tenant_invitation",
                params=lambda vars: {
                    "tenant_id": getattr(vars.get("created_tenant"), "id", "mock-tenant-id"),
                    "create_tenant_invitation_param": CreateTenantInvitationParam(
                        email=unique_email("invitee"),
                        access_token=cognito_tokens["access_token"] if cognito_tokens else "",
                        envs=[InvitedUserEnvironmentInformationInner(
                            id=vars.get("envs_list").envs[0].id if vars.get("envs_list") and vars.get("envs_list").envs else 3,
                            role_names=["admin"]
                        )]
                    )
                },
                description="CreateTenantInvitation",
                store_as="invitation",
                skip=True,
                skip_reason="Requires DNS and SES validation in the environment"
            ),
            Step(
                method_name="get_tenant_invitations",
                params=lambda vars: {
                    "tenant_id": getattr(vars.get("created_tenant"), "id", "mock-tenant-id")
                },
                description="GetTenantInvitations"
            ),
            Step(
                method_name="get_tenant_invitation",
                params=lambda vars: {
                    "tenant_id": getattr(vars.get("created_tenant"), "id", "mock-tenant-id"),
                    "invitation_id": getattr(vars.get("invitation"), "id", "mock-inv-id")
                },
                description="GetTenantInvitation",
                skip=True,
                skip_reason="Requires invitation created (DNS/SES validation needed)"
            ),
            Step(
                method_name="get_invitation_validity",
                params=lambda vars: {
                    "invitation_id": getattr(vars.get("invitation"), "id", "mock-inv-id")
                },
                description="GetInvitationValidity",
                skip=True,
                skip_reason="Requires invitation created (DNS/SES validation needed)"
            ),
            Step(
                method_name="delete_tenant_invitation",
                params=lambda vars: {
                    "tenant_id": getattr(vars.get("created_tenant"), "id", "mock-tenant-id"),
                    "invitation_id": getattr(vars.get("invitation"), "id", "mock-inv-id")
                },
                description="DeleteTenantInvitation",
                skip=True,
                skip_reason="Requires invitation created (DNS/SES validation needed)"
            ),
            Step(
                method_name="validate_invitation",
                params=lambda vars: {
                    "invitation_id": getattr(vars.get("invitation"), "id", "mock-inv-id")
                },
                description="ValidateInvitation",
                skip=True,
                skip_reason="Requires valid invitation (DNS/SES validation needed)"
            ),
            # === tenant-users ===
            Step(
                method_name="create_saas_user",
                params=lambda vars: {
                    "create_saas_user_param": build_create_saas_user_params(unique_email("tenant-user"), get_default_password())
                },
                description="CreateSaasUser for tenant user",
                store_as="saas_user"
            ),
            Step(
                method_name="create_tenant_user",
                params=lambda vars: {
                    "tenant_id": getattr(vars.get("created_tenant"), "id", "mock-tenant-id"),
                    "create_tenant_user_param": CreateTenantUserParam(
                        email=getattr(vars.get("saas_user"), "email", "mock@example.com"),
                        attributes={}
                    )
                },
                description="CreateTenantUser"
            ),
            Step(
                method_name="get_all_tenant_user",
                params=lambda vars: {
                    "user_id": getattr(vars.get("saas_user"), "id", "mock-user-id")
                },
                description="GetAllTenantUser"
            ),
            Step(
                method_name="get_tenant_user",
                params=lambda vars: {
                    "tenant_id": getattr(vars.get("created_tenant"), "id", "mock-tenant-id"),
                    "user_id": getattr(vars.get("saas_user"), "id", "mock-user-id")
                },
                description="GetTenantUser"
            ),
            Step(
                method_name="get_tenant_users",
                params=lambda vars: {
                    "tenant_id": getattr(vars.get("created_tenant"), "id", "mock-tenant-id")
                },
                description="GetTenantUsers"
            ),
            Step(
                method_name="update_tenant_user",
                params=lambda vars: {
                    "tenant_id": getattr(vars.get("created_tenant"), "id", "mock-tenant-id"),
                    "user_id": getattr(vars.get("saas_user"), "id", "mock-user-id"),
                    "update_tenant_user_param": UpdateTenantUserParam(attributes={})
                },
                description="UpdateTenantUser"
            ),
            # === tenant-user-roles ===
            Step(
                method_name="create_tenant_user_roles",
                params=lambda vars: {
                    "tenant_id": getattr(vars.get("created_tenant"), "id", "mock-tenant-id"),
                    "user_id": getattr(vars.get("saas_user"), "id", "mock-user-id"),
                    "env_id": getattr(vars.get("created_env"), "id", 1),
                    "create_tenant_user_roles_param": CreateTenantUserRolesParam(
                        role_names=[getattr(vars.get("created_role"), "role_name", role_name)]
                    )
                },
                description="CreateTenantUserRoles"
            ),
            Step(
                method_name="delete_tenant_user_role",
                params=lambda vars: {
                    "tenant_id": getattr(vars.get("created_tenant"), "id", "mock-tenant-id"),
                    "user_id": getattr(vars.get("saas_user"), "id", "mock-user-id"),
                    "env_id": getattr(vars.get("created_env"), "id", 1),
                    "role_name": getattr(vars.get("created_role"), "role_name", role_name)
                },
                description="DeleteTenantUserRole"
            ),
            # === single-tenant ===
            Step(
                method_name="get_single_tenant_settings",
                params=lambda vars: {},
                description="GetSingleTenantSettings"
            ),
            Step(
                method_name="update_single_tenant_settings",
                params=lambda vars: {
                    "update_single_tenant_settings_param": UpdateSingleTenantSettingsParam(enabled=False)
                },
                description="UpdateSingleTenantSettings"
            ),
            Step(
                method_name="get_cloud_formation_launch_stack_link_for_single_tenant",
                params=lambda vars: {},
                description="GetCloudFormationLaunchStackLinkForSingleTenant"
            ),
            # === auth-credentials ===
            Step(
                method_name="create_auth_credentials",
                params=lambda vars: {
                    "body": {"code": "test-code"}
                },
                description="CreateAuthCredentials",
                skip=True,
                skip_reason="Requires valid authorization code"
            ),
            Step(
                method_name="get_auth_credentials",
                params=lambda vars: {
                    "user_id": getattr(vars.get("saas_user"), "id", "mock-user-id"),
                    "auth_credential_id": "mock-credential-id"
                },
                description="GetAuthCredentials",
                skip=True,
                skip_reason="Requires valid auth credential ID"
            ),
            # === aws-marketplace ===
            Step(
                method_name="sign_up_with_aws_marketplace",
                params=lambda vars: {
                    "sign_up_with_aws_marketplace_param": SignUpWithAwsMarketplaceParam(
                        registration_token="test-token",
                        email=unique_email("aws-marketplace"),
                        password=get_default_password()
                    )
                },
                description="SignUpWithAwsMarketplace",
                skip=True,
                skip_reason="Requires valid AWS Marketplace registration token"
            ),
            # === cleanup ===
            Step(
                method_name="delete_tenant_user",
                params=lambda vars: {
                    "tenant_id": getattr(vars.get("created_tenant"), "id", "mock-tenant-id"),
                    "user_id": getattr(vars.get("saas_user"), "id", "mock-user-id")
                },
                description="DeleteTenantUser"
            ),
            Step(
                method_name="delete_tenant",
                params=lambda vars: {
                    "tenant_id": getattr(vars.get("created_tenant"), "id", "mock-tenant-id")
                },
                description="DeleteTenant"
            ),
            Step(
                method_name="delete_env",
                params=lambda vars: {
                    "env_id": getattr(vars.get("created_env"), "id", 1)
                },
                description="DeleteEnv"
            ),
            Step(
                method_name="delete_saas_user",
                params=lambda vars: {
                    "user_id": getattr(vars.get("saas_user"), "id", "mock-user-id")
                },
                description="DeleteSaasUser"
            ),
            Step(
                method_name="delete_user_attribute",
                params=lambda vars: {
                    "attribute_name": getattr(vars.get("created_user_attr"), "attribute_name", user_attr_name)
                },
                description="DeleteUserAttribute"
            ),
            Step(
                method_name="delete_role",
                params=lambda vars: {
                    "role_name": getattr(vars.get("created_role"), "role_name", role_name)
                },
                description="DeleteRole"
            ),
            Step(
                method_name="delete_tenant_attribute",
                params=lambda vars: {
                    "attribute_name": getattr(vars.get("created_tenant_attr"), "attribute_name", attr_name)
                },
                description="DeleteTenantAttribute"
            ),
        ],
        tags=["auth", "postman", "comprehensive"]
    )


def get_postman_collection_with_http_info_story() -> Story:
    """Postman Collectionに基づいた包括的なストーリー（_with_http_info版）"""
    from saasus_sdk_python.src.auth.models.role import Role
    from saasus_sdk_python.src.auth.models.attribute import Attribute
    from saasus_sdk_python.src.auth.models.attribute_type import AttributeType
    from saasus_sdk_python.src.auth.models.tenant_props import TenantProps
    from saasus_sdk_python.src.auth.models.create_tenant_user_param import CreateTenantUserParam
    from saasus_sdk_python.src.auth.models.update_tenant_user_param import UpdateTenantUserParam
    from saasus_sdk_python.src.auth.models.create_tenant_invitation_param import CreateTenantInvitationParam
    from saasus_sdk_python.src.auth.models.invited_user_environment_information_inner import InvitedUserEnvironmentInformationInner
    from saasus_sdk_python.src.auth.models.update_basic_info_param import UpdateBasicInfoParam
    from saasus_sdk_python.src.auth.models.update_notification_messages_param import UpdateNotificationMessagesParam
    from saasus_sdk_python.src.auth.models.message_template import MessageTemplate
    from saasus_sdk_python.src.auth.models.update_customize_pages_param import UpdateCustomizePagesParam
    from saasus_sdk_python.src.auth.models.customize_page_props import CustomizePageProps
    from saasus_sdk_python.src.auth.models.update_customize_page_settings_param import UpdateCustomizePageSettingsParam
    from saasus_sdk_python.src.auth.models.update_identity_provider_param import UpdateIdentityProviderParam
    from saasus_sdk_python.src.auth.models.identity_provider_props import IdentityProviderProps
    from saasus_sdk_python.src.auth.models.update_env_param import UpdateEnvParam
    from saasus_sdk_python.src.auth.models.env import Env
    from saasus_sdk_python.src.auth.models.update_saas_user_password_param import UpdateSaasUserPasswordParam
    from saasus_sdk_python.src.auth.models.update_saas_user_email_param import UpdateSaasUserEmailParam
    from saasus_sdk_python.src.auth.models.update_software_token_param import UpdateSoftwareTokenParam
    from saasus_sdk_python.src.auth.models.update_single_tenant_settings_param import UpdateSingleTenantSettingsParam
    from saasus_sdk_python.src.auth.models.create_secret_code_param import CreateSecretCodeParam
    from saasus_sdk_python.src.auth.models.mfa_preference import MfaPreference
    from saasus_sdk_python.src.auth.models.tenant_identity_provider_props import TenantIdentityProviderProps
    from saasus_sdk_python.src.auth.models.sign_up_with_aws_marketplace_param import SignUpWithAwsMarketplaceParam
    from saasus_sdk_python.src.auth.models.auth_info import AuthInfo
    from saasus_sdk_python.src.auth.models.plan_reservation import PlanReservation
    from saasus_sdk_python.src.auth.models.billing_info import BillingInfo
    from saasus_sdk_python.src.auth.models.update_sign_in_settings_param import UpdateSignInSettingsParam
    from saasus_sdk_python.src.auth.models.device_configuration import DeviceConfiguration
    from saasus_sdk_python.src.auth.models.billing_address import BillingAddress
    from saasus_sdk_python.src.auth.models.invoice_language import InvoiceLanguage
    from saasus_sdk_python.src.auth.models.mfa_configuration import MfaConfiguration
    from saasus_sdk_python.src.auth.models.account_verification import AccountVerification
    from saasus_sdk_python.src.auth.models.self_regist import SelfRegist
    from saasus_sdk_python.src.auth.models.create_tenant_user_roles_param import CreateTenantUserRolesParam
    
    role_name = unique_string("role")
    attr_name = unique_string("attr")
    user_attr_name = unique_string("uattr")
    env_name = unique_string("env")
    
    cognito_tokens = get_cognito_tokens_safe()
    cognito_configured = cognito_tokens is not None
    
    # Stripe設定を確認
    stripe_configured = is_stripe_configured()
    if stripe_configured:
        setup_stripe_integration()
    
    return Story(
        name="postman_collection_story_with_http_info",
        description="Postman Collectionに基づいた包括的なAuth APIテスト（_with_http_info版）",
        module="auth",
        steps=[
            # === basic-info ===
            Step(
                method_name="get_basic_info_with_http_info",
                params=lambda vars: {},
                description="GetBasicInfoWithHttpInfo",
                store_as="basic_info"
            ),
            Step(
                method_name="update_basic_info_with_http_info",
                params=lambda vars: {
                    "update_basic_info_param": UpdateBasicInfoParam(
                        domain_name=getattr(vars.get("basic_info"), "domain_name", "example"),
                        from_email_address=getattr(vars.get("basic_info"), "from_email_address", "noreply@example.com"),
                        reply_email_address=getattr(vars.get("basic_info"), "reply_email_address", "support@example.com")
                    )
                },
                description="UpdateBasicInfoWithHttpInfo"
            ),
            Step(
                method_name="find_notification_messages_with_http_info",
                params=lambda vars: {},
                description="FindNotificationMessagesWithHttpInfo",
                store_as="notification_messages"
            ),
            Step(
                method_name="update_notification_messages_with_http_info",
                params=lambda vars: {
                    "update_notification_messages_param": UpdateNotificationMessagesParam(
                        authentication_mfa=MessageTemplate(
                            subject="Verify your new account",
                            message="The verification code to your new account is {####}"
                        ),
                        create_user=MessageTemplate(
                            subject="Verify your new account",
                            message="The verification code to your new account is {####}"
                        )
                    )
                },
                description="UpdateNotificationMessagesWithHttpInfo"
            ),
            Step(
                method_name="get_customize_pages_with_http_info",
                params=lambda vars: {},
                description="GetCustomizePagesWithHttpInfo",
                store_as="customize_pages"
            ),
            Step(
                method_name="update_customize_pages_with_http_info",
                params=lambda vars: {
                    "update_customize_pages_param": UpdateCustomizePagesParam(
                        sign_up_page=CustomizePageProps(
                            html_contents="<html><div>Sign Up Page</div></html>",
                            is_privacy_policy=False,
                            is_terms_of_service=False
                        ),
                        sign_in_page=CustomizePageProps(
                            html_contents="<html><div>Sign In Page</div></html>",
                            is_privacy_policy=False,
                            is_terms_of_service=False
                        )
                    )
                },
                description="UpdateCustomizePagesWithHttpInfo"
            ),
            Step(
                method_name="get_customize_page_settings_with_http_info",
                params=lambda vars: {},
                description="GetCustomizePageSettingsWithHttpInfo",
                store_as="customize_page_settings"
            ),
            Step(
                method_name="update_customize_page_settings_with_http_info",
                params=lambda vars: {
                    "update_customize_page_settings_param": UpdateCustomizePageSettingsParam(
                        title="Test Title",
                        terms_of_service_url="https://example.com/tos",
                        privacy_policy_url="https://example.com/privacy",
                        google_tag_manager_container_id="",
                        icon="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNkYPhfDwAChwGA60e6kgAAAABJRU5ErkJggg==",
                        favicon="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNkYPhfDwAChwGA60e6kgAAAABJRU5ErkJggg=="
                    )
                },
                description="UpdateCustomizePageSettingsWithHttpInfo"
            ),
            # === auth-info ===
            Step(
                method_name="get_auth_info_with_http_info",
                params=lambda vars: {},
                description="GetAuthInfoWithHttpInfo",
                store_as="auth_info"
            ),
            Step(
                method_name="update_auth_info_with_http_info",
                params=lambda vars: {
                    "body": AuthInfo(
                        callback_url=getattr(vars.get("auth_info"), "callback_url", "https://example.com/callback")
                    )
                },
                description="UpdateAuthInfoWithHttpInfo"
            ),
            Step(
                method_name="get_identity_providers_with_http_info",
                params=lambda vars: {},
                description="GetIdentityProvidersWithHttpInfo",
                store_as="identity_providers"
            ),
            Step(
                method_name="update_identity_provider_with_http_info",
                params=lambda vars: {
                    "update_identity_provider_param": UpdateIdentityProviderParam(
                        provider="Google",
                        identity_provider_props=IdentityProviderProps(
                            application_id="test-app-id",
                            application_secret="test-app-secret",
                            approval_scope="profile email openid"
                        )
                    )
                },
                description="UpdateIdentityProviderWithHttpInfo"
            ),
            # === sign-in-settings ===
            Step(
                method_name="get_sign_in_settings_with_http_info",
                params=lambda vars: {},
                description="GetSignInSettingsWithHttpInfo",
                store_as="sign_in_settings"
            ),
            Step(
                method_name="update_sign_in_settings_with_http_info",
                params=lambda vars: {
                    "update_sign_in_settings_param": UpdateSignInSettingsParam(
                        device_configuration=DeviceConfiguration(device_remembering="userOptIn"),
                        mfa_configuration=MfaConfiguration(mfa_configuration="optional"),
                        account_verification=AccountVerification(verification_method="code", sending_to="email"),
                        self_regist=SelfRegist(enable=True)
                    )
                },
                description="UpdateSignInSettingsWithHttpInfo"
            ),
            # === user-info ===
            Step(
                method_name="get_user_info_with_http_info",
                params=lambda vars: {
                    "token": cognito_tokens["id_token"] if cognito_tokens else "dummy-token"
                },
                description="GetUserInfoWithHttpInfo",
                store_as="cognito_user_info",
                allow_failure=True
            ),
            # === saas-users ===
            Step(
                method_name="get_saas_users_with_http_info",
                params=lambda vars: {},
                description="GetSaasUsersWithHttpInfo"
            ),
            Step(
                method_name="create_saas_user_with_http_info",
                params=lambda vars: {
                    "create_saas_user_param": build_create_saas_user_params(unique_email("mfa-test"), get_default_password())
                },
                description="CreateSaasUser for MFA testWithHttpInfo",
                store_as="mfa_test_user"
            ),
            Step(
                method_name="get_saas_user_with_http_info",
                params=lambda vars: {
                    "user_id": getattr(vars.get("mfa_test_user"), "id", "mock-user-id")
                },
                description="GetSaasUserWithHttpInfo"
            ),
            Step(
                method_name="update_saas_user_password_with_http_info",
                params=lambda vars: {
                    "user_id": getattr(vars.get("mfa_test_user"), "id", "mock-user-id"),
                    "update_saas_user_password_param": UpdateSaasUserPasswordParam(password=get_default_password())
                },
                description="UpdateSaasUserPasswordWithHttpInfo"
            ),
            Step(
                method_name="update_saas_user_email_with_http_info",
                params=lambda vars: {
                    "user_id": getattr(vars.get("mfa_test_user"), "id", "mock-user-id"),
                    "update_saas_user_email_param": UpdateSaasUserEmailParam(email=unique_email("mfa-test-updated"))
                },
                description="UpdateSaasUserEmailWithHttpInfo"
            ),
            Step(
                method_name="get_user_mfa_preference_with_http_info",
                params=lambda vars: {
                    "user_id": getattr(vars.get("mfa_test_user"), "id", "mock-user-id")
                },
                description="GetUserMfaPreferenceWithHttpInfo"
            ),
            Step(
                method_name="create_secret_code_with_http_info",
                params=lambda vars: {
                    "user_id": getattr(vars.get("mfa_test_user"), "id", "mock-user-id"),
                    "create_secret_code_param": CreateSecretCodeParam(access_token="dummy-token")
                },
                description="CreateSecretCodeWithHttpInfo",
                skip=True,
                skip_reason="Requires valid Cognito access token"
            ),
            Step(
                method_name="update_software_token_with_http_info",
                params=lambda vars: {
                    "user_id": getattr(vars.get("mfa_test_user"), "id", "mock-user-id"),
                    "update_software_token_param": UpdateSoftwareTokenParam(
                        access_token="dummy-token",
                        verification_code="123456"
                    )
                },
                description="UpdateSoftwareTokenWithHttpInfo",
                skip=True,
                skip_reason="Requires valid Cognito access token and verification code"
            ),
            Step(
                method_name="update_user_mfa_preference_with_http_info",
                params=lambda vars: {
                    "user_id": getattr(vars.get("mfa_test_user"), "id", "mock-user-id"),
                    "body": MfaPreference(enabled=False)
                },
                description="UpdateUserMfaPreferenceWithHttpInfo"
            ),
            Step(
                method_name="delete_saas_user_with_http_info",
                params=lambda vars: {
                    "user_id": getattr(vars.get("mfa_test_user"), "id", "mock-user-id")
                },
                description="DeleteSaasUser for MFA testWithHttpInfo"
            ),
            # === user-attributes ===
            Step(
                method_name="get_user_attributes_with_http_info",
                params=lambda vars: {},
                description="GetUserAttributesWithHttpInfo"
            ),
            Step(
                method_name="create_user_attribute_with_http_info",
                params=lambda vars: {
                    "body": Attribute(attribute_name=user_attr_name, display_name=f"User Attr {user_attr_name}", attribute_type=AttributeType.STRING)
                },
                description="CreateUserAttributeWithHttpInfo",
                store_as="created_user_attr"
            ),
            # === roles ===
            Step(
                method_name="get_roles_with_http_info",
                params=lambda vars: {},
                description="GetRoles (before create)WithHttpInfo"
            ),
            Step(
                method_name="create_role_with_http_info",
                params=lambda vars: {
                    "body": Role(role_name=role_name, display_name=f"Test Role {role_name}")
                },
                description="CreateRoleWithHttpInfo",
                store_as="created_role"
            ),
            Step(
                method_name="get_roles_with_http_info",
                params=lambda vars: {},
                description="GetRoles (after create)WithHttpInfo"
            ),
            # === envs ===
            Step(
                method_name="get_envs_with_http_info",
                params=lambda vars: {},
                description="GetEnvsWithHttpInfo",
                store_as="envs_list"
            ),
            Step(
                method_name="create_env_with_http_info",
                params=lambda vars: {
                    "body": Env(id=random.randint(100000, 999999), name=env_name, display_name=f"Test Env {env_name}")
                },
                description="CreateEnvWithHttpInfo",
                store_as="created_env"
            ),
            Step(
                method_name="get_env_with_http_info",
                params=lambda vars: {
                    "env_id": getattr(vars.get("created_env"), "id", 1)
                },
                description="GetEnvWithHttpInfo"
            ),
            Step(
                method_name="update_env_with_http_info",
                params=lambda vars: {
                    "env_id": getattr(vars.get("created_env"), "id", 1),
                    "update_env_param": UpdateEnvParam(
                        name=env_name,
                        display_name=f"Updated Env {env_name}"
                    )
                },
                description="UpdateEnvWithHttpInfo"
            ),
            # === tenant-attributes ===
            Step(
                method_name="get_tenant_attributes_with_http_info",
                params=lambda vars: {},
                description="GetTenantAttributes (before create)WithHttpInfo"
            ),
            Step(
                method_name="create_tenant_attribute_with_http_info",
                params=lambda vars: {
                    "body": Attribute(attribute_name=attr_name, display_name=f"Tenant Attr {attr_name}", attribute_type=AttributeType.STRING)
                },
                description="CreateTenantAttributeWithHttpInfo",
                store_as="created_tenant_attr"
            ),
            Step(
                method_name="get_tenant_attributes_with_http_info",
                params=lambda vars: {},
                description="GetTenantAttributes (after create)WithHttpInfo"
            ),
            # === tenants ===
            Step(
                method_name="get_tenants_with_http_info",
                params=lambda vars: {},
                description="GetTenants (before create)WithHttpInfo"
            ),
            Step(
                method_name="create_tenant_with_http_info",
                params=lambda vars: {
                    "body": TenantProps(
                        name=unique_string("tenant"),
                        attributes={},
                        back_office_staff_email=unique_email("tenant-staff")
                    )
                },
                description="CreateTenantWithHttpInfo",
                store_as="created_tenant"
            ),
            Step(
                method_name="get_tenant_with_http_info",
                params=lambda vars: {
                    "tenant_id": getattr(vars.get("created_tenant"), "id", "mock-tenant-id")
                },
                description="GetTenantWithHttpInfo"
            ),
            Step(
                method_name="update_tenant_with_http_info",
                params=lambda vars: {
                    "tenant_id": getattr(vars.get("created_tenant"), "id", "mock-tenant-id"),
                    "body": TenantProps(
                        name=unique_string("tenant-updated"),
                        attributes={getattr(vars.get("created_tenant_attr"), "attribute_name", attr_name): "test-value"},
                        back_office_staff_email=unique_email("tenant-staff-updated")
                    )
                },
                description="UpdateTenantWithHttpInfo"
            ),
            # === tenant-plan & billing (Stripe連携) ===
            Step(
                method_name="update_tenant_plan_with_http_info",
                params=lambda vars: {
                    "tenant_id": getattr(vars.get("created_tenant"), "id", "mock-tenant-id"),
                    "body": PlanReservation(next_plan_id=get_or_create_test_plan_id())
                },
                description="UpdateTenantPlanWithHttpInfo",
                skip=not stripe_configured,
                skip_reason="Requires Stripe integration (STRIPE_SECRET_KEY)"
            ),
            Step(
                method_name="update_tenant_billing_info_with_http_info",
                params=lambda vars: {
                    "tenant_id": getattr(vars.get("created_tenant"), "id", "mock-tenant-id"),
                    "body": BillingInfo(
                        name="テスト用文字列",
                        invoice_language=InvoiceLanguage.JA_MINUS_JP,
                        address=BillingAddress(
                            city="test_city",
                            country="JP",
                            postal_code="123-4567",
                            state="test_state",
                            street="test_street",
                            additional_address_info="test_additional_info"
                        )
                    )
                },
                description="UpdateTenantBillingInfoWithHttpInfo",
                skip=not stripe_configured,
                skip_reason="Requires Stripe integration (STRIPE_SECRET_KEY)"
            ),
            # クリーンアップ: 前回のテストで残ったStripeデータを削除（エラーは無視）
            Step(
                method_name="delete_stripe_tenant_and_pricing_with_http_info",
                params=lambda vars: {},
                description="CleanupStripeTenantAndPricing",
                skip=not stripe_configured,
                skip_reason="Requires Stripe integration (STRIPE_SECRET_KEY)",
                allow_failure=True
            ),
            Step(
                method_name="reset_plan_with_http_info",
                params=lambda vars: {},
                description="CleanupResetPlan",
                skip=not stripe_configured,
                skip_reason="Requires Stripe integration (STRIPE_SECRET_KEY)",
                allow_failure=True
            ),
            # Stripe連携を再設定
            Step(
                method_name="update_stripe_info_with_http_info",
                params=lambda vars: {
                    "update_stripe_info_param": UpdateStripeInfoParam(secret_key=get_stripe_secret_key())
                },
                description="SetupStripeIntegration",
                skip=not stripe_configured,
                skip_reason="Requires Stripe integration (STRIPE_SECRET_KEY)"
            ),
            Step(
                method_name="create_tenant_and_pricing_with_http_info",
                params=lambda vars: {},
                description="CreateTenantAndPricingWithHttpInfo",
                skip=not stripe_configured,
                skip_reason="Requires Stripe integration (STRIPE_SECRET_KEY)"
            ),
            Step(
                method_name="get_stripe_customer_with_http_info",
                params=lambda vars: {
                    "tenant_id": getattr(vars.get("created_tenant"), "id", "mock-tenant-id")
                },
                description="GetStripeCustomerWithHttpInfo",
                skip=not stripe_configured,
                skip_reason="Requires Stripe integration (STRIPE_SECRET_KEY)"
            ),
            Step(
                method_name="delete_stripe_tenant_and_pricing_with_http_info",
                params=lambda vars: {},
                description="DeleteStripeTenantAndPricingWithHttpInfo",
                skip=not stripe_configured,
                skip_reason="Requires Stripe integration (STRIPE_SECRET_KEY)"
            ),
            Step(
                method_name="reset_plan_with_http_info",
                params=lambda vars: {},
                description="ResetPlanWithHttpInfo",
                skip=not stripe_configured,
                skip_reason="Requires Stripe integration (STRIPE_SECRET_KEY)"
            ),
            Step(
                method_name="get_tenant_identity_providers_with_http_info",
                params=lambda vars: {
                    "tenant_id": getattr(vars.get("created_tenant"), "id", "mock-tenant-id")
                },
                description="GetTenantIdentityProvidersWithHttpInfo"
            ),
            Step(
                method_name="update_tenant_identity_provider_with_http_info",
                params=lambda vars: {
                    "tenant_id": getattr(vars.get("created_tenant"), "id", "mock-tenant-id"),
                    "update_tenant_identity_provider_param": TenantIdentityProviderProps()
                },
                description="UpdateTenantIdentityProviderWithHttpInfo",
                skip=True,
                skip_reason="Requires valid identity provider configuration"
            ),
            # === all-tenant-users ===
            Step(
                method_name="get_all_tenant_users_with_http_info",
                params=lambda vars: {},
                description="GetAllTenantUsersWithHttpInfo"
            ),
            # === invitation (Cognitoアクセストークン必要) ===
            # CognitoユーザーをテナントユーザーとしてCognitoユーザーをテナントに追加（招待者はテナントに所属している必要がある）
            # 注: CognitoユーザーはSaaSユーザーとして事前に登録されている必要がある
            Step(
                method_name="create_tenant_user_with_http_info",
                params=lambda vars: {
                    "tenant_id": getattr(vars.get("created_tenant"), "id", "mock-tenant-id"),
                    "create_tenant_user_param": CreateTenantUserParam(
                        email=getattr(vars.get("cognito_user_info"), "email", "mock@example.com"),
                        attributes={}
                    )
                },
                description="CreateTenantUser for Cognito inviterWithHttpInfo",
                store_as="cognito_tenant_user",
                skip=not cognito_configured,
                skip_reason="Requires Cognito configuration (E2E_COGNITO_*)"
            ),
            Step(
                method_name="create_tenant_invitation_with_http_info",
                params=lambda vars: {
                    "tenant_id": getattr(vars.get("created_tenant"), "id", "mock-tenant-id"),
                    "create_tenant_invitation_param": CreateTenantInvitationParam(
                        email=unique_email("invitee"),
                        access_token=cognito_tokens["access_token"] if cognito_tokens else "",
                        envs=[InvitedUserEnvironmentInformationInner(
                            id=vars.get("envs_list").envs[0].id if vars.get("envs_list") and vars.get("envs_list").envs else 3,
                            role_names=["admin"]
                        )]
                    )
                },
                description="CreateTenantInvitationWithHttpInfo",
                store_as="invitation",
                skip=True,
                skip_reason="Requires DNS and SES validation in the environment"
            ),
            Step(
                method_name="get_tenant_invitations_with_http_info",
                params=lambda vars: {
                    "tenant_id": getattr(vars.get("created_tenant"), "id", "mock-tenant-id")
                },
                description="GetTenantInvitationsWithHttpInfo"
            ),
            Step(
                method_name="get_tenant_invitation_with_http_info",
                params=lambda vars: {
                    "tenant_id": getattr(vars.get("created_tenant"), "id", "mock-tenant-id"),
                    "invitation_id": getattr(vars.get("invitation"), "id", "mock-inv-id")
                },
                description="GetTenantInvitationWithHttpInfo",
                skip=True,
                skip_reason="Requires invitation created (DNS/SES validation needed)"
            ),
            Step(
                method_name="get_invitation_validity_with_http_info",
                params=lambda vars: {
                    "invitation_id": getattr(vars.get("invitation"), "id", "mock-inv-id")
                },
                description="GetInvitationValidityWithHttpInfo",
                skip=True,
                skip_reason="Requires invitation created (DNS/SES validation needed)"
            ),
            Step(
                method_name="delete_tenant_invitation_with_http_info",
                params=lambda vars: {
                    "tenant_id": getattr(vars.get("created_tenant"), "id", "mock-tenant-id"),
                    "invitation_id": getattr(vars.get("invitation"), "id", "mock-inv-id")
                },
                description="DeleteTenantInvitationWithHttpInfo",
                skip=True,
                skip_reason="Requires invitation created (DNS/SES validation needed)"
            ),
            Step(
                method_name="validate_invitation_with_http_info",
                params=lambda vars: {
                    "invitation_id": getattr(vars.get("invitation"), "id", "mock-inv-id")
                },
                description="ValidateInvitationWithHttpInfo",
                skip=True,
                skip_reason="Requires valid invitation (DNS/SES validation needed)"
            ),
            # === tenant-users ===
            Step(
                method_name="create_saas_user_with_http_info",
                params=lambda vars: {
                    "create_saas_user_param": build_create_saas_user_params(unique_email("tenant-user"), get_default_password())
                },
                description="CreateSaasUser for tenant userWithHttpInfo",
                store_as="saas_user"
            ),
            Step(
                method_name="create_tenant_user_with_http_info",
                params=lambda vars: {
                    "tenant_id": getattr(vars.get("created_tenant"), "id", "mock-tenant-id"),
                    "create_tenant_user_param": CreateTenantUserParam(
                        email=getattr(vars.get("saas_user"), "email", "mock@example.com"),
                        attributes={}
                    )
                },
                description="CreateTenantUserWithHttpInfo"
            ),
            Step(
                method_name="get_all_tenant_user_with_http_info",
                params=lambda vars: {
                    "user_id": getattr(vars.get("saas_user"), "id", "mock-user-id")
                },
                description="GetAllTenantUserWithHttpInfo"
            ),
            Step(
                method_name="get_tenant_user_with_http_info",
                params=lambda vars: {
                    "tenant_id": getattr(vars.get("created_tenant"), "id", "mock-tenant-id"),
                    "user_id": getattr(vars.get("saas_user"), "id", "mock-user-id")
                },
                description="GetTenantUserWithHttpInfo"
            ),
            Step(
                method_name="get_tenant_users_with_http_info",
                params=lambda vars: {
                    "tenant_id": getattr(vars.get("created_tenant"), "id", "mock-tenant-id")
                },
                description="GetTenantUsersWithHttpInfo"
            ),
            Step(
                method_name="update_tenant_user_with_http_info",
                params=lambda vars: {
                    "tenant_id": getattr(vars.get("created_tenant"), "id", "mock-tenant-id"),
                    "user_id": getattr(vars.get("saas_user"), "id", "mock-user-id"),
                    "update_tenant_user_param": UpdateTenantUserParam(attributes={})
                },
                description="UpdateTenantUserWithHttpInfo"
            ),
            # === tenant-user-roles ===
            Step(
                method_name="create_tenant_user_roles_with_http_info",
                params=lambda vars: {
                    "tenant_id": getattr(vars.get("created_tenant"), "id", "mock-tenant-id"),
                    "user_id": getattr(vars.get("saas_user"), "id", "mock-user-id"),
                    "env_id": getattr(vars.get("created_env"), "id", 1),
                    "create_tenant_user_roles_param": CreateTenantUserRolesParam(
                        role_names=[getattr(vars.get("created_role"), "role_name", role_name)]
                    )
                },
                description="CreateTenantUserRolesWithHttpInfo"
            ),
            Step(
                method_name="delete_tenant_user_role_with_http_info",
                params=lambda vars: {
                    "tenant_id": getattr(vars.get("created_tenant"), "id", "mock-tenant-id"),
                    "user_id": getattr(vars.get("saas_user"), "id", "mock-user-id"),
                    "env_id": getattr(vars.get("created_env"), "id", 1),
                    "role_name": getattr(vars.get("created_role"), "role_name", role_name)
                },
                description="DeleteTenantUserRoleWithHttpInfo"
            ),
            # === single-tenant ===
            Step(
                method_name="get_single_tenant_settings_with_http_info",
                params=lambda vars: {},
                description="GetSingleTenantSettingsWithHttpInfo"
            ),
            Step(
                method_name="update_single_tenant_settings_with_http_info",
                params=lambda vars: {
                    "update_single_tenant_settings_param": UpdateSingleTenantSettingsParam(enabled=False)
                },
                description="UpdateSingleTenantSettingsWithHttpInfo"
            ),
            Step(
                method_name="get_cloud_formation_launch_stack_link_for_single_tenant_with_http_info",
                params=lambda vars: {},
                description="GetCloudFormationLaunchStackLinkForSingleTenantWithHttpInfo"
            ),
            # === auth-credentials ===
            Step(
                method_name="create_auth_credentials_with_http_info",
                params=lambda vars: {
                    "body": {"code": "test-code"}
                },
                description="CreateAuthCredentialsWithHttpInfo",
                skip=True,
                skip_reason="Requires valid authorization code"
            ),
            Step(
                method_name="get_auth_credentials_with_http_info",
                params=lambda vars: {
                    "user_id": getattr(vars.get("saas_user"), "id", "mock-user-id"),
                    "auth_credential_id": "mock-credential-id"
                },
                description="GetAuthCredentialsWithHttpInfo",
                skip=True,
                skip_reason="Requires valid auth credential ID"
            ),
            # === aws-marketplace ===
            Step(
                method_name="sign_up_with_aws_marketplace_with_http_info",
                params=lambda vars: {
                    "sign_up_with_aws_marketplace_param": SignUpWithAwsMarketplaceParam(
                        registration_token="test-token",
                        email=unique_email("aws-marketplace"),
                        password=get_default_password()
                    )
                },
                description="SignUpWithAwsMarketplaceWithHttpInfo",
                skip=True,
                skip_reason="Requires valid AWS Marketplace registration token"
            ),
            # === cleanup ===
            Step(
                method_name="delete_tenant_user_with_http_info",
                params=lambda vars: {
                    "tenant_id": getattr(vars.get("created_tenant"), "id", "mock-tenant-id"),
                    "user_id": getattr(vars.get("saas_user"), "id", "mock-user-id")
                },
                description="DeleteTenantUserWithHttpInfo"
            ),
            Step(
                method_name="delete_tenant_with_http_info",
                params=lambda vars: {
                    "tenant_id": getattr(vars.get("created_tenant"), "id", "mock-tenant-id")
                },
                description="DeleteTenantWithHttpInfo"
            ),
            Step(
                method_name="delete_env_with_http_info",
                params=lambda vars: {
                    "env_id": getattr(vars.get("created_env"), "id", 1)
                },
                description="DeleteEnvWithHttpInfo"
            ),
            Step(
                method_name="delete_saas_user_with_http_info",
                params=lambda vars: {
                    "user_id": getattr(vars.get("saas_user"), "id", "mock-user-id")
                },
                description="DeleteSaasUserWithHttpInfo"
            ),
            Step(
                method_name="delete_user_attribute_with_http_info",
                params=lambda vars: {
                    "attribute_name": getattr(vars.get("created_user_attr"), "attribute_name", user_attr_name)
                },
                description="DeleteUserAttributeWithHttpInfo"
            ),
            Step(
                method_name="delete_role_with_http_info",
                params=lambda vars: {
                    "role_name": getattr(vars.get("created_role"), "role_name", role_name)
                },
                description="DeleteRoleWithHttpInfo"
            ),
            Step(
                method_name="delete_tenant_attribute_with_http_info",
                params=lambda vars: {
                    "attribute_name": getattr(vars.get("created_tenant_attr"), "attribute_name", attr_name)
                },
                description="DeleteTenantAttributeWithHttpInfo"
            ),
        ],
        tags=["auth", "postman", "comprehensive", "with-http-info"]
    )



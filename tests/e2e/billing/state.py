"""Billing E2E test state management."""

from typing import Any, Optional

from saasus_sdk_python.src.auth.exceptions import ApiException as AuthApiException
from saasus_sdk_python.src.billing.exceptions import ApiException as BillingApiException

LOG_PREFIX = "[Billing E2E]"
STRIPE_KEY_NOT_REGISTERED = "stripe key is not registered"


def _get_status(error: Exception) -> Optional[int]:
    if isinstance(error, (AuthApiException, BillingApiException)):
        return getattr(error, "status", None)
    return getattr(error, "status", None)


def _get_body_text(error: Exception) -> str:
    body = getattr(error, "body", None)
    if body is None:
        return ""
    try:
        return str(body).lower()
    except Exception:
        return ""


def _is_ignorable_tenant_cleanup_error(error: Exception) -> bool:
    status = _get_status(error)
    if status == 400:
        return STRIPE_KEY_NOT_REGISTERED in _get_body_text(error)
    return False


def _is_ignorable_delete_error(error: Exception) -> bool:
    status = _get_status(error)
    return status == 404


def cleanup_tenant_data(client: Any) -> None:
    try:
        client.delete_stripe_tenant_and_pricing()
        print(f"{LOG_PREFIX} Deleted linked Stripe tenant/pricing data.")
    except Exception as error:
        if _is_ignorable_tenant_cleanup_error(error):
            print(f"{LOG_PREFIX} No linked Stripe tenant/pricing data to delete.")
            return
        raise


def remove_stripe_info(client: Any) -> None:
    try:
        client.delete_stripe_info()
        print(f"{LOG_PREFIX} Removed existing Stripe connection info.")
    except Exception as error:
        if _is_ignorable_delete_error(error):
            print(f"{LOG_PREFIX} Stripe connection info already absent.")
            return
        raise


def ensure_stripe_test_preconditions(client: Any) -> None:
    cleanup_tenant_data(client)

    current_info = client.get_stripe_info()
    is_registered = getattr(current_info, "is_registered", False)
    if not is_registered:
        return

    print(f"{LOG_PREFIX} Stripe connection detected. Resetting before tests...")
    remove_stripe_info(client)

    final_info = client.get_stripe_info()
    final_registered = getattr(final_info, "is_registered", False)
    if final_registered:
        raise RuntimeError("Unable to reset Stripe connection before running tests.")


class StateManager:
    """State管理とクリーンアップを提供するマネージャー"""

    @staticmethod
    def cleanup_all_resources() -> None:
        print("\n🧹 Cleaning up billing resources...")

    @staticmethod
    def handle_story_failure(error: Exception) -> None:
        print(f"❌ Story failed: {error}")
        StateManager.cleanup_all_resources()

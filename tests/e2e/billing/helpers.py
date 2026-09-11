"""Billing E2E test helper functions."""

import os
from typing import Optional

from saasus_sdk_python.src.billing.models.update_stripe_info_param import UpdateStripeInfoParam

DEFAULT_STRIPE_KEY = "sk_test_example_key_for_testing"


def get_test_stripe_key() -> str:
    """Get Stripe secret key from env or fallback to default."""
    return os.getenv("STRIPE_SECRET_KEY") or DEFAULT_STRIPE_KEY


def create_update_stripe_info_param(secret_key: Optional[str] = None) -> UpdateStripeInfoParam:
    """Create UpdateStripeInfoParam with provided or default secret key."""
    return UpdateStripeInfoParam(secret_key=secret_key or get_test_stripe_key())

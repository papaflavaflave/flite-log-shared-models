"""
Subscription-related Pydantic models for the flite-log application.
"""

from typing import Optional, Dict, Any
from pydantic import BaseModel, validator
from datetime import datetime
from .enums import SubscriptionTierEnum, PaymentProviderEnum

class SubscriptionTier(BaseModel):
    tier: SubscriptionTierEnum
    max_users: float  # Using float to support infinity
    max_planes: float  # Using float to support infinity
    allows_sharing: bool
    description: str
    monthly_price: float
    annual_price: Optional[float] = None

class CreateSubscription(BaseModel):
    tier: SubscriptionTierEnum
    provider: PaymentProviderEnum
    payment_method_id: Optional[str] = None
    apple_receipt_data: Optional[str] = None
    billing_cycle: str = "monthly"  # "monthly" or "annual"
    subscription_metadata: Optional[Dict[str, Any]] = None

    @validator('payment_method_id', 'apple_receipt_data', always=True)
    def validate_payment_data(cls, v, values):
        provider = values.get('provider')
        if provider == PaymentProviderEnum.STRIPE and not values.get('payment_method_id'):
            raise ValueError('payment_method_id is required for Stripe subscriptions')
        elif provider == PaymentProviderEnum.APPLE and not values.get('apple_receipt_data'):
            raise ValueError('apple_receipt_data is required for Apple subscriptions')
        return v

class UpdateSubscription(BaseModel):
    tier: Optional[SubscriptionTierEnum] = None
    cancel_at_period_end: Optional[bool] = None
    subscription_metadata: Optional[Dict[str, Any]] = None

class UpgradeSubscription(BaseModel):
    tier: SubscriptionTierEnum
    provider: Optional[PaymentProviderEnum] = None  # Make provider optional for upgrades
    payment_method_id: Optional[str] = None
    apple_receipt_data: Optional[str] = None
    billing_cycle: str = "monthly"  # "monthly" or "annual"
    subscription_metadata: Optional[Dict[str, Any]] = None

    @validator('payment_method_id', 'apple_receipt_data', always=True)
    def validate_payment_data(cls, v, values):
        provider = values.get('provider')
        if provider == PaymentProviderEnum.STRIPE and not values.get('payment_method_id'):
            raise ValueError('payment_method_id is required for Stripe subscription upgrades')
        elif provider == PaymentProviderEnum.APPLE and not values.get('apple_receipt_data'):
            raise ValueError('apple_receipt_data is required for Apple subscription upgrades')
        return v

class SubscriptionStatus(BaseModel):
    subscription_id: str
    tier: SubscriptionTierEnum
    is_active: bool
    provider: PaymentProviderEnum
    current_period_start: datetime
    current_period_end: datetime
    cancel_at_period_end: bool = False
    payment_status: str
    subscription_metadata: Optional[Dict[str, Any]] = None 
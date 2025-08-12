"""
Enum definitions for the flite-log application.
"""

from enum import Enum

class SubscriptionTierEnum(str, Enum):
    """Enum for subscription tiers."""
    FREE = "FREE"
    PLANE_SHARE = "PLANE_SHARE"
    CLUB = "CLUB"
    ENTERPRISE = "ENTERPRISE"

class PaymentProviderEnum(str, Enum):
    """Enum for payment providers."""
    STRIPE = "STRIPE"
    APPLE = "APPLE"

class TimePeriodEnum(str, Enum):
    """Enum for time period options."""
    LAST_WEEK = "LAST_WEEK"
    LAST_MONTH = "LAST_MONTH"
    LAST_YEAR = "LAST_YEAR"
    CUSTOM = "CUSTOM"

class ExportFormatEnum(str, Enum):
    """Enum for export format options."""
    CSV = "CSV"
    PDF = "PDF"

class SquawkStatusEnum(str, Enum):
    """Enum for squawk status."""
    OPEN = "OPEN"
    IN_PROGRESS = "IN_PROGRESS"
    DEFERRED = "DEFERRED"
    RESOLVED = "RESOLVED"
    CLOSED = "CLOSED" 
"""
Shared models package for the flite-log monorepo.
Contains Pydantic models used across backend, frontend, and control-tower.
"""

from .enums import (
    SubscriptionTierEnum,
    PaymentProviderEnum,
    TimePeriodEnum,
    ExportFormatEnum,
    SquawkStatusEnum
)

from .user import (
    UserLogin,
    UserCreate,
    ResendVerification
)

from .plane import (
    PlaneCreate,
    PlaneAccessResponse
)

from .flight import (
    FlightLogCreate,
    FlightLogTimeFilter,
    ExportRequest,
    FlightSessionStart,
    FlightSessionEnd,
    FlightSessionResponse,
    QRCodeScanResponse,
    SessionTimeoutResponse
)

from .subscription import (
    SubscriptionTier,
    CreateSubscription,
    UpdateSubscription,
    UpgradeSubscription,
    SubscriptionStatus
)

from .squawk import (
    SquawkCreate,
    SquawkUpdate,
    SquawkResponse
)

from .invitation import (
    InviteUserRequest,
    InviteResponse
)

from .beta import (
    BetaSignupRequest,
    BetaSignupResponse
)

__all__ = [
    # Enums
    "SubscriptionTierEnum",
    "PaymentProviderEnum", 
    "TimePeriodEnum",
    "ExportFormatEnum",
    "SquawkStatusEnum",
    
    # User models
    "UserLogin",
    "UserCreate", 
    "ResendVerification",
    
    # Plane models
    "PlaneCreate",
    "PlaneAccessResponse",
    
    # Flight models
    "FlightLogCreate",
    "FlightLogTimeFilter",
    "ExportRequest",
    "FlightSessionStart",
    "FlightSessionEnd", 
    "FlightSessionResponse",
    "QRCodeScanResponse",
    "SessionTimeoutResponse",
    
    # Subscription models
    "SubscriptionTier",
    "CreateSubscription",
    "UpdateSubscription",
    "UpgradeSubscription",
    "SubscriptionStatus",
    
    # Squawk models
    "SquawkCreate",
    "SquawkUpdate",
    "SquawkResponse",
    
    # Invitation models
    "InviteUserRequest",
    "InviteResponse",
    
    # Beta models
    "BetaSignupRequest",
    "BetaSignupResponse"
] 
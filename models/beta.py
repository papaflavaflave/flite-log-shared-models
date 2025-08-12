"""
Beta-related Pydantic models for the flite-log application.
"""

from pydantic import BaseModel, EmailStr
from typing import Optional

class BetaSignupRequest(BaseModel):
    """Model for beta signup request."""
    email: EmailStr
    name: str
    organization: Optional[str] = None
    role: Optional[str] = None
    fleet_size: Optional[int] = None
    comments: Optional[str] = None

class BetaSignupResponse(BaseModel):
    """Model for beta signup response."""
    message: str
    status: str 
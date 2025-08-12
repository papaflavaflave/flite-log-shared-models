"""
User-related Pydantic models for the flite-log application.
"""

from pydantic import BaseModel, EmailStr
from typing import Optional

class UserLogin(BaseModel):
    """Model for user login data."""
    email: EmailStr
    password: str

class UserCreate(BaseModel):
    """Model for user creation data."""
    name: str
    email: EmailStr
    password: str
    license_number: Optional[str] = None
    account_id: Optional[int] = None
    account_name: Optional[str] = None
    inviter_id: Optional[int] = None

class ResendVerification(BaseModel):
    """Model for resending verification email."""
    email: EmailStr 
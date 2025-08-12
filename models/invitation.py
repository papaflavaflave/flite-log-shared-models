"""
Invitation-related Pydantic models for the flite-log application.
"""

from pydantic import BaseModel, EmailStr

class InviteUserRequest(BaseModel):
    """Model for user invitation request."""
    email: EmailStr
    role: str

class InviteResponse(BaseModel):
    """Model for invitation response."""
    email: str
    role: str
    token: str
    expires_at: str 
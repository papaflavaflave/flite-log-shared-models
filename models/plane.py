"""
Plane-related Pydantic models for the flite-log application.
"""

from pydantic import BaseModel
from typing import Optional, Dict, Any

class PlaneCreate(BaseModel):
    """Model for plane creation data."""
    tail_number: str
    model: str
    has_critical_squawk: bool = False
    current_hobbs: Optional[float] = None
    current_tach: Optional[float] = None
    billing_method: str = "hobbs"
    is_active: bool = True

class PlaneAccessResponse(BaseModel):
    """Model for plane access response."""
    tail_number: str
    model: str
    role: str
    has_critical_squawk: bool
    current_hobbs: Optional[float]
    current_tach: Optional[float]
    total_hobbs_hours: float
    total_tach_hours: float
    billing_method: str
    is_active: bool 
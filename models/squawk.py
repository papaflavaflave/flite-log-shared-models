"""
Squawk-related Pydantic models for the flite-log application.
"""

from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from .enums import SquawkStatusEnum

class SquawkCreate(BaseModel):
    """Model for squawk creation data."""
    plane_id: int
    title: str
    description: str
    severity: str
    hobbs_time: Optional[float] = None
    tach_time: Optional[float] = None
    pilot_action_required: bool = False
    is_recurring: bool = False
    flight_log_id: Optional[int] = None
    photo_url: Optional[str] = None

class SquawkUpdate(BaseModel):
    """Model for squawk update data."""
    status: Optional[SquawkStatusEnum] = None
    assigned_mechanic_id: Optional[int] = None
    resolution_notes: Optional[str] = None
    parts_replaced: Optional[str] = None

class SquawkResponse(BaseModel):
    """Model for squawk response data."""
    id: int
    plane_id: int
    reported_by_id: int
    assigned_mechanic_id: Optional[int]
    date_reported: datetime
    title: str
    description: str
    severity: str
    status: SquawkStatusEnum
    hobbs_time: Optional[float]
    tach_time: Optional[float]
    resolution_notes: Optional[str]
    date_resolved: Optional[datetime]
    parts_replaced: Optional[str]
    photo_url: Optional[str]
    pilot_action_required: bool
    is_recurring: bool
    flight_log_id: Optional[int] 
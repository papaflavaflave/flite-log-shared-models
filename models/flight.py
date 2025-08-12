"""
Flight-related Pydantic models for the flite-log application.
"""

from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from .enums import TimePeriodEnum, ExportFormatEnum

class FlightLogCreate(BaseModel):
    """Model for flight log creation data."""
    plane_id: int
    time_in: datetime
    time_out: datetime
    total_duration: float
    topped: Optional[bool] = None
    hobbs_in: Optional[float] = None
    hobbs_out: Optional[float] = None
    tach_in: Optional[float] = None
    tach_out: Optional[float] = None
    notes: Optional[str] = None

class FlightLogTimeFilter(BaseModel):
    """Model for filtering flight logs by time."""
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    time_period: Optional[TimePeriodEnum] = None

class ExportRequest(BaseModel):
    """Model for export request data."""
    time_period: TimePeriodEnum
    format: ExportFormatEnum
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None

# New models for stateful flight logging
class FlightSessionStart(BaseModel):
    """Model for starting a flight session."""
    plane_id: int
    hobbs_out: Optional[float] = None
    tach_out: Optional[float] = None

class FlightSessionEnd(BaseModel):
    """Model for ending a flight session."""
    session_id: int
    hobbs_in: Optional[float] = None
    tach_in: Optional[float] = None
    notes: Optional[str] = None

class FlightSessionResponse(BaseModel):
    """Model for flight session response."""
    session_id: int
    plane_id: int
    plane_tail_number: str
    status: str  # "in_progress" or "complete"
    hobbs_out: Optional[float] = None
    tach_out: Optional[float] = None
    start_timestamp: datetime
    session_duration_hours: Optional[float] = None
    is_expired: bool = False

class QRCodeScanResponse(BaseModel):
    """Model for QR code scan response."""
    action: str  # "start_flight", "end_flight", "session_exists", "session_expired"
    message: str
    session: Optional[FlightSessionResponse] = None
    plane_info: Optional[dict] = None
    last_flight_info: Optional[dict] = None  # For pre-filling values

class SessionTimeoutResponse(BaseModel):
    """Model for session timeout response."""
    session: FlightSessionResponse
    timeout_hours: float
    options: list[str]  # ["complete", "discard", "edit"] 
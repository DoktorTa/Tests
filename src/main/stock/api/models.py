from datetime import datetime

from pydantic import BaseModel


class ReservationRequest(BaseModel):
    reservation_id: str
    product_id: str
    quantity: int
    timestamp: datetime


class ReservationResponse(BaseModel):
    status: str
    message: str
    reservation_id: int

from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR, HTTP_400_BAD_REQUEST

from src.main.stock.api.models import ReservationResponse, ReservationRequest
from src.main.stock.reservation import reservation_goods
from src.main.stock.utils import StatusCodeReservation

router = APIRouter(prefix='/v1')

@router.post('/reserve', response_model=None)
async def create_reservation(reservation_request: ReservationRequest) -> ReservationResponse | HTTPException:
    response = await reservation_goods(reservation_request)

    if response.status == StatusCodeReservation.CRITICAL:
        return HTTPException(status_code=HTTP_500_INTERNAL_SERVER_ERROR, detail=response)
    elif response.status == StatusCodeReservation.ERROR:
        return HTTPException(status_code=HTTP_400_BAD_REQUEST, detail=response)
    else:
        return response

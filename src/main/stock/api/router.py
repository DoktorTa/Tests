from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND

from src.main.stock.api.models import ReservationResponse, ReservationRequest, StatusResponse
from src.main.stock.reservation import reservation_goods, get_status_reservation
from src.main.stock.utils import StatusCodeResponseReservation, StatusCodeResponseStatus

router = APIRouter(prefix='/v1')

@router.post('/reserve', response_model=None)
async def create_reservation(reservation_request: ReservationRequest) -> ReservationResponse | HTTPException:
    response = await reservation_goods(reservation_request)

    if response.status == StatusCodeResponseReservation.SUCCESS:
        return response
    elif response.status == StatusCodeResponseReservation.ERROR:
        return HTTPException(status_code=HTTP_400_BAD_REQUEST, detail=response)
    else:
        return HTTPException(status_code=HTTP_500_INTERNAL_SERVER_ERROR, detail=response)


@router.get('/status/{reservation_id}', response_model=None)
async def status_reservation(reservation_id: str) -> StatusResponse | HTTPException:
    response = await get_status_reservation(reservation_id)

    if response.status == StatusCodeResponseStatus.FOUND:
        return response
    elif response.status == StatusCodeResponseStatus.NOT_FOUND:
        return HTTPException(status_code=HTTP_404_NOT_FOUND, detail=response)
    else:
        return HTTPException(status_code=HTTP_500_INTERNAL_SERVER_ERROR, detail=response)

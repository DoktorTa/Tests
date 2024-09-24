import logging
from datetime import datetime

from src.main.stock.api.models import ReservationRequest, ReservationResponse
from src.main.stock.db.models import GoodsHold
from src.main.stock.db.repository import StockReservationRepository
from src.main.stock.utils import StatusCodeReservation


async def reservation_goods(reservation_request: ReservationRequest) -> ReservationResponse:
    response = None

    try:
        await StockReservationRepository.sub_goods(reservation_request.product_id, reservation_request.quantity)

        gds_hold = GoodsHold(
            reservation_id=reservation_request.reservation_id,
            product_id=reservation_request.product_id,
            quantity=reservation_request.quantity,
            timestamp_hold=reservation_request.timestamp.replace(microsecond=0, tzinfo=None)
        )

        await StockReservationRepository.create_hold(gds_hold)

        response = ReservationResponse(
            reservation_id=reservation_request.reservation_id,
            status=StatusCodeReservation.SUCCESS,
            message=f'Successfully added {reservation_request.quantity} products with ID '
                     f'{reservation_request.product_id}'
        )
    except ValueError as e:
        response = ReservationResponse(
            reservation_id=reservation_request.reservation_id,
            status=StatusCodeReservation.ERROR,
            message=str(e)
        )
    finally:
        if response is None:
            response = ReservationResponse(
                reservation_id=reservation_request.reservation_id,
                status=StatusCodeReservation.ERROR,
                message='Something went wrong'
            )
        return response


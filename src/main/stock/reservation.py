from src.main.stock.api.models import ReservationRequest, ReservationResponse, StatusResponse
from src.main.stock.db.models import GoodsHold
from src.main.stock.db.repository import StockReservationRepository
from src.main.stock.utils import StatusCodeResponseReservation, StatusCodeResponseStatus


async def reservation_goods(reservation_request: ReservationRequest) -> ReservationResponse:
    response = None

    try:
        hold = await StockReservationRepository.get_hold(reservation_request.reservation_id)
        if hold is not None:
            response = ReservationResponse(
                reservation_id=reservation_request.reservation_id,
                status=StatusCodeResponseReservation.ERROR,
                message=f'Reservation with that ID={reservation_request.product_id} exists.'
            )
        else:
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
                status=StatusCodeResponseReservation.SUCCESS,
                message=f'Successfully added {reservation_request.quantity} products with ID '
                         f'{reservation_request.product_id}'
            )
    except ValueError as e:
        response = ReservationResponse(
            reservation_id=reservation_request.reservation_id,
            status=StatusCodeResponseReservation.ERROR,
            message=str(e)
        )
    finally:
        if response is None:
            response = ReservationResponse(
                reservation_id=reservation_request.reservation_id,
                status=StatusCodeResponseReservation.ERROR,
                message='Something went wrong'
            )

    return response

async def get_status_reservation(reservation_id: str) -> StatusResponse:
    response = None

    try:
        hold = await StockReservationRepository.get_hold(reservation_id)

        if hold is None:
            response = StatusResponse(
                status=StatusCodeResponseStatus.NOT_FOUND,
                message='Reservation not found',
                reservation_id=reservation_id,
            )
        else:
            response = StatusResponse(
                status=StatusCodeResponseStatus.FOUND,
                message=f'Found reservation. Product {hold.product_id} has quantity {hold.quantity}',
                reservation_id=reservation_id,
            )
    finally:
        if response is None:
            response = StatusResponse(
                status=StatusCodeResponseStatus.ERROR,
                message='Error',
                reservation_id=reservation_id,
            )

    return response

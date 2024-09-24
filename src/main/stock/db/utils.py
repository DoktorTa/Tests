from datetime import datetime
from random import randint

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.main.db.base import get_session, async_session
from src.main.stock.db.models import Goods, GoodsHold
from src.main.stock.db.repository import StockReservationRepository


async def create_many_goods():
    # goods = []
    # for i in range(1, count_goods + 1):
    #     print(i, '- created')
    #     goods.append(Goods(product_id=str(i), quantity=randint(1, 100)))
    print(datetime.now().replace(microsecond=0))
    x = "2024-09-25 03:00:31"
    gds_hold = GoodsHold(
        reservation_id='10',
        product_id='10',
        quantity=10,
        timestamp_hold=datetime.now().replace(microsecond=0),
    )
    await StockReservationRepository.create_hold(gds_hold)
    # await repo.create_goods(goods)



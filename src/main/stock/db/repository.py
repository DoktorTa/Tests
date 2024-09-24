from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.main.db.base import async_session
from src.main.stock.db.models import Goods, GoodsHold


class StockReservationRepository:

    @staticmethod
    async def create_goods(goods: list[Goods], session: AsyncSession = async_session()) -> None:
        session.add_all(goods)
        await session.commit()

    @staticmethod
    async def sub_goods(product_id: str, quantity: int, session: AsyncSession = async_session()) -> None:
        stmt = select(Goods).filter_by(product_id=product_id).limit(1)
        result = await session.execute(stmt)

        goods = result.scalar_one_or_none()
        if goods is None:
            await session.rollback()
            raise ValueError(f"Product with id {product_id} not found.")
        elif goods.quantity >= quantity:
            goods.quantity -= quantity
        else:
            await session.rollback()
            raise ValueError(f"Product with id {product_id} is insufficient.")

        await session.commit()

    @staticmethod
    async def create_hold(hold: GoodsHold, session: AsyncSession = async_session()) -> None:
        session.add(hold)
        await session.commit()

    @staticmethod
    async def get_hold(reservation_id: str, session: AsyncSession = async_session()) -> GoodsHold | None:
        stmt = select(GoodsHold).filter_by(reservation_id=reservation_id).limit(1)
        result = await session.execute(stmt)

        hold = result.scalar_one_or_none()
        await session.commit()

        return hold

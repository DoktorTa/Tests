from datetime import datetime

from sqlalchemy import Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import mapped_column, Mapped

from db.base import Base


class Goods(Base):
    """ Товар """
    __tablename__ = "goods"

    product_id: Mapped[str] = mapped_column(String(255), nullable=False, primary_key=True)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    def __repr__(self) -> str:
        return f"Goods(product_id={self.product_id!r}, quantity={self.quantity!r})"


class GoodsHold(Base):
    """ Блокировка товара при его заказе """
    __tablename__ = "goods_holds"

    reservation_id: Mapped[str] = mapped_column(String(255), nullable=False, primary_key=True)
    product_id: Mapped[str] = mapped_column(ForeignKey("goods.product_id"), nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    timestamp_hold: Mapped[datetime] = mapped_column(DateTime, nullable=False)

    def __repr__(self) -> str:
        return (f"GoodsHold("
                f"reservation_id={self.reservation_id!r}, "
                f"product_id={self.product_id!r}, "
                f"quantity={self.quantity!r}, "
                f"timestamp_hold={self.timestamp_hold!r})")

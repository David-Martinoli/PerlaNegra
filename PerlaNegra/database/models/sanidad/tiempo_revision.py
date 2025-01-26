import reflex as rx
from sqlmodel import Field, func
from ..mixins.timestamp_mixin import TimestampMixin

# //tiempo de revicion 3 / 6 / 9 por ejemplo
class TiempoRevision(rx.Model, TimestampMixin, table=True):
    __tablename__ = "tiemporevision"
    id: int | None = Field(default=None, primary_key=True)
    valor: float

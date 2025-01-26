import reflex as rx
from sqlmodel import Field, func
from ..mixins.timestamp_mixin import TimestampMixin


# //graves leves ( gravisimas  generan actuacion disiplinaria )
class TipoSancion(rx.Model, TimestampMixin, table=True):
    __tablename__ = "tiposancion"
    id: int | None = Field(default=None, primary_key=True)
    nombre: str

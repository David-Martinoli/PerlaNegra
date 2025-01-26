import reflex as rx
from sqlmodel import Field, func
from ..mixins.timestamp_mixin import TimestampMixin


# positiva o negativa
class Ergometria(rx.Model, TimestampMixin, table=True):
    __tablename__ = "ergometria"
    id: int | None = Field(default=None, primary_key=True)
    nombre: str

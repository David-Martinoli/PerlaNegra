import reflex as rx
from sqlmodel import Field
from ..mixins.timestamp_mixin import TimestampMixin


# positiva o negativa
class Ergometria(rx.Model, TimestampMixin, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nombre: str

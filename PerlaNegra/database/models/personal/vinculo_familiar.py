import reflex as rx
from sqlmodel import Field, func
from ..mixins.timestamp_mixin import TimestampMixin


class VinculoFamiliar(rx.Model, TimestampMixin, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nombre: str

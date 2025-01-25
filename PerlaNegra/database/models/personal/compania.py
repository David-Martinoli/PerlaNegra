import reflex as rx
from sqlmodel import Field, func
from ..mixins.timestamp_mixin import TimestampMixin


class Compania(rx.Model, TimestampMixin, table=True):
    id: int | None = Field(default=None, primary_key=True)
    unidad_id: int | None = Field(foreign_key="unidad.id")
    nombre: str

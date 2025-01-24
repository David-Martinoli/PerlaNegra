import reflex as rx
from sqlmodel import Field
from ..mixins.timestamp_mixin import TimestampMixin


# secciones dentro de una compania
class Seccion(rx.Model, TimestampMixin, table=True):
    id: int | None = Field(default=None, primary_key=True)
    compania_id: int | None = Field(foreign_key="compania.id")
    nombre: str

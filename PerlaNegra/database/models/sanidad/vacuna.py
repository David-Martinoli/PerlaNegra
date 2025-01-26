import reflex as rx
from sqlmodel import Field, func
from ..mixins.timestamp_mixin import TimestampMixin


class Vacuna(rx.Model, TimestampMixin, table=True):
    __tablename__ = "vacuna"
    id: int | None = Field(default=None, primary_key=True)
    nombre: str
    descripcion: str

import reflex as rx
from sqlmodel import Field, func
from ..mixins.timestamp_mixin import TimestampMixin


class Enfermedad(rx.Model, TimestampMixin, table=True):
    __tablename__ = "enfermedad"
    id: int | None = Field(default=None, primary_key=True)
    nombre: str
    observacion: str

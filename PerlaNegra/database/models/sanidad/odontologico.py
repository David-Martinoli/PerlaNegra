import reflex as rx
from sqlmodel import Field, func
from datetime import date
from ..mixins.timestamp_mixin import TimestampMixin


class Odontologico(rx.Model, TimestampMixin, table=True):
    __tablename__ = "odontologico"
    id: int | None = Field(default=None, primary_key=True)
    personal_id: int | None = Field(foreign_key="personal.id")
    examen_odontologico: str = ""
    observacion_odontologica: str = ""
    fecha_odontograma: date

import reflex as rx
from sqlmodel import Field, func
from datetime import date
from ..mixins.timestamp_mixin import TimestampMixin


class Cardiologico(rx.Model, TimestampMixin, table=True):
    __tablename__ = "cardiologico"
    id: int | None = Field(default=None, primary_key=True)
    examen_medico_id: int | None = Field(foreign_key="examenmedico.id")
    ecg: str = ""
    ergometria_id: int | None = Field(foreign_key="ergometria.id")
    radiologia: str = ""
    otros: str = ""
    fecha: date

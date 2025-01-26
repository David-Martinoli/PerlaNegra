import reflex as rx
from sqlmodel import Field, func
from ..mixins.timestamp_mixin import TimestampMixin


class ExamenMedico(rx.Model, TimestampMixin, table=True):
    __tablename__ = "examenmedico"
    id: int | None = Field(default=None, primary_key=True)
    personal_id: int | None = Field(foreign_key="personal.id")
    peso: float
    talla: float
    imc: float  # formula peso / talla al cuadrada  indice de talla corporal

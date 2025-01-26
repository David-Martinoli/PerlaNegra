# database/models/personal.py
import reflex as rx
from sqlmodel import Field, func
from datetime import date, datetime, timezone
from ..mixins.timestamp_mixin import TimestampMixin


class FormacionAcademica(rx.Model, TimestampMixin, table=True):
    __tablename__ = "formacionacademica"
    id: int | None = Field(default=None, primary_key=True)
    nombre_titulo: str
    descripcion: str
    fecha_egreso: date
    personal_id: int | None = Field(foreign_key="personal.id")  # personalR
    created_at: datetime = Field(default=datetime.now(timezone.utc))

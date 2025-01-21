# database/models/personal.py
import reflex as rx
from sqlmodel import Field
from datetime import date, datetime, timezone
from ..mixins.timestamp_mixin import TimestampMixin


class FormacionAcademica(rx.Model, TimestampMixin, table=True):
    id: int = Field(primary_key=True)
    nombre_titulo: str
    descripcion: str
    fecha_egreso: date
    personal_id: int = Field(foreign_key="personal.id")  # personalR
    created_at: datetime = Field(default=datetime.now(timezone.utc))

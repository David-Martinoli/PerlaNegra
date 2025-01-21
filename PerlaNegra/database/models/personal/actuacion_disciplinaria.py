import reflex as rx
from sqlalchemy import Column, ForeignKey
from sqlmodel import Field
from datetime import date, datetime, timezone
from ..mixins.timestamp_mixin import TimestampMixin
from personal_s import PersonalS


class ActuacionDisciplinaria(rx.Model, TimestampMixin, table=True):
    id: int = Field(primary_key=True)
    numero_experiente: str
    fecha_inicio: date
    fecha_fin: date
    personal_id: int = Field(foreign_key="personal.id")
    actuante_id: int = Field(foreign_key="personal.id")
    causa: str
    observacion: str
    created_at: datetime = datetime.now(timezone.utc)
    updated_at: datetime = datetime.now(timezone.utc)

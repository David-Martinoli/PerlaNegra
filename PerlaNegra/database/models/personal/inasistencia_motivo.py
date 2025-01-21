import reflex as rx
from sqlalchemy import Column, ForeignKey
from sqlmodel import Field
from datetime import date, datetime, timezone
from ..mixins.timestamp_mixin import TimestampMixin
from personal_s import PersonalS


class InasistenciaMotivo(rx.Model, TimestampMixin, table=True):
    id: int = Field(primary_key=True)
    nombre: str
    descripcion: str
    created_at: datetime = datetime.now(timezone.utc)

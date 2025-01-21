import reflex as rx
from sqlalchemy import Column, ForeignKey
from sqlmodel import Field
from datetime import date, datetime, timezone
from ..mixins.timestamp_mixin import TimestampMixin
from personal_s import PersonalS


class ActuacionScan(rx.Model, TimestampMixin, table=True):
    id: int = Field(primary_key=True)
    actuacion_id: int = Field(foreign_key="actuacion.id")
    imagen: str
    descripcion: str
    created_at: datetime = datetime.now(timezone.utc)

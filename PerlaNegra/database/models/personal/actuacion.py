import reflex as rx
from sqlmodel import Field
from datetime import date, datetime, timezone
from ..mixins.timestamp_mixin import TimestampMixin


class Actuacion(rx.Model, TimestampMixin, table=True):
    id: int = Field(primary_key=True)
    personal_id: int = Field(foreign_key="personal.id")
    numero_experiente = str
    causa = str
    fecha_inicio = date
    fecha_fin = date
    estado_tramite = str
    actuante_id: int = Field(foreign_key="personal.id")
    created_at: datetime = datetime.now(timezone.utc)
    updated_at: datetime = datetime.now(timezone.utc)

import reflex as rx
from sqlmodel import Field
from datetime import date, datetime, timezone
from ..mixins.timestamp_mixin import TimestampMixin


class ActuacionDisciplinaria(rx.Model, TimestampMixin, table=True):
    id: int | None = Field(default=None, primary_key=True)
    numero_experiente: str
    fecha_inicio: date
    fecha_fin: date
    personal_id: int | None = Field(foreign_key="personal.id")
    actuante_id: int | None = Field(foreign_key="personal.id")
    causa: str
    observacion: str
    created_at: datetime = datetime.now(timezone.utc)
    updated_at: datetime = datetime.now(timezone.utc)

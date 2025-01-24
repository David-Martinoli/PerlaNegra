import reflex as rx
from sqlmodel import Field
from datetime import date, datetime, timezone
from ..mixins.timestamp_mixin import TimestampMixin


class Inasistencia(rx.Model, TimestampMixin, table=True):
    id: int | None = Field(default=None, primary_key=True)
    fecha = date
    personal_id: int | None = Field(foreign_key="personal.id")  # personalS
    inasistencia_motivo_id: int | None = Field(foreign_key="inasistenciamotivo.id")
    motivo = str
    created_at: datetime = datetime.now(timezone.utc)

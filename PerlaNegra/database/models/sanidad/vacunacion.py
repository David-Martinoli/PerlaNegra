import reflex as rx
from sqlmodel import Field, func
from datetime import datetime, timezone
from ..mixins.timestamp_mixin import TimestampMixin


class Vacunacion(rx.Model, TimestampMixin, table=True):
    id: int | None = Field(default=None, primary_key=True)
    profesional_id: int | None = Field(foreign_key="personal.id")
    personal_id: int | None = Field(foreign_key="personal.id")
    vacuna_id: int | None = Field(foreign_key="vacuna.id")
    fecha_vacunacion: datetime
    observaciones: str
    created_at: datetime = Field(default=datetime.now(timezone.utc))

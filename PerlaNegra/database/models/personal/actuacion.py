import reflex as rx
from sqlmodel import Field, func
from datetime import date, datetime, timezone
from ..mixins.timestamp_mixin import TimestampMixin


class Actuacion(rx.Model, TimestampMixin, table=True):
    id: int | None = Field(default=None, primary_key=True)
    personal_id: int | None = Field(foreign_key="personal.id")
    numero_experiente = str
    causa = str
    fecha_inicio = date
    fecha_fin = date
    estado_tramite = str
    actuante_id: int | None = Field(foreign_key="personal.id")
    created_at: datetime | None = Field(
        default=None,
        nullable=True,
        sa_column_kwargs={"server_default": func.now()},
    )
    updated_at: datetime = datetime.now(timezone.utc)

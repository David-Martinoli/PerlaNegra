import reflex as rx
from sqlmodel import Field, func
from datetime import datetime, timezone
from ..mixins.timestamp_mixin import TimestampMixin


class PersonalSeguro(rx.Model, TimestampMixin, table=True):
    id: int | None = Field(default=None, primary_key=True)
    personal_id: int | None = Field(foreign_key="personal.id")
    seguro_id: int | None = Field(foreign_key="seguro.id")
    fecha_asignacion: datetime = datetime.now(timezone.utc)

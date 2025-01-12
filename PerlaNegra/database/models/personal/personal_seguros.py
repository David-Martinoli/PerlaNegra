import reflex as rx
from sqlmodel import Field
from datetime import datetime, timezone
from ..mixins.timestamp_mixin import TimestampMixin


class PersonalSeguros(rx.Model, TimestampMixin, table=True):
    id: int = Field(primary_key=True)
    personal_id: int = Field(foreign_key="personal.id")
    seguro_id: int = Field(foreign_key="seguro.id")
    fecha_asignacion: datetime = datetime.now(timezone.utc)

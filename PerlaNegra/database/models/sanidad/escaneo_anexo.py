import reflex as rx
from sqlmodel import Field
from datetime import datetime, timezone
from ..mixins.timestamp_mixin import TimestampMixin


class EscaneoAnexo(rx.Model, TimestampMixin, table=True):
    id: int = Field(primary_key=True)
    declaracion_jurada_id: int = Field(foreign_key="declaracionjurada.id")
    nombre_archivo: str
    created_at: datetime = datetime.now(timezone.utc)

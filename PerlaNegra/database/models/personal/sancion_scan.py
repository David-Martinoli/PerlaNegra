import reflex as rx
from sqlmodel import Field
from datetime import datetime, timezone
from ..mixins.timestamp_mixin import TimestampMixin


class SancionScan(rx.Model, TimestampMixin, table=True):
    id: int | None = Field(default=None, primary_key=True)
    sancion_id: int | None = Field(foreign_key="sancion.id")
    imagen: str
    descripcion: str
    created_at: datetime = datetime.now(timezone.utc)

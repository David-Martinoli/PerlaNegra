import reflex as rx
from sqlmodel import Field
from datetime import datetime, timezone
from ..mixins.timestamp_mixin import TimestampMixin


class Direccion(rx.Model, TimestampMixin, table=True):
    id: int | None = Field(default=None, primary_key=True)
    personal_id: int | None = Field(foreign_key="personal.id")  # personalR
    calle: str
    ciudad: str = ""
    estado: str = ""
    codigo_postal: str = ""
    pais: str = ""
    tipo_direccion: str = ""
    created_at: datetime = datetime.now(timezone.utc)
    updated_at: datetime = datetime.now(timezone.utc)

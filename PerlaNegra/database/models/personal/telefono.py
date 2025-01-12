import reflex as rx
from sqlmodel import Field
from datetime import datetime, timezone
from ..mixins.timestamp_mixin import TimestampMixin


class Telefono(rx.Model, TimestampMixin, table=True):
    id: int = Field(primary_key=True)
    personal_id: int = Field(foreign_key="personal_r.id")
    numero_telefono: str
    tipo_telefono: str = ""
    creado_en: datetime = datetime.now(timezone.utc)
    actualizado_en: datetime = datetime.now(timezone.utc)

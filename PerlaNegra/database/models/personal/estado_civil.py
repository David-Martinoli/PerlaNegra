# database/models/estado_civil.py
import reflex as rx
from sqlmodel import Field
from datetime import date, datetime, timezone
from ..mixins.timestamp_mixin import TimestampMixin


class EstadoCivil(rx.Model, TimestampMixin, table=True):
    id: int = Field(primary_key=True)
    nombre: str
    creado_en: datetime = datetime.now(timezone.utc)

# database/models/personal.py
import reflex as rx
from sqlmodel import Field
from datetime import date, datetime, timezone
from ..mixins.timestamp_mixin import TimestampMixin


class Felicitaciones(rx.Model, TimestampMixin, table=True):
    id: int = Field(primary_key=True)
    quien_impone: str
    fecha: datetime
    causa: str
    descripcion: str
    imagen: str
    creado_en: datetime = datetime.now(timezone.utc)
    personal_id = Field(foreign_key="personal_s.id")

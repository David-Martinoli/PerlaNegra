import reflex as rx
from sqlmodel import Field
from datetime import datetime, timezone
from ..mixins.timestamp_mixin import TimestampMixin


class ActuacionDisciplinariaScan(rx.Model, TimestampMixin, table=True):
    id: int = Field(primary_key=True)
    imagen: str
    descripcion: str
    actuacion_disciplinaria_id: int = Field(foreign_key="actuaciondisciplinaria.id")
    created_at: datetime = datetime.now(timezone.utc)

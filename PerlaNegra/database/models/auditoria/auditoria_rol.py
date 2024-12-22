import reflex as rx
from sqlmodel import Field
from datetime import datetime, timezone
from ..mixins.timestamp_mixin import TimestampMixin

class AuditoriaRol(rx.Model, TimestampMixin, table=True):
    id: int = Field(primary_key=True)
    usuario_id: int = Field(foreign_key='usuario.id')
    rol_id: int = Field(foreign_key='rol.id')
    accion: str
    fecha: datetime = Field(default=datetime.now(timezone.utc))
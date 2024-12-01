import reflex as rx
from datetime import date, datetime
from .mixins.timestamp_mixin import TimestampMixin

class AuditoriaRol(rx.Model, TimestampMixin, table=True):
    id: int = rx.Field(primary_key=True)
    usuario_id: int = rx.Field(foreign_key='usuario.id')
    rol_id: int = rx.Field(foreign_key='rol.id')
    accion: str
    fecha: datetime = rx.Field(default_factory=datetime.utcnow)
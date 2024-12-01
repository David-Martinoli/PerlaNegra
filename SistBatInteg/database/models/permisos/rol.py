import reflex as rx
from ..mixins.timestamp_mixin import TimestampMixin

class Rol(rx.Model, TimestampMixin, table=True):
    id: int = rx.Field(primary_key=True)
    nombre: str
    descripcion: str = ''
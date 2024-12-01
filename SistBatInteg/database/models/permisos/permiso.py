import reflex as rx
from ..mixins.timestamp_mixin import TimestampMixin

class Permiso(rx.Model, TimestampMixin, table=True):
    id: int = rx.Field(primary_key=True)
    modulo: str
    accion: str
    descripcion: str = ''
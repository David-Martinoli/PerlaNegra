import reflex as rx
from sqlmodel import Field
from ..mixins.timestamp_mixin import TimestampMixin

class Permiso(rx.Model, TimestampMixin, table=True):
    id: int = Field(primary_key=True)
    modulo: str
    accion: str
    descripcion: str = ''
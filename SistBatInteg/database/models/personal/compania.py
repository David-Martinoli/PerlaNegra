import reflex as rx
from ..mixins.timestamp_mixin import TimestampMixin

class Compania(rx.Model, TimestampMixin, table=True):
    id: int = rx.Field(primary_key=True)
    unidad_id: int = rx.Field(foreign_key='unidad.id')
    nombre: str
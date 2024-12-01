import reflex as rx
from ..mixins.timestamp_mixin import TimestampMixin

class Cuadro(rx.Model, TimestampMixin, table=True):
    id: int = rx.Field(primary_key=True)
    categoria_personal_id: int = rx.Field(foreign_key='categoria_personal.id')
    nombre: str
    iniciales: str
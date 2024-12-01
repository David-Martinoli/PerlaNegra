import reflex as rx
from sqlmodel import Field
from ..mixins.timestamp_mixin import TimestampMixin

class Compania(rx.Model, TimestampMixin, table=True):
    id: int = Field(primary_key=True)
    unidad_id: int = Field(foreign_key='unidad.id')
    nombre: str
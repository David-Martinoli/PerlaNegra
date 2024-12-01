import reflex as rx
from sqlmodel import Field
from ..mixins.timestamp_mixin import TimestampMixin

class ProgramaSalud(rx.Model, TimestampMixin, table=True):
    id: int = Field(primary_key=True)
    nombre: str
    tiempo_revision_id: int = Field(foreign_key='tiemporevision.id')
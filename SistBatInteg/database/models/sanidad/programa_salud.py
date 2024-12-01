import reflex as rx
from ..mixins.timestamp_mixin import TimestampMixin

class ProgramaSalud(rx.Model, TimestampMixin, table=True):
    id: int = rx.Field(primary_key=True)
    nombre: str
    tiempo_revision_id: int = rx.Field(foreign_key='tiempo_revision.id')
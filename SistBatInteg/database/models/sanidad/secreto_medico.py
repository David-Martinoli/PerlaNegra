import reflex as rx
from ..mixins.timestamp_mixin import TimestampMixin

class SecretoMedico(rx.Model, TimestampMixin, table=True):
    id: int = rx.Field(primary_key=True)
    profesional_id: int = rx.Field(foreign_key='personal.id')
    paciente_id: int = rx.Field(foreign_key='personal.id')
    descripcion: str
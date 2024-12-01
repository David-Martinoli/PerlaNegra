import reflex as rx
from sqlmodel import Field
from ..mixins.timestamp_mixin import TimestampMixin

class SecretoMedico(rx.Model, TimestampMixin, table=True):
    id: int = Field(primary_key=True)
    profesional_id: int = Field(foreign_key='personal.id')
    paciente_id: int = Field(foreign_key='personal.id')
    descripcion: str
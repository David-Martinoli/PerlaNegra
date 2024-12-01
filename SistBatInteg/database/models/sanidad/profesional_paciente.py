import reflex as rx
from sqlmodel import Field
from datetime import datetime, timezone
from ..mixins.timestamp_mixin import TimestampMixin

class ProfesionalPaciente(rx.Model, TimestampMixin, table=True):
    id: int = Field(primary_key=True)
    profesional_id: int = Field(foreign_key='personal.id')
    paciente_id: int = Field(foreign_key='personal.id')
    acceso: bool = True
    fecha_asignacion: datetime = datetime.now(timezone.utc)
import reflex as rx
from datetime import datetime
from ..mixins.timestamp_mixin import TimestampMixin

class ProfesionalPaciente(rx.Model, TimestampMixin, table=True):
    id: int = rx.Field(primary_key=True)
    profesional_id: int = rx.Field(foreign_key='personal.id')
    paciente_id: int = rx.Field(foreign_key='personal.id')
    acceso: bool = True
    fecha_asignacion: datetime = datetime.now(datetime.UTC)
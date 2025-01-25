import reflex as rx
from sqlmodel import Field, func
from datetime import datetime, timezone
from ..mixins.timestamp_mixin import TimestampMixin


## tabla para asociar profesionales con sus pacientes,
## garantiza el acceso exclusivo:
class ProfesionalPaciente(rx.Model, TimestampMixin, table=True):
    id: int | None = Field(default=None, primary_key=True)
    profesional_id: int | None = Field(foreign_key="personal.id")
    paciente_id: int | None = Field(foreign_key="personal.id")
    acceso: bool = True
    fecha_asignacion: datetime = datetime.now(timezone.utc)

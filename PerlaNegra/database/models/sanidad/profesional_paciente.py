import reflex as rx
from sqlmodel import Field, func, Relationship
from datetime import datetime, timezone
from ..mixins.timestamp_mixin import TimestampMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..personal.personal import Personal


## tabla para asociar profesionales con sus pacientes,
## garantiza el acceso exclusivo:
class ProfesionalPaciente(rx.Model, TimestampMixin, table=True):
    __tablename__ = "profesional_paciente"
    id: int | None = Field(default=None, primary_key=True)
    profesional_id: int | None = Field(foreign_key="personal.id")
    paciente_id: int | None = Field(foreign_key="personal.id")
    acceso: bool = True
    fecha_asignacion: datetime = datetime.now(timezone.utc)

    # Relaciones
    profesional_paciente_profesionalid_personal_relation: "Personal" = Relationship(
        back_populates="personal_profesional_paciente_profesionalid_relation",
        sa_relationship_kwargs={
            "foreign_keys": "ProfesionalPaciente.profesional_id",
            "lazy": "joined",
        },
    )
    profesional_paciente_pacienteid_personal_relation: "Personal" = Relationship(
        back_populates="personal_profesional_paciente_pacienteid_relation",
        sa_relationship_kwargs={
            "foreign_keys": "ProfesionalPaciente.paciente_id",
            "lazy": "joined",
        },
    )

import reflex as rx
from sqlmodel import Field, func, Relationship
from datetime import date, datetime, timezone
from ..mixins.timestamp_mixin import TimestampMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..personal.personal import Personal


## tabla para asociar profesionales con sus pacientes,
## garantiza el acceso exclusivo:
class ProfesionalPaciente(rx.Model, TimestampMixin, table=True):
    """Modelo para gestionar asignación profesional-paciente."""

    __tablename__ = "profesional_paciente"

    id: int | None = Field(default=None, primary_key=True)
    profesional_id: int | None = Field(foreign_key="personal.id")
    paciente_id: int | None = Field(foreign_key="personal.id")
    acceso: bool = True
    fecha_asignacion: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )
    fecha_revocacion: date | None = Field(default=None)

    # Relaciones
    profesional_paciente_profesionalid_personal_relation: "Personal" = Relationship(
        back_populates="personal_profesional_paciente_profesionalid_relation",
        sa_relationship_kwargs={
            "foreign_keys": "ProfesionalPaciente.profesional_id",
        },
    )
    profesional_paciente_pacienteid_personal_relation: "Personal" = Relationship(
        back_populates="personal_profesional_paciente_pacienteid_relation",
        sa_relationship_kwargs={
            "foreign_keys": "ProfesionalPaciente.paciente_id",
        },
    )

    # @validator("fecha_revocacion")
    # def validar_fechas(cls, v, values):
    #    if v and values.get("fecha_asignacion") and v < values["fecha_asignacion"]:
    #        raise ValueError("Fecha revocación debe ser posterior a asignación")
    #    return v

    def __repr__(self) -> str:
        return f"ProfesionalPaciente(prof_id={self.profesional_id}, pac_id={self.paciente_id})"

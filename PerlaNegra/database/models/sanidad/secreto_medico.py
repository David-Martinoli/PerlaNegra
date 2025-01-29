import reflex as rx
from sqlmodel import Field, func, Relationship
from ..mixins.timestamp_mixin import TimestampMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..personal.personal import Personal


## agregar tabla de secreto medico a los pacientes segun profesional.
## un profesional no debe leer la informacion almacenada de otro profesional
class SecretoMedico(rx.Model, TimestampMixin, table=True):
    __tablename__ = "secretomedico"
    id: int | None = Field(default=None, primary_key=True)
    profesional_id: int | None = Field(foreign_key="personal.id")
    paciente_id: int | None = Field(foreign_key="personal.id")
    descripcion: str

    # Relaciones
    secreto_medico_profesionalid_personal_relation: "Personal" = Relationship(
        back_populates="personal_secreto_medico_profesionalid_relation",
        sa_relationship_kwargs={
            "foreign_keys": "SecretoMedico.profesional_id",
            "lazy": "joined",
        },
    )
    secreto_medico_pacienteid_personal_relation: "Personal" = Relationship(
        back_populates="personal_secreto_medico_pacienteid_relation",
        sa_relationship_kwargs={
            "foreign_keys": "SecretoMedico.paciente_id",
            "lazy": "joined",
        },
    )

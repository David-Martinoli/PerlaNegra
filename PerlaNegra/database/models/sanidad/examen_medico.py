import reflex as rx
from sqlmodel import Field, func, Relationship
from ..mixins.timestamp_mixin import TimestampMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..personal.personal import Personal
    from .cardiologico import Cardiologico
    from .declaracion_jurada import DeclaracionJurada


class ExamenMedico(rx.Model, TimestampMixin, table=True):
    __tablename__ = "examenmedico"
    id: int | None = Field(default=None, primary_key=True)
    personal_id: int | None = Field(foreign_key="personal.id")
    peso: float
    talla: float
    imc: float  # formula peso / talla al cuadrada  indice de talla corporal

    # Relaciones
    examen_medico_personal_relation: "Personal" = Relationship(
        back_populates="personal_examen_medico_relation",
        sa_relationship_kwargs={"lazy": "joined"},
    )
    examen_medico_cardiologico_relation: list["Cardiologico"] = Relationship(
        back_populates="cardiologico_examen_medico_relation",
        sa_relationship_kwargs={"lazy": "joined"},
    )
    examen_medico_declaracion_jurada_relation: list["DeclaracionJurada"] = Relationship(
        back_populates="declaracion_jurada_examen_medico_relation",
        sa_relationship_kwargs={"lazy": "joined"},
    )

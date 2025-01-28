import reflex as rx
from sqlmodel import Field, Relationship
from typing import TYPE_CHECKING
from ..mixins.timestamp_mixin import TimestampMixin

if TYPE_CHECKING:
    from .actuacion_disciplinaria import ActuacionDisciplinaria
    from .personal_r import PersonalR
    from .personal_s import PersonalS


class Personal(rx.Model, TimestampMixin, table=True):
    """Modelo unificado de personal que vincula datos personales y de servicio.

    Attributes:
        id: Identificador único
        personalR_id: ID de referencia a datos personales
        personalS_id: ID de referencia a datos de servicio
        datos_personales: Relación con datos personales
        datos_servicio: Relación con datos de servicio
        actuaciones: Lista de actuaciones disciplinarias
        actuaciones_como_actuante: Lista de actuaciones donde actúa como supervisor
    """

    __tablename__ = "personal"
    id: int | None = Field(default=None, primary_key=True)
    personalR_id: int | None = Field(
        foreign_key="personalr.id", nullable=False, ondelete="RESTRICT"
    )
    personalS_id: int | None = Field(
        foreign_key="personals.id", nullable=False, ondelete="RESTRICT"
    )

    # Relaciones
    personal_personals_relation: "PersonalS" = Relationship(
        back_populates="personals_personal_relation",
        sa_relationship_kwargs={"lazy": "joined"},
    )
    personal_personalr_relation: "PersonalR" = Relationship(
        back_populates="personalr_personal_relation",
        sa_relationship_kwargs={"lazy": "joined"},
    )
    personal_actuacion_p_relation: list["ActuacionDisciplinaria"] = Relationship(
        back_populates="actuacion_p_personal_relation",
        sa_relationship_kwargs={"foreign_keys": "ActuacionDisciplinaria.personal_id"},
    )
    personal_actuacion_a_relation: list["ActuacionDisciplinaria"] = Relationship(
        back_populates="actuacion_a_personal_relation",
        sa_relationship_kwargs={"foreign_keys": "ActuacionDisciplinaria.actuante_id"},
    )

    # @property
    # def nombre_completo(self) -> str:
    #    return self.datos_personales.nombre_completo if self.datos_personales else ""

    # @property
    # def legajo(self) -> str:
    #    return self.datos_servicio.numero_legajo if self.datos_servicio else ""

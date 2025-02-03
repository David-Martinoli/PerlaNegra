import reflex as rx
from sqlmodel import Field, func, Relationship
from datetime import date, datetime
from ..mixins.timestamp_mixin import TimestampMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .personal import Personal
    from .inasistencia_motivo import InasistenciaMotivo


class Inasistencia(rx.Model, TimestampMixin, table=True):
    """Modelo para gestionar inasistencias del personal.

    Attributes:
        fecha: Fecha de la inasistencia
        personal_id: ID del personal
        motivo_id: ID del otivo
        observaciones: Detalles adicionales
    """

    __tablename__ = "inasistencia"
    id: int | None = Field(default=None, primary_key=True)
    fecha: date = Field()
    personal_id: int | None = Field(foreign_key="personal.id")
    inasistencia_motivo_id: int | None = Field(foreign_key="inasistenciamotivo.id")
    motivo = str
    justificada: bool = Field(default=True)

    created_at: datetime | None = Field(
        default=None,
        nullable=True,
        sa_column_kwargs={"server_default": func.now()},
    )

    # Relaciones
    inasistencia_personal_relation: "Personal" = Relationship(
        back_populates="personal_inasistencia_relation"
    )
    inasistencia_inasistrencia_motivo_relation: "InasistenciaMotivo" = Relationship(
        back_populates="inasistencia_motivo_inasistencia_relation"
    )

    # @validator("fecha")
    # def validar_fecha(cls, v):
    #    if v > date.today():
    #        raise ValueError("La fecha no puede ser futura")
    #    return v

    def __repr__(self) -> str:
        return f"Inasistencia(fecha={self.fecha})"

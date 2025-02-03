import reflex as rx
from sqlmodel import Field, func, Relationship
from ..mixins.timestamp_mixin import TimestampMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .tiempo_revision import TiempoRevision


class ProgramaSalud(rx.Model, TimestampMixin, table=True):
    """Modelo para gestionar programas de salud."""

    __tablename__ = "programasalud"

    id: int | None = Field(default=None, primary_key=True)
    nombre: str = Field(..., min_length=2, max_length=100)
    descripcion: str | None = Field(default=None, max_length=500)
    tiempo_revision_id: int | None = Field(
        foreign_key="tiemporevision.id", nullable=False, ondelete="RESTRICT"
    )
    activo: bool = Field(default=True)
    orden: int = Field(default=0)

    # Relaciones
    programa_salud_tiempo_revision_relation: "TiempoRevision" = Relationship(
        back_populates="tiempo_revision_programa_salud_relation"
    )

    # @validator("nombre")
    # def validar_nombre(cls, v):
    #    return v.strip().upper()

    def __repr__(self) -> str:
        return f"ProgramaSalud(nombre={self.nombre})"

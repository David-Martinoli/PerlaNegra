import reflex as rx
from sqlmodel import Field, func, Relationship
from ..mixins.timestamp_mixin import TimestampMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .tiempo_revision import TiempoRevision


class ProgramaSalud(rx.Model, TimestampMixin, table=True):
    __tablename__ = "programasalud"
    id: int | None = Field(default=None, primary_key=True)
    nombre: str
    tiempo_revision_id: int | None = Field(
        foreign_key="tiemporevision.id", nullable=False, ondelete="RESTRICT"
    )

    # Relaciones
    programa_salud_tiempo_revision_relation: "TiempoRevision" = Relationship(
        back_populates="tiempo_revision_programa_salud_relation"
    )

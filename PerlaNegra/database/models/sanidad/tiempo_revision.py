import reflex as rx
from sqlmodel import Field, func, Relationship
from ..mixins.timestamp_mixin import TimestampMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .programa_salud import ProgramaSalud


# //tiempo de revicion 3 / 6 / 9 por ejemplo
class TiempoRevision(rx.Model, TimestampMixin, table=True):
    __tablename__ = "tiemporevision"
    id: int | None = Field(default=None, primary_key=True)
    valor: float

    # Relaciones
    tiempo_revision_programa_salud_relation: list["ProgramaSalud"] = Relationship(
        back_populates="programa_salud_tiempo_revision_relation"
    )

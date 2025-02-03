import reflex as rx
from sqlmodel import Field, func, Relationship
from ..mixins.timestamp_mixin import TimestampMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .programa_salud import ProgramaSalud


# //tiempo de revicion 3 / 6 / 9 por ejemplo
class TiempoRevision(rx.Model, TimestampMixin, table=True):
    """Modelo para gestionar intervalos de tiempo entre revisiones médicas."""

    __tablename__ = "tiemporevision"

    id: int | None = Field(default=None, primary_key=True)
    valor: float = Field(ge=0, le=24)  # meses
    descripcion: str = Field(max_length=1000)
    activo: bool = Field(default=True)
    orden: int = Field(default=0)

    # Relaciones
    tiempo_revision_programa_salud_relation: list["ProgramaSalud"] = Relationship(
        back_populates="programa_salud_tiempo_revision_relation"
    )

    # @validator("valor")
    # def validar_valor(cls, v):
    #    if v not in [3, 6, 9, 12, 18, 24]:
    #        raise ValueError("Valor debe ser 3, 6, 9, 12, 18 o 24 meses")
    #    return v

    def __repr__(self) -> str:
        return f"TiempoRevision(valor={self.valor})"

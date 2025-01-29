import reflex as rx
from sqlmodel import Field, func, Relationship
from ..mixins.timestamp_mixin import TimestampMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .vacunacion import Vacunacion


class Vacuna(rx.Model, TimestampMixin, table=True):
    """Modelo para gestionar tipos de vacunas."""

    __tablename__ = "vacuna"

    id: int | None = Field(default=None, primary_key=True)
    nombre: str = Field(min_length=2, max_length=100)
    descripcion: str = Field(max_length=500)
    activo: bool = Field(default=True)

    # Relaciones
    vacuna_vacunacion_relation: list["Vacunacion"] = Relationship(
        back_populates="vacunacion_vacuna_relation",
        sa_relationship_kwargs={"lazy": "joined"},
    )

    # @validator("nombre")
    # def validar_nombre(cls, v):
    #    return v.strip().upper()

    def __repr__(self) -> str:
        return f"Vacuna(nombre={self.nombre})"

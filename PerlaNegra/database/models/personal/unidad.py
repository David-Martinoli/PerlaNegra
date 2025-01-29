import reflex as rx
from sqlmodel import Field, func, Relationship
from ..mixins.timestamp_mixin import TimestampMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .compania import Compania


class Unidad(rx.Model, TimestampMixin, table=True):
    """Modelo para gestionar unidades militares."""

    __tablename__ = "unidad"

    id: int | None = Field(default=None, primary_key=True)
    nombre: str = Field(min_length=2, max_length=100)
    ubicacion: str | None = Field(default=None, max_length=200)
    activo: bool = Field(default=True)
    orden: int = Field(default=0)

    # Relaciones
    unidad_compania_relation: list["Compania"] = Relationship(
        back_populates="compania_unidad_relation"
    )

    # @validator("nombre", "codigo")
    # def validar_texto(cls, v):
    #    return v.strip().upper()

    def __repr__(self) -> str:
        return f"Unidad(nombre={self.nombre})"

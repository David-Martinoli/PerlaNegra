import reflex as rx
from sqlmodel import Field, func, Relationship
from ..mixins.timestamp_mixin import TimestampMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .compania import Compania
    from .movimiento_personal import MovimientoPersonal


# secciones dentro de una compania
class Seccion(rx.Model, TimestampMixin, table=True):
    """Modelo para gestionar secciones dentro de una compañía."""

    __tablename__ = "seccion"

    id: int | None = Field(default=None, primary_key=True)
    compania_id: int | None = Field(foreign_key="compania.id")
    nombre: str = Field(min_length=2, max_length=100)
    descripcion: str | None = Field(default=None, max_length=200)
    activo: bool = Field(default=True)
    orden: int = Field(default=0)

    # Relaciones
    seccion_movimiento_personal_relation: list["MovimientoPersonal"] = Relationship(
        back_populates="movimiento_personal_seccion_relation",
    )
    seccion_compania_relation: "Compania" = Relationship(
        back_populates="compania_seccion_relation",
    )

    # @validator("nombre")
    # def validar_nombre(cls, v):
    #    return v.strip().upper()

    def __repr__(self) -> str:
        return f"Seccion(nombre={self.nombre})"

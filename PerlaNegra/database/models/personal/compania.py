import reflex as rx
from sqlmodel import Field, func, Relationship
from ..mixins.timestamp_mixin import TimestampMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .unidad import Unidad
    from .movimiento_personal import MovimientoPersonal
    from .seccion import Seccion


class Compania(rx.Model, TimestampMixin, table=True):
    """Modelo para representar compañías militares.

    Attributes:
        nombre: Nombre de la compañía
        unidad_id: ID de la unidad a la que pertenece
        descripcion: Descripción adicional
        activo: Estado de la compañía
    """

    __tablename__ = "compania"
    id: int | None = Field(default=None, primary_key=True)
    unidad_id: int | None = Field(foreign_key="unidad.id")
    nombre: str = Field(min_length=2, max_length=100)
    descripcion: str | None = Field(default=None, max_length=200)
    activo: bool = Field(default=True)
    orden: int = Field(default=0)

    # Relaciones
    compania_unidad_relation: "Unidad" = Relationship(
        back_populates="unidad_compania_relation",
    )
    compania_movimiento_personal_relation: list["MovimientoPersonal"] = Relationship(
        back_populates="movimiento_personal_compania_relation",
    )
    compania_seccion_relation: list["Seccion"] = Relationship(
        back_populates="seccion_compania_relation",
    )

    # @validator("nombre")
    # def validar_nombre(cls, v):
    #    return v.strip().upper()

    def __repr__(self) -> str:
        return f"Compania(nombre={self.nombre})"

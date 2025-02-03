import reflex as rx
from sqlmodel import Field, func, Relationship
from ..mixins.timestamp_mixin import TimestampMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .cuadro import Cuadro
    from .personal_s import PersonalS


class CategoriaPersonal(rx.Model, TimestampMixin, table=True):
    """Modelo para categorías de personal.

    Attributes:
        nombre: Nombre de la categoría
        descripcion: Descripción detallada
        activo: Estado de la categoría
    """

    __tablename__ = "categoriapersonal"
    id: int | None = Field(default=None, primary_key=True)
    nombre: str = Field(min_length=2, max_length=100)
    descripcion: str | None = Field(default=None, max_length=500)
    activo: bool = Field(default=True)
    orden: int = Field(default=0)

    # Relaciones
    categoria_personal_cuadro_relation: list["Cuadro"] = Relationship(
        back_populates="cuadro_categoria_personal_relation",
    )
    categoria_personal_personals_relation: list["PersonalS"] = Relationship(
        back_populates="personals_categoria_personal_relation",
    )

    # @validator("nombre")
    # def validar_nombre(cls, v):
    #    """Valida y formatea el nombre."""
    #    return v.strip().upper()

    def __repr__(self) -> str:
        return f"CategoriaPersonal(nombre={self.nombre})"

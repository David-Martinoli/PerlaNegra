import reflex as rx
from sqlmodel import Field, func, Relationship
from ..mixins.timestamp_mixin import TimestampMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from categoria_personal import CategoriaPersonal


class Cuadro(rx.Model, TimestampMixin, table=True):
    """Modelo para representar cuadros de personal militar.

    Attributes:
        nombre: Nombre del cuadro
        iniciales: Iniciales/abreviatura del cuadro
        categoria_personal_id: ID de la categoría asociada
        activo: Estado del cuadro
    """

    __tablename__ = "cuadro"
    id: int | None = Field(default=None, primary_key=True)
    categoria_personal_id: int | None = Field(foreign_key="categoriapersonal.id")
    nombre: str = Field(min_length=2, max_length=100)
    iniciales: str = Field(min_length=1, max_length=10)
    activo: bool = Field(default=True)
    orden: int = Field(default=0)

    # Relaciones
    cuadro_categoria_personal_relation: "CategoriaPersonal" = Relationship(
        back_populates="categoria_personal_cuadro_relation",
    )

    # @validator("iniciales")
    # def validar_iniciales(cls, v):
    #    return v.strip().upper()

    # @validator("nombre")
    # def validar_nombre(cls, v):
    #    return v.strip().title()

    def __repr__(self) -> str:
        return f"Cuadro(iniciales={self.iniciales})"

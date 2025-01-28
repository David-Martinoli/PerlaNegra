import reflex as rx
from sqlmodel import Field, func, Relationship
from ..mixins.timestamp_mixin import TimestampMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from categoria_personal import CategoriaPersonal


class Cuadro(rx.Model, TimestampMixin, table=True):
    __tablename__ = "cuadro"
    id: int | None = Field(default=None, primary_key=True)
    categoria_personal_id: int | None = Field(foreign_key="categoriapersonal.id")
    nombre: str
    iniciales: str

    # Relaciones
    cuadro_categoria_personal_relation: "CategoriaPersonal" = Relationship(
        back_populates="categoria_personal_cuadro_relation",
        sa_relationship_kwargs={"lazy": "joined"},
    )

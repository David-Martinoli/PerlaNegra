import reflex as rx
from sqlmodel import Field, func, Relationship
from ..mixins.timestamp_mixin import TimestampMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from cuadro import Cuadro


class CategoriaPersonal(rx.Model, TimestampMixin, table=True):
    __tablename__ = "categoriapersonal"
    id: int | None = Field(default=None, primary_key=True)
    nombre: str

    # Relaciones
    categoria_personal_cuadro_relation: list["Cuadro"] = Relationship(
        back_populates="cuadro_categoria_personal_relation",
        sa_relationship_kwargs={"lazy": "joined"},
    )

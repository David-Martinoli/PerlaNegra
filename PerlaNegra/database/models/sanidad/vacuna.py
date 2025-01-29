import reflex as rx
from sqlmodel import Field, func, Relationship
from ..mixins.timestamp_mixin import TimestampMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .vacunacion import Vacunacion


class Vacuna(rx.Model, TimestampMixin, table=True):
    __tablename__ = "vacuna"
    id: int | None = Field(default=None, primary_key=True)
    nombre: str
    descripcion: str

    # Relaciones
    vacuna_vacunacion_relation: list["Vacunacion"] = Relationship(
        back_populates="vacunacion_vacuna_relation",
        sa_relationship_kwargs={"lazy": "joined"},
    )

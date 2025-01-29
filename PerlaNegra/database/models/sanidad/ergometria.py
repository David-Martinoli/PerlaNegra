import reflex as rx
from sqlmodel import Field, func, Relationship
from ..mixins.timestamp_mixin import TimestampMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .cardiologico import Cardiologico  


# positiva o negativa
class Ergometria(rx.Model, TimestampMixin, table=True):
    __tablename__ = "ergometria"
    id: int | None = Field(default=None, primary_key=True)
    nombre: str

    # Relaciones
    ergometria_cardiologico_relation: list["Cardiologico"] = Relationship(
        back_populates="cardiologico_ergometria_relation",
        sa_relationship_kwargs={"lazy": "joined"},
    )
import reflex as rx
from sqlmodel import Field, func, Relationship
from ..mixins.timestamp_mixin import TimestampMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .unidad import Unidad


class Compania(rx.Model, TimestampMixin, table=True):
    __tablename__ = "compania"
    id: int | None = Field(default=None, primary_key=True)
    unidad_id: int | None = Field(foreign_key="unidad.id")
    nombre: str

    # Relaciones
    compania_unidad_relation: "Unidad" = Relationship(
        back_populates="unidad_compania_relation"
    )

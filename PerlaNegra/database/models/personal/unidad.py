import reflex as rx
from sqlmodel import Field, func, Relationship
from ..mixins.timestamp_mixin import TimestampMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .compania import Compania


class Unidad(rx.Model, TimestampMixin, table=True):
    __tablename__ = "unidad"
    id: int | None = Field(default=None, primary_key=True)
    nombre: str

    # Relaciones
    unidad_compania_relation: list["Compania"] = Relationship(
        back_populates="compania_unidad_relation"
    )

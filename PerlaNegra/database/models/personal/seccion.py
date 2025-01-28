import reflex as rx
from sqlmodel import Field, func, Relationship
from ..mixins.timestamp_mixin import TimestampMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .compania import Compania
    from .movimiento_personal import MovimientoPersonal


# secciones dentro de una compania
class Seccion(rx.Model, TimestampMixin, table=True):
    __tablename__ = "seccion"
    id: int | None = Field(default=None, primary_key=True)
    compania_id: int | None = Field(foreign_key="compania.id")
    nombre: str

    # Relaciones
    seccion_movimiento_personal_relation: list["MovimientoPersonal"] = Relationship(
        back_populates="movimiento_personal_seccion_relation",
        sa_relationship_kwargs={"lazy": "joined"},
    )
    seccion_compania_relation: "Compania" = Relationship(
        back_populates="compania_seccion_relation",
        sa_relationship_kwargs={"lazy": "joined"},
    )

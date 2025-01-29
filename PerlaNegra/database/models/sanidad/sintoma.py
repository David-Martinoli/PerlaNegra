import reflex as rx
from sqlmodel import Field, func, Relationship
from ..mixins.timestamp_mixin import TimestampMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .declaracion_sintoma import DeclaracionSintoma


class Sintoma(rx.Model, TimestampMixin, table=True):
    __tablename__ = "sintoma"
    id: int | None = Field(default=None, primary_key=True)
    nombre: str
    observacion: str

    # Relaciones
    sintoma_declaracion_sintoma_relation: list["DeclaracionSintoma"] = Relationship(
        back_populates="declaracion_sintoma_sintoma_relation",
        sa_relationship_kwargs={"lazy": "joined"},
    )

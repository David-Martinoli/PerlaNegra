import reflex as rx
from sqlmodel import Field, func, Relationship
from ..mixins.timestamp_mixin import TimestampMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .laboratorio import Laboratorio


class PruebaHemograma(rx.Model, TimestampMixin, table=True):
    __tablename__ = "pruebahemograma"
    id: int | None = Field(default=None, primary_key=True)
    globulos_rojos: int
    hematocritos: int
    hb: int
    vcm: int
    hcm: int
    chcm: int
    rdw: int
    cv: int
    plaquetas: int
    globulos_blancos: int
    formula: str = ""

    # Relaciones
    prueba_hemograma_laboratorio_relation: "Laboratorio" = Relationship(
        back_populates="laboratorio_prueba_hemograma_relation"
    )

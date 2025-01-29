import reflex as rx
from sqlmodel import Field, func, Relationship
from datetime import date
from ..mixins.timestamp_mixin import TimestampMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .prueba_hemograma import PruebaHemograma
    from .declaracion_jurada import DeclaracionJurada


class Laboratorio(rx.Model, TimestampMixin, table=True):
    __tablename__ = "laboratorio"
    id: int | None = Field(default=None, primary_key=True)
    prueba_hemograma_id: int | None = Field(foreign_key="pruebahemograma.id")
    eritrosedimentacion: str = ""
    glucemia: float
    uremia: float
    colesterol_total: float
    hdl_colesterol: float
    ldl_colesterol: float
    trigliceridos: float
    orina_completa: str = ""
    toxicologico: str = ""
    fecha: date
    hiv: str = ""
    hemograma: str = ""
    eritrocito: str = ""
    glucemia: str = ""
    creatinina: str = ""
    colesterol_total_texto: str = ""
    hdl: str = ""
    ldl: str = ""
    vdrl: str = ""
    orina_completa_texto: str = ""
    toxicologico_texto: str = ""
    hepatograma: str = ""
    indice_castelli: str = ""
    observaciones: str = ""

    # Relaciones
    laboratorio_declaracion_jurada_relation: list["DeclaracionJurada"] = Relationship(
        back_populates="declaracion_jurada_laboratorio_relation"
    )
    laboratorio_prueba_hemograma_relation: "PruebaHemograma" = Relationship(
        back_populates="prueba_hemograma_laboratorio_relation"
    )

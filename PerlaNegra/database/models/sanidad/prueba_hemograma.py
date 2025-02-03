from datetime import date
from enum import Enum
import reflex as rx
from sqlmodel import Field, func, Relationship
from ..mixins.timestamp_mixin import TimestampMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .laboratorio import Laboratorio


class EstadoHemograma(str, Enum):
    NORMAL = "NORMAL"
    ANEMIA = "ANEMIA"
    LEUCOCITOSIS = "LEUCOCITOSIS"
    TROMBOCITOPENIA = "TROMBOCITOPENIA"


class PruebaHemograma(rx.Model, TimestampMixin, table=True):
    """Modelo para almacenar resultados de hemogramas."""

    __tablename__ = "pruebahemograma"

    id: int | None = Field(default=None, primary_key=True)
    fecha: date = Field(default=func.now(), nullable=False)

    # Valores con rangos normales
    globulos_rojos: float = Field(ge=3.5, le=6.5)  # millones/μL
    hematocritos: float = Field(ge=35.0, le=55.0)  # %
    hemoglobina: float = Field(ge=11.0, le=18.0)  # g/dL
    # hb: float = Field(ge=11.0, le=18.0)  # g/dL
    vcm: float = Field(ge=80.0, le=100.0)  # fL
    hcm: float = Field(ge=27.0, le=32.0)  # pg
    chcm: float = Field(ge=32.0, le=36.0)  # g/dL
    rdw: float = Field(ge=11.5, le=14.5)  # %
    # cv: float = Field(ge=11.5, le=14.5)  # %
    plaquetas: int = Field(ge=150000, le=450000)  # /μL
    globulos_blancos: int = Field(ge=4000, le=11000)  # /μL

    formula: str = Field(max_length=500)
    observaciones: str | None = Field(default=None, max_length=1000)

    # Relaciones
    prueba_hemograma_laboratorio_relation: "Laboratorio" = Relationship(
        back_populates="laboratorio_prueba_hemograma_relation"
    )

    # @validator("fecha")
    # def validar_fecha(cls, v):
    #    if v > date.today():
    #        raise ValueError("La fecha no puede ser futura")
    #    return v

    @property
    def anemia(self) -> bool:
        """Detecta posible anemia."""
        return self.hemoglobina < 12.0

    @property
    def estado(self) -> str:
        """Evalúa estado general del hemograma."""
        if self.anemia:
            return EstadoHemograma.ANEMIA
        if self.globulos_blancos > 11000:
            return EstadoHemograma.LEUCOCITOSIS
        if self.plaquetas < 150000:
            return EstadoHemograma.TROMBOCITOPENIA
        return EstadoHemograma.NORMAL

    def __repr__(self) -> str:
        return f"PruebaHemograma(fecha={self.fecha}, estado={self.estado})"

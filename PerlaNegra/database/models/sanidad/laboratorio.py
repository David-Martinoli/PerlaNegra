from enum import Enum
import reflex as rx
from sqlmodel import Field, func, Relationship
from datetime import date
from ..mixins.timestamp_mixin import TimestampMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .prueba_hemograma import PruebaHemograma
    from .declaracion_jurada import DeclaracionJurada


class ResultadoTest(str, Enum):
    POSITIVO = "POSITIVO"
    NEGATIVO = "NEGATIVO"
    NO_REALIZADO = "NO_REALIZADO"


class RiesgoCardiovascular(str, Enum):
    BAJO = "BAJO"
    MODERADO = "MODERADO"
    ALTO = "ALTO"


class Laboratorio(rx.Model, TimestampMixin, table=True):
    """Modelo para gestionar análisis de laboratorio."""

    __tablename__ = "laboratorio"

    id: int | None = Field(default=None, primary_key=True)
    prueba_hemograma_id: int | None = Field(foreign_key="pruebahemograma.id")
    fecha: date = Field()

    # Hemograma
    eritrocitos: float = Field(default=0.0, ge=0, le=10)
    hemoglobina: float = Field(default=0.0, ge=0, le=20)
    hematocrito: float = Field(default=0.0, ge=0, le=100)
    eritrosedimentacion: int = Field(default=0, ge=0, le=200)
    hemograma: float = Field(default=0.0, ge=0, le=200)

    # Química sanguínea
    glucemia: float = Field(ge=0, le=500)
    uremia: float = Field(ge=0, le=200)
    creatinina: float = Field(ge=0, le=15)

    # Perfil lipídico
    colesterol_total: float = Field(ge=0, le=500)
    hdl_colesterol: float = Field(ge=0, le=100)
    ldl_colesterol: float = Field(ge=0, le=400)
    trigliceridos: float = Field(ge=0, le=1000)

    # Serología
    hiv: ResultadoTest = Field(default=ResultadoTest.NO_REALIZADO)
    vdrl: ResultadoTest = Field(default=ResultadoTest.NO_REALIZADO)
    hepatitis: ResultadoTest = Field(default=ResultadoTest.NO_REALIZADO)

    # Otros análisis
    orina_completa: str | None = Field(default=None, max_length=500)
    toxicologico: ResultadoTest = Field(default=ResultadoTest.NO_REALIZADO)
    observaciones: str | None = Field(default=None, max_length=1000)

    glucemia: str = ""
    colesterol_total_texto: str = ""
    hdl: str = ""
    ldl: str = ""

    hepatograma: str = Field(default="", max_length=500)
    indice_castelli: float = Field(default=0.0)

    # Relaciones
    laboratorio_declaracion_jurada_relation: list["DeclaracionJurada"] = Relationship(
        back_populates="declaracion_jurada_laboratorio_relation"
    )
    laboratorio_prueba_hemograma_relation: "PruebaHemograma" = Relationship(
        back_populates="prueba_hemograma_laboratorio_relation"
    )

    @property
    def indice_castelli(self) -> float:
        """Calcula índice de Castelli (CT/HDL)."""
        return (
            round(self.colesterol_total / self.hdl_colesterol, 2)
            if self.hdl_colesterol
            else 0
        )

    @property
    def riesgo_cardiovascular(self) -> RiesgoCardiovascular:
        """Determina nivel de riesgo cardiovascular."""
        ic = self.indice_castelli
        if ic < 4.5:
            return RiesgoCardiovascular.BAJO
        elif ic < 5:
            return RiesgoCardiovascular.MODERADO
        return RiesgoCardiovascular.ALTO

    def __repr__(self) -> str:
        return f"Laboratorio(fecha={self.fecha})"

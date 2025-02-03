from datetime import date
from enum import Enum
import reflex as rx
from sqlmodel import Field, func, Relationship
from ..mixins.timestamp_mixin import TimestampMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..personal.personal import Personal
    from .cardiologico import Cardiologico
    from .declaracion_jurada import DeclaracionJurada


class ResultadoExamen(str, Enum):
    APTO = "APTO"
    NO_APTO = "NO_APTO"
    PENDIENTE = "PENDIENTE"


class EstadoNutricional(str, Enum):
    BAJO_PESO = "BAJO PESO"
    NORMAL = "NORMAL"
    SOBREPESO = "SOBREPESO"
    OBESIDAD = "OBESIDAD"


class ExamenMedico(rx.Model, TimestampMixin, table=True):
    """Modelo para registrar exámenes médicos del personal."""

    __tablename__ = "examenmedico"

    id: int | None = Field(default=None, primary_key=True)
    personal_id: int | None = Field(foreign_key="personal.id")

    fecha: date = Field()
    peso: float = Field(ge=30.0, le=200.0)
    talla: float = Field(ge=1.0, le=2.5)
    imc: float  # formula peso / talla al cuadrada  indice de talla corporal

    resultado: ResultadoExamen = Field(default=ResultadoExamen.PENDIENTE)
    observaciones: str | None = Field(default=None, max_length=1000)

    # Relaciones
    examen_medico_personal_relation: "Personal" = Relationship(
        back_populates="personal_examen_medico_relation",
    )
    examen_medico_cardiologico_relation: list["Cardiologico"] = Relationship(
        back_populates="cardiologico_examen_medico_relation",
    )
    examen_medico_declaracion_jurada_relation: list["DeclaracionJurada"] = Relationship(
        back_populates="declaracion_jurada_examen_medico_relation",
    )

    @property
    def imc(self) -> float:
        """Calcula el Índice de Masa Corporal."""
        return round(self.peso / (self.talla**2), 2)

    @property
    def estado_nutricional(self) -> str:
        """Determina estado nutricional según IMC."""
        imc = self.imc
        if imc < 18.5:
            return EstadoNutricional.BAJO_PESO
        elif imc < 25:
            return EstadoNutricional.NORMAL
        elif imc < 30:
            return EstadoNutricional.SOBREPESO
        return EstadoNutricional.OBESIDAD

    def __repr__(self) -> str:
        return f"ExamenMedico(fecha={self.fecha}, imc={self.imc})"

    def __repr__(self) -> str:
        return f"ExamenMedico(fecha={self.fecha}, imc={self.imc})"

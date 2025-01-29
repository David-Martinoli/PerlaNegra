from enum import Enum
import reflex as rx
from sqlmodel import Field, func, Relationship
from ..mixins.timestamp_mixin import TimestampMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .cardiologico import Cardiologico


class ResultadoErgometria(str, Enum):
    POSITIVA = "POSITIVA"
    NEGATIVA = "NEGATIVA"
    DUDOSA = "DUDOSA"
    NO_CONCLUYENTE = "NO_CONCLUYENTE"


# positiva o negativa
class Ergometria(rx.Model, TimestampMixin, table=True):
    """Modelo para gestionar pruebas ergométricas."""

    __tablename__ = "ergometria"

    id: int | None = Field(default=None, primary_key=True)
    resultado: ResultadoErgometria = Field(default=ResultadoErgometria.NO_CONCLUYENTE)
    nombre: str

    tiempo_ejercicio: int = Field(ge=0)  # en minutos
    frecuencia_max: int = Field(ge=0)
    tension_max: int = Field(ge=0)
    mets_alcanzados: float = Field(ge=0)
    protocolo: str = Field(max_length=100)

    motivo_finalizacion: str = Field(max_length=200)
    observaciones: str | None = Field(default=None, max_length=1000)

    # Relaciones
    ergometria_cardiologico_relation: list["Cardiologico"] = Relationship(
        back_populates="cardiologico_ergometria_relation",
        sa_relationship_kwargs={"lazy": "joined"},
    )

    # @validator("fecha")
    # def validar_fecha(cls, v):
    #    if v > date.today():
    #        raise ValueError("La fecha no puede ser futura")
    #    return v

    def __repr__(self) -> str:
        return f"Ergometria(fecha={self.fecha}, resultado={self.resultado})"

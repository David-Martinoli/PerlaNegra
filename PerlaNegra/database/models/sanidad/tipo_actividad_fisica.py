from enum import Enum
import reflex as rx
from sqlmodel import Field, func, Relationship
from ..mixins.timestamp_mixin import TimestampMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .declaracion_jurada import DeclaracionJurada


class NivelActividad(str, Enum):
    SEDENTARIO = "SEDENTARIO"
    LIGERO = "LIGERO"
    MODERADO = "MODERADO"
    INTENSO = "INTENSO"
    ATLETA = "ATLETA"


class TipoActividadFisica(rx.Model, TimestampMixin, table=True):
    """Modelo para gestionar tipos de actividad física."""

    __tablename__ = "tipoactividadfisica"

    id: int | None = Field(default=None, primary_key=True)
    nombre: str = Field(min_length=2, max_length=100)
    nivel: NivelActividad = Field(default=NivelActividad.SEDENTARIO)
    observacion: str | None = Field(default=None, max_length=500)
    activo: bool = Field(default=True)
    orden: int = Field(default=0)

    # Relaciones
    tipo_actividad_fisica_declaracion_jurada_relation: list["DeclaracionJurada"] = (
        Relationship(back_populates="declaracion_jurada_tipo_actividad_fisica_relation")
    )

    # @validator("nombre")
    # def validar_nombre(cls, v):
    #    return v.strip().upper()

    def __repr__(self) -> str:
        return f"TipoActividadFisica(nombre={self.nombre})"

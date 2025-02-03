from enum import Enum
import reflex as rx
from sqlmodel import Field, func, Relationship
from ..mixins.timestamp_mixin import TimestampMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .declaracion_sintoma import DeclaracionSintoma


class TipoSintoma(str, Enum):
    RESPIRATORIO = "RESPIRATORIO"
    DIGESTIVO = "DIGESTIVO"
    MUSCULAR = "MUSCULAR"
    NEUROLOGICO = "NEUROLOGICO"
    OTRO = "OTRO"


class Sintoma(rx.Model, TimestampMixin, table=True):
    """Modelo para gestionar síntomas médicos."""

    __tablename__ = "sintoma"

    id: int | None = Field(default=None, primary_key=True)
    tipo: TipoSintoma = Field(default=TipoSintoma.OTRO)

    nombre: str = Field(min_length=2, max_length=100)
    observacion: str = Field(max_length=500)
    gravedad: int = Field(default=1, ge=1, le=5)
    activo: bool = Field(default=True)

    # Relaciones
    sintoma_declaracion_sintoma_relation: list["DeclaracionSintoma"] = Relationship(
        back_populates="declaracion_sintoma_sintoma_relation",
        sa_relationship_kwargs={"lazy": "joined"},
    )

    # @validator("nombre")
    # def validar_nombre(cls, v):
    #    return v.strip().upper()

    def __repr__(self) -> str:
        return f"Sintoma(nombre={self.nombre})"

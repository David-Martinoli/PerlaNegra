from enum import Enum
import reflex as rx
from sqlmodel import Field, func
from ..mixins.timestamp_mixin import TimestampMixin


class TipoEnfermedad(str, Enum):
    CRONICA = "CRONICA"
    INFECCIOSA = "INFECCIOSA"
    HEREDITARIA = "HEREDITARIA"
    LABORAL = "LABORAL"
    OTRA = "OTRA"


class Enfermedad(rx.Model, TimestampMixin, table=True):
    """Modelo para registrar enfermedades."""

    __tablename__ = "enfermedad"

    id: int | None = Field(default=None, primary_key=True)
    tipo: TipoEnfermedad = Field(default=TipoEnfermedad.OTRA)
    nombre: str = Field(min_length=2, max_length=100)
    observacion: str = Field(max_length=500)

    codigo_cie10: str | None = Field(default=None, max_length=10)
    activo: bool = Field(default=True)

    # @validator("nombre")
    # def validar_nombre(cls, v):
    #    return v.strip().upper()

    def __repr__(self) -> str:
        return f"Enfermedad(nombre={self.nombre})"

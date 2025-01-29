from enum import Enum
import reflex as rx
from sqlmodel import Field, func, Relationship
from ..mixins.timestamp_mixin import TimestampMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .sancion import Sancion


class GravedadSancion(str, Enum):
    LEVE = "LEVE"
    GRAVE = "GRAVE"
    GRAVISIMA = "GRAVISIMA"


# //graves leves ( gravisimas  generan actuacion disiplinaria )
class TipoSancion(rx.Model, TimestampMixin, table=True):
    """Modelo para clasificar tipos de sanciones disciplinarias."""

    __tablename__ = "tiposancion"

    id: int | None = Field(default=None, primary_key=True)
    nombre: GravedadSancion = Field(default=GravedadSancion.LEVE)
    dias_minimos: int = Field(default=0, ge=0)
    dias_maximos: int = Field(default=30, ge=0)
    activo: bool = Field(default=True)

    # Relaciones
    tipo_sancion_sancion_relation: list["Sancion"] = Relationship(
        back_populates="sancion_tipo_sancion_relation",
    )

    # @validator("nombre")
    # def validar_nombre(cls, v):
    #    return v.strip().upper()

    def __repr__(self) -> str:
        return f"TipoSancion(nombre={self.nombre})"

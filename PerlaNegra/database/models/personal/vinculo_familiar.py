from enum import Enum
import reflex as rx
from sqlmodel import Field, func, Relationship
from ..mixins.timestamp_mixin import TimestampMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .familiar import Familiar


class TipoVinculo(str, Enum):
    CONYUGE = "CONYUGE"
    HIJO = "HIJO"
    PADRE = "PADRE"
    MADRE = "MADRE"
    HERMANO = "HERMANO"
    OTRO = "OTRO"


class VinculoFamiliar(rx.Model, TimestampMixin, table=True):
    """Modelo para gestionar tipos de vínculos familiares."""

    __tablename__ = "vinculofamiliar"

    id: int | None = Field(default=None, primary_key=True)
    nombre: str = Field(min_length=2, max_length=50)
    # TipoVinculo = Field(default=TipoVinculo.OTRO)
    activo: bool = Field(default=True)

    # Relaciones
    vinculo_familiar_familiar_relation: list["Familiar"] = Relationship(
        back_populates="familiar_vinculo_familiar_relation",
    )

    # @validator("nombre")
    # def validar_nombre(cls, v):
    #    return v.strip().upper()

    def __repr__(self) -> str:
        return f"VinculoFamiliar(nombre={self.nombre})"

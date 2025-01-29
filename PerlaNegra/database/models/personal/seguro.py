from enum import Enum
import reflex as rx
from sqlmodel import Field, func, Relationship
from datetime import datetime
from ..mixins.timestamp_mixin import TimestampMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .personal_seguro import PersonalSeguro


class TipoSeguro(str, Enum):
    VIDA = "VIDA"
    SALUD = "SALUD"
    ACCIDENTES = "ACCIDENTES"
    OTRO = "OTRO"


class Seguro(rx.Model, TimestampMixin, table=True):
    """Modelo para gestionar seguros del personal."""

    __tablename__ = "seguro"

    id: int | None = Field(default=None, primary_key=True)
    nombre: str = Field(min_length=2, max_length=100)
    tipo: TipoSeguro = Field(default=TipoSeguro.OTRO)
    descripcion: str | None = Field(default=None, max_length=500)

    poliza: str = Field(max_length=50)
    compania: str = Field(max_length=100)
    activo: bool = Field(default=True)

    created_at: datetime | None = Field(
        default=None,
        nullable=True,
        sa_column_kwargs={"server_default": func.now()},
    )

    # Relaciones
    seguro_personal_seguro_relation: list["PersonalSeguro"] = Relationship(
        back_populates="personal_seguro_seguro_relation",
    )

    # @validator("nombre", "compania")
    # def validar_texto(cls, v):
    #    return v.strip().upper()

    def __repr__(self) -> str:
        return f"Seguro(nombre={self.nombre})"

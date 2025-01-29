import reflex as rx
from enum import Enum
from sqlmodel import Field, func, Relationship
from datetime import datetime, timezone
from ..mixins.timestamp_mixin import TimestampMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .personal_s import PersonalS


class TipoClase(str, Enum):
    CIVIL = "CIVIL"
    MILITAR = "MILITAR"


# //civil o militar
class Clase(rx.Model, TimestampMixin, table=True):
    """Modelo para clasificar personal civil o militar.

    Attributes:
        nombre: Tipo de clase (CIVIL/MILITAR)
        descripcion: Descripción detallada
        activo: Estado de la clase
    """

    __tablename__ = "clase"
    id: int | None = Field(default=None, primary_key=True)
    nombre: TipoClase = Field(description="Tipo de clase")
    descripcion: str | None = Field(default=None, max_length=200)
    activo: bool = Field(default=True)

    created_at: datetime | None = Field(
        default=None,
        nullable=True,
        sa_column_kwargs={"server_default": func.now()},
    )

    # Relaciones
    clase_personals_relation: list["PersonalS"] = Relationship(
        back_populates="personals_clase_relation",
    )

    # @validator("nombre")
    # def validar_nombre(cls, v):
    #    """Normaliza el nombre."""
    #    return v.upper()

    def __repr__(self) -> str:
        return f"Clase(nombre={self.nombre})"

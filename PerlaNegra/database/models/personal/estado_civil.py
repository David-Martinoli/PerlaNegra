from enum import Enum
from typing import TYPE_CHECKING
import reflex as rx
from sqlmodel import Field, func, Relationship
from datetime import datetime
from ..mixins.timestamp_mixin import TimestampMixin

if TYPE_CHECKING:
    from .personal_r import PersonalR


class TipoEstadoCivil(str, Enum):
    SOLTERO = "SOLTERO"
    CASADO = "CASADO"
    DIVORCIADO = "DIVORCIADO"
    VIUDO = "VIUDO"
    UNION_CIVIL = "UNION_CIVIL"


class EstadoCivil(rx.Model, TimestampMixin, table=True):
    """Modelo que representa el estado civil de una persona.

    Attributes:
        id (int): Identificador único del estado civil
        nombre (str): Nombre del estado civil (ej: Soltero, Casado, etc)
        created_at (datetime): Fecha de creación del registro
        personal_r (List[PersonalR]): Lista de personal relacionado
    """

    __tablename__ = "estadocivil"

    id: int | None = Field(default=None, primary_key=True)
    nombre: str = Field(min_length=2, max_length=50, unique=True, index=True)
    descripcion: str | None = Field(default=None, max_length=200)
    activo: bool = Field(default=True)
    created_at: datetime | None = Field(
        default=None, nullable=True, sa_column_kwargs={"server_default": func.now()}
    )

    # Relaciones
    estadocivil_personalr: list["PersonalR"] = Relationship(
        back_populates="personalr_estado_civil",
        sa_relationship_kwargs={"cascade": "all, delete-orphan"},
    )

    # @validator("nombre")
    # def validar_nombre(cls, v):
    #    return v.upper()

    def __repr__(self) -> str:
        return f"EstadoCivil(nombre={self.nombre})"

    @property
    def total_personal(self) -> int:
        """Retorna el total de personal con este estado civil"""
        return len(self.personal_r)

from enum import Enum
import reflex as rx
from sqlmodel import Field, func, Relationship
from datetime import datetime
from ..mixins.timestamp_mixin import TimestampMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .inasistencia import Inasistencia


class TipoMotivo(str, Enum):
    ENFERMEDAD = "ENFERMEDAD"
    PERSONAL = "PERSONAL"
    FAMILIAR = "FAMILIAR"
    ESTUDIO = "ESTUDIO"
    OTRO = "OTRO"


class InasistenciaMotivo(rx.Model, TimestampMixin, table=True):
    """Modelo para gestionar los motivos de inasistencias.

    Attributes:
        nombre: Nombre del motivo
        descripcion: Descripción detallada
        tipo: Tipo de motivo
        activo: Estado del motivo
    """

    __tablename__ = "inasistenciamotivo"
    id: int | None = Field(default=None, primary_key=True)
    nombre: str = Field(min_length=2, max_length=100)
    descripcion: str = Field(max_length=500)
    tipo: TipoMotivo = Field(default=TipoMotivo.OTRO)
    activo: bool = Field(default=True)
    created_at: datetime | None = Field(
        default=None,
        nullable=True,
        sa_column_kwargs={"server_default": func.now()},
    )

    # Relaciones
    inasistencia_motivo_inasistencia_relation: list["Inasistencia"] = Relationship(
        back_populates="inasistencia_inasistrencia_motivo_relation"
    )

    # @validator("nombre")
    # def validar_nombre(cls, v):
    #    return v.strip().upper()

    def __repr__(self) -> str:
        return f"InasistenciaMotivo(nombre={self.nombre})"

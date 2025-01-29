from enum import Enum
import reflex as rx
from sqlmodel import Field, func, Relationship
from datetime import date, datetime
from ..mixins.timestamp_mixin import TimestampMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .personal import Personal
    from .tipo_sancion import TipoSancion
    from .sancion_scan import SancionScan


class EstadoSancion(str, Enum):
    ACTIVA = "activa"
    CUMPLIDA = "cumplida"
    ANULADA = "anulada"
    EN_RECURSO = "en_recurso"


# //graves leves ( gravisimas  generan actuacion disiplinaria )
class Sancion(rx.Model, TimestampMixin, table=True):
    """Modelo para gestionar sanciones disciplinarias."""

    __tablename__ = "sancion"

    id: int | None = Field(default=None, primary_key=True)
    personal_id: int | None = Field(foreign_key="personal.id")
    autoridad_id: int | None = Field(foreign_key="personal.id")
    tipo_sansion_id: int | None = Field(foreign_key="tiposancion.id")

    motivo: str | None = Field(default=None)
    fecha: date | None = Field(default=None)
    fecha_comision: date | None = Field(default=None)
    fecha_aplicacion: date | None = Field(default=None)
    fecha_revision_jefe: date | None = Field(default=None)
    fecha_recurso: date | None = Field(default=None)
    dias_arresto: int | None = Field(default=None)
    descripcion_reglamentaria: str | None = Field(default=None)

    created_at: datetime | None = Field(
        default=None,
        nullable=True,
        sa_column_kwargs={"server_default": func.now()},
    )

    # Relaciones
    sancion_sancion_scan_relation: list["SancionScan"] = Relationship(
        back_populates="sancion_scan_sancion_relation",
        sa_relationship_kwargs={"lazy": "joined"},
    )
    sancion_tipo_sancion_relation: "TipoSancion" = Relationship(
        back_populates="tipo_sancion_sancion_relation",
        sa_relationship_kwargs={"lazy": "joined"},
    )
    sancion_personal_personal_relation: "Personal" = Relationship(
        back_populates="personal_sancion_personal_relation",
        sa_relationship_kwargs={
            "foreign_keys": "Sancion.personal_id",
            "lazy": "joined",
        },
    )
    sancion_personal_autoridad_relation: "Personal" = Relationship(
        back_populates="personal_autoridad_sancion_relation",
        sa_relationship_kwargs={
            "foreign_keys": "Sancion.autoridad_id",
            "lazy": "joined",
        },
    )

    # @validator("fecha_recurso")
    # def validar_fechas(cls, v, values):
    #    if v and values.get("fecha_sancion") and v < values["fecha_sancion"]:
    #        raise ValueError("Fecha recurso debe ser posterior a sanción")
    #    return v

    def __repr__(self) -> str:
        return f"Sancion(personal_id={self.personal_id}, dias={self.dias_arresto})"

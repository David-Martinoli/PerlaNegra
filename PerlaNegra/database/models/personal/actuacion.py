from enum import Enum
import reflex as rx
from sqlmodel import Field, func, Relationship
from datetime import date, datetime
from ..mixins.timestamp_mixin import TimestampMixin

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .actuacion_scan import ActuacionScan
    from .personal import Personal


class EstadoTramite(str, Enum):
    INICIADO = "iniciado"
    EN_PROCESO = "en_proceso"
    FINALIZADO = "finalizado"
    ARCHIVADO = "archivado"


class Actuacion(rx.Model, TimestampMixin, table=True):
    __tablename__ = "actuacion"
    id: int | None = Field(default=None, primary_key=True)

    personal_id: int | None = Field(
        foreign_key="personal.id", nullable=False, ondelete="RESTRICT"
    )
    actuante_id: int | None = Field(
        foreign_key="personal.id", nullable=False, ondelete="RESTRICT"
    )

    numero_experiente: str = Field(..., unique=True, index=True)
    causa: str = Field(max_length=500)
    fecha_inicio: date
    fecha_fin: date | None = None
    estado_tramite: EstadoTramite = Field(default=EstadoTramite.INICIADO)
    observaciones: str | None = Field(default=None, max_length=1000)

    created_at: datetime | None = Field(
        default=None,
        nullable=True,
        sa_column_kwargs={"server_default": func.now()},
    )
    updated_at: datetime | None = Field(
        default_factory=datetime.now,
        nullable=False,
        sa_column_kwargs={"onupdate": func.now()},
    )

    # Relaciones
    actuacion_actuacion_scan_relation: list["ActuacionScan"] = Relationship(
        back_populates="actuacion_scan_actuacion_relation",
        sa_relationship_kwargs={"cascade": "all, delete-orphan"},
    )
    actuacion_personal_personal_relation: "Personal" = Relationship(
        back_populates="personal_actuacion_personal_relation",
        sa_relationship_kwargs={
            "foreign_keys": "Actuacion.personal_id",
            "lazy": "joined",
        },
    )
    actuacion_actuante_personal_relation: "Personal" = Relationship(
        back_populates="personal_actuacion_actuante_relation",
        sa_relationship_kwargs={
            "foreign_keys": "Actuacion.actuante_id",
            "lazy": "joined",
        },
    )

    # Validadores
    # @validator("fecha_fin")
    # def validar_fechas(cls, v, values):
    #    if v and values.get("fecha_inicio") and v < values["fecha_inicio"]:
    #        raise ValueError("Fecha fin debe ser posterior a fecha inicio")
    #    return v

    @property
    def duracion_dias(self) -> int | None:
        """Retorna la duración en días de la actuación."""
        if self.fecha_fin:
            return (self.fecha_fin - self.fecha_inicio).days
        return None

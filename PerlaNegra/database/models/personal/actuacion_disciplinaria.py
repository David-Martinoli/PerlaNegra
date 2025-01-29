from typing import TYPE_CHECKING
import reflex as rx
from enum import Enum
from sqlmodel import Field, func, Relationship
from datetime import date, datetime, timezone
from ..mixins.timestamp_mixin import TimestampMixin

if TYPE_CHECKING:
    from .actuacion_disciplinaria_scan import ActuacionDisciplinariaScan
    from .personal import Personal


class EstadoActuacion(str, Enum):
    INICIADO = "iniciado"
    EN_PROCESO = "en_proceso"
    FINALIZADO = "finalizado"
    ARCHIVADO = "archivado"


class ActuacionDisciplinaria(rx.Model, TimestampMixin, table=True):
    """Modelo para registrar actuaciones disciplinarias del personal.

    Attributes:
        numero_expediente: Número único del expediente
        estado: Estado actual de la actuación
        fecha_inicio: Fecha de inicio del expediente
        fecha_fin: Fecha de finalización del expediente
        personal: Personal involucrado en la actuación
        actuante: Personal que realiza la actuación
        scans: Documentos escaneados relacionados
    """

    __tablename__ = "actuaciondisciplinaria"
    id: int | None = Field(default=None, primary_key=True)
    numero_expediente: str = Field(unique=True, index=True)
    estado: EstadoActuacion = Field(default=EstadoActuacion.INICIADO)
    fecha_inicio: date
    fecha_fin: date | None = None
    personal_id: int = Field(foreign_key="personal.id", index=True)
    actuante_id: int = Field(foreign_key="personal.id", index=True)
    causa: str | None = Field(default=None, max_length=500)
    observacion: str | None = Field(default=None, max_length=2000)
    created_at: datetime | None = Field(
        default=None,
        nullable=True,
        sa_column_kwargs={"server_default": func.now()},
    )
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        sa_column_kwargs={"onupdate": func.now()},
    )

    # Relaciones
    actuacion_disciplinaria_personalid_personal_relation: "Personal" = Relationship(
        back_populates="personal_actuacion_disciplinaria_personalid_relation",
        sa_relationship_kwargs={"foreign_keys": "ActuacionDisciplinaria.personal_id"},
    )
    actuacion_disciplinaria_actuanteid_personal_relation: "Personal" = Relationship(
        back_populates="personal_actuacion_disciplinaria_actuanteid_relation",
        sa_relationship_kwargs={"foreign_keys": "ActuacionDisciplinaria.actuante_id"},
    )
    actuacion_disciplinaria_actuacion_isciplinaria_scan_relation: list[
        "ActuacionDisciplinariaScan"
    ] = Relationship(
        back_populates="actuacion_disciplinaria_scan_actuacion_disciplinaria_relation",
        sa_relationship_kwargs={"lazy": "joined"},
    )

    @property
    def esta_activa(self) -> bool:
        """Indica si la actuación está actualmente activa."""
        return self.fecha_fin is None

    @property
    def duracion_dias(self) -> int:
        """Retorna la duración en días de la actuación."""
        if not self.fecha_fin:
            return (date.today() - self.fecha_inicio).days
        return (self.fecha_fin - self.fecha_inicio).days

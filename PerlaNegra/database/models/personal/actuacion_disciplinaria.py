from typing import TYPE_CHECKING
import reflex as rx
from sqlmodel import Field, func, Relationship
from datetime import date, datetime, timezone
from ..mixins.timestamp_mixin import TimestampMixin

if TYPE_CHECKING:
    from .actuacion_disciplinaria_scan import ActuacionDisciplinariaScan
    from .personal import Personal


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
    numero_expediente: str
    fecha_inicio: date
    fecha_fin: date | None = None
    personal_id: int = Field(foreign_key="personal.id")
    actuante_id: int = Field(foreign_key="personal.id")
    causa: str
    observacion: str | None = None
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
    actuacion_p_personal_relation: "Personal" = Relationship(
        back_populates="personal_actuacion_p_relation",
        sa_relationship_kwargs={"foreign_keys": "ActuacionDisciplinaria.personal_id"},
    )
    actuacion_a_personal_relation: "Personal" = Relationship(
        back_populates="personal_actuacion_a_relation",
        sa_relationship_kwargs={"foreign_keys": "ActuacionDisciplinaria.actuante_id"},
    )
    scans: list["ActuacionDisciplinariaScan"] = Relationship(back_populates="actuacion")

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

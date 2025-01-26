import reflex as rx
from typing import TYPE_CHECKING
from sqlmodel import Field, func, Relationship
from datetime import date, datetime, timezone
from ..mixins.timestamp_mixin import TimestampMixin

if TYPE_CHECKING:
    from .actuacion_disciplinaria_scan import ActuacionDisciplinariaScan


class ActuacionDisciplinaria(rx.Model, TimestampMixin, table=True):
    """Modelo para registrar actuaciones disciplinarias del personal.

    Attributes:
        numero_expediente: Número único del expediente
        estado: Estado actual de la actuación
        scans: Relación con los documentos escaneados
    """

    __tablename__ = "actuaciondisciplinaria"
    id: int | None = Field(default=None, primary_key=True)
    numero_experiente: str
    fecha_inicio: date
    fecha_fin: date
    personal_id: int | None = Field(foreign_key="personal.id")
    actuante_id: int | None = Field(foreign_key="personal.id")
    causa: str
    observacion: str
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
    scans: list["ActuacionDisciplinariaScan"] = Relationship(back_populates="actuacion")

import reflex as rx
from sqlmodel import Field, func, Relationship
from datetime import datetime
from ..mixins.timestamp_mixin import TimestampMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .personal import Personal


class Calificacion(rx.Model, TimestampMixin, table=True):
    """Modelo para calificaciones del personal.

    Attributes:
        personal_id: ID del personal evaluado
        val1-val5: Valores de calificación (1-10)
        promedio: Promedio calculado automáticamente
        periodo: Período de evaluación
    """

    __tablename__ = "calificacion"
    id: int | None = Field(default=None, primary_key=True)
    personal_id: int | None = Field(foreign_key="personal.id")
    periodo: str = Field(max_length=20)  # Ej: "2024-1"
    val1: int = Field(default=0, ge=1, le=10)
    val2: int = Field(default=0, ge=1, le=10)
    val3: int = Field(default=0, ge=1, le=10)
    val4: int = Field(default=0, ge=1, le=10)
    val5: int = Field(default=0, ge=1, le=10)
    promedio: float = Field(default=0.0)

    observaciones: str | None = Field(default=None, max_length=500)

    created_at: datetime | None = Field(
        default=None,
        nullable=True,
        sa_column_kwargs={"server_default": func.now()},
    )

    # Relaciones
    calificacion_personal_relation: "Personal" = Relationship(
        back_populates="personal_calificacion_relation"
    )

    # @validator("promedio", always=True)
    # def calcular_promedio(cls, v, values):
    #    """Calcula promedio automáticamente."""
    #    vals = [
    #        values.get(f"val{i}", 0)
    #        for i in range(1,6)
    #    ]
    #    return sum(vals) / len(vals)

    def __repr__(self) -> str:
        return f"Calificacion(personal_id={self.personal_id}, promedio={self.promedio})"

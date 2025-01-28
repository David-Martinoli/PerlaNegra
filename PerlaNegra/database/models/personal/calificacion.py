import reflex as rx
from sqlmodel import Field, func, Relationship
from datetime import datetime, timezone
from ..mixins.timestamp_mixin import TimestampMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .personal import Personal


class Calificacion(rx.Model, TimestampMixin, table=True):
    __tablename__ = "calificacion"
    id: int | None = Field(default=None, primary_key=True)
    personal_id: int | None = Field(foreign_key="personal.id")
    val1: int = 0
    val2: int = 0
    val3: int = 0
    val4: int = 0
    val5: int = 0
    promedio: float = 0.0
    created_at: datetime | None = Field(
        default=None,
        nullable=True,
        sa_column_kwargs={"server_default": func.now()},
    )

    # Relaciones
    calificacion_personal_relation: "Personal" = Relationship(
        back_populates="personal_calificacion_relation"
    )

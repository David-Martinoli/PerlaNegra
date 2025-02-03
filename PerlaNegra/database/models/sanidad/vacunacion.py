import reflex as rx
from sqlmodel import Field, func, Relationship
from datetime import date, datetime, timezone
from ..mixins.timestamp_mixin import TimestampMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .vacuna import Vacuna
    from ..personal.personal import Personal


class Vacunacion(rx.Model, TimestampMixin, table=True):
    """Modelo para gestionar vacunaciones del personal."""

    __tablename__ = "vacunacion"

    id: int | None = Field(default=None, primary_key=True)
    profesional_id: int | None = Field(foreign_key="personal.id")
    personal_id: int | None = Field(foreign_key="personal.id")
    vacuna_id: int | None = Field(foreign_key="vacuna.id")

    fecha_vacunacion: date | None = Field(default=None)
    observaciones: str | None = Field(default=None, max_length=500)

    created_at: datetime | None = Field(
        default=None,
        nullable=True,
        sa_column_kwargs={"server_default": func.now()},
    )

    # Relaciones
    vacunacion_vacuna_relation: "Vacuna" = Relationship(
        back_populates="vacuna_vacunacion_relation",
    )
    vacunacion_peofesionalid_personal_relation: "Personal" = Relationship(
        back_populates="personal_vacunacion_profesionalid_relation",
        sa_relationship_kwargs={
            "foreign_keys": "Vacunacion.profesional_id",
        },
    )
    vacunacion_personalid_personal_relation: "Personal" = Relationship(
        back_populates="personal_vacunacion_personalid_relation",
        sa_relationship_kwargs={
            "foreign_keys": "Vacunacion.personal_id",
        },
    )

    # @validator("fecha_vacunacion")
    # def validar_fecha(cls, v):
    #    if v > datetime.now(timezone.utc):
    #        raise ValueError("La fecha no puede ser futura")
    #    return v

    def __repr__(self) -> str:
        return f"Vacunacion(personal_id={self.personal_id}, vacuna_id={self.vacuna_id})"

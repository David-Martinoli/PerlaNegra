import reflex as rx
from sqlmodel import Field, func, Relationship
from datetime import datetime, timezone
from ..mixins.timestamp_mixin import TimestampMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .vacuna import Vacuna
    from ..personal.personal import Personal


class Vacunacion(rx.Model, TimestampMixin, table=True):
    __tablename__ = "vacunacion"
    id: int | None = Field(default=None, primary_key=True)
    profesional_id: int | None = Field(foreign_key="personal.id")
    personal_id: int | None = Field(foreign_key="personal.id")
    vacuna_id: int | None = Field(foreign_key="vacuna.id")
    fecha_vacunacion: datetime
    observaciones: str
    created_at: datetime = Field(default=datetime.now(timezone.utc))

    # Relaciones
    vacunacion_vacuna_relation: "Vacuna" = Relationship(
        back_populates="vacuna_vacunacion_relation",
        sa_relationship_kwargs={"lazy": "joined"},
    )
    vacunacion_peofesionalid_personal_relation: "Personal" = Relationship(
        back_populates="personal_vacunacion_profesionalid_relation",
        sa_relationship_kwargs={
            "foreign_keys": "Vacunacion.profesional_id",
            "lazy": "joined",
        },
    )
    vacunacion_personalid_personal_relation: "Personal" = Relationship(
        back_populates="personal_vacunacion_personalid_relation",
        sa_relationship_kwargs={
            "foreign_keys": "Vacunacion.personal_id",
            "lazy": "joined",
        },
    )

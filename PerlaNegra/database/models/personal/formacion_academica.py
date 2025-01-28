# database/models/personal.py
import reflex as rx
from sqlmodel import Field, func, Relationship
from datetime import date, datetime, timezone
from ..mixins.timestamp_mixin import TimestampMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .personal import Personal


class FormacionAcademica(rx.Model, TimestampMixin, table=True):
    __tablename__ = "formacionacademica"
    id: int | None = Field(default=None, primary_key=True)
    nombre_titulo: str
    descripcion: str
    fecha_egreso: date
    personal_id: int | None = Field(foreign_key="personal.id")
    created_at: datetime | None = Field(
        default=None,
        nullable=True,
        sa_column_kwargs={"server_default": func.now()},
    )

    # Relaciones
    formacion_academica_personal_relation: "Personal" = Relationship(
        back_populates="personal_formacion_academica_relation",
        sa_relationship_kwargs={"lazy": "joined"},
    )

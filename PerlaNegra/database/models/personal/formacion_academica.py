# database/models/personal.py
from enum import Enum
import reflex as rx
from sqlmodel import Field, func, Relationship
from datetime import date, datetime, timezone
from ..mixins.timestamp_mixin import TimestampMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .personal import Personal


class TipoFormacion(str, Enum):
    UNIVERSITARIO = "UNIVERSITARIO"
    TERCIARIO = "TERCIARIO"
    TECNICO = "TECNICO"
    POSTGRADO = "POSTGRADO"
    OTRO = "OTRO"


class FormacionAcademica(rx.Model, TimestampMixin, table=True):
    """Modelo para gestionar la formación académica del personal."""

    __tablename__ = "formacionacademica"
    id: int | None = Field(default=None, primary_key=True)
    personal_id: int | None = Field(foreign_key="personal.id")

    nombre_titulo: str
    descripcion: str
    fecha_egreso: date
    tipo: TipoFormacion = Field(default=TipoFormacion.OTRO)
    institucion: str = Field(..., max_length=200)

    created_at: datetime | None = Field(
        default=None,
        nullable=True,
        sa_column_kwargs={"server_default": func.now()},
    )

    # Relaciones
    formacion_academica_personal_relation: "Personal" = Relationship(
        back_populates="personal_formacion_academica_relation",
    )

    # @validator("nombre_titulo", "institucion")
    # def validar_texto(cls, v):
    #    return v.strip().upper()

    def __repr__(self) -> str:
        return f"FormacionAcademica(titulo={self.nombre_titulo})"

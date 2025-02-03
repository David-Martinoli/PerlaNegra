import reflex as rx
from sqlmodel import Field, func, Relationship
from datetime import datetime, timezone
from ..mixins.timestamp_mixin import TimestampMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .personal import Personal
    from .seguro import Seguro


class PersonalSeguro(rx.Model, TimestampMixin, table=True):
    """Modelo para gestionar seguros asignados al personal."""

    __tablename__ = "personalseguro"

    id: int | None = Field(default=None, primary_key=True)
    personal_id: int | None = Field(foreign_key="personal.id")
    seguro_id: int | None = Field(foreign_key="seguro.id")
    activo: bool = Field(default=True)
    fecha_asignacion: datetime = datetime.now(timezone.utc)
    observaciones: str | None = Field(default=None, max_length=500)

    # Relaciones
    personal_seguro_personal_relation: "Personal" = Relationship(
        back_populates="personal_personal_seguro_relation",
    )
    personal_seguro_seguro_relation: "Seguro" = Relationship(
        back_populates="seguro_personal_seguro_relation",
    )

    # @validator("fecha_asignacion")
    # def validar_fecha(cls, v):
    #    if v > datetime.now(timezone.utc):
    #        raise ValueError("La fecha no puede ser futura")
    #    return v

    def __repr__(self) -> str:
        return f"PersonalSeguro(personal_id={self.personal_id})"

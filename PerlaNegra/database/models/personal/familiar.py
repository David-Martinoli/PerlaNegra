import reflex as rx
from sqlmodel import Field, func, Relationship
from datetime import date, datetime
from ..mixins.timestamp_mixin import TimestampMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .vinculo_familiar import VinculoFamiliar
    from .personal import Personal


class Familiar(rx.Model, TimestampMixin, table=True):
    """Modelo para gestionar familiares del personal.

    Attributes:
        nombre: Nombre del familiar
        apellido: Apellido del familiar
        dni: Documento de identidad
        fecha_nacimiento: Fecha de nacimiento
        fecha_vinculo: Fecha de inicio del vínculo
    """

    __tablename__ = "familiar"
    id: int | None = Field(default=None, primary_key=True)
    personal_id: int | None = Field(foreign_key="personal.id")
    vinculo_familiar_id: int | None = Field(foreign_key="vinculofamiliar.id")

    # Datos personales
    nombre: str = Field(min_length=2, max_length=100)
    apellido: str = Field(..., min_length=2, max_length=100)
    dni: str = Field(min_length=7, max_length=10)
    nacionalidad: str = Field(default="ARGENTINA", max_length=50)
    fecha_nacimiento: date
    fecha_vinculo: date

    created_at: datetime | None = Field(
        default=None,
        nullable=True,
        sa_column_kwargs={"server_default": func.now()},
    )
    updated_at: datetime | None = Field(
        default_factory=datetime.now,
        nullable=False,
        sa_column_kwargs={"onupdate": func.now()},
    )

    # Relaciones
    familiar_personal_relation: "Personal" = Relationship(
        back_populates="personal_familiar_relation",
    )
    familiar_vinculo_familiar_relation: "VinculoFamiliar" = Relationship(
        back_populates="vinculo_familiar_familiar_relation",
    )

    # @validator("dni")
    # def validar_dni(cls, v):
    #    return v.strip().replace(".", "")

    @property
    def nombre_completo(self) -> str:
        return f"{self.nombre} {self.apellido}"

    def __repr__(self) -> str:
        return f"Familiar(nombre={self.nombre_completo})"

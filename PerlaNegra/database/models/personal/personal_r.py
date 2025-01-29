from enum import Enum
import reflex as rx
from typing import TYPE_CHECKING
from sqlmodel import (
    Field,
    func,
    Relationship,
    SQLModel,
    Column,
    String,
    Index,
)
from datetime import date, datetime
from ..mixins.timestamp_mixin import TimestampMixin

if TYPE_CHECKING:
    # Importaciones condicionales para evitar circulares
    from .personal import Personal
    from .estado_civil import EstadoCivil


class EstadoServicio(str, Enum):
    ACTIVO = "ACTIVO"
    LICENCIA = "LICENCIA"
    COMISION = "COMISION"
    BAJA = "BAJA"


class PersonalR(rx.Model, TimestampMixin, table=True):
    """Modelo que representa al personal de la empresa."""

    __tablename__ = "personalr"  # Mantener el nombre

    id: int | None = Field(default=None, primary_key=True)
    nombre: str = Field(min_length=2, max_length=100)
    apellido: str = Field(min_length=2, max_length=100)
    fecha_nacimiento: date = Field()
    dni: str = Field(max_length=20, unique=True)

    cantidad_hijos: int = Field(default=0, ge=0)
    nacionalidad: str = Field(default="ARGENTINA", max_length=50)
    activo: bool = Field(default=True)

    created_at: datetime = Field(
        default_factory=datetime.now,
        nullable=False,
        sa_column_kwargs={"server_default": func.now()},
    )
    updated_at: datetime | None = Field(
        default_factory=datetime.now,
        nullable=False,
        sa_column_kwargs={"onupdate": func.now()},
    )

    # Relaciones
    personalr_personal_relation: list["Personal"] = Relationship(
        back_populates="personal_personalr_relation",
    )

    personalr_estado_civil: "EstadoCivil" = Relationship(
        back_populates="estadocivil_personalr",
    )

    # @validator("dni")
    # def validar_dni(cls, v):
    #    return v.strip().replace(".", "")

    # @validator("nombre", "apellido")
    # def validar_nombres(cls, v):
    #    return v.strip().title()

    # Propiedades calculadas
    @property
    def nombre_completo(self) -> str:
        """Retorna el nombre completo del empleado."""
        return f"{self.nombre.strip()} {self.apellido.strip()}".title()

    @property
    def edad(self) -> int:
        """Calcula la edad actual del empleado."""
        today = date.today()
        return (
            today.year
            - self.fecha_nacimiento.year
            - (
                (today.month, today.day)
                < (self.fecha_nacimiento.month, self.fecha_nacimiento.day)
            )
        )

    def __repr__(self) -> str:
        return f"PersonalR(id={self.id}, nombre={self.nombre_completo}, dni={self.dni})"

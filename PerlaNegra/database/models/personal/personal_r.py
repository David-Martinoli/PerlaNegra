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


class PersonalR(rx.Model, TimestampMixin, table=True):
    """Modelo que representa al personal de la empresa."""

    __tablename__ = "personalr"  # Mantener el nombre

    id: int | None = Field(default=None, primary_key=True)
    nombre: str = Field(max_length=100)
    apellido: str = Field(max_length=100)
    fecha_nacimiento: date
    dni: str = Field(max_length=20, unique=True)
    estado_civil_id: int | None = Field(
        foreign_key="estadocivil.id", nullable=False, ondelete="RESTRICT"
    )
    cantidad_hijos: int = Field(default=0, ge=0)
    # Timestamps heredados de TimestampMixin
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
        back_populates="personal_personalr_relation"  # , sa_relationship_kwargs={"lazy": "joined"}
    )

    estado_civil: "EstadoCivil" = Relationship(
        back_populates="personal_r",
        # sa_relationship_kwargs={"lazy": "joined"},
    )

    # Índices
    __table_args__ = (
        Index("idx_dni_personalr", "dni", unique=True),
        Index("idx_nombre_apellido_personalr", "nombre", "apellido"),
    )

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

from typing import TYPE_CHECKING, List, Optional
import reflex as rx
from sqlmodel import Field, func, Relationship
from datetime import datetime
from ..mixins.timestamp_mixin import TimestampMixin

if TYPE_CHECKING:
    from .personal_r import PersonalR


class EstadoCivil(rx.Model, TimestampMixin, table=True):
    """Modelo que representa el estado civil de una persona.

    Attributes:
        id (int): Identificador único del estado civil
        nombre (str): Nombre del estado civil (ej: Soltero, Casado, etc)
        created_at (datetime): Fecha de creación del registro
        personal_r (List[PersonalR]): Lista de personal relacionado
    """

    __tablename__ = "estadocivil"

    id: int = Field(primary_key=True)
    nombre: str = Field(min_length=2, max_length=50, unique=True, index=True)
    created_at: datetime | None = Field(
        default=None, nullable=True, sa_column_kwargs={"server_default": func.now()}
    )

    # Relaciones
    personal_r: List["PersonalR"] = Relationship(
        back_populates="estado_civil",
        sa_relationship_kwargs={"cascade": "all, delete-orphan"},
    )

    # class Config:
    #    orm_mode = True
    #    arbitrary_types_allowed = True

    def __str__(self) -> str:
        return self.nombre

    @property
    def total_personal(self) -> int:
        """Retorna el total de personal con este estado civil"""
        return len(self.personal_r)

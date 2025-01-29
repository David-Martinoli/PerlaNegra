from enum import Enum
import reflex as rx
from sqlmodel import Field, func, Relationship
from datetime import datetime
from ..mixins.timestamp_mixin import TimestampMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .personal import Personal


class TipoTelefono(str, Enum):
    CELULAR = "CELULAR"
    FIJO = "FIJO"
    LABORAL = "LABORAL"
    OTRO = "OTRO"


class Telefono(rx.Model, TimestampMixin, table=True):
    """Modelo para gestionar teléfonos del personal."""

    __tablename__ = "telefono"

    id: int | None = Field(default=None, primary_key=True)
    personal_id: int | None = Field(foreign_key="personal.id")

    numero_telefono: str = Field(min_length=8, max_length=20)
    tipo: TipoTelefono = Field(default=TipoTelefono.CELULAR)
    activo: bool = Field(default=True)
    principal: bool = Field(default=False)

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
    telefono_personal_relation: "Personal" = Relationship(
        back_populates="personal_telefono_relation"
    )

    # @validator("numero")
    # def validar_numero(cls, v):
    #    """Limpia y valida formato del número."""
    #    num = v.strip().replace(" ", "").replace("-", "")
    #    if not num.isdigit():
    #        raise ValueError("Número inválido")
    #    return num

    def __repr__(self) -> str:
        return f"Telefono(numero={self.numero})"

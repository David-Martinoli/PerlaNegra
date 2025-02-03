from enum import Enum
import reflex as rx
from datetime import datetime
from sqlmodel import Field, func, Relationship
from ..mixins.timestamp_mixin import TimestampMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .declaracion_jurada import DeclaracionJurada
    from .sintoma import Sintoma


class TipoSintoma(str, Enum):
    RESPIRATORIO = "RESPIRATORIO"
    CARDIOVASCULAR = "CARDIOVASCULAR"
    DIGESTIVO = "DIGESTIVO"
    NEUROLOGICO = "NEUROLOGICO"
    OTRO = "OTRO"


class DeclaracionSintoma(rx.Model, TimestampMixin, table=True):
    """Modelo para registrar síntomas en declaraciones juradas."""

    __tablename__ = "declaracionsintoma"

    id: int | None = Field(default=None, primary_key=True)
    declaracionjurada_id: int | None = Field(foreign_key="declaracionjurada.id")
    sintoma_id: int | None = Field(foreign_key="sintoma.id")
    tipo: TipoSintoma = Field(default=TipoSintoma.OTRO)
    respuesta: str | None = Field(default=None, min_length=2, max_length=100)
    gravedad: str | None = Field(default=None, min_length=2, max_length=100)
    observacion: str | None = Field(default=None, min_length=2, max_length=100)
    created_at: datetime | None = Field(
        default=None,
        nullable=True,
        sa_column_kwargs={"server_default": func.now()},
    )

    # Relaciones
    declaracion_sintoma_declaracion_jurada_relation: "DeclaracionJurada" = Relationship(
        back_populates="declaracion_jurada_declaracion_sintoma_relation"
    )
    declaracion_sintoma_sintoma_relation: "Sintoma" = Relationship(
        back_populates="sintoma_declaracion_sintoma_relation"
    )

    # @validator("fecha_fin")
    # def validar_fechas(cls, v, values):
    #    if v and values.get("fecha_inicio") and v < values["fecha_inicio"]:
    #        raise ValueError("Fecha fin debe ser posterior a inicio")
    #    return v

    def __repr__(self) -> str:
        return f"DeclaracionSintoma(sintoma={self.sintoma})"

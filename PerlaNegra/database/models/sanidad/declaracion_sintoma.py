import reflex as rx
from datetime import datetime
from sqlmodel import Field, func, Relationship
from ..mixins.timestamp_mixin import TimestampMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .declaracion_jurada import DeclaracionJurada
    from .sintoma import Sintoma


class DeclaracionSintoma(rx.Model, TimestampMixin, table=True):
    __tablename__ = "declaracionsintoma"
    id: int | None = Field(default=None, primary_key=True)
    declaracionjurada_id: int | None = Field(foreign_key="declaracionjurada.id")
    sintoma_id: int | None = Field(foreign_key="sintoma.id")
    respuesta: str
    gravedad: str
    observacion: str
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

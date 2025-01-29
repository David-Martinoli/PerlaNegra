import reflex as rx
from sqlmodel import Field, func, Relationship
from datetime import datetime
from ..mixins.timestamp_mixin import TimestampMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .compania import Compania
    from .personal import Personal
    from .seccion import Seccion


class MovimientoPersonal(rx.Model, TimestampMixin, table=True):
    """Modelo para gestionar movimientos del personal entre secciones/compañías."""

    __tablename__ = "movimientopersonal"
    id: int | None = Field(default=None, primary_key=True)
    personal_id: int | None = Field(foreign_key="personal.id")
    compania_id: int | None = Field(foreign_key="compania.id")
    seccion_id: int | None = Field(foreign_key="seccion.id")

    fecha_inicio: datetime = Field()
    fecha_fin: datetime | None = Field()

    motivo: str | None = Field(default=None, max_length=500)

    created_at: datetime | None = Field(
        default=None,
        nullable=True,
        sa_column_kwargs={"server_default": func.now()},
    )

    # Relaciones
    movimiento_personal_personal_relation: "Personal" = Relationship(
        back_populates="personal_movimiento_personal_relation"
    )
    movimiento_personal_compania_relation: "Compania" = Relationship(
        back_populates="compania_movimiento_personal_relation"
    )
    movimiento_personal_seccion_relation: "Seccion" = Relationship(
        back_populates="seccion_movimiento_personal_relation"
    )

    # @validator("fecha_hasta")
    # def validar_fechas(cls, v, values):
    #    if v and values.get("fecha_desde") and v < values["fecha_desde"]:
    #        raise ValueError("Fecha hasta debe ser posterior a fecha desde")
    #    return v

    def __repr__(self) -> str:
        return f"MovimientoPersonal(personal={self.personal_id}, desde={self.fecha_inicio})"

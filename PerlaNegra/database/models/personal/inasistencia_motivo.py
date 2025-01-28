import reflex as rx
from sqlmodel import Field, func, Relationship
from datetime import datetime
from ..mixins.timestamp_mixin import TimestampMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .inasistencia import Inasistencia


class InasistenciaMotivo(rx.Model, TimestampMixin, table=True):
    __tablename__ = "inasistenciamotivo"
    id: int | None = Field(default=None, primary_key=True)
    nombre: str
    descripcion: str
    created_at: datetime | None = Field(
        default=None,
        nullable=True,
        sa_column_kwargs={"server_default": func.now()},
    )

    # Relaciones
    inasistencia_motivo_inasistencia_relation: list["Inasistencia"] = Relationship(
        back_populates="inasistencia_inasistrencia_motivo_relation"
    )

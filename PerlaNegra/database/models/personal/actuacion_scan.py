import reflex as rx
from sqlmodel import Field, func, Relationship
from datetime import datetime, timezone
from ..mixins.timestamp_mixin import TimestampMixin

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .actuacion import Actuacion


class ActuacionScan(rx.Model, TimestampMixin, table=True):

    __tablename__ = "actuacionscan"
    id: int | None = Field(default=None, primary_key=True)
    actuacion_id: int | None = Field(foreign_key="actuacion.id")
    imagen: str
    descripcion: str
    created_at: datetime | None = Field(
        default=None,
        nullable=True,
        sa_column_kwargs={"server_default": func.now()},
    )

    # Relaciones
    actuacion_scan_actuacion_relation: "Actuacion" = Relationship(
        back_populates="actuacion_actuacion_scan_relation"
    )

import reflex as rx
from sqlmodel import Field, func, Relationship
from datetime import datetime
from ..mixins.timestamp_mixin import TimestampMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .sancion import Sancion


class SancionScan(rx.Model, TimestampMixin, table=True):
    __tablename__ = "sancionscan"
    id: int | None = Field(default=None, primary_key=True)
    sancion_id: int | None = Field(foreign_key="sancion.id")
    imagen: str
    descripcion: str
    created_at: datetime | None = Field(
        default=None,
        nullable=True,
        sa_column_kwargs={"server_default": func.now()},
    )

    # Relaciones
    sancion_scan_sancion_relation: "Sancion" = Relationship(
        back_populates="sancion_sancion_scan_relation",
        sa_relationship_kwargs={"lazy": "joined"},
    )
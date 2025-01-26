import reflex as rx
from sqlmodel import Field, func
from datetime import datetime, timezone
from ..mixins.timestamp_mixin import TimestampMixin


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

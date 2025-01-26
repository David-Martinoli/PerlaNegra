import reflex as rx
from sqlmodel import Field, func
from datetime import datetime, timezone
from ..mixins.timestamp_mixin import TimestampMixin


class Seguro(rx.Model, TimestampMixin, table=True):
    __tablename__ = "seguro"
    id: int | None = Field(default=None, primary_key=True)
    nombre: str
    descripcion: str
    created_at: datetime | None = Field(
        default=None,
        nullable=True,
        sa_column_kwargs={"server_default": func.now()},
    )

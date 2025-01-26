import reflex as rx
from sqlmodel import Field, func
from datetime import datetime, timezone
from ..mixins.timestamp_mixin import TimestampMixin


class EscaneoAnexo(rx.Model, TimestampMixin, table=True):
    __tablename__ = "escaneoanexo"
    id: int | None = Field(default=None, primary_key=True)
    declaracion_jurada_id: int | None = Field(foreign_key="declaracionjurada.id")
    nombre_archivo: str
    created_at: datetime | None = Field(
        default=None,
        nullable=True,
        sa_column_kwargs={"server_default": func.now()},
    )

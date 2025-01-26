import reflex as rx
from sqlmodel import Field, func
from datetime import datetime, timezone
from ..mixins.timestamp_mixin import TimestampMixin


class Telefono(rx.Model, TimestampMixin, table=True):
    __tablename__ = "telefono"
    id: int | None = Field(default=None, primary_key=True)
    personal_id: int | None = Field(foreign_key="personal.id")
    numero_telefono: str
    tipo_telefono: str = ""
    created_at: datetime | None = Field(
        default=None,
        nullable=True,
        sa_column_kwargs={"server_default": func.now()},
    )
    updated_at: datetime = datetime.now(timezone.utc)

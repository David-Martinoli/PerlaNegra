import reflex as rx
from sqlmodel import Field, func
from datetime import datetime, timezone
from ..mixins.timestamp_mixin import TimestampMixin


# //civil o militar
class Clase(rx.Model, TimestampMixin, table=True):
    __tablename__ = "clase"
    id: int | None = Field(default=None, primary_key=True)
    nombre: str
    created_at: datetime | None = Field(
        default=None,
        nullable=True,
        sa_column_kwargs={"server_default": func.now()},
    )

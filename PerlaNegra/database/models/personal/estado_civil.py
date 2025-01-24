import reflex as rx
from sqlmodel import Field, Date, DateTime
from ..mixins.timestamp_mixin import TimestampMixin


class EstadoCivil(rx.Model, TimestampMixin, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nombre: str
    created_at: datetime = datetime.now(timezone.utc)

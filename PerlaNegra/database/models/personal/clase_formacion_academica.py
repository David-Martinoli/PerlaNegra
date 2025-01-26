import reflex as rx
from sqlmodel import Field, func
from ..mixins.timestamp_mixin import TimestampMixin


class ClaseFormacionAcademica(rx.Model, TimestampMixin, table=True):
    __tablename__ = "claseformacionacademica"
    id: int | None = Field(default=None, primary_key=True)
    nombre: str

import reflex as rx
from sqlmodel import Field, func
from ..mixins.timestamp_mixin import TimestampMixin


class ProgramaSalud(rx.Model, TimestampMixin, table=True):
    __tablename__ = "programasalud"
    id: int | None = Field(default=None, primary_key=True)
    nombre: str
    tiempo_revision_id: int | None = Field(
        foreign_key="tiemporevision.id",
        sa_column_kwargs={"name": "fk_programasalud_tiemporevision"},
    )

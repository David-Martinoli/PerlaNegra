import reflex as rx
from sqlmodel import Field
from ..mixins.timestamp_mixin import TimestampMixin


class Cuadro(rx.Model, TimestampMixin, table=True):
    id: int | None = Field(default=None, primary_key=True)
    categoria_personal_id: int | None = Field(foreign_key="categoriapersonal.id")
    nombre: str
    iniciales: str

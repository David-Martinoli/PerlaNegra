import reflex as rx
from sqlmodel import Field, func
from ..mixins.timestamp_mixin import TimestampMixin


class Cuadro(rx.Model, TimestampMixin, table=True):
    __tablename__ = "cuadro"
    id: int | None = Field(default=None, primary_key=True)
    categoria_personal_id: int | None = Field(foreign_key="categoriapersonal.id")
    nombre: str
    iniciales: str

import reflex as rx
from sqlmodel import Field
from ..mixins.timestamp_mixin import TimestampMixin

class Cuadro(rx.Model, TimestampMixin, table=True):
    id: int = Field(primary_key=True)
    categoria_personal_id: int = Field(foreign_key='categoriapersonal.id')
    nombre: str
    iniciales: str
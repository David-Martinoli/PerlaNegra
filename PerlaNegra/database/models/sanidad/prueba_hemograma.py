import reflex as rx
from sqlmodel import Field, func
from ..mixins.timestamp_mixin import TimestampMixin


class PruebaHemograma(rx.Model, TimestampMixin, table=True):
    __tablename__ = "pruebahemograma"
    id: int | None = Field(default=None, primary_key=True)
    globulos_rojos: int
    hematocritos: int
    hb: int
    vcm: int
    hcm: int
    chcm: int
    rdw: int
    cv: int
    plaquetas: int
    globulos_blancos: int
    formula: str = ""

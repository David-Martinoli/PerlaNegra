import reflex as rx
from sqlmodel import Field, func, Relationship
from ..mixins.timestamp_mixin import TimestampMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .declaracion_jurada import DeclaracionJurada


class TipoActividadFisica(rx.Model, TimestampMixin, table=True):
    __tablename__ = "tipoactividadfisica"
    id: int | None = Field(default=None, primary_key=True)
    nombre: str
    observacion: str

    # Relaciones
    tipo_actividad_fisica_declaracion_jurada_relation: list["DeclaracionJurada"] = (
        Relationship(back_populates="declaracion_jurada_tipo_actividad_fisica_relation")
    )

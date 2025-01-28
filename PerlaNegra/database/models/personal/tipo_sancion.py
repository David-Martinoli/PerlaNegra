import reflex as rx
from sqlmodel import Field, func, Relationship
from ..mixins.timestamp_mixin import TimestampMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .sancion import Sancion


# //graves leves ( gravisimas  generan actuacion disiplinaria )
class TipoSancion(rx.Model, TimestampMixin, table=True):
    __tablename__ = "tiposancion"
    id: int | None = Field(default=None, primary_key=True)
    nombre: str

    # Relaciones
    tipo_sancion_sancion_relation: list["Sancion"] = Relationship(
        back_populates="sancion_tipo_sancion_relation",
        sa_relationship_kwargs={"lazy": "joined"},
    )

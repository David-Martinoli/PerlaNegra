import reflex as rx
from sqlmodel import Field, func, Relationship
from ..mixins.timestamp_mixin import TimestampMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .familiar import Familiar


class VinculoFamiliar(rx.Model, TimestampMixin, table=True):
    __tablename__ = "vinculofamiliar"
    id: int | None = Field(default=None, primary_key=True)
    nombre: str

    # Relaciones
    vinculo_familiar_familiar_relation: list["Familiar"] = Relationship(
        back_populates="familiar_vinculo_familiar_relation",
    )

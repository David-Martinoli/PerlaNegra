import reflex as rx
from sqlmodel import Field, func, Relationship
from datetime import date
from ..mixins.timestamp_mixin import TimestampMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..personal.personal import Personal


class Odontologico(rx.Model, TimestampMixin, table=True):
    __tablename__ = "odontologico"
    id: int | None = Field(default=None, primary_key=True)
    personal_id: int | None = Field(foreign_key="personal.id")
    examen_odontologico: str = ""
    observacion_odontologica: str = ""
    fecha_odontograma: date

    # Relaciones
    odontologico_personal_relation: "Personal" = Relationship(
        back_populates="personal_odontologico_relation",
        sa_relationship_kwargs={"lazy": "joined"},
    )
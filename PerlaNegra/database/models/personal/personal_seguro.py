import reflex as rx
from sqlmodel import Field, func, Relationship
from datetime import datetime, timezone
from ..mixins.timestamp_mixin import TimestampMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .personal import Personal
    from .seguro import Seguro


class PersonalSeguro(rx.Model, TimestampMixin, table=True):
    __tablename__ = "personalseguro"
    id: int | None = Field(default=None, primary_key=True)
    personal_id: int | None = Field(foreign_key="personal.id")
    seguro_id: int | None = Field(foreign_key="seguro.id")
    fecha_asignacion: datetime = datetime.now(timezone.utc)

    # Relaciones
    personal_seguro_personal_relation: "Personal" = Relationship(
        back_populates="personal_personal_seguro_relation",
        sa_relationship_kwargs={"lazy": "joined"},
    )
    personal_seguro_seguro_relation: "Seguro" = Relationship(
        back_populates="seguro_personal_seguro_relation",
        sa_relationship_kwargs={"lazy": "joined"},
    )

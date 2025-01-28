import reflex as rx
from sqlmodel import Field, func, Relationship
from datetime import datetime
from ..mixins.timestamp_mixin import TimestampMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .personal_seguro import PersonalSeguro


class Seguro(rx.Model, TimestampMixin, table=True):
    __tablename__ = "seguro"
    id: int | None = Field(default=None, primary_key=True)
    nombre: str
    descripcion: str
    created_at: datetime | None = Field(
        default=None,
        nullable=True,
        sa_column_kwargs={"server_default": func.now()},
    )

    # Relaciones
    seguro_personal_seguro_relation: list["PersonalSeguro"] = Relationship(
        back_populates="personal_seguro_seguro_relation",
        # sa_relationship_kwargs={"lazy": "joined"},
    )

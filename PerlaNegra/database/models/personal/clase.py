import reflex as rx
from sqlmodel import Field, func, Relationship
from datetime import datetime, timezone
from ..mixins.timestamp_mixin import TimestampMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .personal_s import PersonalS


# //civil o militar
class Clase(rx.Model, TimestampMixin, table=True):
    __tablename__ = "clase"
    id: int | None = Field(default=None, primary_key=True)
    nombre: str
    created_at: datetime | None = Field(
        default=None,
        nullable=True,
        sa_column_kwargs={"server_default": func.now()},
    )

    # Relaciones
    clase_personals_relation: list["PersonalS"] = Relationship(
        back_populates="personals_clase_relation",
    )
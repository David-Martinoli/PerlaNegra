import reflex as rx
from sqlmodel import Field, func, Relationship
from datetime import datetime, timezone
from ..mixins.timestamp_mixin import TimestampMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .personal import Personal


class Direccion(rx.Model, TimestampMixin, table=True):
    __tablename__ = "direccion"
    id: int | None = Field(default=None, primary_key=True)
    personal_id: int | None = Field(foreign_key="personal.id")  # personalR
    calle: str
    ciudad: str = ""
    estado: str = ""
    codigo_postal: str = ""
    pais: str = ""
    tipo_direccion: str = ""
    created_at: datetime | None = Field(
        default=None,
        nullable=True,
        sa_column_kwargs={"server_default": func.now()},
    )
    updated_at: datetime | None = datetime.now(timezone.utc)

    # Relaciones
    personal_direccion_relation: "Personal" = Relationship(
        back_populates="direccion_personal_relation",
    )

import reflex as rx

# from sqlalchemy import Column, ForeignKey
from sqlmodel import Field, func, Relationship
from datetime import date, datetime

# from PerlaNegra.database.models.personal.personal import Personal

# from ..personal.personal import Personal
from ..mixins.timestamp_mixin import TimestampMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .personal import Personal


class Felicitacion(rx.Model, TimestampMixin, table=True):
    __tablename__ = "felicitacion"
    id: int | None = Field(default=None, primary_key=True)

    quien_impone: int = Field(foreign_key="personal.id")
    personal_id: int | None = Field(foreign_key="personal.id")

    fecha: date
    causa: str
    descripcion: str
    imagen: str
    created_at: datetime | None = Field(
        default=None,
        nullable=True,
        sa_column_kwargs={"server_default": func.now()},
    )
    updated_at: datetime | None = Field(
        default_factory=datetime.now,
        nullable=False,
        sa_column_kwargs={"onupdate": func.now()},
    )

    # Relaciones
    personal_quien_impone_felicitacion_relation: "Personal" = Relationship(
        back_populates="felicitacion_personal_quien_impone_relation",
        sa_relationship_kwargs={
            "foreign_keys": "Felicitacion.quien_impone",
            "lazy": "joined",
        },
    )
    personal_personal_felicitacion_relation: "Personal" = Relationship(
        back_populates="personal_felicitacion_personal_relation",
        sa_relationship_kwargs={
            "foreign_keys": "Felicitacion.personal_id",
            "lazy": "joined",
        },
    )

import reflex as rx
from sqlmodel import Field, func, Relationship
from datetime import datetime
from ..mixins.timestamp_mixin import TimestampMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .declaracion_jurada import DeclaracionJurada


class EscaneoAnexo(rx.Model, TimestampMixin, table=True):
    __tablename__ = "escaneoanexo"
    id: int | None = Field(default=None, primary_key=True)
    declaracion_jurada_id: int | None = Field(foreign_key="declaracionjurada.id")
    nombre_archivo: str
    created_at: datetime | None = Field(
        default=None,
        nullable=True,
        sa_column_kwargs={"server_default": func.now()},
    )

    # Relaciones
    escaneo_anexo_declaracion_jurada_relation: "DeclaracionJurada" = Relationship(
        back_populates="declaracion_jurada_escaneo_anexo_relation",
        sa_relationship_kwargs={"lazy": "joined"},
    )
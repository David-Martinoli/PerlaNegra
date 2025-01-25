import reflex as rx
from sqlmodel import Field, func
from ..mixins.timestamp_mixin import TimestampMixin
from sqlmodel import Field, func


class AccesoSector(rx.Model, TimestampMixin, table=True):
    id: int | None = Field(default=None, primary_key=True)
    sector_origen_id: int | None = Field(foreign_key="unidad.id")
    sector_destino_id: int | None = Field(foreign_key="unidad.id")
    permiso_id: int | None = Field(foreign_key="permiso.id")

import reflex as rx
from sqlmodel import Field
from ..mixins.timestamp_mixin import TimestampMixin
from sqlmodel import Field

class AccesoSector(rx.Model, TimestampMixin, table=True):
    id: int = Field(primary_key=True)
    sector_origen_id: int = Field(foreign_key='unidad.id')
    sector_destino_id: int = Field(foreign_key='unidad.id')
    permiso_id: int = Field(foreign_key='permiso.id')
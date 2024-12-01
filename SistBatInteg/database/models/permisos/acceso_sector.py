import reflex as rx
from ..mixins.timestamp_mixin import TimestampMixin

class AccesoSector(rx.Model, TimestampMixin, table=True):
    id: int = rx.Field(primary_key=True)
    sector_origen_id: int = rx.Field(foreign_key='unidad.id')
    sector_destino_id: int = rx.Field(foreign_key='unidad.id')
    permiso_id: int = rx.Field(foreign_key='permiso.id')
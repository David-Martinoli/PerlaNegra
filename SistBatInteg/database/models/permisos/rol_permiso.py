import reflex as rx
from ..mixins.timestamp_mixin import TimestampMixin

class RolPermiso(rx.Model, TimestampMixin, table=True):
    id: int = rx.Field(primary_key=True)
    rol_id: int = rx.Field(foreign_key='rol.id')
    permiso_id: int = rx.Field(foreign_key='permiso.id')
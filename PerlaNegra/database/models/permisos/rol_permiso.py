import reflex as rx
from sqlmodel import Field
from ..mixins.timestamp_mixin import TimestampMixin

class RolPermiso(rx.Model, TimestampMixin, table=True):
    id: int = Field(primary_key=True)
    rol_id: int = Field(foreign_key='rol.id')
    permiso_id: int = Field(foreign_key='permiso.id')
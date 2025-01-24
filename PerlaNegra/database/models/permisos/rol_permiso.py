import reflex as rx
from sqlmodel import Field
from ..mixins.timestamp_mixin import TimestampMixin


class RolPermiso(rx.Model, TimestampMixin, table=True):
    id: int | None = Field(default=None, primary_key=True)
    rol_id: int | None = Field(foreign_key="rol.id")
    permiso_id: int | None = Field(foreign_key="permiso.id")

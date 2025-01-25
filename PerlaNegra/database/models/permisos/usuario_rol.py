import reflex as rx
from sqlmodel import Field, func
from ..mixins.timestamp_mixin import TimestampMixin


class UsuarioRol(rx.Model, TimestampMixin, table=True):
    id: int | None = Field(default=None, primary_key=True)
    usuario_id: int | None = Field(foreign_key="usuario.id")
    rol_id: int | None = Field(foreign_key="rol.id")

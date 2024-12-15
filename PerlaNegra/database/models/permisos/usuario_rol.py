import reflex as rx
from sqlmodel import Field
from ..mixins.timestamp_mixin import TimestampMixin

class UsuarioRol(rx.Model, TimestampMixin, table=True):
    id: int = Field(primary_key=True)
    usuario_id: int = Field(foreign_key='usuario.id')
    rol_id: int = Field(foreign_key='rol.id')
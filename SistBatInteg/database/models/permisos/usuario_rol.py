import reflex as rx
from ..mixins.timestamp_mixin import TimestampMixin

class UsuarioRol(rx.Model, TimestampMixin, table=True):
    id: int = rx.Field(primary_key=True)
    usuario_id: int = rx.Field(foreign_key='usuario.id')
    rol_id: int = rx.Field(foreign_key='rol.id')
import reflex as rx
from datetime import date, datetime

class UsuarioRol(rx.Model, table=True):
    id: int = rx.Field(primary_key=True)
    usuario_id: int = rx.Field(foreign_key='usuario.id')
    rol_id: int = rx.Field(foreign_key='rol.id')
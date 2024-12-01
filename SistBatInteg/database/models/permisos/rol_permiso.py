import reflex as rx
from datetime import date, datetime

class RolPermiso(rx.Model, table=True):
    id: int = rx.Field(primary_key=True)
    rol_id: int = rx.Field(foreign_key='rol.id')
    permiso_id: int = rx.Field(foreign_key='permiso.id')
import reflex as rx
from datetime import date, datetime

class Permiso(rx.Model, table=True):
    id: int = rx.Field(primary_key=True)
    modulo: str
    accion: str
    descripcion: str = ''
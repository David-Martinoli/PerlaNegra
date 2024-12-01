import reflex as rx
from datetime import date, datetime

class Compania(rx.Model, table=True):
    id: int = rx.Field(primary_key=True)
    unidad_id: int = rx.Field(foreign_key='unidad.id')
    nombre: str
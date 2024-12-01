import reflex as rx
from datetime import date, datetime

class Unidad(rx.Model, table=True):
    id: int = rx.Field(primary_key=True)
    nombre: str
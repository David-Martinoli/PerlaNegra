import reflex as rx
from datetime import date, datetime

class Cuadro(rx.Model, table=True):
    id: int = rx.Field(primary_key=True)
    categoria_personal_id: int = rx.Field(foreign_key='categoria_personal.id')
    nombre: str
    iniciales: str
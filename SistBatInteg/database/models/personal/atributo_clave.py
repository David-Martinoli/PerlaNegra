import reflex as rx
from datetime import date, datetime

class AtributoClave(rx.Model, table=True):
    id: int = rx.Field(primary_key=True)
    clave: str
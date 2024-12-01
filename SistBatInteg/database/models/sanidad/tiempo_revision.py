import reflex as rx
from datetime import date, datetime

class TiempoRevision(rx.Model, table=True):
    id: int = rx.Field(primary_key=True)
    valor: float
import reflex as rx
from datetime import date, datetime

class ProgramaSalud(rx.Model, table=True):
    id: int = rx.Field(primary_key=True)
    nombre: str
    tiempo_revision_id: int = rx.Field(foreign_key='tiempo_revision.id')
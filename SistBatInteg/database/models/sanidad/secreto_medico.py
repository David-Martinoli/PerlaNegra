import reflex as rx
from datetime import date, datetime

class SecretoMedico(rx.Model, table=True):
    id: int = rx.Field(primary_key=True)
    profesional_id: int = rx.Field(foreign_key='personal.id')
    paciente_id: int = rx.Field(foreign_key='personal.id')
    descripcion: str
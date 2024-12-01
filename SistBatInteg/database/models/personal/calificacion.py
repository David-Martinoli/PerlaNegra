import reflex as rx
from datetime import date, datetime

class Calificacion(rx.Model, table=True):
    id: int = rx.Field(primary_key=True)
    personal_id: int = rx.Field(foreign_key='personal.id')
    val1: int = 0
    val2: int = 0
    val3: int = 0
    val4: int = 0
    val5: int = 0
    creado_en: datetime = datetime.utcnow()
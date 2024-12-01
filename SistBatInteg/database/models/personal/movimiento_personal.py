import reflex as rx
from datetime import date, datetime

class MovimientoPersonal(rx.Model, table=True):
    id: int = rx.Field(primary_key=True)
    personal_id: int = rx.Field(foreign_key='personal.id')
    compania_id: int = rx.Field(foreign_key='compania.id')
    fecha_inicio: datetime
    fecha_fin: datetime
    motivo: str = ''
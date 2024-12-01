import reflex as rx
from datetime import date, datetime

class Telefono(rx.Model, table=True):
    id: int = rx.Field(primary_key=True)
    personal_id: int = rx.Field(foreign_key='personal.id')
    numero_telefono: str
    tipo_telefono: str = ''
    creado_en: datetime = datetime.now(datetime.UTC)
    actualizado_en: datetime = datetime.now(datetime.UTC)
import reflex as rx
from datetime import date, datetime

class Direccion(rx.Model, table=True):
    id: int = rx.Field(primary_key=True)
    personal_id: int = rx.Field(foreign_key='personal.id')
    calle: str
    ciudad: str = ''
    estado: str = ''
    codigo_postal: str = ''
    pais: str = ''
    tipo_direccion: str = ''
    creado_en: datetime = datetime.now(datetime.UTC)
    actualizado_en: datetime = datetime.now(datetime.UTC)
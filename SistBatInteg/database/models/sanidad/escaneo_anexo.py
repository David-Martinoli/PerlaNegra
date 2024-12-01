import reflex as rx
from datetime import date, datetime

class EscaneoAnexo(rx.Model, table=True):
    id: int = rx.Field(primary_key=True)
    declaracion_jurada_id: int = rx.Field(foreign_key='declaracion_jurada.id')
    nombre_archivo: str
    creado_en: datetime = datetime.utcnow()
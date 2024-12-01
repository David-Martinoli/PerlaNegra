import reflex as rx
from datetime import date, datetime

class Auditoria(rx.Model, table=True):
    id: int = rx.Field(primary_key=True)
    tabla_afectada: str
    registro_id: int
    campo_modificado: str = ''
    valor_anterior: str = ''
    valor_nuevo: str = ''
    modificado_por: str = ''
    fecha_modificacion: datetime = datetime.utcnow()
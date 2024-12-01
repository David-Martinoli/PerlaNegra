import reflex as rx
from datetime import datetime
from ..mixins.timestamp_mixin import TimestampMixin

class Auditoria(rx.Model, TimestampMixin, table=True):
    id: int = rx.Field(primary_key=True)
    tabla_afectada: str
    registro_id: int
    campo_modificado: str = ''
    valor_anterior: str = ''
    valor_nuevo: str = ''
    modificado_por: str = ''
    fecha_modificacion: datetime = datetime.now(datetime.UTC)
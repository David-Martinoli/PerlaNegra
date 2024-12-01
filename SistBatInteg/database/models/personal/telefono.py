import reflex as rx
from datetime import datetime
from ..mixins.timestamp_mixin import TimestampMixin

class Telefono(rx.Model, TimestampMixin, table=True):
    id: int = rx.Field(primary_key=True)
    personal_id: int = rx.Field(foreign_key='personal.id')
    numero_telefono: str
    tipo_telefono: str = ''
    creado_en: datetime = datetime.now(datetime.UTC)
    actualizado_en: datetime = datetime.now(datetime.UTC)
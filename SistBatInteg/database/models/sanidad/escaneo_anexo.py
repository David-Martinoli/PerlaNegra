import reflex as rx
from datetime import datetime
from ..mixins.timestamp_mixin import TimestampMixin

class EscaneoAnexo(rx.Model, TimestampMixin, table=True):
    id: int = rx.Field(primary_key=True)
    declaracion_jurada_id: int = rx.Field(foreign_key='declaracion_jurada.id')
    nombre_archivo: str
    creado_en: datetime = datetime.now(datetime.UTC)
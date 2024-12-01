import reflex as rx
from datetime import date
from ..mixins.timestamp_mixin import TimestampMixin

class Odontologico(rx.Model, TimestampMixin, table=True):
    id: int = rx.Field(primary_key=True)
    personal_id: int = rx.Field(foreign_key='personal.id')
    examen_odontologico: str = ''
    observacion_odontologica: str = ''
    fecha_odontograma: date
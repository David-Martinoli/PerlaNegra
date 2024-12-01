import reflex as rx
from datetime import date
from ..mixins.timestamp_mixin import TimestampMixin

class Cardiologico(rx.Model, TimestampMixin, table=True):
    id: int = rx.Field(primary_key=True)
    examen_medico_id: int = rx.Field(foreign_key='examen_medico.id')
    ecg: str = ''
    ergometria_id: int = rx.Field(foreign_key='ergometria.id')
    radiologia: str = ''
    otros: str = ''
    fecha: date
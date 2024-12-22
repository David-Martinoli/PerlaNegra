import reflex as rx
from sqlmodel import Field
from datetime import datetime
from ..mixins.timestamp_mixin import TimestampMixin

class MovimientoPersonal(rx.Model, TimestampMixin, table=True):
    id: int = Field(primary_key=True)
    personal_id: int = Field(foreign_key='personal.id')
    compania_id: int = Field(foreign_key='compania.id')
    fecha_inicio: datetime
    fecha_fin: datetime
    motivo: str = ''
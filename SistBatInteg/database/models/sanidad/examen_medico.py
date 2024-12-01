import reflex as rx
from sqlmodel import Field
from ..mixins.timestamp_mixin import TimestampMixin

class ExamenMedico(rx.Model, TimestampMixin, table=True):
    id: int = Field(primary_key=True)
    personal_id: int = Field(foreign_key='personal.id')
    peso: float
    talla: float
    imc: float #formula peso / talla al cuadrada  indice de talla corporal
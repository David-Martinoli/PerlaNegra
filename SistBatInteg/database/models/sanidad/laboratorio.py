import reflex as rx
from sqlmodel import Field
from datetime import date
from ..mixins.timestamp_mixin import TimestampMixin

class Laboratorio(rx.Model, TimestampMixin, table=True):
    id: int = Field(primary_key=True)
    prueba_hemograma_id: int = Field(foreign_key='pruebahemograma.id')
    eritrosedimentacion: str = ''
    glucemia: float
    uremia: float
    colesterol_total: float
    hdl_colesterol: float
    ldl_colesterol: float
    trigliceridos: float
    orina_completa: str = ''
    toxicologico: str = ''
    fecha: date
    hiv: str = ''
    hemograma: str = ''
    eritrocito: str = ''
    glucemia: str = ''
    creatinina: str = ''
    colesterol_total_texto: str = ''
    hdl: str = ''
    ldl: str = ''
    vdrl: str = ''
    orina_completa_texto: str = ''
    toxicologico_texto: str = ''
    hepatograma: str = ''
    indice_castelli: str = ''
    observaciones: str = ''
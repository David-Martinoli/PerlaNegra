import reflex as rx
from datetime import date, datetime

class Laboratorio(rx.Model, table=True):
    id: int = rx.Field(primary_key=True)
    prueba_hemograma_id: int = rx.Field(foreign_key='prueba_hemograma.id')
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
# database/models/personal.py
import reflex as rx
from datetime import date, datetime

class Personal(rx.Model, table=True):
    id: int = rx.Field(primary_key=True)
    nombre: str
    apellido: str
    fecha_nacimiento: date
    dni: str
    numero_legajo: str
    categoria_personal_id: int = rx.Field(foreign_key='categoria_personal.id')
    arma_especialidad: str = ''
    grado: str = ''
    cuadro: str = ''
    en_campo: str = ''
    creado_en: datetime = datetime.now(datetime.UTC)
    actualizado_en: datetime = datetime.now(datetime.UTC)
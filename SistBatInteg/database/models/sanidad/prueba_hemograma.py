import reflex as rx
from datetime import date, datetime

class PruebaHemograma(rx.Model, table=True):
    id: int = rx.Field(primary_key=True)
    globulos_rojos: int
    hematocritos: int
    hb: int
    vcm: int
    hcm: int
    chcm: int
    rdw: int
    plaquetas: int
    globulos_blancos: int
    formula: str = ''